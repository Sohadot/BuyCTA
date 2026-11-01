# BuyCTA.com — Strategic domain acquisition page

A minimal, static, English-language acquisition landing page for **the BuyCTA.com domain name itself**. Prepared for [Sohadot](https://sohadot.com/).

## Positioning

**BUY** is a commercially direct verb; **CTA** refers here to *Commodity Trading Advisor*, an established U.S. futures-industry term. The page presents possible future uses for an acquirer in CTA acquisitions, managed-futures manager discovery and specialist financial platforms. These examples do **not** imply an existing operating firm, financial registration, trading product, revenue, valuation, investor endorsement or completed transaction.

## Repository contents

- `index.html` — complete responsive landing page (inline CSS and small, dependency-free JavaScript).
- `robots.txt` and `sitemap.xml` — single-page discovery metadata for the intended canonical domain.
- `scripts/check_site.py` — dependency-free integrity checks.
- `.github/workflows/check.yml` — tests on pull requests and changes to `main`; **no deployment action**.

No external fonts, trackers, analytics, form processors or frameworks are included. Screenshots and ZIP distribution bundles are intentionally not committed.

## Inquiry behavior

The form uses **`mailto:`** to prepare a draft in the visitor's installed email client, addressed to **agent@sohadot.com**. Clicking its button does not submit data to a server or guarantee an email was sent. An ordinary email link is also available. If a backend is introduced later, add tested delivery, spam controls, privacy disclosures and confirmation semantics before advertising it as a submission form.

## Local checks

```sh
python3 scripts/check_site.py
python3 -m http.server 8000
```

Open `http://localhost:8000/` and verify layout, accessible keyboard navigation, and mail-client behavior in browsers. The Python test checks key static invariants but is not a substitute for browser testing.

## Deployment (not performed by this repository)

Cloudflare Pages or any static host can serve this repository from its root with **no build command**. Configure `buycta.com`, TLS and DNS separately only after reviewing the content and verifying domain control. The canonical and sitemap intentionally refer to `https://buycta.com/`; preview URLs are not the production canonical.

**Before publication**: verify the seller controls the domain and that agent@sohadot.com receives messages; test real devices and email-client fallback; verify the asset-sale and regulatory disclosures; agree escrow/transfer terms directly with a purchaser. Independent escrow is an option, not a representation of an existing arrangement.

**Commercial policy**: domain-only sale, no public asking price, confidential negotiation. No investment solicitation or regulated financial services are offered.
