"""Build the BluArc Labs static site.

Each page's metadata lives in PAGES below; its main sections live in
src/pages/<key>.html. Shared head, header, page hero, FAQ, related links,
call-to-action band and footer are rendered here so every page stays
consistent. Output is plain HTML at the repo root (index.html and
<slug>/index.html), plus sitemap.xml.

Run from anywhere:  python src/build.py
"""

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = Path(__file__).resolve().parent / "pages"
SITE = "https://bluarclabs.com"
EMAIL = "founder@bluarclabs.com"
LASTMOD = "2026-10-08"

NAV = [
    ("ot-security", "/ot-security/", "OT security"),
    ("plant-analytics", "/plant-analytics/", "Plant analytics"),
    ("embedded-sensing", "/embedded-sensing/", "Embedded sensing"),
    ("safe", "/safe/", "SAFE"),
    ("company", "/company/", "Company"),
]

FOCUS = [
    ("ot-security", "/ot-security/", "01", "OT security",
     "Protecting the computers that run production."),
    ("plant-analytics", "/plant-analytics/", "02", "Plant analytics",
     "Turning process data into decisions."),
    ("embedded-sensing", "/embedded-sensing/", "03", "Embedded sensing",
     "Wireless sensing for harsh industrial environments."),
]

PAGES = [
    {
        "key": "home",
        "path": "/",
        "title": "BluArc Labs | OT Security & Plant Analytics, India",
        "description": "Industrial technology company in India building OT security, plant analytics and embedded sensing for manufacturing plants. Real conditions. Clearer decisions.",
        "og_image": "/assets/og/home.png",
        "og_alt": "BluArc Labs. Progress, on common ground. Industrial technology, India.",
        "custom_hero": True,
        "priority": "1.0",
        "faq": [
            ("What does BluArc Labs do?",
             "BluArc Labs is an industrial technology company in India. We work on three connected areas for industrial plants: OT (operational technology) security, Industry 4.0 and plant analytics, and embedded hardware and sensing."),
            ("What is OT security?",
             "OT security protects the systems that run physical operations: the plant-floor PCs, operator stations and engineering workstations behind production. It differs from IT security because uptime, safety and long equipment lifecycles come first."),
            ("What is SAFE?",
             "SAFE by BluArc Labs is our first product: security for industrial computers, built for plant-floor PCs and operator stations where standard IT tools don't fit. It is in development, and we share details in private briefings."),
            ("Where is BluArc Labs based?",
             "BluArc Labs is based in India. We design for industrial plants, starting with manufacturing in India."),
            ("How can we work with BluArc Labs?",
             f"Email {EMAIL} with a short note about your plant, your data or your security questions."),
        ],
    },
    {
        "key": "ot-security",
        "path": "/ot-security/",
        "title": "OT Security for Industrial Plants | BluArc Labs",
        "description": "OT security for plant-floor PCs, operator stations and engineering workstations, built around uptime, long lifecycles and the realities of plants in India.",
        "og_image": "/assets/og/ot-security.png",
        "og_alt": "OT security for industrial plants. BluArc Labs.",
        "crumb": "OT security",
        "label": "Focus area 01",
        "h1": ["OT security for", "industrial plants."],
        "lead": "Protecting the computers that run production: operator stations, engineering workstations and plant-floor PCs, where standard IT security tools don't fit.",
        "toc": [("challenge", "The challenge"), ("focus", "What we focus on"), ("approach", "How we approach it"), ("safe", "SAFE"), ("faq", "Questions")],
        "service": ("OT security", "Industrial cybersecurity"),
        "related": True,
        "priority": "0.9",
        "faq": [
            ("What is the difference between IT security and OT security?",
             "IT security protects information: data, email and business systems. OT security protects operations: the systems that run machines and processes. In OT, availability and safety come first, systems run for many years, and changes must fit around production."),
            ("Why don't standard IT security tools fit plant-floor computers?",
             "Many IT tools assume frequent updates, constant internet access and current operating systems. Plant-floor computers often have none of these, and their software is qualified for a fixed configuration, so tools that change that configuration can disrupt production."),
            ("What is IEC 62443?",
             "IEC 62443 is a series of international standards for the security of industrial automation and control systems. It covers how to organise systems into zones, how to manage access and change, and what security capabilities components should have."),
            ("Do you work with plants in India?",
             "Yes. BluArc Labs is based in India, and we design with the conditions of Indian manufacturing plants in mind."),
        ],
    },
    {
        "key": "plant-analytics",
        "path": "/plant-analytics/",
        "title": "Plant Analytics & Predictive Maintenance | BluArc Labs",
        "description": "Industry 4.0 plant analytics from BluArc Labs: condition monitoring, predictive maintenance and process data turned into decisions operators can act on.",
        "og_image": "/assets/og/plant-analytics.png",
        "og_alt": "Plant data into clearer decisions. BluArc Labs.",
        "crumb": "Plant analytics",
        "label": "Focus area 02",
        "h1": ["Plant data into", "clearer decisions."],
        "lead": "Industry 4.0 work that starts from the decisions operators and maintenance teams actually make: condition monitoring, plant analytics and predictive maintenance.",
        "toc": [("opportunity", "The opportunity"), ("work", "What we work on"), ("approach", "How we approach it"), ("faq", "Questions")],
        "service": ("Plant analytics and predictive maintenance", "Industrial analytics"),
        "related": True,
        "priority": "0.9",
        "faq": [
            ("What is predictive maintenance?",
             "Predictive maintenance uses equipment data, such as vibration and temperature, to estimate when a machine is likely to fail, so maintenance can be planned before a breakdown instead of after it."),
            ("What is Industry 4.0?",
             "Industry 4.0 describes the connection of machines, sensors and software in manufacturing, so that data can flow from the plant floor to the people making decisions."),
            ("Do we need new sensors to start?",
             "Not always. Many plants can start with data they already collect. Where key signals are missing, sensing can be added to specific assets."),
            ("How does plant analytics relate to OT security?",
             "Connecting plant data creates new paths into production systems. We treat security as part of every analytics design, not a separate project."),
        ],
    },
    {
        "key": "embedded-sensing",
        "path": "/embedded-sensing/",
        "title": "Wireless Industrial Sensors & Hardware | BluArc Labs",
        "description": "Wireless sensors and embedded hardware designed in-house for harsh industrial environments: condition monitoring for motors, pumps and rotating equipment.",
        "og_image": "/assets/og/embedded-sensing.png",
        "og_alt": "Sensing built for real conditions. BluArc Labs.",
        "crumb": "Embedded sensing",
        "label": "Focus area 03",
        "h1": ["Sensing built for", "real conditions."],
        "lead": "Wireless sensing and instrumentation designed in-house for harsh industrial environments, so the data behind decisions comes from the machines themselves.",
        "toc": [("why", "Why it matters"), ("design", "What we design"), ("floor", "Built for the floor"), ("faq", "Questions")],
        "service": ("Embedded hardware and industrial sensing", "Industrial IoT sensing"),
        "related": True,
        "priority": "0.9",
        "faq": [
            ("What is a wireless condition monitoring sensor?",
             "A small device mounted on a machine that measures signals such as vibration and temperature and sends them wirelessly, so equipment health can be tracked without manual rounds or new cabling."),
            ("Which equipment benefits most from condition monitoring?",
             "Rotating equipment that production depends on, such as motors, pumps, fans, compressors and gearboxes, where an unplanned failure stops a line."),
            ("Is your hardware designed in-house?",
             "Yes. We design sensing hardware and firmware together, with security and harsh conditions considered from the start."),
        ],
    },
    {
        "key": "safe",
        "path": "/safe/",
        "title": "SAFE by BluArc Labs | Security for Industrial Computers",
        "description": "SAFE by BluArc Labs is security for plant-floor PCs and operator stations, where standard IT tools don't fit. In development; private briefings available.",
        "og_image": "/assets/og/safe.png",
        "og_alt": "SAFE by BluArc Labs. Security for industrial computers.",
        "crumb": "SAFE",
        "label": "Product / In development",
        "h1": ["Security for", "industrial computers."],
        "lead": "SAFE by BluArc Labs is built for plant-floor PCs and operator stations, where standard IT tools don't fit. A shared view. A clearer next step.",
        "aside": '<div class="safe-card"><img src="/assets/brand/filament-fan.svg" width="1080" height="1080" alt="" fetchpriority="high"><p class="safe-card-name">SAFE</p><p class="safe-card-status"><span class="status-mark" aria-hidden="true"></span>In development</p></div>',
        "priority": "0.9",
        "faq": [
            ("Is SAFE available today?",
             "SAFE is in development. A 3-month pilot is planned with a large Indian manufacturer. Contact us to request a briefing."),
            ("What does SAFE protect?",
             "SAFE is built for industrial computers: the plant-floor PCs and operator stations that run production, where standard IT security tools don't fit."),
            ("How does SAFE work?",
             f"We share technical detail in private briefings. Email {EMAIL} to request one."),
            ("Who is SAFE for?",
             "Plant, OT and IT teams responsible for the computers on the plant floor, from a single site to multi-plant groups."),
        ],
    },
    {
        "key": "company",
        "path": "/company/",
        "title": "About BluArc Labs | Industrial Technology Company, India",
        "description": "BluArc Labs is an industrial technology lab based in India, working where operational technology, data and hardware meet. Built around the plant floor.",
        "og_image": "/assets/og/company.png",
        "og_alt": "Built around the plant floor. BluArc Labs.",
        "crumb": "Company",
        "label": "Company",
        "h1": ["Built around", "the plant floor."],
        "lead": "BluArc Labs is an industrial technology lab based in India. We work where operational technology, data and hardware meet, and we build our products alongside the plants that use them.",
        "toc": [("what", "What we do"), ("name", "The name"), ("principles", "Principles"), ("where", "Where we work")],
        "page_type": "AboutPage",
        "priority": "0.7",
    },
    {
        "key": "contact",
        "path": "/contact/",
        "title": "Contact BluArc Labs | Industrial Technology, India",
        "description": f"Talk to BluArc Labs about OT security, plant analytics, industrial sensing or a SAFE briefing. Email {EMAIL}.",
        "og_image": "/assets/og/contact.png",
        "og_alt": "Let's talk about your plant. BluArc Labs.",
        "crumb": "Contact",
        "label": "Contact",
        "h1": ["Let's talk about", "your plant."],
        "lead": "Tell us about your plant, your data or your security questions. Email is the fastest way to reach us.",
        "aside": f'<div class="hero-contact"><p class="label">Email</p><a class="contact-email contact-email-dark" href="mailto:{EMAIL}">{EMAIL}</a><p class="hero-contact-note">Based in India. Working in English.</p></div>',
        "page_type": "ContactPage",
        "no_cta": True,
        "priority": "0.6",
    },
]


