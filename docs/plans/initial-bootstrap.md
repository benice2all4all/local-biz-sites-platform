# Local Business Sites Platform Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Build a reusable repo for managing many low-maintenance local-business brochure sites in parallel.

**Architecture:** Use a multi-project repository with reusable templates, per-client site folders, lightweight helper scripts, and Cloudflare Pages deployment conventions. Use Astro as the default template so the sites remain static-friendly while gaining reusable layouts and components.

**Tech Stack:** GitHub, Cloudflare Pages, Astro, Python helper scripts.

---

### Task 1: Define the multi-project repository layout

**Objective:** Establish a repo structure that supports many concurrent client projects.

**Files:**
- Create: `README.md`
- Create: `docs/project-brief.md`
- Create: `docs/architecture.md`
- Create: `sites/README.md`

**Verification:**
- Confirm the README explains `templates/`, `sites/active/`, and `sites/archived/`
- Confirm the docs explain why Cloudflare Pages is the default target

### Task 2: Create a reusable Astro brochure-site template

**Objective:** Provide a simple Astro template that can be reused for many businesses.

**Files:**
- Create: `templates/brochure-site/package.json`
- Create: `templates/brochure-site/astro.config.mjs`
- Create: `templates/brochure-site/src/pages/index.astro`
- Create: `templates/brochure-site/src/pages/services.astro`
- Create: `templates/brochure-site/src/pages/about.astro`
- Create: `templates/brochure-site/src/pages/contact.astro`
- Create: `templates/brochure-site/src/layouts/BaseLayout.astro`
- Create: `templates/brochure-site/src/components/SiteHeader.astro`
- Create: `templates/brochure-site/src/styles/global.css`
- Create: `templates/brochure-site/site.json`

**Verification:**
- Run `npm install && npm run build` inside a generated site
- Confirm the generated site builds to static output in `dist/`

### Task 3: Add a site scaffolding helper

**Objective:** Make it fast to start a new client site without hand-copying files.

**Files:**
- Create: `scripts/new_site.py`
- Create: `tests/test_astro_scaffold.py`

**Verification:**
- Run: `python3 -m unittest tests.test_astro_scaffold -v`
- Expected: PASS after the Astro template is in place

### Task 4: Document deployment conventions

**Objective:** Capture how Astro sites should be deployed to Cloudflare Pages.

**Files:**
- Create: `infra/cloudflare/README.md`

**Verification:**
- Confirm the doc explains one Cloudflare Pages project per site folder
- Confirm the doc uses `npm run build` and `dist`
