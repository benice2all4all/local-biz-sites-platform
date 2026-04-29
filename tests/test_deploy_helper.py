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


if __name__ == "__main__":
    unittest.main()
