"""Build the Kayonne Creatives site.

Every page is generated from _src/content_en.py and _src/content_de.py into
<slug>/index.html (English) and de/<slug>/index.html (German), with one shared
header, footer and head. Run from the repo root:

    python3 _src/build.py

Edit the content files, not the generated HTML.
"""
import datetime
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
import content_de  # noqa: E402
import content_en  # noqa: E402

SITE = "https://kayonnecreatives.com"
EMAIL = "hello@kayonnecreatives.com"
YEAR = datetime.date.today().year
LANGS = {"en": content_en, "de": content_de}

# (slug, English name, German name)
DIGITAL = [
    ("websites", "Websites", "Websites"),
    ("web-apps", "Web apps", "Web-Apps"),
    ("mobile-apps", "Mobile apps", "Mobile Apps"),
    ("domains-email", "Domains and business email", "Domains und geschäftliche E-Mail"),
    ("seo", "SEO", "SEO"),
    ("speed", "Speed and accessibility", "Ladezeit und Barrierefreiheit"),
    ("care", "Care plans", "Wartungspläne"),
]
LANGUAGE = [
    ("certified-translation", "Certified translation (UK)", "Certified Translation (UK)"),
    ("documents", "Document translation", "Dokumentübersetzung"),
    ("localization", "Website and app localisation", "Website- und App-Lokalisierung"),
    ("games", "Game localisation", "Spielelokalisierung"),
    ("medical", "Medical translation", "Medizinische Übersetzung"),
    ("patents", "Patent translation", "Patentübersetzung"),
    ("legal", "Legal translation", "Juristische Übersetzung"),
    ("subtitling", "Subtitling and transcription", "Untertitelung und Transkription"),
    ("proofreading", "Proofreading and revision", "Korrektorat und Revision"),
    ("quality", "MTPE and quality checks", "MTPE und Qualitätsprüfung"),
]

UI = {
    "en": {
        "skip": "Skip to content", "services": "Services", "digital": "Digital", "language": "Language",
        "languages": "Languages", "pricing": "Pricing", "work": "Work", "about": "About", "insights": "Insights",
        "process": "Process", "industries": "Industries", "faq": "FAQ", "contact": "Contact",
        "quote": "Get a quote", "menu": "Menu", "switch": "Deutsch", "switch_short": "DE",
        "tagline": "Websites and translation from Glasgow, for European and Asian markets.",
        "place": "Glasgow, United Kingdom", "company": "Company", "legal": "Legal",
        "privacy": "Privacy", "cookies": "Cookies", "terms": "Terms",
        "why": "Why it helps", "incl": "What is included", "steps": "How it works", "who": "Who it is for",
        "questions": "Questions", "cta_text": "Tell us what you need. You get a written quote before any work starts.",
        "locale": "en_GB", "home": "Home",
    },
    "de": {
        "skip": "Zum Inhalt springen", "services": "Leistungen", "digital": "Digital", "language": "Sprache",
        "languages": "Sprachen", "pricing": "Preise", "work": "Arbeiten", "about": "Über uns", "insights": "Ratgeber",
        "process": "Ablauf", "industries": "Branchen", "faq": "FAQ", "contact": "Kontakt",
        "quote": "Angebot anfragen", "menu": "Menü", "switch": "English", "switch_short": "EN",
        "tagline": "Websites und Übersetzungen aus Glasgow, für europäische und asiatische Märkte.",
        "place": "Glasgow, Vereinigtes Königreich", "company": "Agentur", "legal": "Rechtliches",
        "privacy": "Datenschutz", "cookies": "Cookies", "terms": "AGB",
        "why": "Ihr Vorteil", "incl": "Leistungsumfang", "steps": "Ablauf", "who": "Für wen", "questions": "Fragen",
        "cta_text": "Beschreiben Sie Ihr Projekt. Sie erhalten ein schriftliches Angebot, bevor die Arbeit beginnt.",
        "locale": "de_DE", "home": "Start",
    },
}


def esc(s):
    return html.escape(s, quote=True)


def path(lang, slug):
    base = "/de/" if lang == "de" else "/"
    return base + (slug + "/" if slug else "")


