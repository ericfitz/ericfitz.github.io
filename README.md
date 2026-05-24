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
- `.github/workflows-template/hugo.yml` — the deploy workflow, staged here until
  it is activated (see Deployment below)

## Local development

Requires [Hugo](https://gohugo.io/installation/) (the build pins v0.140.2).

```sh
hugo server -D     # live preview at http://localhost:1313/
hugo new posts/my-post.md
hugo --gc --minify # production build into ./public
```

## Deployment

The deploy workflow is staged at `.github/workflows-template/hugo.yml` because
it could not be pushed into `.github/workflows/` from the environment that
created it (that requires the `workflow` OAuth scope). To activate it, run from
a machine whose credentials have that scope (or move it via the GitHub web UI):

```sh
git mv .github/workflows-template/hugo.yml .github/workflows/hugo.yml
git commit -m "Activate Hugo Pages workflow"
git push
```

Once active, pushing to `main` builds the site and publishes it to GitHub Pages.
The Pages source must also be set to **GitHub Actions**
(Settings → Pages → Build and deployment → Source).
