# Brochure site template

This is the default Astro template for low-maintenance local business websites.

Replace placeholder values such as:
- `__BUSINESS_NAME__`
- `__TAGLINE__`
- `__PHONE__`
- `__EMAIL__`
- `__CITY_STATE__`

Default image slots included in every scaffolded site:
- `public/images/logo.svg`
- `public/images/hero.svg`
- `public/images/feature.svg`
- `public/images/gallery-1.svg`
- `public/images/gallery-2.svg`
- `public/images/gallery-3.svg`

These are wired through `site.json` so they can be replaced later with real business photos, logos, storefront shots, service images, or portfolio/gallery items.

Typical workflow:

```bash
npm install
npm run dev
npm run build
```

The template uses static output so it deploys cleanly to Cloudflare Pages.
