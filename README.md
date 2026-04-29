# local-biz-sites-platform

A multi-project starter repo for building and managing simple brochure websites for local businesses.

Default opinionated stack:
- GitHub for source control
- Cloudflare Pages for hosting
- static HTML/CSS-first brochure sites for low maintenance
- one reusable template plus per-client site folders

Why this repo exists:
- keep many small projects organized at the same time
- reuse a proven brochure-site template
- make it easy to hand a single client site off later
- keep hosting cheap and operations simple

## Repository layout

```
docs/                  strategy, architecture, plans
infra/cloudflare/      deployment notes and conventions
scripts/               helper scripts for scaffolding sites
shared/                reusable assets, copy blocks, brand snippets
templates/             reusable site templates
sites/active/          current client sites in progress or live
sites/archived/        completed or retired sites
```

## Quick start

Create a new site from the default brochure template:

```bash
python3 scripts/new_site.py maple-street-plumbing "Maple Street Plumbing"
```

That creates:

```
sites/active/maple-street-plumbing/
```

## Recommended workflow

1. Start each business site in `sites/active/<slug>/`
2. Customize copy, colors, images, and contact details
3. Deploy each site to its own Cloudflare Pages project
4. If a client needs full ownership later, move that folder into its own repo
5. Archive inactive work under `sites/archived/`

## Initial defaults

- simple brochure-site pages: home, services, about, contact
- static-first approach to reduce maintenance and hosting cost
- custom-domain-friendly deployment via Cloudflare Pages
- lightweight structure for parallel client work

## Next steps

- add Astro-based template when you want component reuse
- add image optimization workflow
- add content intake forms per client
- add a deployment helper for Cloudflare Pages
