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

# The three teams. Each item: (slug, English name, German name, English blurb, German blurb).
TEAMS = {
    "digital": {
        "en": "Digital", "de": "Digital", "hub": "digital", "cls": "d",
        "en_line": "The build team: sites, shops, apps and the plumbing behind them.",
        "de_line": "Das Entwicklungsteam: Websites, Shops, Apps und die Technik dahinter.",
        "items": [
            ("websites", "Websites", "Websites", "Business sites, shops, landing pages", "Unternehmensseiten, Shops, Landingpages"),
            ("web-design-glasgow", "Web design Glasgow", "Webdesign Glasgow", "A local team you can meet", "Ein Team vor Ort in Glasgow"),
            ("web-apps", "Web apps", "Web-Apps", "Custom tools and PWAs", "Individuelle Tools und PWAs"),
            ("mobile-apps", "Mobile apps", "Mobile Apps", "iOS and Android", "iOS und Android"),
            ("domains-email", "Domains and business email", "Domains und geschäftliche E-Mail", "Domain, inbox, SPF/DKIM/DMARC", "Domain, Postfach, SPF/DKIM/DMARC"),
            ("seo", "SEO", "SEO", "Technical, local, multilingual", "Technisch, lokal, mehrsprachig"),
            ("speed", "Speed and accessibility", "Ladezeit und Barrierefreiheit", "Core Web Vitals, WCAG 2.2 AA", "Core Web Vitals, WCAG 2.2 AA"),
            ("care", "Care plans", "Wartungspläne", "Updates, backups, monitoring", "Updates, Backups, Monitoring"),
            ("website-check", "Free website check", "Kostenloser Website-Check", "Speed, mobile and SEO basics", "Ladezeit, Mobilansicht, SEO-Grundlagen"),
        ],
    },
    "language": {
        "en": "Language", "de": "Sprache", "hub": "language", "cls": "l",
        "en_line": "The translation team: qualified linguists, a second check on every job.",
        "de_line": "Das Übersetzungsteam: qualifizierte Fachleute, zweite Prüfung bei jedem Auftrag.",
        "items": [
            ("documents", "Document translation", "Dokumentübersetzung", "Certificates, statements, manuals", "Urkunden, Zeugnisse, Handbücher"),
            ("legal", "Legal translation", "Juristische Übersetzung", "Contracts and court papers", "Verträge und Gerichtsunterlagen"),
            ("medical", "Medical translation", "Medizinische Übersetzung", "Life sciences, under NDA", "Life Sciences, mit NDA"),
            ("patents", "Patent translation", "Patentübersetzung", "Claims kept consistent", "Einheitliche Ansprüche"),
            ("subtitling", "Subtitling and transcription", "Untertitelung und Transkription", "SRT, VTT, SDH, burned-in", "SRT, VTT, SDH, eingebrannt"),
            ("proofreading", "Proofreading and revision", "Korrektorat und Revision", "Check a translation you have", "Vorhandene Übersetzung prüfen"),
            ("quality", "MTPE and quality checks", "MTPE und Qualitätsprüfung", "Post-editing and LQA", "Post-Editing und LQA"),
            ("languages", "All languages", "Alle Sprachen", "Into and out of English", "Aus dem und ins Englische"),
        ],
    },
    "global": {
        "en": "Global", "de": "Global", "hub": "global", "cls": "b",
        "en_line": "Both teams together: your site and your words, ready for the next market.",
        "de_line": "Beide Teams zusammen: Website und Texte, bereit für den nächsten Markt.",
        "items": [
            ("international-launch", "International launch", "Internationaler Marktstart", "One team, one launch plan", "Ein Team, ein Startplan"),
            ("localization", "Website and app localisation", "Website- und App-Lokalisierung", "Your product, in their language", "Ihr Produkt in ihrer Sprache"),
            ("multilingual-seo", "Multilingual SEO", "Mehrsprachige SEO", "Found in every market", "In jedem Markt gefunden"),
            ("ecommerce-localisation", "Shop localisation", "Shop-Lokalisierung", "Shopify and WooCommerce", "Shopify und WooCommerce"),
            ("games", "Game localisation", "Spielelokalisierung", "Strings, stores, subtitles", "Strings, Stores, Untertitel"),
            ("readiness-check", "Free readiness check", "Kostenloser Readiness-Check", "Is your site ready to translate?", "Ist Ihre Website übersetzungsbereit?"),
            ("demo", "Live localisation demo", "Live-Lokalisierungsdemo", "Watch a page change language", "Eine Seite wechselt die Sprache"),
        ],
    },
}
# Footer and older code use these flat lists.
DIGITAL = [(s, en, de) for s, en, de, *_ in TEAMS["digital"]["items"] if s not in ("website-check", "web-design-glasgow")]
LANGUAGE = [(s, en, de) for s, en, de, *_ in TEAMS["language"]["items"] if s not in ("languages", "certified-translation-glasgow")] + \
    [(s, en, de) for s, en, de, *_ in TEAMS["global"]["items"] if s in ("localization", "multilingual-seo")]