def esc(s):
    return html.escape(s, quote=True)


def org_schema():
    return {
        "@type": "Organization",
        "@id": f"{SITE}/#organization",
        "name": "BluArc Labs",
        "alternateName": ["BluArc", "Bluarc Labs"],
        "url": f"{SITE}/",
        "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/icons/icon-512.png", "width": 512, "height": 512},
        "image": f"{SITE}/assets/og/home.png",
        "email": EMAIL,
        "description": "Industrial technology company in India building OT security, plant analytics and embedded sensing for industrial plants.",
        "slogan": "Real conditions. Clearer decisions.",
        "address": {"@type": "PostalAddress", "addressCountry": "IN"},
        "areaServed": "Worldwide",
        "knowsAbout": [
            "Operational technology (OT) security", "Industrial control system security", "IEC 62443",
            "Industry 4.0", "Plant analytics", "Condition monitoring", "Predictive maintenance",
            "Industrial IoT", "Embedded hardware", "Wireless industrial sensors",
        ],
        "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "email": EMAIL, "availableLanguage": ["English"]},
    }


def schema(page):
    url = SITE + page["path"]
    graph = [
        org_schema(),
        {"@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/", "name": "BluArc Labs",
         "inLanguage": "en-IN", "publisher": {"@id": f"{SITE}/#organization"}},
    ]
    webpage = {
        "@type": page.get("page_type", "WebPage"),
        "@id": f"{url}#webpage",
        "url": url,
        "name": page["title"],
        "description": page["description"],
        "isPartOf": {"@id": f"{SITE}/#website"},
        "about": {"@id": f"{SITE}/#organization"},
        "primaryImageOfPage": SITE + page["og_image"],
        "inLanguage": "en-IN",
        "dateModified": LASTMOD,
    }
    if page["key"] != "home":
        webpage["breadcrumb"] = {"@id": f"{url}#breadcrumb"}
        graph.append({
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": page["crumb"], "item": url},
            ],
        })
    graph.append(webpage)
    if page.get("service"):
        name, stype = page["service"]
        graph.append({
            "@type": "Service",
            "@id": f"{url}#service",
            "name": name,
            "serviceType": stype,
            "description": page["description"],
            "provider": {"@id": f"{SITE}/#organization"},
            "areaServed": [{"@type": "Country", "name": "India"}, "Worldwide"],
            "url": url,
        })
    if page.get("faq"):
        graph.append({
            "@type": "FAQPage",
            "@id": f"{url}#faq",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in page["faq"]
            ],
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)


