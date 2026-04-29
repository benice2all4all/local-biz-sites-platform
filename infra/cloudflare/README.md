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

Domain workflow:
- attach the client domain in Cloudflare Pages
- manage DNS in Cloudflare when possible
- keep SSL fully managed by Cloudflare

Handoff workflow:
- if a client wants their own repo, split out `sites/active/<slug>/`
- keep the folder layout simple so it migrates cleanly