# "What you get" on service pages. Only promises the site already makes elsewhere.
GETS = {
    "digital": {
        "en": ["A written quote before work starts", "A layout to review before the build", "A speed and accessibility report at launch",
               "The site, the code and the domain in your name", "CMS training at handover", "An optional care plan, never a requirement"],
        "de": ["Ein schriftliches Angebot vor Arbeitsbeginn", "Ein Layout zur Prüfung vor der Entwicklung", "Ein Bericht zu Ladezeit und Barrierefreiheit zum Start",
               "Website, Code und Domain auf Ihren Namen", "CMS-Schulung bei der Übergabe", "Ein optionaler Wartungsplan, keine Pflicht"],
    },
    "language": {
        "en": ["A written quote that names who works on your language pair", "A qualified translator for the subject", "A second linguist checking every job",
               "Layout matched to the original", "Delivery in the format you need", "One round of revisions on the delivered files"],
        "de": ["Ein schriftliches Angebot, das die Fachkraft für Ihr Sprachpaar nennt", "Eine qualifizierte Fachkraft für das Thema", "Eine zweite Prüfung bei jedem Auftrag",
               "Layout wie im Original", "Lieferung im gewünschten Format", "Eine Korrekturrunde an den gelieferten Dateien"],
    },
    "global": {
        "en": ["One project lead for the build and the language work", "One launch plan with dates per market", "Search terms researched in each language",
               "hreflang and locale URLs set up", "A check of every market version before launch", "Files you own, ready for the next language"],
        "de": ["Eine Projektleitung für Entwicklung und Sprache", "Ein Startplan mit Terminen je Markt", "Suchbegriffe in jeder Sprache recherchiert",
               "hreflang und Sprach-URLs eingerichtet", "Eine Prüfung jeder Marktversion vor dem Start", "Dateien, die Ihnen gehören, bereit für die nächste Sprache"],
    },
}


def team_of(slug):
    if slug.startswith("languages/"):
        return "language"
    for key, team in TEAMS.items():
        if slug == team["hub"] or any(it[0] == slug for it in team["items"]):
            return key
    return None


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
        "handle": "What we handle", "get": "What you get", "related": "Related services", "all_team": "All {team} services",
        "next": "Next step", "cta_h": "Tell us the job and the markets. We will scope it properly.",
        "cta_ticks": ["Written quote before work starts", "One project lead in Glasgow", "Second linguist on every translation"],
        "talk": "Let's talk", "talk_text": "Planning a site, a translation or a launch abroad? Send the brief and we reply by email with a quote or questions.",
        "standards": "Qualifications and standards", "contact_h": "Contact",
        "creds": ["MA in Translation Studies, Middlebury Institute", "CIOL Diploma in Translation, Merit",
                  "Processes aligned with ISO 17100 on request", "Sites tested against WCAG 2.2 AA"],
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
        "handle": "Was wir übernehmen", "get": "Das bekommen Sie", "related": "Verwandte Leistungen", "all_team": "Alle Leistungen: {team}",
        "next": "Nächster Schritt", "cta_h": "Nennen Sie uns Auftrag und Märkte. Wir planen es sorgfältig.",
        "cta_ticks": ["Schriftliches Angebot vor Arbeitsbeginn", "Eine Projektleitung in Glasgow", "Zweite Prüfung bei jeder Übersetzung"],
        "talk": "Sprechen wir", "talk_text": "Sie planen eine Website, eine Übersetzung oder einen Marktstart im Ausland? Schicken Sie uns das Briefing, und wir antworten per E-Mail mit Angebot oder Rückfragen.",
        "standards": "Qualifikationen und Standards", "contact_h": "Kontakt",
        "creds": ["MA in Translation Studies, Middlebury Institute", "CIOL Diploma in Translation, Merit",
                  "Abläufe nach ISO 17100 auf Wunsch", "Websites geprüft nach WCAG 2.2 AA"],
    },
}