def head(page):
    url = SITE + page["path"]
    img = SITE + page["og_image"]
    t, d, alt = esc(page["title"]), esc(page["description"]), esc(page["og_alt"])
    return f"""<!doctype html>
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{t}</title>
  <meta name="description" content="{d}">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="theme-color" content="#1F8FD8">
  <meta name="color-scheme" content="light">
  <meta name="author" content="BluArc Labs">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="BluArc Labs">
  <meta property="og:locale" content="en_IN">
  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{d}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{img}">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{alt}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t}">
  <meta name="twitter:description" content="{d}">
  <meta name="twitter:image" content="{img}">
  <meta name="twitter:image:alt" content="{alt}">

  <link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">
  <link rel="icon" href="/assets/icons/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">

  <link rel="preload" href="/assets/fonts/BluArcSans-Bold.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/BluArcSans-Regular.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/css/styles.css">
  <script>document.documentElement.classList.add('js');</script>

  <script type="application/ld+json">
{schema(page)}
  </script>
</head>"""


def header(page):
    links = []
    for key, href, label in NAV:
        cur = ' aria-current="page"' if page["key"] == key else ""
        links.append(f'        <a href="{href}"{cur}>{label}</a>')
    cur = ' aria-current="page"' if page["key"] == "contact" else ""
    links.append(f'        <a class="btn btn-primary btn-sm" href="/contact/"{cur}>Contact</a>')
    links = "\n".join(links)
    return f"""<body class="page-{page['key']}">
  <a class="skip-link" href="#main">Skip to content</a>

  <header class="site-header" id="top">
    <div class="container header-inner">
      <a class="brand" href="/" aria-label="BluArc Labs home">
        <img src="/assets/brand/logo.svg" width="196" height="35" alt="BluArc Labs">
      </a>

      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
        <span class="nav-toggle-bar"></span>
        <span class="nav-toggle-bar"></span>
        <span class="visually-hidden">Menu</span>
      </button>

      <nav class="site-nav" id="site-nav" aria-label="Main">
{links}
      </nav>
    </div>
  </header>
"""


