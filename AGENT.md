# AGENT.md — maintenance guide

## Scope
- Site: Jekyll, bilingual (en/zh), baseurl set in `_config.yml` (`/personal_website` on GitHub Pages).
- Main assets: `assets/css/style.css`, `assets/js/site.js`, content in Markdown under root and `zh/`. Special landing: `igem/` with its own CSS/JS and docs.

## Editing rules
- Keep bilingual parity: if you add/remove text on an `en` page, mirror in the `zh` version (and set `alt_url` in front matter).
- Nav items live in `_data/navigation.yml`. Update both `en` and `zh` lists when adding/removing sections.
- Page front matter: include `layout`, `title`, `description`, `lang`, `alt_url` (to the other language), and `permalink` if needed.
- Style direction: neon/dark glassmorphism on the main site; iGEM page keeps its own palette from `igem/styles.css`.
- Fonts: global uses Space Grotesk + Noto Sans TC (imported in `assets/css/style.css`); iGEM imports its own Google font set.

## Building & testing
- Install deps: `bundle install`
- Local serve: `bundle exec jekyll serve --livereload`
- Check paths with `relative_url` helpers to respect `baseurl`.

## Version habits
- Use `rg` for search, `apply_patch` for small edits.
- Avoid touching unrelated files; keep deletions intentional (e.g., removed Trading Log and Art pages/nav).
- Commit messages: prefix with area, e.g., `nav: drop trading log` or `igem: sync styles`.
