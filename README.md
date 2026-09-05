# Morning Glory

Static website with ready-to-serve files in `dist/`. No dependency installation or build step is required.

## Deploy to Vercel

Import this repository and keep **Root Directory** at the repository root (leave the field empty). The root `vercel.json` selects the **Other** framework preset, skips the build command, and publishes `dist/`.

For an existing project, ensure Root Directory is empty and deploy the commit containing `vercel.json`. Alternatively, set Framework Preset to **Other**, enable an empty Build Command override, and set Output Directory to `dist` in Settings > Build and Deployment, then redeploy.

Verify `/`, `/experience/`, and `/assets/morning-glory-logo.svg` after deployment. The nested page is a real HTML page; no SPA fallback rewrite is required.

## Preview locally

Run `python -m http.server 8000 --directory dist`, then open http://localhost:8000.
