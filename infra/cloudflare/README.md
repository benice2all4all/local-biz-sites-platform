# Cloudflare Pages deployment notes

Default convention:
- one Cloudflare Pages project per client site
- publish from the specific site folder under `sites/active/<slug>/`
- use GitHub as the deployment source

Recommended setup per site:
- framework preset: None for plain static template
- build command: leave empty
- output directory: `sites/active/<slug>/`

Domain workflow:
- attach the client domain in Cloudflare Pages
- manage DNS in Cloudflare when possible
- keep SSL fully managed by Cloudflare

Handoff workflow:
- if a client wants their own repo, split out `sites/active/<slug>/`
- keep the folder layout simple so it migrates cleanly