def headline(lines, hid):
    out = []
    for i, line in enumerate(lines):
        cls = "hl-line hl-ground" if i == len(lines) - 1 else "hl-line"
        out.append(f'<span class="{cls}"><span class="hl-in">{esc(line)}</span></span>')
    return f'<h1 id="{hid}" class="display">{"".join(out)}</h1>'


def page_hero(page):
    crumbs = f"""<nav class="crumbs" aria-label="Breadcrumb">
          <ol><li><a href="/">Home</a></li><li><span aria-current="page">{esc(page['crumb'])}</span></li></ol>
        </nav>"""
    if page.get("aside"):
        aside = page["aside"]
    elif page.get("toc"):
        items = "".join(f'<li><a href="#{a}">{esc(b)}</a></li>' for a, b in page["toc"])
        aside = f'<nav class="toc" aria-label="On this page"><p class="label">On this page</p><ol>{items}</ol></nav>'
    else:
        aside = ""
    return f"""    <section class="page-hero" aria-labelledby="page-title">
      <div class="container page-hero-grid">
        <div class="page-hero-main">
        {crumbs}
          <p class="label">{esc(page['label'])}</p>
          {headline(page['h1'], 'page-title')}
          <p class="page-lead hero-anim">{esc(page['lead'])}</p>
        </div>
        <div class="page-hero-aside">{aside}</div>
      </div>
    </section>
"""


def faq_section(page):
    if not page.get("faq"):
        return ""
    items = "\n".join(
        f"""          <details class="faq-item">
            <summary><h3>{esc(q)}</h3><span class="faq-icon" aria-hidden="true"></span></summary>
            <div class="faq-answer"><p>{esc(a)}</p></div>
          </details>""" for q, a in page["faq"])
    return f"""    <section class="block" id="faq" aria-labelledby="faq-title">
      <div class="container block-grid">
        <div class="block-head">
          <p class="label">Questions</p>
          <h2 id="faq-title">Frequently asked.</h2>
        </div>
        <div class="faq reveal">
{items}
        </div>
      </div>
    </section>
"""


