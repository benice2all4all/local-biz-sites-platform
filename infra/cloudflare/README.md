# Cloudflare Pages deployment notes

Default convention:
- one Cloudflare Pages project per client site
- set the project root directory to the specific site folder under `sites/active/<slug>/`
- use GitHub as the deployment source

Recommended setup per Astro site:
- framework preset: Astro
- root directory: `sites/active/<slug>`
- build command: `npm run build`
- output directory: `dist`

Repo-level deploy helper:

```bash
python3 scripts/deploy_site.py <slug>
```

By default, the helper reads `sites/active/<slug>/deployment.json` and uses `pagesProjectName` as the Cloudflare Pages project name. Use `--project-name` to override it for a one-off deploy.

Site inventory helper:

```bash
python3 scripts/site_inventory.py
python3 scripts/site_inventory.py --format json
```

Each site should keep deployment metadata in `deployment.json`, including:
- `pagesProjectName`
- `cloudflarePagesUrl`
- `customDomain`
- `status`
- `lastDeployedAt`

Useful flags:
- `--dry-run` prints the commands without executing them
- `--project-name <name>` overrides the Cloudflare Pages project name
- `--branch preview` deploys to a non-production branch
- `--skip-install` and `--skip-build` reuse an already-built site

The deploy helper runs these steps from `sites/active/<slug>/`:
- `npm install`
- `npm run build`
- `npx wrangler pages deploy dist --project-name <pagesProjectName>`

Before first real deploy, authenticate Wrangler with Cloudflare:

```bash
npx wrangler login
```

Domain workflow:
- attach the client domain in Cloudflare Pages
- manage DNS in Cloudflare when possible
- keep SSL fully managed by Cloudflare

Handoff workflow:
- if a client wants their own repo, split out `sites/active/<slug>/`
- keep the folder layout simple so it migrates cleanly
