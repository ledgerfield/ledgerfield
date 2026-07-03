// LedgerField site generator → writes static HTML into web/
// Wiki is fully data-driven from TERMS, so cross-links can never break.
// Guide + landing bodies come from content/*.json (produced by the workflow);
// if a body file is missing, a placeholder is emitted so the site still builds.
import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.argv[2] || '/tmp/lf-sprint';
const WEB = path.join(ROOT, 'web');
const CONTENT = path.join(WEB, '_content');           // guide/landing bodies (json)
const BASE = '/ledgerfield';                           // deploy base: www.5mart.ml/ledgerfield/
const ORIGIN = 'https://www.5mart.ml';                 // absolute origin for canonical / og: URLs
// Inline SVG favicon (a ledger "L" mark) — no external asset, CSP-safe.
const FAVICON = 'data:image/svg+xml,' + encodeURIComponent(
  '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#6c63ff"/><path d="M9 8v16h14" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M13 13h8M13 17.5h6" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".85"/></svg>');
function canonUrl(file) {
  if (!file || file === 'index.html') return BASE + '/';
  if (file.endsWith('/index.html')) return BASE + '/' + file.slice(0, -'index.html'.length);
  return BASE + '/' + file;
}

// ── glossary registry (single source of truth for the wiki) ──────────────────
const CLUSTERS = {
  knitweb:    { file: 'knitweb-p2p.html',       title: 'Knitweb & P2P' },
  privacy:    { file: 'privacy-datamarket.html', title: 'Privacy & Data market' },
  accounting: { file: 'accounting.html',         title: 'Accounting' },
  taxation:   { file: 'taxation.html',           title: 'Taxation' },
};