def esc(s):
    return html.escape(s, quote=True)


def path(lang, slug):
    base = "/de/" if lang == "de" else "/"
    return base + (slug + "/" if slug else "")


def name_of(item, lang):
    return item[1] if lang == "en" else item[2]


def mega(lang, key):
    team = TEAMS[key]
    p = lambda x: path(lang, x)  # noqa: E731
    idx = 0 if lang == "en" else 1
    items = []
    for slug, en, de, den, dde in team["items"]:
        name, desc = (en, den) if lang == "en" else (de, dde)
        img = f"/img/scenes/{SCENES.get(slug, 'default')}.webp"
        items.append(f'<li><a href="{p(slug)}" data-img="{img}" data-desc="{esc(desc)}"><span class="roll"><span>{esc(name)}</span></span>'
                     f'<small>{esc(desc)}</small></a></li>')
    line = team[lang + "_line"]
    label = team[lang]
    meet = {"en": f"Meet the {label} team", "de": f"Zum Team {label}"}[lang]
    hub_img = f"/img/scenes/{SCENES.get(team['hub'], 'default')}.webp"
    return f"""<details class="menu team-{team['cls']}" data-mega>
        <summary><span class="roll"><span>{label}</span></span></summary>
        <div class="drop">
          <ul class="mega-list">{''.join(items)}</ul>
          <a class="mega-preview" href="{p(team['hub'])}">
            <img src="{hub_img}" alt="" width="900" height="675" loading="lazy" data-default="{hub_img}">
            <span class="mega-desc" data-default="{esc(line)}">{esc(line)}</span>
            <span class="mega-more">{meet} →</span>
          </a>
        </div>
      </details>"""


def header(lang, slug):
    t = UI[lang]
    other = "de" if lang == "en" else "en"
    p = lambda s: path(lang, s)  # noqa: E731
    top = [("work", t["work"]), ("pricing", t["pricing"]), ("about", t["about"])]
    top_links = "".join(f'<a href="{p(s)}"><span class="roll"><span>{esc(n)}</span></span></a>' for s, n in top)
    def drawer_team(key):
        team = TEAMS[key]
        lis = "".join(f'<li><a href="{p(s)}">{esc(en if lang == "en" else de)}</a></li>' for s, en, de, *_ in team["items"])
        return f'<div class="team-{team["cls"]}"><p class="kicker"><a href="{p(team["hub"])}">{team[lang]}</a></p><ul>{lis}</ul></div>'
    drawer_more = "".join(f'<li><a href="{p(s)}">{esc(n)}</a></li>' for s, n in
                          top + [("process", t["process"]), ("insights", t["insights"]), ("faq", t["faq"])])
    return f"""<a class="skip" href="#content">{t['skip']}</a>
<div class="progress" aria-hidden="true"></div>
<header class="nav">
  <div class="shell nav-row">
    <a class="mark" href="{p('')}"><span class="roll"><span>Kayonne</span></span></a>
    <nav class="links" aria-label="{t['services']}">
      {mega(lang, "digital")}
      {mega(lang, "language")}
      {mega(lang, "global")}
      {top_links}
    </nav>
    <div class="nav-actions">
      <a class="btn ghost" href="{path(other, slug)}" hreflang="{other}" lang="{other}" title="{UI[lang]['switch']}">{t['switch_short']}</a>
      <a class="btn nav-quote magnetic" href="{p('contact')}">{t['quote']}</a>
      <button class="btn ghost burger" type="button" aria-expanded="false" aria-controls="drawer">{t['menu']}</button>
    </div>
  </div>
  <div class="shell drawer" id="drawer">
    <p class="drawer-cta"><a class="btn" href="{p('contact')}">{t['quote']}</a></p>
    {drawer_team("digital")}
    {drawer_team("language")}
    {drawer_team("global")}
    <div><p class="kicker">{t['company']}</p><ul>{drawer_more}</ul></div>
  </div>
</header>"""


