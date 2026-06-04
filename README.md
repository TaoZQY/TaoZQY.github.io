# Tao Zhang's Academic Homepage

This repository contains the source for [taozqy.github.io](https://taozqy.github.io), Tao Zhang's academic homepage.

The site is built with Jekyll and GitHub Pages. Main editable content lives in:

- `_pages/about.md` for the homepage
- `_pages/cv.md` for the CV page
- `_publications/` for publication entries
- `_config.yml` for site-wide profile metadata
- `images/tao-zhang.jpg` for the profile photo

## Local Checks

Run the lightweight content check:

```bash
python scripts/validate_site_content.py
```

To preview the full site locally, install Ruby and Bundler, then run:

```bash
bundle install
bundle exec jekyll serve -l -H localhost
```