def related_section(page):
    if not page.get("related"):
        return ""
    cards = "\n".join(
        f"""          <a class="related-card reveal" href="{href}">
            <span class="related-num">{num} /</span>
            <span class="related-title">{esc(title)}</span>
            <span class="related-desc">{esc(desc)}</span>
            <span class="related-arrow" aria-hidden="true">&rarr;</span>
          </a>""" for key, href, num, title, desc in FOCUS if key != page["key"])
    return f"""    <section class="block block-tight block-wash" aria-labelledby="related-title">
      <div class="container">
        <p class="label">More from BluArc Labs</p>
        <h2 id="related-title" class="h2-sm">Keep exploring.</h2>
        <div class="related-grid">
{cards}
          <a class="related-card reveal" href="/safe/">
            <span class="related-num">Product /</span>
            <span class="related-title">SAFE by BluArc Labs</span>
            <span class="related-desc">Security for industrial computers.</span>
            <span class="related-arrow" aria-hidden="true">&rarr;</span>
          </a>
        </div>
      </div>
    </section>
"""


def cta_band(page):
    if page.get("no_cta"):
        return ""
    return f"""    <section class="cta-band" aria-labelledby="cta-title">
      <div class="container cta-inner reveal">
        <p class="label label-reverse">Get in touch</p>
        <h2 id="cta-title" class="cta-title"><span class="hl-ground">Progress, on common ground.</span></h2>
        <p class="cta-lead">Tell us about your plant, your data or your security questions.</p>
        <div class="cta-actions">
          <a class="contact-email" href="mailto:{EMAIL}">{EMAIL}</a>
          <a class="btn btn-reverse" href="/contact/">All ways to reach us</a>
        </div>
      </div>
    </section>
"""


def footer():
    focus = "".join(f'<li><a href="{href}">{esc(title)}</a></li>' for _, href, _, title, _ in FOCUS)
    return f"""  <footer class="site-footer">
    <div class="footer-lattice" aria-hidden="true"></div>
    <div class="container footer-inner">
      <div class="footer-brand">
        <a class="brand" href="/" aria-label="BluArc Labs home">
          <img src="/assets/brand/logo.svg" width="196" height="35" alt="BluArc Labs" loading="lazy" decoding="async">
        </a>
        <p class="footer-about">Industrial technology company in India: OT security, plant analytics and embedded sensing for industrial plants.</p>
      </div>
      <nav class="footer-col" aria-label="Focus areas">
        <p class="footer-head">Focus</p>
        <ul>{focus}</ul>
      </nav>
      <nav class="footer-col" aria-label="Company">
        <p class="footer-head">Company</p>
        <ul><li><a href="/safe/">SAFE</a></li><li><a href="/company/">About</a></li><li><a href="/contact/">Contact</a></li></ul>
      </nav>
      <div class="footer-col">
        <p class="footer-head">Contact</p>
        <ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><span>India</span></li></ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>&copy; <span id="year">2026</span> BluArc Labs. All rights reserved.</p>
      <p class="footer-sign">Real conditions. Clearer decisions.</p>
    </div>
  </footer>

  <script src="/js/main.js" defer></script>
</body>
</html>
"""


def render(page):
    body = (PAGES_DIR / f"{page['key']}.html").read_text(encoding="utf-8").replace("{{EMAIL}}", EMAIL)
    parts = [head(page), header(page), '  <main id="main">\n']
    if not page.get("custom_hero"):
        parts.append(page_hero(page))
    parts += [body, faq_section(page), related_section(page), cta_band(page), "  </main>\n\n", footer()]
    return "".join(parts)


def sitemap():
    urls = "\n".join(
        f"""  <url>
    <loc>{SITE}{p['path']}</loc>
    <lastmod>{LASTMOD}</lastmod>
    <priority>{p['priority']}</priority>
    <image:image><image:loc>{SITE}{p['og_image']}</image:loc></image:image>
  </url>""" for p in PAGES)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
{urls}
</urlset>
"""


def main():
    for page in PAGES:
        out = ROOT / page["path"].strip("/") / "index.html" if page["path"] != "/" else ROOT / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(page), encoding="utf-8", newline="\n")
        print("wrote", out.relative_to(ROOT))
    (ROOT / "sitemap.xml").write_text(sitemap(), encoding="utf-8", newline="\n")
    print("wrote sitemap.xml")


if __name__ == "__main__":
    main()
