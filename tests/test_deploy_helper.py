import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class DeployHelperTests(unittest.TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).resolve().parents[1]
        self.temp_dir = Path(tempfile.mkdtemp(prefix="local-biz-sites-platform-deploy-test-"))
        self.worktree = self.temp_dir / "repo"
        shutil.copytree(
            self.repo_root,
            self.worktree,
            ignore=shutil.ignore_patterns(".git", "node_modules", "dist", ".astro", "__pycache__"),
        )
        subprocess.run(
            ["python3", str(self.worktree / "scripts" / "new_site.py"), "acme-roofing", "Acme Roofing"],
            cwd=self.worktree,
            check=True,
        )

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_deploy_helper_dry_run_prints_expected_commands(self):
        script = self.worktree / "scripts" / "deploy_site.py"
        result = subprocess.run(
            ["python3", str(script), "acme-roofing", "--dry-run"],
            cwd=self.worktree,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("npm install", result.stdout)
        self.assertIn("npm run build", result.stdout)
        self.assertIn("wrangler pages deploy dist --project-name acme-roofing", result.stdout)

    def test_deploy_helper_uses_project_name_from_deployment_metadata(self):
        deployment_path = self.worktree / "sites" / "active" / "acme-roofing" / "deployment.json"
        deployment = json.loads(deployment_path.read_text(encoding="utf-8"))
        deployment["pagesProjectName"] = "acme-roofing-prod"
        deployment_path.write_text(json.dumps(deployment, indent=2) + "\n", encoding="utf-8")

        script = self.worktree / "scripts" / "deploy_site.py"
        result = subprocess.run(
            ["python3", str(script), "acme-roofing", "--dry-run"],
            cwd=self.worktree,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("wrangler pages deploy dist --project-name acme-roofing-prod", result.stdout)

    def test_site_inventory_reports_deployment_metadata(self):
        script = self.worktree / "scripts" / "site_inventory.py"
        result = subprocess.run(
            ["python3", str(script), "--format", "json"],
            cwd=self.worktree,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0)
        sites = json.loads(result.stdout)
        acme_site = next(site for site in sites if site["slug"] == "acme-roofing")
        self.assertEqual(acme_site["businessName"], "Acme Roofing")
        self.assertEqual(acme_site["pagesProjectName"], "acme-roofing")
        self.assertEqual(acme_site["cloudflarePagesUrl"], "https://acme-roofing.pages.dev")
        self.assertEqual(acme_site["customDomain"], "")
        self.assertEqual(acme_site["status"], "draft")


if __name__ == "__main__":
    unittest.main()
