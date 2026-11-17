bergdb.org
==========

This repository is the website [bergdb.org](https://bergdb.org), the site
of BergDB, an embedded, append-only key-value database for Java. BergDB
itself is at [github.com/bergdb/bergdb](https://github.com/bergdb/bergdb).

GitHub Pages serves the site from the root of the `main` branch, at the
custom domain bergdb.org.


Files
-----

* `index.html`: the site, one page. Plain HTML with its CSS in the file;
  no JavaScript, no external fonts or scripts, no cookies, no analytics.
* `404.html`: the page for an address that does not exist. Its `<style>`
  block is a copy of `index.html`'s.
* `CNAME`: the custom domain, one line. GitHub Pages reads it; do not
  remove it.
* `.nojekyll`: empty. It tells GitHub Pages to serve the files as they
  are, without a Jekyll build.


How to change the site
----------------------

Edit `index.html`, open it in a browser to check it (in light and dark
mode, and at a phone's width), commit to `main` and push. GitHub Pages
publishes the new commit by itself.

* After a change of the CSS, copy the `<style>` block to `404.html`.
* At a release of BergDB, change the release's number, date and tag
  under "Status" and "Get it", and the jar's name under "Try it".
* The page's facts come from BergDB's `README.md` and its release notes.
  Change them there first.

The settings of GitHub Pages (Settings, Pages): source "Deploy from a
branch", branch `main`, folder `/ (root)`; custom domain `bergdb.org`;
"Enforce HTTPS" on.


DNS
---

The domain bergdb.org needs these records. The addresses are GitHub
Pages'.

| Name           | Type  | Value               |
|----------------|-------|---------------------|
| bergdb.org     | A     | 185.199.108.153     |
| bergdb.org     | A     | 185.199.109.153     |
| bergdb.org     | A     | 185.199.110.153     |
| bergdb.org     | A     | 185.199.111.153     |
| bergdb.org     | AAAA  | 2606:50c0:8000::153 |
| bergdb.org     | AAAA  | 2606:50c0:8001::153 |
| bergdb.org     | AAAA  | 2606:50c0:8002::153 |
| bergdb.org     | AAAA  | 2606:50c0:8003::153 |
| www.bergdb.org | CNAME | bergdb.github.io    |

The domain bergdb.org is verified for the GitHub organisation `bergdb`,
so only the organisation's repositories can publish a site at it.