HELLOS = ["Hello", "Hallo", "Bonjour", "こんにちは", "Hola", "你好", "Ciao", "안녕하세요", "Olá", "Cześć",
          "Merhaba", "Привіт", "مرحبا", "नमस्ते", "Hej", "Xin chào", "Salut", "Γεια σας"]


def marquee():
    words = "".join(f'<span lang="und">{w}</span><i>✦</i>' for w in HELLOS)
    return (f'<div class="marquee" aria-hidden="true"><div class="marquee-track">{words}{words}</div></div>'
            f'<div class="marquee rev" aria-hidden="true"><div class="marquee-track">{words}{words}</div></div>')


def footer(lang):
    t = UI[lang]
    p = lambda s: path(lang, s)  # noqa: E731
    cols = ""
    for key in ("digital", "language", "global"):
        team = TEAMS[key]
        links = "".join(f'<li><a href="{p(s)}">{esc(en if lang == "en" else de)}</a></li>' for s, en, de, *_ in team["items"])
        cols += f'<div class="team-{team["cls"]}"><p class="kicker"><a href="{p(team["hub"])}">{team[lang]}</a></p><ul>{links}</ul></div>'
    comp = "".join(f'<li><a href="{p(s)}">{esc(t[k])}</a></li>' for s, k in [
        ("about", "about"), ("process", "process"), ("industries", "industries"),
        ("pricing", "pricing"), ("work", "work"), ("faq", "faq"), ("insights", "insights"), ("contact", "contact")])
    legal = " · ".join(f'<a href="{p(s)}">{esc(t[s])}</a>' for s in ("privacy", "cookies", "terms"))
    return f"""{marquee()}<footer><div class="shell foot">
    <div>
      <p class="mark">Kayonne Creatives</p>
      <p class="note">{t['tagline']}</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p class="note">{t['place']}</p>
    </div>
    {cols}
    <div><p class="kicker">{t['company']}</p><ul>{comp}</ul></div>
  </div>
  <div class="shell foot-row">
    <div><p class="kicker">{t['contact_h']}</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p class="note">{t['place']}</p></div>
    <div><p class="kicker">{t['standards']}</p><ul class="ticks">{lis(t['creds'])}</ul></div>
    <div class="foot-talk"><p class="kicker">{t['talk']}</p><p class="note">{t['talk_text']}</p><p><a class="btn magnetic" href="{p('contact')}">{t['quote']}</a></p></div>
  </div>
  <p class="shell wordmark" aria-hidden="true">Kayonne</p>
  <div class="shell foot-base note"><p>© {YEAR} Kayonne Creatives · {t['place']}</p><p>{legal}</p></div>
</footer>"""


SCRIPT = """<script>
(function(){
  var b=document.querySelector(".burger"),d=document.getElementById("drawer");
  if(b&&d){b.addEventListener("click",function(){var o=d.classList.toggle("open");b.setAttribute("aria-expanded",o?"true":"false");});}
  var menus=[].slice.call(document.querySelectorAll("details[data-mega]"));
  var hover=window.matchMedia("(hover: hover) and (min-width: 1000px)").matches;
  function closeAll(except){menus.forEach(function(m){if(m!==except)m.open=false;});}
  menus.forEach(function(m){
    var t;
    m.addEventListener("toggle",function(){if(m.open)closeAll(m);});
    if(hover){
      m.addEventListener("mouseenter",function(){clearTimeout(t);m.open=true;});
      m.addEventListener("mouseleave",function(){t=setTimeout(function(){m.open=false;},180);});
    }
    var img=m.querySelector(".mega-preview img"),desc=m.querySelector(".mega-desc");
    [].slice.call(m.querySelectorAll(".mega-list a")).forEach(function(a){
      function show(){
        if(img&&img.getAttribute("src")!==a.dataset.img){img.classList.remove("swap");void img.offsetWidth;img.src=a.dataset.img;img.classList.add("swap");}
        if(desc)desc.textContent=a.dataset.desc;
      }
      a.addEventListener("mouseenter",show);a.addEventListener("focus",show);
    });
  });
  document.addEventListener("click",function(e){menus.forEach(function(m){if(m.open&&!m.contains(e.target))m.open=false;});});
  document.addEventListener("keydown",function(e){if(e.key==="Escape"){menus.forEach(function(m){if(m.open){m.open=false;m.querySelector("summary").focus();}});}});
  var q=new URLSearchParams(location.search).get("service"),sel=document.getElementById("f-service");
  if(q&&sel){[].slice.call(sel.options).forEach(function(o){if(o.text===q)sel.value=o.value||o.text;});}
})();
</script>
<script src="/js/motion.js" defer></script>"""

