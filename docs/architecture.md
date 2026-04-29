# Architecture

## Core idea

This repo is a platform/workbench for many small local-business websites, not just a single site.

## Structure choices

- `templates/` holds reusable starting points
- `sites/active/` holds current client work
- `sites/archived/` preserves retired projects
- `shared/` holds reusable copy snippets, brand tokens, and common assets
- `infra/cloudflare/` documents deployment conventions

## Why static first

Static brochure sites are a good default because they are:
- cheap to host
- easy to cache globally
- low maintenance
- easy to transfer into a dedicated repo later

## Deployment model

Each client site should eventually map to:
- one site folder in this repo during active development
- one Cloudflare Pages project for deployment
- one custom domain when ready

## Handoff model

When a client needs full ownership, copy or split their folder into a standalone repo while preserving the same simple file structure.
