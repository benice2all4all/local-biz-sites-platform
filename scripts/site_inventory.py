#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / "sites" / "active"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_sites() -> list[dict[str, str]]:
    sites: list[dict[str, str]] = []
    for site_dir in sorted(path for path in ACTIVE.iterdir() if path.is_dir()):
        site_path = site_dir / "site.json"
        deployment_path = site_dir / "deployment.json"
        if not site_path.exists() or not deployment_path.exists():
            continue

        site = load_json(site_path)
        deployment = load_json(deployment_path)
        sites.append(
            {
                "slug": site_dir.name,
                "businessName": site.get("businessName", ""),
                "pagesProjectName": deployment.get("pagesProjectName", site_dir.name),
                "cloudflarePagesUrl": deployment.get("cloudflarePagesUrl", ""),
                "customDomain": deployment.get("customDomain", ""),
                "status": deployment.get("status", ""),
                "lastDeployedAt": deployment.get("lastDeployedAt", ""),
            }
        )
    return sites


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Report deployment metadata for active sites.")
    parser.add_argument("--format", choices=["table", "json"], default="table")
    return parser.parse_args()


def print_table(sites: list[dict[str, str]]) -> None:
    headers = ["slug", "status", "pagesProjectName", "customDomain"]
    widths = {
        header: max(len(header), *(len(site.get(header, "")) for site in sites))
        for header in headers
    }
    print("  ".join(header.ljust(widths[header]) for header in headers))
    print("  ".join("-" * widths[header] for header in headers))
    for site in sites:
        print("  ".join(site.get(header, "").ljust(widths[header]) for header in headers))


def main() -> int:
    args = parse_args()
    if not ACTIVE.exists():
        print("[]" if args.format == "json" else "No active sites found.")
        return 0

    sites = collect_sites()
    if args.format == "json":
        json.dump(sites, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        if not sites:
            print("No active sites found.")
        else:
            print_table(sites)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