# The 3D object shown at the top of each page (see js/scene.js for the list).
SCENES = {
    "": "hero", "services": "hero", "websites": "windows", "web-apps": "cubes", "mobile-apps": "phone",
    "domains-email": "network", "seo": "bars", "speed": "tunnel", "care": "shield", "certified-translation": "seal",
    "documents": "sheets", "localization": "globe", "games": "dice", "medical": "helix", "patents": "gears",
    "legal": "scales", "subtitling": "film", "proofreading": "lens", "quality": "check", "languages": "globe",
    "industries": "shards", "work": "windows", "process": "path", "pricing": "bars", "about": "orbit", "faq": "ico",
    "insights": "sheets", "insights/localise-a-website": "globe", "insights/speed-mistakes": "tunnel",
    "contact": "plane", "thanks": "plane", "privacy": "shield", "cookies": "shield", "terms": "scales",
    "studio": "cubes", "demo": "globe", "404": "ico",
    "digital": "windows", "language": "sheets", "global": "globe", "web-design-glasgow": "windows",
    "website-check": "lens", "certified-translation-glasgow": "seal", "apostille": "scales",
    "multilingual-seo": "bars", "international-launch": "plane", "ecommerce-localisation": "tiles",
    "readiness-check": "check",
    "insights/home-office-certified-translation": "seal", "insights/website-cost-glasgow": "windows",
    "insights/multilingual-seo-keywords": "bars",
}


REDIRECTS = {
    "certified-translation": "documents",
    "certified-translation-glasgow": "documents",
    "apostille": "documents",
    "insights/home-office-certified-translation": "insights",
}


def intro_html(page, slug, ticks=None, actions=""):
    scene = page.get("scene") or SCENES.get(slug, "globe" if slug.startswith("languages/") else "default")
    art = ""
    if os.path.exists(f"img/scenes/{scene}.webp"):
        art = (f'<figure class="intro-art"><img src="/img/scenes/{scene}.webp" alt="" width="900" height="675" '
               f'decoding="async" fetchpriority="low"></figure>')
    inner = f'<p class="kicker">{page.get("label", "")}</p><h1>{page["h1"]}</h1>'
    if page.get("lede"):
        inner += f'<p class="lede">{page["lede"]}</p>'
    if ticks:
        inner += f'<ul class="ticks cols intro-ticks">{lis(ticks)}</ul>'
    if actions:
        inner += f'<p class="actions">{actions}</p>'
    cls ="intro has-art" if art else "intro"
    return f'<header class="{cls}" data-scene="{scene}">{inner}{art}</header>'


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
    return f'<section class="split" data-scene="ico"><h2>{t["questions"]}</h2><div class="stack">{items}</div></section>'


def cta(lang):
    t = UI[lang]
    return (f'<section class="cta-band" data-scene="ring"><div><p class="kicker">{t["next"]}</p><h2>{t["cta_h"]}</h2>'
            f'<ul class="ticks inline">{lis(t["cta_ticks"])}</ul></div>'
            f'<p><a class="btn magnetic" href="{path(lang, "contact")}">{t["quote"]}</a></p></section>')


