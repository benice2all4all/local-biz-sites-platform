# Local Business Sites Platform Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Build a reusable repo for managing many low-maintenance local-business brochure sites in parallel.

**Architecture:** Use a multi-project repository with reusable templates, per-client site folders, lightweight helper scripts, and Cloudflare Pages deployment conventions. Keep the first version static-first so each site is easy to host and easy to hand off later.

**Tech Stack:** GitHub, Cloudflare Pages, static HTML/CSS, Python helper scripts.

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

### Task 2: Create a reusable brochure-site template

**Objective:** Provide a simple static template that can be reused for many businesses.

**Files:**
- Create: `templates/brochure-site/index.html`
- Create: `templates/brochure-site/services.html`
- Create: `templates/brochure-site/about.html`
- Create: `templates/brochure-site/contact.html`
- Create: `templates/brochure-site/assets/styles.css`
- Create: `templates/brochure-site/site.json`

**Verification:**
- Open the template files and confirm placeholder values are obvious and easy to replace
- Confirm the site is deployable as static files

### Task 3: Add a site scaffolding helper

**Objective:** Make it fast to start a new client site without hand-copying files.

**Files:**
- Create: `scripts/new_site.py`

**Verification:**
- Run: `python3 scripts/new_site.py demo-site "Demo Site"`
- Expected: `sites/active/demo-site/` exists and placeholders are replaced

### Task 4: Document deployment conventions

**Objective:** Capture how sites should be deployed to Cloudflare Pages.

**Files:**
- Create: `infra/cloudflare/README.md`

**Verification:**
- Confirm the doc explains one Cloudflare Pages project per site folder
- Confirm the doc names the expected publish directory strategy
