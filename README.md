# efitz blog

The source for my blog at [blog.efitz.net](https://blog.efitz.net/), built with
[Hugo](https://gohugo.io/) and deployed to GitHub Pages.

Content was originally migrated from efitz.mataroa.blog.

## Structure

- `content/posts/` — blog posts (Markdown with TOML front matter)
- `content/about.md`, `content/projects.md` — standalone pages
- `themes/minimal/` — a small, dependency-free theme (layouts + CSS)
- `hugo.toml` — site configuration
- `static/CNAME` — custom domain for GitHub Pages
- `.github/workflows/hugo.yml` — builds and deploys on push to `main`

## Local development

Requires [Hugo](https://gohugo.io/installation/) (the build pins v0.140.2).

```sh
hugo server -D     # live preview at http://localhost:1313/
hugo new posts/my-post.md
hugo --gc --minify # production build into ./public
```

## Deployment

Pushing to `main` triggers the GitHub Actions workflow, which builds the site
and publishes it to GitHub Pages. The Pages source must be set to
**GitHub Actions** (Settings → Pages → Build and deployment → Source).