// def: HTML string. related/knitweb: arrays of term ids (auto-resolved to file#anchor).
const TERMS = [
  // ── knitweb / p2p ──────────────────────────────────────────────────────────
  { id:'knitweb', term:'Knitweb', cluster:'knitweb',
    def:`The peer-to-peer knowledge-web primitive LedgerField rides on. A knitweb is an append-only mesh of content-addressed records that peers replicate directly, with no central server. Public tax rulesets and anonymised market aggregates travel this mesh; private books never do.`,
    related:['pulse','knitwebs','gossip'], knitweb:[] },
  { id:'pulse', term:'Pulse', cluster:'knitweb',
    def:`The CID-stable, event-sourced runtime that implements the knitweb protocol. Pulse guarantees that the same logical record produces the same identifier on every peer, which is what lets independently-run nodes agree on a ruleset or aggregate without trusting each other.`,
    related:['knitweb','canonical-encoding','cid'], knitweb:[] },
  { id:'knitwebs', term:'Knitwebs (domain plugins)', cluster:'knitweb',
    def:`Domain-specific webs built on the primitive — a chemistry knitweb, an accounting knitweb, and so on. LedgerField's ruleset exchange is a knitweb whose records are jurisdiction tax parameters.`,
    related:['knitweb','ruleset'], knitweb:[] },
  { id:'cid', term:'CID — Content Identifier', cluster:'knitweb',
    def:`A <code>sha256</code> hash of a record's canonical payload, used as its address. Because the address is derived from the bytes, two peers that hold the same ruleset or data package compute the same CID and know they hold the same thing.`,
    related:['content-addressing','canonical-encoding'], knitweb:[] },
  { id:'content-addressing', term:'Content addressing', cluster:'knitweb',
    def:`Referring to data by <em>what it is</em> (its hash) rather than <em>where it lives</em> (a URL). It makes records immutable, verifiable and cache-friendly across a mesh of untrusted peers.`,
    related:['cid'], knitweb:[] },
  { id:'canonical-encoding', term:'Canonical encoding', cluster:'knitweb',
    def:`A deterministic serialization (sorted keys, fixed number formatting) so that semantically-identical data always yields identical bytes — and therefore an identical <a href="#cid">CID</a>. LedgerField sorts object keys before hashing both rulesets and market packages.`,
    related:['cid','content-addressing'], knitweb:[] },
  { id:'gossip', term:'Gossip / anti-entropy', cluster:'knitweb',
    def:`The propagation mechanism: peers periodically exchange the records they have, converging on the full set without any coordinator. New rulesets spread peer-to-peer this way.`,
    related:['node','relay'], knitweb:[] },
  { id:'node', term:'Node', cluster:'knitweb',
    def:`A single peer. Its identity is a <code>SHA-256</code> id derived without personal data, so participation carries no PII. k-anonymity counts distinct nodes, not rows.`,
    related:['gossip','relay'], knitweb:[] },
  { id:'relay', term:'Relay', cluster:'knitweb',
    def:`A well-known rendezvous node that helps peers behind firewalls find each other and exchange gossip. LedgerField's public relay is <a href="#relay-5mart">5mart.ml</a>.`,
    related:['relay-5mart','gossip','node'], knitweb:[] },
  { id:'relay-5mart', term:'5mart.ml relay', cluster:'knitweb',
    def:`The public knitweb relay that hosts this site (<code>www.5mart.ml/ledgerfield</code>) and carries LedgerField ruleset and aggregate gossip. Running your own relay is optional — the mesh works peer-to-peer.`,
    related:['relay','pulse'], knitweb:[] },
  // ── privacy / data market ───────────────────────────────────────────────────
  { id:'k-anonymity', term:'k-anonymity (k ≥ 5)', cluster:'privacy',
    def:`A privacy floor: an aggregate is only published once at least <b>K_MIN = 5</b> distinct <a href="/ledgerfield/wiki/knitweb-p2p.html#node">nodes</a> have contributed to it, so no single business can be singled out. Below the threshold, publication is refused.`,
    related:['aggregate','data-package','consent'], knitweb:['node'] },
  { id:'aggregate', term:'Aggregate (AggregateStats)', cluster:'privacy',
    def:`A privacy-preserving summary of many contributions — <code>count, min, max, mean, median, p25, p75</code>. Only the summary is ever shared; the underlying figures stay on each node.`,
    related:['k-anonymity','data-package'], knitweb:[] },
  { id:'data-package', term:'Data package', cluster:'privacy',
    def:`The unit sold on the market: a CID-addressed bundle of an <a href="#aggregate">aggregate</a> plus its category, jurisdiction, sector, year and contributor count.`,
    related:['aggregate','revenue-distribution'], knitweb:['cid','content-addressing'] },
  { id:'consent', term:'Consent', cluster:'privacy',
    def:`Per <a href="#data-category">category</a> and jurisdiction opt-in. Default is to share nothing; you explicitly grant each category you want to contribute, and can revoke at any time.`,
    related:['data-category','k-anonymity'], knitweb:[] },
  { id:'data-category', term:'Data categories (7)', cluster:'privacy',
    def:`The seven shareable aggregate types: salary benchmarks, cost ratios, margin benchmarks, effective tax rates, cash-flow patterns, payroll costs and invoice cycles.`,
    related:['consent'], knitweb:[] },
  { id:'revenue-distribution', term:'Revenue distribution', cluster:'privacy',
    def:`When a package sells, proceeds (after the <a href="#platform-fee">platform fee</a>) are split across the contributing nodes — either equally or weighted by contribution.`,
    related:['data-package','platform-fee'], knitweb:['node'] },
  { id:'platform-fee', term:'Platform fee', cluster:'privacy',
    def:`A small percentage retained by the marketplace on each sale (10% in the reference UI); the remainder is distributed to contributors.`,
    related:['revenue-distribution'], knitweb:[] },
  { id:'vault', term:'Vault', cluster:'privacy',
    def:`The local encrypted store (PBKDF2-HMAC-SHA256, HMAC-authenticated). Your ledgers, entities and payroll live here in the browser; raw data never leaves the device.`,
    related:['offline-first'], knitweb:['node'] },
  { id:'offline-first', term:'Offline-first', cluster:'privacy',
    def:`The whole application runs in your browser with no server. Only public artefacts — anonymised aggregates and tax rulesets — ever touch the network, and only over the knitweb.`,
    related:['vault','ruleset'], knitweb:['gossip'] },
  // ── accounting ───────────────────────────────────────────────────────────────
  { id:'chart-of-accounts', term:'Chart of accounts', cluster:'accounting',
    def:`The account structure of the ledger. LedgerField ships NL (RGS), UK (FRS 102) and US (GAAP) charts, plus country schemas for 100+ jurisdictions.`,
    related:['journal-entry','trial-balance'], knitweb:[] },
  { id:'journal-entry', term:'Journal entry', cluster:'accounting',
    def:`A dated line with a debit account, a credit account and an amount — the atom of double-entry bookkeeping.`,
    related:['chart-of-accounts','trial-balance'], knitweb:[] },
  { id:'trial-balance', term:'Trial balance', cluster:'accounting',
    def:`The per-account sum of debits and credits; it must balance before you close a period.`,
    related:['journal-entry','profit-loss'], knitweb:[] },
  { id:'profit-loss', term:'Profit & loss (Winst & Verlies)', cluster:'accounting',
    def:`Revenue minus costs over a period. LedgerField derives it directly from your journal entries.`,
    related:['trial-balance'], knitweb:[] },
  { id:'entity', term:'Entity / holding structure', cluster:'accounting',
    def:`A company in your structure (BV, Holding, ZZP, Ltd, GmbH…), optionally nested under a parent. Reports and filings are scoped per entity.`,
    related:['chart-of-accounts'], knitweb:[] },
  { id:'saft', term:'SAF-T export', cluster:'accounting',
    def:`Standard Audit File for Tax — an XML export of your ledger for tax authorities. Deterministically generated from the same canonical data model.`,
    related:['journal-entry'], knitweb:['canonical-encoding'] },
  // ── taxation ─────────────────────────────────────────────────────────────────
  { id:'vpb', term:'VPB — NL corporate income tax', cluster:'taxation',
    def:`Vennootschapsbelasting: 19% up to €200k taxable profit, 25.8% above (2025). Built-in calculator with effective-rate output.`,
    related:['ib','cit','effective-rate'], knitweb:[] },
  { id:'ib', term:'IB — NL personal income tax', cluster:'taxation',
    def:`Inkomstenbelasting across Box 1 (work), Box 2 (substantial-interest dividend) and Box 3 (wealth), with the 2025 brackets and credits.`,
    related:['vpb','dga'], knitweb:[] },
  { id:'wbso', term:'WBSO — R&D payroll credit', cluster:'taxation',
    def:`A Dutch payroll-tax reduction on qualifying R&D wage costs (32%, or 40% for starters, on the first band). Modelled in the tax tab.`,
    related:['vpb'], knitweb:[] },
  { id:'dga', term:'DGA gebruikelijk loon', cluster:'taxation',
    def:`The customary-salary rule for director-shareholders. The 2025 benchmark (ijkpunt) is <b>€41,138</b>; the app flags salaries below the norm as a correction risk.`,
    related:['ib'], knitweb:[] },
  { id:'btw', term:'BTW — VAT', cluster:'taxation',
    def:`Value-added tax (21% standard NL). Quarterly return helper computes VAT charged minus deductible input VAT.`,
    related:['vpb'], knitweb:[] },
  { id:'cit', term:'CIT — corporate income tax (global)', cluster:'taxation',
    def:`Corporate income tax modelled for 100+ jurisdictions from CID-addressed <a href="#ruleset">rulesets</a>, each with its own brackets, entity types and 2025 rates.`,
    related:['vpb','ruleset','effective-rate'], knitweb:['cid'] },
  { id:'effective-rate', term:'Effective tax rate', cluster:'taxation',
    def:`Tax actually payable divided by the taxable base — the number that matters for benchmarking, and one of the seven shareable aggregate categories.`,
    related:['cit','vpb','data-category'], knitweb:[] },
  { id:'ruleset', term:'Ruleset', cluster:'taxation',
    def:`A jurisdiction's tax parameters as a canonical JSON, addressed by <a href="/ledgerfield/wiki/knitweb-p2p.html#cid">CID</a> and shared peer-to-peer over <a href="/ledgerfield/wiki/knitweb-p2p.html#gossip">gossip</a>. Rates are public-domain, so rulesets are safe to replicate; you verify one by recomputing its CID.`,
    related:['cit','btw','vpb'], knitweb:['cid','gossip','canonical-encoding'] },
  { id:'payroll', term:'Payroll (loonstrook)', cluster:'taxation',
    def:`Gross-to-net payslip generation with employer burden (pension, WW, WIA, ZVW), plus the DGA customary-salary check.`,
    related:['dga'], knitweb:[] },
];