def related(lang, slug):
    key = team_of(slug)
    if not key:
        return ""
    t = UI[lang]
    team = TEAMS[key]
    if slug.startswith("languages/"):
        picks = [it for it in team["items"] if it[0] in ("documents", "proofreading", "subtitling")]
    else:
        skip = {slug, "website-check", "readiness-check", "demo", "languages", "web-design-glasgow"}
        picks = [it for it in team["items"] if it[0] not in skip][:3]
    cards = "".join(f'<li><a class="card team-{team["cls"]}" href="{path(lang, s_)}"><strong>{esc(en if lang == "en" else de)}</strong>'
                    f'<span class="note">{esc(den if lang == "en" else dde)}</span></a></li>'
                    for s_, en, de, den, dde in picks)
    more = t["all_team"].format(team=team[lang])
    return (f'<section data-scene="tiles"><div class="sec-head"><h2>{t["related"]}</h2>'
            f'<a class="text-link" href="{path(lang, team["hub"])}">{esc(more)} →</a></div>'
            f'<ul class="grid-3 link-cards accent-cards">{cards}</ul></section>')


def service_main(lang, page, slug):
    t = UI[lang]
    key = team_of(slug)
    team = TEAMS.get(key)
    actions = f'<a class="btn magnetic" href="{path(lang, "contact")}">{t["quote"]}</a>'
    if team:
        actions += f' <a class="btn ghost" href="{path(lang, team["hub"])}">{esc(t["all_team"].format(team=team[lang]))}</a>'
    cls = f' team-{team["cls"]}' if team else ""
    parts = [intro_html(page, slug, page.get("why"), actions)]
    if page.get("incl"):
        cards = "".join(f'<li class="card">{x}</li>' for x in page["incl"])
        parts.append(f'<section class="tint{cls}" data-scene="tiles"><h2>{t["handle"]}</h2><ul class="grid-3 handle">{cards}</ul></section>')
    parts.append(page.get("extra", ""))
    if page.get("steps"):
        steps = "".join(f'<li><h3>{a}</h3><p class="note">{b}</p></li>' for a, b in page["steps"])
        parts.append(f'<section class="split band{cls}" data-scene="path"><h2>{t["steps"]}</h2><ol class="num-list">{steps}</ol></section>')
    if key:
        parts.append(f'<section data-scene="orbit"><h2>{t["get"]}</h2><ul class="get-list{cls}">{lis(GETS[key][lang])}</ul></section>')
    if page.get("who"):
        parts.append(f'<section class="split" data-scene="shards"><h2>{t["who"]}</h2><p class="lede">{page["who"]}</p></section>')
    parts.append(faq_html(page.get("faq"), t))
    parts.append(related(lang, slug))
    parts.append(cta(lang))
    return "".join(parts)


def raw_main(lang, page, slug):
    t = UI[lang]
    body = page["body"]
    intro = intro_html(page, slug) if page.get("h1") else ""
    tail = faq_html(page.get("faq"), t) + ("" if page.get("no_cta") else cta(lang))
    return intro + body + tail


def team_cards(lang, key):
    team = TEAMS[key]
    out = []
    for s_, en, de, den, dde in team["items"]:
        name, desc = (en, den) if lang == "en" else (de, dde)
        out.append(f'<li><a class="card img-card team-{team["cls"]}" href="{path(lang, s_)}">'
                   f'<img src="/img/scenes/{SCENES.get(s_, "default")}.webp" alt="" width="900" height="675" loading="lazy" decoding="async">'
                   f'<strong>{esc(name)}</strong><span class="note">{esc(desc)}</span></a></li>')
    return '<ul class="grid-3 link-cards img-cards">' + "".join(out) + "</ul>"


def service_grid(lang):
    """Every paid service, coloured by team, for the home page."""
    skip = {"website-check", "readiness-check", "demo", "languages", "web-design-glasgow"}
    out = []
    for key in ("digital", "language", "global"):
        team = TEAMS[key]
        for s_, en, de, den, dde in team["items"]:
            if s_ in skip:
                continue
            name, desc = (en, den) if lang == "en" else (de, dde)
            out.append(f'<li><a class="card team-{team["cls"]}" href="{path(lang, s_)}"><span class="kicker">{team[lang]}</span>'
                       f'<strong>{esc(name)}</strong><span class="note">{esc(desc)}</span></a></li>')
    return '<ul class="grid-4 link-cards accent-cards">' + "".join(out) + "</ul>"


