# local-biz-sites-platform

A multi-project starter repo for building and managing simple brochure websites for local businesses.

Default opinionated stack:
- GitHub for source control
- Cloudflare Pages for hosting
- Astro for reusable static brochure sites
- one reusable Astro template plus per-client site folders

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

Create a new Astro site from the default brochure template:

```bash
python3 scripts/new_site.py maple-street-plumbing "Maple Street Plumbing"
cd sites/active/maple-street-plumbing
npm install
npm run dev
```

Deploy a site with the repo-level helper:

```bash
python3 scripts/deploy_site.py maple-street-plumbing
```

That creates:

```
sites/active/maple-street-plumbing/
```

## Recommended workflow

1. Start each business site in `sites/active/<slug>/`
2. Customize `site.json`, page copy, colors, images, and contact details
3. Deploy each site to its own Cloudflare Pages project
4. If a client needs full ownership later, move that folder into its own repo
5. Archive inactive work under `sites/archived/`

## Initial defaults

- Astro-based brochure-site pages: home, services, about, contact
- static output for low maintenance and cheap hosting
- custom-domain-friendly deployment via Cloudflare Pages
- lightweight structure for parallel client work

## Next steps

- add shared content collections for testimonials and FAQs
- add image optimization workflow
- add contact-form integration patterns
- add per-site domain metadata and deployment tracking
