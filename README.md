# LedgerField

P2P global accounting engine — privacy-first, offline-capable, knitweb-integrated.

## What it is
- Double-entry bookkeeping with national chart-of-accounts standards (RGS/NEN4400 for NL, FRS 102 for UK, US GAAP, SKR03 for DE, PCG for FR)
- Global tax engine: CID-addressed rulesets gossipable via knitweb P2P network
- Multi-year tax rules: NL 2022–2025 (VPB, IB Box1/2/3, Loonheffing, WBSO, Innovatiebox, WKR, KIA, EIA, NEN4400)
- Payroll/loonstrook generation per jurisdiction
- SAF-T XML + JSON filing export
- AES-GCM encrypted local vault — PII never leaves device unless user opts in
- Fully offline: runs in browser (file://) — no server required

## Layout
```
src/ledgerfield/
  schemas/NL/   RGS NEN4400 (128 accounts)
  schemas/UK/   FRS 102
  schemas/US/   US GAAP
  schemas/DE/   SKR03
  tax/NL/       VPB + IB + Loonheffing + WBSO + WKR + KIA 2022-2025
  tax/UK/       Corporation Tax + Income Tax + NIC
  tax/US/       Federal CIT + Income Tax + Payroll
  payroll/NL/   Loonstrook met alle inhoudingen
  filing/NL/    VPB/IB aangifte, SAF-T export
  p2p/          knitweb CID-node, ruleset gossip, secure vault
  static/       ledgerfield.html — 7-tab offline GUI
rulesets/       NL_2022..2025, US_2025, UK_2025, EU_VAT_2025 (JSON)
tests/          property tests per jurisdiction
```