def insight_cards(lang, n=None):
    mod = LANGS[lang]
    items = [(s_, p_) for s_, p_ in mod.PAGES.items() if s_.startswith("insights/")][::-1][:n]
    out = "".join(f'<li><a class="card img-card team-d" href="{path(lang, s_)}">'
                  f'<img src="/img/scenes/{SCENES.get(s_, "default")}.webp" alt="" width="900" height="675" loading="lazy" decoding="async">'
                  f'<strong>{strip(p_["h1"])}</strong><span class="note">{esc(p_["desc"])}</span></a></li>' for s_, p_ in items)
    return '<ul class="grid-3 link-cards img-cards">' + out + "</ul>"


def pair_cards(lang):
    mod = LANGS[lang]
    out = []
    for slug, page in mod.PAGES.items():
        if slug.startswith("languages/"):
            out.append(f'<li><a class="card" href="{path(lang, slug)}"><strong>{page["label"]}</strong>'
                       f'<span class="note">{esc(strip(page["h1"]))}</span></a></li>')
    return '<ul class="grid-3 link-cards">' + "".join(out) + "</ul>"


def render(lang, slug, page, weights=""):
    main = service_main(lang, page, slug) if page.get("kind") == "service" else raw_main(lang, page, slug)
    main = main.replace("{{WEIGHTS}}", weights).replace("{{PAIRS}}", pair_cards(lang) if "{{PAIRS}}" in main else "")
    main = main.replace("{{SERVICES}}", service_grid(lang) if "{{SERVICES}}" in main else "")
    main = main.replace("{{INSIGHTS3}}", insight_cards(lang, 3) if "{{INSIGHTS3}}" in main else "")
    main = main.replace("{{INSIGHTS}}", insight_cards(lang) if "{{INSIGHTS}}" in main else "")
    main = re.sub(r"\{\{TEAM:(\w+)\}\}", lambda m: team_cards(lang, m.group(1)), main)
    cls = "page" + (" home" if slug == "" else "")
    link_slug = "" if slug == "404" else slug
    return (head(lang, slug, page) + "\n<body>\n" + header(lang, link_slug) +
            f'\n<main id="content" class="shell {cls}">{main}</main>\n' + footer(lang) + "\n" + SCRIPT +
            page.get("script", "") + "\n</body>\n</html>\n")


def kb(n):
    return f"{n / 1024:.1f} KB"


def weights_table(lang):
    heads = {"en": ("Page", "HTML", "Compressed (gzip)"), "de": ("Seite", "HTML", "Komprimiert (gzip)")}[lang]
    shared = {"en": "Shared stylesheet, fonts and motion script", "de": "Gemeinsames Stylesheet, Schriften und Animationsskript"}[lang]
    import gzip
    rows = []
    for slug in ("", "services", "websites", "documents", "contact", "languages"):
        data = open(out_file(lang, slug), "rb").read()
        label = LANGS[lang].PAGES[slug]["title"].split(" | ")[0] if slug else UI[lang]["home"]
        rows.append(f'<tr><td><a href="{path(lang, slug)}">{esc(label)}</a></td><td class="n">{kb(len(data))}</td>'
                    f'<td class="n">{kb(len(gzip.compress(data)))}</td></tr>')
    assets = ["css/site.css", "js/motion.js"] + sorted("fonts/" + f for f in os.listdir("fonts"))
    total = sum(os.path.getsize(a) for a in assets)
    rows.append(f'<tr><td>{shared}</td><td class="n">{kb(total)}</td><td class="n">–</td></tr>')
    three = ["js/scene.js", "js/three.module.min.js", "js/RoomEnvironment.js"]
    raw3 = sum(os.path.getsize(a) for a in three)
    gz3 = sum(len(gzip.compress(open(a, "rb").read())) for a in three)
    label3 = {"en": "3D scenes (three.js), loaded after the page", "de": "3D-Szenen (three.js), nach der Seite geladen"}[lang]
    rows.append(f'<tr><td>{label3}</td><td class="n">{kb(raw3)}</td><td class="n">{kb(gz3)}</td></tr>')
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
    # Removed pages forward to the closest page that still exists.
    for lang in LANGS:
        for old, new in REDIRECTS.items():
            f = out_file(lang, old)
            os.makedirs(os.path.dirname(f), exist_ok=True)
            target = path(lang, new)
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><title>Kayonne Creatives</title>'
                         f'<meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url={target}">'
                         f'<link rel="canonical" href="{SITE + target}"></head><body><p><a href="{target}">{target}</a></p></body></html>\n')
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
