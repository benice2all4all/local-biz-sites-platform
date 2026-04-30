#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / "sites" / "active"


def shell_join(parts: list[str]) -> str:
    return " ".join(shlex.quote(part) for part in parts)


def run_step(command: list[str], cwd: Path, dry_run: bool) -> None:
    print(shell_join(command))
    if dry_run:
        return
    subprocess.run(command, cwd=cwd, check=True)


def load_deployment_metadata(site_dir: Path) -> dict[str, str]:
    deployment_path = site_dir / "deployment.json"
    if not deployment_path.exists():
        return {}
    return json.loads(deployment_path.read_text(encoding="utf-8"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install, build, and deploy a site in sites/active/<slug> to Cloudflare Pages."
    )
    parser.add_argument("slug", help="Site slug under sites/active/")
    parser.add_argument("--project-name", help="Override Cloudflare Pages project name")
    parser.add_argument("--branch", help="Optional Cloudflare Pages branch name")
    parser.add_argument("--skip-install", action="store_true", help="Skip npm install")
    parser.add_argument("--skip-build", action="store_true", help="Skip npm run build")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without executing them")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    slug = args.slug.strip()
    site_dir = ACTIVE / slug

    if not site_dir.exists():
        print(f"Error: site does not exist: {site_dir}", file=sys.stderr)
        return 2
    if not (site_dir / "package.json").exists():
        print(f"Error: not an Astro/npm site: {site_dir}", file=sys.stderr)
        return 3

    deployment = load_deployment_metadata(site_dir)
    project_name = args.project_name or deployment.get("pagesProjectName") or slug

    if not args.skip_install:
        run_step(["npm", "install"], cwd=site_dir, dry_run=args.dry_run)
    if not args.skip_build:
        run_step(["npm", "run", "build"], cwd=site_dir, dry_run=args.dry_run)

    deploy_command = [
        "npx",
        "wrangler",
        "pages",
        "deploy",
        "dist",
        "--project-name",
        project_name,
    ]
    if args.branch:
        deploy_command.extend(["--branch", args.branch])

    run_step(deploy_command, cwd=site_dir, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