def name_of(item, lang):
    return item[1] if lang == "en" else item[2]


def header(lang, slug):
    t = UI[lang]
    other = "de" if lang == "en" else "en"
    p = lambda s: path(lang, s)  # noqa: E731
    dig = "".join(f'<li><a href="{p(s)}">{esc(name_of(i, lang))}</a></li>' for i in DIGITAL for s in [i[0]])
    lan = "".join(f'<li><a href="{p(s)}">{esc(name_of(i, lang))}</a></li>' for i in LANGUAGE for s in [i[0]])
    top = [("languages", t["languages"]), ("pricing", t["pricing"]), ("work", t["work"]),
           ("about", t["about"]), ("insights", t["insights"])]
    top_links = "".join(f'<a href="{p(s)}">{esc(n)}</a>' for s, n in top)
    drawer_more = "".join(f'<li><a href="{p(s)}">{esc(n)}</a></li>' for s, n in
                          top + [("process", t["process"]), ("faq", t["faq"])])
    return f"""<a class="skip" href="#content">{t['skip']}</a>
<header class="nav">
  <div class="shell nav-row">
    <a class="mark" href="{p('')}">Kayonne</a>
    <nav class="links" aria-label="{t['services']}">
      <details class="menu">
        <summary>{t['services']}</summary>
        <div class="drop">
          <div><p class="kicker">{t['digital']}</p><ul>{dig}</ul></div>
          <div><p class="kicker">{t['language']}</p><ul>{lan}</ul></div>
        </div>
      </details>
      {top_links}
    </nav>
    <div class="nav-actions">
      <a class="btn ghost" href="{path(other, slug)}" hreflang="{other}" lang="{other}" title="{UI[lang]['switch']}">{t['switch_short']}</a>
      <a class="btn nav-quote" href="{p('contact')}">{t['quote']}</a>
      <button class="btn ghost burger" type="button" aria-expanded="false" aria-controls="drawer">{t['menu']}</button>
    </div>
  </div>
  <div class="shell drawer" id="drawer">
    <p class="drawer-cta"><a class="btn" href="{p('contact')}">{t['quote']}</a></p>
    <div><p class="kicker">{t['digital']}</p><ul>{dig}</ul></div>
    <div><p class="kicker">{t['language']}</p><ul>{lan}</ul></div>
    <div><p class="kicker">{t['company']}</p><ul>{drawer_more}</ul></div>
  </div>
</header>"""


def footer(lang):
    t = UI[lang]
    p = lambda s: path(lang, s)  # noqa: E731
    dig = "".join(f'<li><a href="{p(i[0])}">{esc(name_of(i, lang))}</a></li>' for i in DIGITAL)
    lan = "".join(f'<li><a href="{p(i[0])}">{esc(name_of(i, lang))}</a></li>' for i in LANGUAGE)
    comp = "".join(f'<li><a href="{p(s)}">{esc(t[k])}</a></li>' for s, k in [
        ("about", "about"), ("process", "process"), ("industries", "industries"), ("languages", "languages"),
        ("pricing", "pricing"), ("work", "work"), ("faq", "faq"), ("insights", "insights"), ("contact", "contact")])
    legal = " · ".join(f'<a href="{p(s)}">{esc(t[s])}</a>' for s in ("privacy", "cookies", "terms"))
    return f"""<footer><div class="shell foot">
    <div>
      <p class="mark">Kayonne Creatives</p>
      <p class="note">{t['tagline']}</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p class="note">{t['place']}</p>
    </div>
    <div><p class="kicker">{t['digital']}</p><ul>{dig}</ul></div>
    <div><p class="kicker">{t['language']}</p><ul>{lan}</ul></div>
    <div><p class="kicker">{t['company']}</p><ul>{comp}</ul></div>
  </div>
  <div class="shell foot-base note"><p>© {YEAR} Kayonne Creatives · {t['place']}</p><p>{legal}</p></div>
</footer>"""


