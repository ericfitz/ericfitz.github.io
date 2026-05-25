---
name: publish-post
description: >-
  Author and publish a blog post to the efitz writings Hugo blog
  (blog.efitz.net) in one shot. Use when the user wants to publish,
  post, or put something on their blog, or hands over finished prose
  to turn into a live blog post. Handles filename/slug, TOML front
  matter, tags, images, Mermaid diagrams, a local Hugo build check,
  and commit + push straight to main (which deploys the site).
---

# Publish a blog post

This blog is a **Hugo** static site. Posts are Markdown files with **TOML
`+++` front matter** in `content/posts/`. Pushing to `main` triggers the
GitHub Actions workflow (`.github/workflows/hugo.yml`) that builds and
deploys to GitHub Pages — usually live within ~1 minute.

## Operating principles

- **You are doing mechanics, not authoring.** The user's prose is final.
  Do not rewrite, restructure, or "improve" their wording. Fix only
  unambiguous typos, and only if asked. Everything below is plumbing
  around their text.
- **Zero friction.** Do not ask for confirmation before pushing. Run the
  whole flow end to end. The only time to stop and ask is a genuine
  blocker (e.g. the build fails for a reason you can't safely fix, or the
  user gave no title and none can be inferred).

## Steps

### 1. Get the post text and a title
The user provides the finished body text. Determine the **title**:
- Use a title the user gave explicitly.
- Otherwise infer a concise title from the content and state the title you
  chose in one line (no question — just proceed).

### 2. Derive the filename / slug
Slug = title, lowercased, spaces → hyphens, punctuation stripped,
collapsed hyphens. File path: `content/posts/<slug>.md`.
- Match the style of existing files in `content/posts/` (all lowercase,
  hyphenated, descriptive).
- If `content/posts/<slug>.md` already exists, that's an **edit/update** of
  an existing post: keep its original `date`, and you'll refresh `lastmod`
  (see below). Otherwise it's a new post.

### 3. Build the TOML front matter
Wrap in `+++` delimiters. Fields, in this order:

```
+++
title = "Exact Title Here"
date = YYYY-MM-DD
lastmod = YYYY-MM-DD
tags = ["Tag1", "Tag2"]
+++
```

- `date`: today's date for a new post; preserve the existing `date` when
  updating a post.
- `lastmod`: always today's date.
- `title`: double-quoted; escape any embedded double quotes.
- Omit the `tags` line entirely if there are no tags (some existing posts
  have none — that's fine).
- Do **not** set `draft`. Posts publish immediately.

### 4. Tags — reuse the existing taxonomy
Before assigning tags, discover what already exists so you reuse rather
than fragment the taxonomy:

```sh
grep -rh "^tags" content/posts/ | sed 's/^tags = //' | tr ',' '\n' \
  | tr -d '[]" ' | sort -u
```

(Current taxonomy includes: `AI`, `development`, `self-improvement`.)
Prefer matching an existing tag exactly (including capitalization). Assign
1–3 tags. If the post genuinely needs a new tag, add it but **say so in one
line** so the user knows a new tag entered the taxonomy.

### 5. Images
If the user supplied images (paths, attachments, or URLs to download):
- Place files under `static/images/<slug>/` (create the directory).
- Reference them in the Markdown as `/images/<slug>/<filename>` — Hugo
  serves `static/` at the site root.
- Include descriptive **alt text**: `![alt text](/images/<slug>/pic.png)`.
  If you can't determine good alt text, ask the user for a one-line
  description (this is a content question, not a mechanics one).

### 6. Mermaid diagrams
Mermaid works via a theme render hook
(`themes/minimal/layouts/_default/_markup/render-codeblock-mermaid.html`)
plus a conditional CDN loader in `baseof.html`. Authors just use a fenced
block:

````
```mermaid
graph TD
  A --> B
```
````

- These render **client-side as SVG** in the browser; no build-time image
  is produced.
- Sanity-check that any Mermaid block the user provided is syntactically
  valid before publishing. If the `mcp__*__validate_and_render_mermaid_diagram`
  tool is available, use it; otherwise eyeball the syntax.
- If the render hook or the loader in `baseof.html` is somehow missing
  (e.g. theme was reset), recreate them — the post won't render diagrams
  without both.

### 7. Local Hugo build check
Catch front-matter and template errors before they hit the live deploy.
Hugo may not be installed in a fresh cloud container — install the pinned
version (matching the workflow) if needed, then build:

```sh
HUGO_VERSION=0.140.2
if ! command -v hugo >/dev/null 2>&1; then
  wget -qO /tmp/hugo.deb \
    "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb"
  sudo dpkg -i /tmp/hugo.deb
fi
hugo --gc --minify
```

If the build fails, fix the cause (almost always malformed front matter or
a bad Mermaid/template reference) and rebuild. Do not push a failing build.

### 8. Commit and publish (straight to main)
Publishing = pushing to `main`. Commit just the post and any image assets
with a clear message, then push:

```sh
git add content/posts/<slug>.md static/images/<slug>/   # images only if any
git commit -m "Add post: <Title>"     # use "Update post: <Title>" when editing
git push origin HEAD:main
```

- Use `Add post:` for new posts, `Update post:` when revising an existing one.
- If the current branch isn't `main`, still publish by pushing to `main`
  with `git push origin HEAD:main` (the post must land on `main` to deploy).
- After pushing, tell the user it's live shortly at
  `https://blog.efitz.net/posts/<slug>/` and that the Actions deploy takes
  ~1 minute.

## Done
Report: the file path created, the chosen tags (flagging any new one), the
live URL, and that the deploy is in progress.
