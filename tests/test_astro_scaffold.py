import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class AstroScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).resolve().parents[1]
        self.temp_dir = Path(tempfile.mkdtemp(prefix="local-biz-sites-platform-test-"))
        self.worktree = self.temp_dir / "repo"
        shutil.copytree(
            self.repo_root,
            self.worktree,
            ignore=shutil.ignore_patterns(".git", "node_modules", "dist", ".astro", "__pycache__"),
        )

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_new_site_scaffolds_astro_project(self):
        script = self.worktree / "scripts" / "new_site.py"
        subprocess.run(
            ["python3", str(script), "acme-roofing", "Acme Roofing"],
            cwd=self.worktree,
            check=True,
        )

        site_root = self.worktree / "sites" / "active" / "acme-roofing"
        self.assertTrue((site_root / "package.json").exists())
        self.assertTrue((site_root / "astro.config.mjs").exists())
        self.assertTrue((site_root / "src" / "pages" / "index.astro").exists())
        self.assertTrue((site_root / "src" / "layouts" / "BaseLayout.astro").exists())


if __name__ == "__main__":
    unittest.main()
