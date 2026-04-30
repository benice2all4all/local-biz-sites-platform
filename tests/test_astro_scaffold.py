import json
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
        self.assertTrue((site_root / "public" / "images" / "logo.svg").exists())
        self.assertTrue((site_root / "public" / "images" / "hero.svg").exists())
        self.assertTrue((site_root / "public" / "images" / "feature.svg").exists())
        self.assertTrue((site_root / "public" / "images" / "gallery-1.svg").exists())
        self.assertTrue((site_root / "public" / "images" / "gallery-2.svg").exists())
        self.assertTrue((site_root / "public" / "images" / "gallery-3.svg").exists())

        site_data = json.loads((site_root / "site.json").read_text(encoding="utf-8"))
        self.assertEqual(site_data["logoImage"], "/images/logo.svg")
        self.assertEqual(site_data["heroImage"], "/images/hero.svg")
        self.assertEqual(site_data["featureImage"], "/images/feature.svg")
        self.assertEqual(len(site_data["galleryImages"]), 3)
        self.assertEqual(site_data["galleryImages"][0]["src"], "/images/gallery-1.svg")
        self.assertEqual(site_data["galleryImages"][1]["src"], "/images/gallery-2.svg")
        self.assertEqual(site_data["galleryImages"][2]["src"], "/images/gallery-3.svg")

    def test_new_site_scaffolds_deployment_metadata(self):
        script = self.worktree / "scripts" / "new_site.py"
        subprocess.run(
            ["python3", str(script), "acme-roofing", "Acme Roofing"],
            cwd=self.worktree,
            check=True,
        )

        deployment_path = self.worktree / "sites" / "active" / "acme-roofing" / "deployment.json"
        self.assertTrue(deployment_path.exists())

        deployment = json.loads(deployment_path.read_text(encoding="utf-8"))
        self.assertEqual(deployment["siteSlug"], "acme-roofing")
        self.assertEqual(deployment["pagesProjectName"], "acme-roofing")
        self.assertEqual(deployment["productionBranch"], "main")
        self.assertEqual(deployment["cloudflarePagesUrl"], "https://acme-roofing.pages.dev")
        self.assertEqual(deployment["customDomain"], "")
        self.assertEqual(deployment["status"], "draft")
        self.assertEqual(deployment["lastDeployedAt"], "")


if __name__ == "__main__":
    unittest.main()