SCRIPT = """<script>
(function(){
  var b=document.querySelector(".burger"),d=document.getElementById("drawer");
  if(b&&d){b.addEventListener("click",function(){var o=d.classList.toggle("open");b.setAttribute("aria-expanded",o?"true":"false");});}
  var m=document.querySelector("details.menu");
  if(m){
    document.addEventListener("click",function(e){if(m.open&&!m.contains(e.target))m.open=false;});
    document.addEventListener("keydown",function(e){if(e.key==="Escape"&&m.open){m.open=false;m.querySelector("summary").focus();}});
  }
})();
</script>"""


def org_schema(lang):
    return {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "Kayonne Creatives",
        "url": SITE + "/",
        "email": EMAIL,
        "logo": SITE + "/favicon.svg",
        "image": SITE + "/og.png",
        "description": UI[lang]["tagline"],
        "address": {"@type": "PostalAddress", "addressLocality": "Glasgow", "addressCountry": "GB"},
        "areaServed": ["GB", "Europe", "Asia"],
        "knowsLanguage": ["en", "de", "fr", "es", "it", "nl", "pl", "ja", "zh", "ko"],
    }


def faq_schema(faq):
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": strip(q),
                        "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faq],
    }


def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def head(lang, slug, page):
    title = page["title"]
    desc = page["desc"]
    url = SITE + path(lang, slug)
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE + path(l, slug)}" />' for l in ("en", "de"))
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE + path("en", slug)}" />'
    schemas = list(page.get("schema", []))
    if slug == "":
        schemas.insert(0, org_schema(lang))
    if page.get("faq"):
        schemas.append(faq_schema(page["faq"]))
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    robots = '<meta name="robots" content="noindex" />' if page.get("noindex") else ""
    if page.get("noindex"):
        alts = ""
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}" />
{robots}{'' if page.get('noindex') else f'<link rel="canonical" href="{url}" />'}
{alts}
<meta property="og:type" content="website" />
<meta property="og:site_name" content="Kayonne Creatives" />
<meta property="og:title" content="{esc(title)}" />
<meta property="og:description" content="{esc(desc)}" />
<meta property="og:url" content="{url}" />
<meta property="og:image" content="{SITE}/og.png" />
<meta property="og:locale" content="{UI[lang]['locale']}" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="preload" href="/fonts/outfit-latin.woff2" as="font" type="font/woff2" crossorigin />
<link rel="preload" href="/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin />
<link rel="stylesheet" href="/css/site.css" />
{ld}
</head>"""


def lis(items):
    return "".join(f"<li>{x}</li>" for x in items)


def faq_html(faq, t):
    if not faq:
        return ""
    items = "".join(f'<details class="card"><summary>{q}</summary><p>{a}</p></details>' for q, a in faq)
    return f'<section><h2>{t["questions"]}</h2><div class="stack">{items}</div></section>'


def cta(lang):
    t = UI[lang]
    return (f'<section class="cta card"><p>{t["cta_text"]}</p>'
            f'<p><a class="btn" href="{path(lang, "contact")}">{t["quote"]}</a></p></section>')


def service_main(lang, page):
    t = UI[lang]
    parts = [f'<header class="intro"><p class="kicker">{page["label"]}</p><h1>{page["h1"]}</h1><p class="lede">{page["lede"]}</p></header>']
    if page.get("why"):
        parts.append(f'<section><h2>{t["why"]}</h2><ul class="ticks">{lis(page["why"])}</ul></section>')
    if page.get("incl"):
        parts.append(f'<section><h2>{t["incl"]}</h2><ul class="ticks cols">{lis(page["incl"])}</ul></section>')
    parts.append(page.get("extra", ""))
    if page.get("steps"):
        steps = "".join(f'<li class="card"><h3>{a}</h3><p>{b}</p></li>' for a, b in page["steps"])
        parts.append(f'<section><h2>{t["steps"]}</h2><ol class="grid-4 steps">{steps}</ol></section>')
    if page.get("who"):
        parts.append(f'<section><h2>{t["who"]}</h2><p>{page["who"]}</p></section>')
    parts.append(faq_html(page.get("faq"), t))
    parts.append(cta(lang))
    return "".join(parts)


def raw_main(lang, page):
    t = UI[lang]
    body = page["body"]
    intro = ""
    if page.get("h1"):
        intro = f'<p class="kicker">{page.get("label", "")}</p><h1>{page["h1"]}</h1>'
        if page.get("lede"):
            intro += f'<p class="lede">{page["lede"]}</p>'
        intro = f'<header class="intro">{intro}</header>'
    tail = faq_html(page.get("faq"), t) + ("" if page.get("no_cta") else cta(lang))
    return intro + body + tail


def render(lang, slug, page, weights=""):
    main = service_main(lang, page) if page.get("kind") == "service" else raw_main(lang, page)
    main = main.replace("{{WEIGHTS}}", weights)
    cls = "page" + (" home" if slug == "" else "")
    link_slug = "" if slug == "404" else slug
    return (head(lang, slug, page) + "\n<body>\n" + header(lang, link_slug) +
            f'\n<main id="content" class="shell {cls}">{main}</main>\n' + footer(lang) + "\n" + SCRIPT +
            page.get("script", "") + "\n</body>\n</html>\n")


def kb(n):
    return f"{n / 1024:.1f} KB"


def weights_table(lang):
    heads = {"en": ("Page", "HTML", "Compressed (gzip)"), "de": ("Seite", "HTML", "Komprimiert (gzip)")}[lang]
    shared = {"en": "Shared stylesheet and fonts", "de": "Gemeinsames Stylesheet und Schriften"}[lang]
    import gzip
    rows = []
    for slug in ("", "services", "websites", "certified-translation", "contact", "languages"):
        data = open(out_file(lang, slug), "rb").read()
        label = LANGS[lang].PAGES[slug]["title"].split(" | ")[0] if slug else UI[lang]["home"]
        rows.append(f'<tr><td><a href="{path(lang, slug)}">{esc(label)}</a></td><td class="n">{kb(len(data))}</td>'
                    f'<td class="n">{kb(len(gzip.compress(data)))}</td></tr>')
    assets = ["css/site.css"] + sorted("fonts/" + f for f in os.listdir("fonts"))
    total = sum(os.path.getsize(a) for a in assets)
    rows.append(f'<tr><td>{shared}</td><td class="n">{kb(total)}</td><td class="n">–</td></tr>')
    return (f'<div class="table-wrap"><table><thead><tr><th scope="col">{heads[0]}</th><th scope="col">{heads[1]}</th>'
            f'<th scope="col">{heads[2]}</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>')


def out_file(lang, slug):
    d = ("de/" if lang == "de" else "") + slug
    return os.path.join(d, "index.html") if d else "index.html"


def main():
    en_slugs = set(content_en.PAGES)
    de_slugs = set(content_de.PAGES)
    if en_slugs != de_slugs:
        sys.exit(f"Page lists differ. Only EN: {sorted(en_slugs - de_slugs)} Only DE: {sorted(de_slugs - en_slugs)}")
    written = []
    for lang, mod in LANGS.items():
        for slug, page in mod.PAGES.items():
            if slug == "studio":
                continue
            f = out_file(lang, slug)
            os.makedirs(os.path.dirname(f) or ".", exist_ok=True)
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(render(lang, slug, page))
            written.append((lang, slug, page))
    # The studio page lists the real size of the pages built above, so it is built last.
    for lang, mod in LANGS.items():
        f = out_file(lang, "studio")
        os.makedirs(os.path.dirname(f), exist_ok=True)
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(render(lang, "studio", mod.PAGES["studio"], weights_table(lang)))
        written.append((lang, "studio", mod.PAGES["studio"]))
    # 404 page, English with a German link, at the root.
    with open("404.html", "w", encoding="utf-8") as fh:
        fh.write(render("en", "404", content_en.NOT_FOUND))
    # Sitemap, with both language versions listed for every page.
    urls = []
    for lang, slug, page in written:
        if page.get("noindex"):
            continue
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE + path(l, slug)}"/>' for l in ("en", "de"))
        urls.append(f"  <url><loc>{SITE + path(lang, slug)}</loc>{alts}</url>")
    with open("sitemap.xml", "w", encoding="utf-8") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                 'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
    print(f"Built {len(written)} pages, 404.html and sitemap.xml")


if __name__ == "__main__":
    main()