const TERM_BY_ID = Object.fromEntries(TERMS.map(t => [t.id, t]));
const hrefFor = id => {
  const t = TERM_BY_ID[id];
  if (!t) throw new Error('unknown term id referenced: ' + id);
  return `${BASE}/wiki/${CLUSTERS[t.cluster].file}#${id}`;
};
const linkTerm = id => `<a href="${hrefFor(id)}">${TERM_BY_ID[id].term}</a>`;

// ── page template ────────────────────────────────────────────────────────────
const NAV = [
  { href:`${BASE}/`,               label:'Home',   key:'home' },
  { href:`${BASE}/guides/`,        label:'Guides', key:'guides' },
  { href:`${BASE}/wiki/`,          label:'Wiki',   key:'wiki' },
  { href:`${BASE}/coverage.html`,  label:'Coverage', key:'coverage' },
  { href:`${BASE}/app.html`,       label:'Open app', key:'app', cta:true },
];
function wrap({ title, desc, active, main, file, noindex }) {
  const nav = NAV.map(n => {
    const cls = n.cta ? ' class="cta"' : (n.key === active ? ' class="active"' : '');
    const cur = n.key === active ? ' aria-current="page"' : '';
    return `<a href="${n.href}"${cls}${cur}>${n.label}</a>`;
  }).join('');
  const esc = s => String(s).replace(/"/g, '&quot;');
  const url = ORIGIN + canonUrl(file);
  const full = `${title} · LedgerField`;
  const img = `${ORIGIN}${BASE}/social-card.svg`;
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${full}</title>
<meta name="description" content="${esc(desc)}">
<link rel="canonical" href="${url}">
<meta name="theme-color" content="#0d1117">
<link rel="icon" href="${FAVICON}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="LedgerField">
<meta property="og:title" content="${esc(full)}">
<meta property="og:description" content="${esc(desc)}">
<meta property="og:url" content="${url}">
<meta property="og:image" content="${img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${esc(full)}">
<meta name="twitter:description" content="${esc(desc)}">
<meta name="twitter:image" content="${img}">
${noindex ? '<meta name="robots" content="noindex">\n' : ''}<link rel="stylesheet" href="${BASE}/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="bar">
  <a href="${BASE}/" class="brand">LedgerField<span>offline P2P accounting</span></a>
  <nav aria-label="Primary">${nav}</nav>
</div></header>
<main id="main" class="wrap" tabindex="-1">
${main}
</main>
<footer class="site"><div class="inner">
  <div class="relay">
    <h4>LedgerField</h4>
    Offline-first, privacy-first accounting for 100+ jurisdictions.<br>
    Served peer-to-peer over the knitweb relay <code>5mart.ml</code>. No server, no cloud, no telemetry.
  </div>
  <div class="cols">
    <div><h4>Docs</h4>
      <a href="${BASE}/guides/">Guides</a><br>
      <a href="${BASE}/wiki/">Wiki</a><br>
      <a href="${BASE}/coverage.html">Coverage</a><br>
      <a href="${BASE}/faq.html">FAQ</a><br>
      <a href="${BASE}/app.html">Open the app</a></div>
    <div><h4>Project</h4>
      <a href="https://github.com/ledgerfield/ledgerfield">GitHub</a><br>
      <a href="${BASE}/wiki/knitweb-p2p.html">Knitweb &amp; P2P</a><br>
      <a href="${BASE}/wiki/privacy-datamarket.html">Privacy model</a></div>
  </div>
</div></footer>
</body>
</html>`;
}

// ── wiki rendering (data-driven) ─────────────────────────────────────────────
function renderDef(t) {
  const rel = t.related.length
    ? `<div class="rel"><b>Related:</b> ${t.related.map(linkTerm).join(' · ')}</div>` : '';
  const kw = t.knitweb.length
    ? `<div class="kw"><b>On the knitweb:</b> ${t.knitweb.map(linkTerm).join(' · ')}</div>` : '';
  return `<article class="wiki-def" id="${t.id}">
  <h3>${t.term} <a class="anchor" href="#${t.id}" aria-label="Permalink to ${t.term}">#</a></h3>
  <p>${t.def}</p>
  ${rel}${kw}
</article>`;
}
function clusterPage(key) {
  const c = CLUSTERS[key];
  const defs = TERMS.filter(t => t.cluster === key);
  const main = `<div class="crumbs"><a href="${BASE}/">Home</a> / <a href="${BASE}/wiki/">Wiki</a> / ${c.title}</div>
<h1>${c.title}</h1>
<p>${defs.length} definitions. Every term links to related concepts and, where it touches the mesh, to the underlying <a href="${BASE}/wiki/knitweb-p2p.html">knitweb / P2P</a> primitives.</p>
${defs.map(renderDef).join('\n')}`;
  return { file: `wiki/${c.file}`, html: wrap({ title: c.title, desc: `${c.title} glossary — LedgerField`, active:'wiki', main, file: `wiki/${c.file}` }) };
}
function wikiIndex() {
  const sorted = [...TERMS].sort((a,b) => a.term.localeCompare(b.term));
  const byLetter = {};
  for (const t of sorted) { const L = t.term.replace(/^[^A-Za-z]*/,'')[0].toUpperCase(); (byLetter[L] ||= []).push(t); }
  const alpha = Object.keys(byLetter).sort().map(L => `<a href="#L${L}">${L}</a>`).join('');
  const groups = Object.keys(byLetter).sort().map(L =>
    `<h2 id="L${L}">${L}</h2><ul class="wiki-toc">${byLetter[L].map(t =>
      `<li><a href="${hrefFor(t.id)}">${t.term}</a> <span class="tag">${CLUSTERS[t.cluster].title}</span></li>`).join('')}</ul>`
  ).join('\n');
  const clusters = Object.entries(CLUSTERS).map(([k,c]) =>
    `<a class="feature" href="${BASE}/wiki/${c.file}"><h3>${c.title}</h3><p>${TERMS.filter(t=>t.cluster===k).length} terms</p></a>`).join('');
  const main = `<div class="crumbs"><a href="${BASE}/">Home</a> / Wiki</div>
<h1>Wiki &amp; glossary</h1>
<p>Every LedgerField concept, cross-linked. Definitions that touch the peer-to-peer layer link straight into the <a href="${BASE}/wiki/knitweb-p2p.html">knitweb</a> primitives that make them work.</p>
<div class="feature-grid">${clusters}</div>
<div class="alpha">${alpha}</div>
${groups}`;
  return { file:'wiki/index.html', html: wrap({ title:'Wiki', desc:'LedgerField glossary — every concept cross-linked to the knitweb P2P layer.', active:'wiki', main, file:'wiki/index.html' }) };
}

// ── guide + landing rendering (bodies from _content, else placeholder) ───────
function loadBody(slug) {
  const p = path.join(CONTENT, slug + '.json');
  if (fs.existsSync(p)) return JSON.parse(fs.readFileSync(p,'utf8'));
  return null;
}
const GUIDES = [
  { slug:'getting-started', title:'Getting started' },
  { slug:'bookkeeping',     title:'Bookkeeping' },
  { slug:'taxes',           title:'Taxes' },
  { slug:'payroll-filing',  title:'Payroll & filing' },
  { slug:'datamarket',      title:'Data market' },
  { slug:'p2p-sync',        title:'P2P ruleset sync' },
];
function guidePage(g) {
  const body = loadBody('guide-' + g.slug);
  const main = `<div class="crumbs"><a href="${BASE}/">Home</a> / <a href="${BASE}/guides/">Guides</a> / ${g.title}</div>
<h1>${g.title}</h1>
${body ? body.main_html : `<p class="note">${g.title} guide — content pending.</p>`}
<hr><p><a href="${BASE}/guides/">← All guides</a></p>`;
  return { file:`guides/${g.slug}.html`, html: wrap({ title:g.title, desc: body?.desc || `${g.title} — LedgerField guide`, active:'guides', main, file:`guides/${g.slug}.html` }) };
}
function guidesIndex() {
  const cards = GUIDES.map(g => {
    const body = loadBody('guide-' + g.slug);
    return `<a class="feature" href="${BASE}/guides/${g.slug}.html"><h3>${g.title}</h3><p>${body?.desc || ''}</p></a>`;
  }).join('');
  const main = `<div class="crumbs"><a href="${BASE}/">Home</a> / Guides</div>
<h1>Guides</h1>
<p>Step-by-step, from your first entity to selling anonymised benchmarks on the data market. New to the concepts? Keep the <a href="${BASE}/wiki/">wiki</a> open alongside.</p>
<div class="feature-grid">${cards}</div>`;
  return { file:'guides/index.html', html: wrap({ title:'Guides', desc:'LedgerField how-to guides.', active:'guides', main, file:'guides/index.html' }) };
}
function landing() {
  const body = loadBody('landing');
  const main = body ? body.main_html : `<section class="hero"><h1>LedgerField</h1><p class="tagline">Offline P2P accounting.</p></section>`;
  return { file:'index.html', html: wrap({ title:'Offline P2P accounting', desc: body?.desc || 'LedgerField — offline-first, privacy-first accounting for 100+ jurisdictions, synced peer-to-peer over the knitweb.', active:'home', main, file:'index.html' }) };
}

// ── coverage page (data-driven from repo dirs + rulesets) ────────────────────
const COUNTRY = { AR:'Argentina', AU:'Australia', BE:'Belgium', BR:'Brazil', CA:'Canada', CH:'Switzerland', CN:'China', DE:'Germany', DK:'Denmark', ES:'Spain', FI:'Finland', FR:'France', HK:'Hong Kong', IE:'Ireland', IN:'India', IT:'Italy', JP:'Japan', MX:'Mexico', NL:'Netherlands', NO:'Norway', NZ:'New Zealand', PL:'Poland', PT:'Portugal', SE:'Sweden', SG:'Singapore', TW:'Taiwan', UK:'United Kingdom', US:'United States', ZA:'South Africa' };
const REGION = { Europe:['BE','CH','DE','DK','ES','FI','FR','IE','IT','NL','NO','PL','PT','SE','UK'], Americas:['AR','BR','CA','MX','US'], 'Asia-Pacific':['AU','CN','HK','IN','JP','NZ','SG','TW'], Africa:['ZA'] };
const regionOf = cc => Object.keys(REGION).find(r => REGION[r].includes(cc)) || 'Other';
function dirCodes(rel) {
  const d = path.join(ROOT, rel);
  if (!fs.existsSync(d)) return new Set();
  return new Set(fs.readdirSync(d).filter(n => /^[A-Z]{2}$/.test(n)));
}
function citHeadline(cc) {
  const f = path.join(ROOT, 'rulesets', cc + '_2025.json');
  if (!fs.existsSync(f)) return null;
  let d; try { d = JSON.parse(fs.readFileSync(f, 'utf8')); } catch (e) { return null; }
  const c = (d.parameters || {}).corporate_income_tax;
  if (!c) return null;
  const norm = r => r <= 1 ? r * 100 : r;                 // rulesets store fraction OR percent
  const pct = x => (Math.round(x * 100) / 100) + '%';
  if (typeof c.flat_rate === 'number') return pct(norm(c.flat_rate));
  if (Array.isArray(c.brackets) && c.brackets.length) {
    const rs = c.brackets.map(b => b.rate).filter(x => typeof x === 'number');
    if (rs.length) { const top = norm(Math.max(...rs)); return new Set(rs).size > 1 ? 'up to ' + pct(top) : pct(top); }
  }
  if (typeof c.rate === 'number') return pct(norm(c.rate));
  return null;
}
function coverage() {
  const schemas = dirCodes('src/ledgerfield/schemas'), tax = dirCodes('src/ledgerfield/tax'),
        payroll = dirCodes('src/ledgerfield/payroll'), filing = dirCodes('src/ledgerfield/filing');
  const rulesets = new Set(fs.readdirSync(path.join(ROOT, 'rulesets')).filter(n => /^[A-Z]{2}_/.test(n)).map(n => n.slice(0, 2)));
  const codes = [...new Set([...schemas, ...tax])].sort((a, b) => (COUNTRY[a] || a).localeCompare(COUNTRY[b] || b));
  const y = '<span class="cov y">&#10003;</span>', n = '<span class="cov n">&middot;</span>';
  const rows = codes.map(cc => {
    const cit = citHeadline(cc);
    return `<tr data-name="${(COUNTRY[cc] || cc).toLowerCase()} ${cc.toLowerCase()}" data-region="${regionOf(cc)}">
    <td><b>${COUNTRY[cc] || cc}</b> <span class="tag">${cc}</span></td>
    <td>${regionOf(cc)}</td>
    <td>${schemas.has(cc) ? y : n}</td>
    <td>${tax.has(cc) ? y : n}</td>
    <td>${rulesets.has(cc) ? y : n}</td>
    <td>${payroll.has(cc) ? y : n}</td>
    <td>${filing.has(cc) ? y : n}</td>
    <td>${cit || '<span class="muted">&mdash; in app</span>'}</td>
  </tr>`;
  }).join('\n');
  const main = `<div class="crumbs"><a href="${BASE}/">Home</a> / Coverage</div>
<h1>Jurisdiction coverage</h1>
<p>${codes.length} jurisdictions &middot; ${tax.size} tax engines &middot; ${rulesets.size} 2025 rulesets &middot; payroll &amp; filing: NL (more on the roadmap). Rates are computed in full inside the <a href="${BASE}/app.html">app</a> &mdash; the headline <a href="${BASE}/wiki/taxation.html#cit">CIT</a> here is indicative only.</p>
<div class="covbar">
  <input id="covq" type="text" placeholder="Search country…" oninput="covFilter()">
  <select id="covr" onchange="covFilter()"><option value="">All regions</option>${Object.keys(REGION).map(r => `<option value="${r}">${r}</option>`).join('')}</select>
</div>
<table id="covtab">
<thead><tr><th>Country</th><th>Region</th><th>CoA</th><th>Tax</th><th>Ruleset</th><th>Payroll</th><th>Filing</th><th>Headline CIT</th></tr></thead>
<tbody>
${rows}
</tbody></table>
<p id="covcount" class="muted"></p>
<div class="note">Legend &mdash; <b>CoA</b>: chart of accounts &middot; <b>Tax</b>: tax-calculation engine &middot; <b>Ruleset</b>: CID-addressed 2025 <a href="${BASE}/wiki/taxation.html#ruleset">ruleset</a> &middot; <b>Payroll</b> / <b>Filing</b>: country modules. A missing dot means &ldquo;not yet &mdash; contributions welcome&rdquo;.</div>
<script>
function covFilter(){
  var q=document.getElementById('covq').value.toLowerCase().trim();
  var r=document.getElementById('covr').value;
  var rows=document.querySelectorAll('#covtab tbody tr'),shown=0;
  rows.forEach(function(tr){
    var ok=(!q||tr.dataset.name.indexOf(q)>-1)&&(!r||tr.dataset.region===r);
    tr.style.display=ok?'':'none'; if(ok)shown++;
  });
  document.getElementById('covcount').textContent=shown+' of '+rows.length+' shown';
}
covFilter();
</script>`;
  return { file:'coverage.html', html: wrap({ title:'Coverage', desc:'LedgerField jurisdiction coverage — chart of accounts, tax engine, rulesets, payroll and filing per country.', active:'coverage', main, file:'coverage.html' }) };
}

const FAQS = [
  { q:'Is my financial data safe?', a:`Yes. Your books live in an encrypted <a href="${BASE}/wiki/privacy-datamarket.html#vault">vault</a> (PBKDF2-HMAC-SHA256) inside your own browser. LedgerField is <a href="${BASE}/wiki/privacy-datamarket.html#offline-first">offline-first</a> — raw data never leaves your device.` },
  { q:'Do I need an internet connection?', a:`No. The whole app is a single HTML file that runs offline. A connection is only needed if you choose to sync public tax <a href="${BASE}/wiki/taxation.html#ruleset">rulesets</a> or publish anonymised aggregates — see the <a href="${BASE}/guides/p2p-sync.html">P2P sync guide</a>.` },
  { q:'Which countries are supported?', a:`Chart of accounts and the tax engine cover 100+ jurisdictions, with 25 CID-addressed 2025 rulesets shipping today. See the full <a href="${BASE}/coverage.html">coverage matrix</a>.` },
  { q:'How do tax rates stay up to date?', a:`Rates live in <a href="${BASE}/wiki/taxation.html#ruleset">rulesets</a> addressed by <a href="${BASE}/wiki/knitweb-p2p.html#cid">CID</a> and shared peer-to-peer via <a href="${BASE}/wiki/knitweb-p2p.html#gossip">gossip</a>. You verify any ruleset by recomputing its content ID — no trust in a server required.` },
  { q:'What is the data market, and is it private?', a:`An opt-in marketplace for anonymised benchmarks. You <a href="${BASE}/wiki/privacy-datamarket.html#consent">consent</a> per category, and an aggregate is only publishable at <a href="${BASE}/wiki/privacy-datamarket.html#k-anonymity">k&#8805;5</a> distinct contributors. Only summaries ever leave your device — see the <a href="${BASE}/guides/datamarket.html">data-market guide</a>.` },
  { q:'Is it free and open source?', a:`Yes — the project is open source on <a href="https://github.com/ledgerfield/ledgerfield">GitHub</a>.` },
  { q:'Can I manage multiple entities?', a:`Yes. Add any number of <a href="${BASE}/wiki/accounting.html#entity">entities</a> (BV, Holding, ZZP, Ltd, GmbH…) with parent/holding structures; reports and filings are scoped per entity.` },
  { q:'How do I back up my data?', a:`Export an encrypted backup of your <a href="${BASE}/wiki/privacy-datamarket.html#vault">vault</a> from the Vault tab, then restore it on any device with your password.` },
  { q:'Does it replace my accountant?', a:`No — it is a tool. You keep the books and compute figures locally, then export JSON or <a href="${BASE}/wiki/accounting.html#saft">SAF-T XML</a> to hand to your accountant or file with the authority.` },
  { q:'What is the knitweb, and who runs the relay?', a:`The <a href="${BASE}/wiki/knitweb-p2p.html#knitweb">knitweb</a> is the peer-to-peer layer (built on <a href="${BASE}/wiki/knitweb-p2p.html#pulse">pulse</a>) that carries public artefacts. The default public <a href="${BASE}/wiki/knitweb-p2p.html#relay-5mart">relay is 5mart.ml</a>, but the mesh works peer-to-peer and you can run your own.` },
];
const stripTags = s => s.replace(/<[^>]+>/g, '').replace(/&#8805;/g, '≥').replace(/\s+/g, ' ').trim();
function faqPage() {
  const items = FAQS.map(f => `<details class="faq-item"><summary>${f.q}</summary><div class="faq-a">${f.a}</div></details>`).join('\n');
  const ld = { '@context':'https://schema.org', '@type':'FAQPage', mainEntity: FAQS.map(f => ({ '@type':'Question', name: f.q, acceptedAnswer: { '@type':'Answer', text: stripTags(f.a) } })) };
  const main = `<div class="crumbs"><a href="${BASE}/">Home</a> / FAQ</div>
<h1>Frequently asked questions</h1>
<p>Short answers, with links into the <a href="${BASE}/wiki/">wiki</a> and <a href="${BASE}/guides/">guides</a> for depth.</p>
<div class="faq">
${items}
</div>
<div class="note">Still stuck? The <a href="${BASE}/guides/">guides</a> walk through every tab step by step.</div>
<script type="application/ld+json">${JSON.stringify(ld)}</script>`;
  return { file:'faq.html', html: wrap({ title:'FAQ', desc:'LedgerField FAQ — data safety, offline use, country coverage, the data market and the knitweb P2P layer.', active:'', main, file:'faq.html' }) };
}

function notFound() {
  const main = `<section class="hero" style="padding-top:30px">
  <h1>404 &mdash; page not found</h1>
  <p class="tagline">That page isn&rsquo;t in the ledger. It may have moved, or never existed.</p>
  <div style="margin-top:18px">
    <a class="cta" href="${BASE}/">Home</a>
    <a class="cta secondary" href="${BASE}/guides/">Guides</a>
    <a class="cta secondary" href="${BASE}/wiki/">Wiki</a>
    <a class="cta secondary" href="${BASE}/coverage.html">Coverage</a>
  </div>
</section>`;
  return { file:'404.html', noindex:true, html: wrap({ title:'Page not found', desc:'404 — page not found.', active:'', main, file:'404.html', noindex:true }) };
}

// ── build ────────────────────────────────────────────────────────────────────
const pages = [
  landing(), guidesIndex(), ...GUIDES.map(guidePage),
  wikiIndex(), ...Object.keys(CLUSTERS).map(clusterPage), coverage(), faqPage(), notFound(),
];
for (const p of pages) {
  const out = path.join(WEB, p.file);
  fs.mkdirSync(path.dirname(out), { recursive:true });
  fs.writeFileSync(out, p.html);
}
// copy the SPA so "Open app" works on the served site
const spa = path.join(ROOT, 'src/ledgerfield/static/ledgerfield.html');
if (fs.existsSync(spa)) fs.copyFileSync(spa, path.join(WEB, 'app.html'));

// ── social card (1200×630 SVG, referenced by og:image) ───────────────────────
const badge = (x, w, label) => `<g transform="translate(${x},432)"><rect width="${w}" height="54" rx="27" fill="#161b22" stroke="#30363d"/><text x="${w/2}" y="35" text-anchor="middle" font-size="26" fill="#c9d1e8">${label}</text></g>`;
const socialCard = `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" font-family="system-ui,Segoe UI,Roboto,sans-serif">
<defs><radialGradient id="g" cx="18%" cy="-10%" r="110%"><stop offset="0%" stop-color="#1c1748"/><stop offset="55%" stop-color="#0d1117"/></radialGradient></defs>
<rect width="1200" height="630" fill="url(#g)"/>
<rect width="1200" height="8" fill="#6c63ff"/>
<g transform="translate(80,80)">
  <rect width="74" height="74" rx="17" fill="#6c63ff"/>
  <path d="M22 19v40h34" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M31 31h20M31 43h15" stroke="#fff" stroke-width="5.5" stroke-linecap="round" opacity=".85"/>
  <text x="98" y="50" fill="#e6edf3" font-size="42" font-weight="800">LedgerField</text>
</g>
<text x="80" y="300" fill="#e6edf3" font-size="74" font-weight="800">Offline P2P accounting</text>
<text x="80" y="362" fill="#8b949e" font-size="31">Private, offline-first books &#183; tax engine &#183; payroll &#183; data market</text>
${badge(80, 210, 'Offline-first')}${badge(310, 320, '100+ jurisdictions')}${badge(650, 200, 'No cloud')}${badge(870, 250, 'Encrypted vault')}
<text x="80" y="576" fill="#6c63ff" font-size="30" font-weight="600">www.5mart.ml/ledgerfield</text>
</svg>`;
fs.writeFileSync(path.join(WEB, 'social-card.svg'), socialCard);

// ── sitemap.xml + robots.txt ─────────────────────────────────────────────────
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${pages.filter(p => !p.noindex).map(p => `  <url><loc>${ORIGIN}${canonUrl(p.file)}</loc></url>`).join('\n')}
  <url><loc>${ORIGIN}${BASE}/app.html</loc></url>
</urlset>
`;
fs.writeFileSync(path.join(WEB, 'sitemap.xml'), sitemap);
fs.writeFileSync(path.join(WEB, 'robots.txt'), `User-agent: *\nAllow: /\nSitemap: ${ORIGIN}${BASE}/sitemap.xml\n`);

// ── link checker ─────────────────────────────────────────────────────────────
const files = pages.map(p => p.file).concat(fs.existsSync(path.join(WEB,'app.html')) ? ['app.html'] : []);
const anchorsByFile = {};
for (const f of files) {
  const html = fs.readFileSync(path.join(WEB, f), 'utf8');
  anchorsByFile[f] = new Set([...html.matchAll(/\sid="([^"]+)"/g)].map(m => m[1]));
}
const exists = rel => fs.existsSync(path.join(WEB, rel));
let broken = 0, checked = 0;
for (const f of files) {
  const html = fs.readFileSync(path.join(WEB, f), 'utf8');
  for (const m of html.matchAll(/href="([^"]+)"/g)) {
    let href = m[1];
    if (!href.startsWith(BASE + '/') && !href.startsWith('#')) continue; // skip external
    checked++;
    let target = href.startsWith('#') ? f : href.slice(BASE.length + 1);
    let frag = null;
    if (target.includes('#')) [target, frag] = target.split('#');
    if (href.startsWith('#')) { target = f; frag = href.slice(1); }
    if (target === '' || target.endsWith('/')) target = target + 'index.html';
    if (!exists(target)) { console.log(`BROKEN FILE  ${f}  ->  ${href}`); broken++; continue; }
    if (frag && !(anchorsByFile[target] || new Set()).has(frag)) {
      // recompute anchors for files not in pages (e.g. app.html already covered)
      if (!anchorsByFile[target]) anchorsByFile[target] = new Set([...fs.readFileSync(path.join(WEB,target),'utf8').matchAll(/\sid="([^"]+)"/g)].map(x=>x[1]));
      if (!anchorsByFile[target].has(frag)) { console.log(`BROKEN ANCHOR ${f}  ->  ${href}`); broken++; }
    }
  }
}
console.log(`\nPages written: ${pages.length + (fs.existsSync(path.join(WEB,'app.html'))?1:0)}`);
console.log(`Links checked: ${checked}  Broken: ${broken}`);
process.exit(broken ? 1 : 0);
