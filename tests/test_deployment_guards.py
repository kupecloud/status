"""Prevent template regeneration from restoring feature-branch production deploys."""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


def block(text, key, indent):
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if re.match(r"^" + " " * indent + re.escape(key) + r":", line))
    end = next((i for i in range(start + 1, len(lines)) if lines[i].strip() and len(lines[i]) - len(lines[i].lstrip()) <= indent), len(lines))
    return "\n".join(lines[start:end])


class DeploymentGuards(unittest.TestCase):
    def test_setup_and_site_only_publish_reviewed_main(self):
        for name in ("setup.yml", "site.yml"):
            with self.subTest(workflow=name):
                text = (ROOT / ".github/workflows" / name).read_text()
                push = block(block(text, "on", 0), "push", 2)
                self.assertEqual([line.strip() for line in block(push, "branches", 4).splitlines()], ["branches:", "- main"])
                release = block(block(text, "jobs", 0), "release", 2)
                self.assertRegex(release, r"(?m)^    if: github\.ref == 'refs/heads/main'(?: && !contains\(github.event.head_commit.message, '\[skip ci\]'\))?$")
                self.assertNotIn('command: "update-template"', text)

    def test_manual_upgrade_cannot_mutate_production(self):
        text = (ROOT / ".github/workflows/update-template.yml").read_text()
        self.assertIn("contents: read", text)
        self.assertNotRegex(text, r"contents:\s*write|GH_PAT|command:\s*[\"']?update-template")


if __name__ == "__main__":
    unittest.main()
