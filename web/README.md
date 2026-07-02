# LedgerField website (`web/`)

Static promotional site, guides and wiki for **LedgerField**, served at
`https://www.5mart.ml/ledgerfield/` over the knitweb relay. Deploy base path is
`/ledgerfield/` (all internal links are absolute under that prefix).

## Structure

```
web/
├── index.html                 promotional landing page
├── style.css                  single shared stylesheet (no page ships its own CSS)
├── app.html                   the LedgerField app (generated copy of the SPA)
├── guides/
│   ├── index.html             guides hub
│   ├── getting-started.html
│   ├── bookkeeping.html
│   ├── taxes.html
│   ├── payroll-filing.html
│   ├── datamarket.html
│   └── p2p-sync.html
├── wiki/
│   ├── index.html             glossary index (A–Z + by cluster)
│   ├── knitweb-p2p.html        Knitweb & P2P terms
│   ├── privacy-datamarket.html Privacy & data-market terms
│   ├── accounting.html         Accounting terms
│   └── taxation.html           Taxation terms
├── _content/                  guide + landing bodies (source, JSON)
└── _build/build.mjs           the generator
```

## Regenerating

The **wiki is data-driven**: every definition and every cross-link is generated
from the single `TERMS` registry in `_build/build.mjs`, so cross-links can never
go stale or break. Guide and landing bodies live in `_content/*.json`.

```
node web/_build/build.mjs .        # run from the repo root
```

This rewrites all HTML, copies the current SPA to `app.html`, and runs an internal
link checker (exits non-zero on any broken file link or `#anchor`).

Do not hand-edit the generated `*.html`, `app.html`, or the wiki — edit the
registry (for glossary terms) or `_content/*.json` (for guide/landing prose) and
rebuild.

## Design notes

- Definitions that touch the peer-to-peer layer link straight into the
  [Knitweb & P2P](wiki/knitweb-p2p.html) primitives (CID, gossip, node, relay,
  canonical encoding), so the whole glossary is anchored to the substrate it runs on.
- Content identifiers on the site match the app: a CID is the `sha256` of a
  canonical payload, computed identically for rulesets and market packages.
- Offline-first: only public artefacts (tax rulesets, anonymised aggregates) are
  ever described as leaving the device.
