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
import content_growth  # noqa: E402
import settings  # noqa: E402

SITE = "https://kayonnecreatives.com"
EMAIL = "hello@kayonnecreatives.com"
YEAR = datetime.date.today().year
LANGS = {"en": content_en, "de": content_de}

from divisions import DIVISIONS, GROWTH_BOOK_URL, NOT_SERVICES  # noqa: E402

# Pages that exist in English only (no German version, no language switcher, no hreflang pair).
EN_ONLY = set(content_growth.PAGES)
content_en.PAGES.update(content_growth.PAGES)

# Divisions keyed by id. The extra keys keep older code working: team["en"] is the menu label,
# team["hub"] the landing page, team["en_line"] the one-line description.
TEAMS = {}
for _d in DIVISIONS:
    _d.update(hub=_d["slug"], en=_d["name"]["en"], de=_d["name"].get("de", ""),
              en_line=_d["line"]["en"], de_line=_d["line"].get("de", ""))
    TEAMS[_d["key"]] = _d


# Each division's colour, so a new division needs no CSS edit.
TEAM_STYLE = "<style>" + "".join(f".team-{d['cls']}{{--team:{d['color']}}}" for d in DIVISIONS) + "</style>"


def lean(page):
    """True for pages of a division that drops the language extras (switcher, greetings, qualifications, 3D)."""
    d = TEAMS.get((page or {}).get("division"))
    return bool(d and d.get("lean"))


def divisions(lang):
    """The divisions that have pages in this language, in menu order."""
    return [d for d in DIVISIONS if lang in d["langs"]]


# "What you get" on service pages. Only promises the site already makes elsewhere.
GETS = {
    "digital": {
        "en": ["A written quote before work starts", "A layout to review before the build", "A speed and accessibility report at launch",
               "The site, the code and the domain in your name", "CMS training at handover", "An optional care plan, never a requirement"],
        "de": ["Ein schriftliches Angebot vor Arbeitsbeginn", "Ein Layout zur Prüfung vor der Entwicklung", "Ein Bericht zu Ladezeit und Barrierefreiheit zum Start",
               "Website, Code und Domain auf Ihren Namen", "CMS-Schulung bei der Übergabe", "Ein optionaler Wartungsplan, keine Pflicht"],
    },
    "localize": {
        "en": ["A written quote that names who works on your language pair", "A qualified translator for the subject", "A second linguist checking every job",
               "Layout matched to the original", "Delivery in the format you need", "One round of revisions on the delivered files"],
        "de": ["Ein schriftliches Angebot, das die Fachkraft für Ihr Sprachpaar nennt", "Eine qualifizierte Fachkraft für das Thema", "Eine zweite Prüfung bei jedem Auftrag",
               "Layout wie im Original", "Lieferung im gewünschten Format", "Eine Korrekturrunde an den gelieferten Dateien"],
    },
    "launch": {
        "en": ["One project lead for the build and the language work", "One launch plan with dates per market", "Search terms researched in each language",
               "hreflang and locale URLs set up", "A check of every market version before launch", "Files you own, ready for the next language"],
        "de": ["Eine Projektleitung für Entwicklung und Sprache", "Ein Startplan mit Terminen je Markt", "Suchbegriffe in jeder Sprache recherchiert",
               "hreflang und Sprach-URLs eingerichtet", "Eine Prüfung jeder Marktversion vor dem Start", "Dateien, die Ihnen gehören, bereit für die nächste Sprache"],
    },
}


# Localize services that take a website or product abroad, as opposed to translation work.
LAUNCH = set(content_en.LAUNCH)


def team_of(slug):
    if slug.startswith("languages/"):
        return "localize"
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
        "tagline": "Websites, translation and customer growth, from Glasgow.",
        "place": "Glasgow, United Kingdom", "company": "Company", "legal": "Legal",
        "privacy": "Privacy", "cookies": "Cookies", "terms": "Terms",
        "why": "Why it helps", "incl": "What is included", "steps": "How it works", "who": "Who it is for",
        "questions": "Questions", "cta_text": "Tell us what you need. You get a written quote before any work starts.",
        "locale": "en_GB", "home": "Home",
        "handle": "What we handle", "get": "What you get", "related": "Related services", "all_team": "All {team} services",
        "next": "Next step", "cta_h": "Tell us the job and the markets. We will scope it properly.",
        "cta_ticks": ["Written quote before work starts", "One project lead in Glasgow", "Second linguist on every translation"],
        "talk": "Let's talk", "talk_text": "Planning a site, a translation or a launch abroad? Send the brief and we reply by email with a quote or questions.",
        "standards": "How we work", "contact_h": "Contact",
        "creds": ["Every translation checked by a second linguist", "A written quote before work starts",
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
        "standards": "So arbeiten wir", "contact_h": "Kontakt",
        "creds": ["Jede Übersetzung von einer zweiten Fachkraft geprüft", "Ein schriftliches Angebot vor Arbeitsbeginn",
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


COMPANY = ["about", "work", "process", "industries", "pricing", "insights", "faq", "contact"]


def company_menu(lang):
    t = UI[lang]
    items = "".join(f'<li><a href="{path(lang, s_)}"><span class="roll"><span>{esc(t[s_])}</span></span></a></li>' for s_ in COMPANY)
    return (f'<details class="menu company" data-mega><summary><span class="roll"><span>{t["company"]}</span></span></summary>'
            f'<div class="drop simple"><ul class="mega-list">{items}</ul></div></details>')


def crumbs(lang, slug, page):
    """Breadcrumb trail for division pages and the pages under them, or None."""
    key = team_of(slug)
    if not key or page.get("noindex"):
        return None
    d = TEAMS[key]
    trail = [(UI[lang]["home"], path(lang, ""))]
    names = {s_: (en if lang == "en" else de) for s_, en, de, *_ in d["items"]}
    if slug == d["slug"]:
        trail.append((d["name"][lang], None))
        return trail
    trail.append((d["name"][lang], path(lang, d["slug"])))
    if slug.startswith("languages/"):
        trail.append((names["languages"], path(lang, "languages")))
    trail.append((page.get("crumb") or names.get(slug) or strip(page.get("label") or page["h1"]), None))
    return trail


def crumbs_html(trail):
    lis_ = "".join(f'<li><a href="{h}">{esc(n)}</a></li>' if h else f'<li aria-current="page">{esc(n)}</li>' for n, h in trail)
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{lis_}</ol></nav>'


def crumbs_schema(trail, lang, slug):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + (h or path(lang, slug))} for i, (n, h) in enumerate(trail)]}


def person_block():
    """ "Who you'll work with": photo (or initials until a photo is set), name, role, bio, LinkedIn."""
    p = settings.PERSON
    initials = "".join(w[0] for w in p["name"].split()[:2])
    pic = (f'<img src="{esc(p["photo"])}" alt="{esc(p["name"])}" width="400" height="400" loading="lazy">' if p["photo"]
           else f'<span class="person-initials" aria-hidden="true">{initials}</span>')
    li = (f'<p><a class="social" href="{esc(settings.LINKEDIN_URL)}" rel="noopener">{LINKEDIN_ICON}<span>{esc(p["name"].split()[0])} on LinkedIn</span></a></p>'
          if settings.LINKEDIN_URL else "")
    return (f'<section class="person" aria-labelledby="person-h"><div class="person-pic">{pic}</div><div>'
            f'<p class="kicker">Who you&#39;ll work with</p><h2 id="person-h">{esc(p["name"])}</h2>'
            f'<p class="person-role">{esc(p["role"])}</p><p>{esc(p["bio"])}</p>{li}</div></section>')


def phone_line(lang):
    if not settings.PHONE:
        return ""
    label = "Prefer to call?" if lang == "en" else "Lieber anrufen?"
    return f'<p class="phone-line">{label} {tel(settings.PHONE)}</p>'


def chooser(lang):
    """The home page "What do you need?" cards, one per division."""
    h = "What do you need?" if lang == "en" else "Was brauchen Sie?"
    cards = "".join(f'<li><a class="need team-{d["cls"]}" href="{path(lang, d["slug"])}"><span class="g-ico">{icon(d["icon"], 28)}</span>'
                    f'<strong>{esc(d["need"][lang])}</strong><span class="need-more">{esc(d["brand"][lang])} →</span></a></li>'
                    for d in divisions(lang) if d.get("need", {}).get(lang))
    return f'<section class="chooser" aria-labelledby="need-h"><h2 id="need-h">{h}</h2><ul>{cards}</ul></section>'


def header(lang, slug, page=None):
    t = UI[lang]
    d = TEAMS.get((page or {}).get("division"))
    cta_label, cta_href = ((d or {}).get("cta") or {}).get(lang) or (t["quote"], path(lang, "contact"))
    switch = "" if slug in EN_ONLY else (f'<a class="btn ghost" href="{path("de" if lang == "en" else "en", slug)}" hreflang="{"de" if lang == "en" else "en"}" '
                                         f'lang="{"de" if lang == "en" else "en"}" title="{UI[lang]["switch"]}">{t["switch_short"]}</a>')
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
      {"".join(mega(lang, d["key"]) for d in divisions(lang))}
      {company_menu(lang)}
    </nav>
    <div class="nav-actions">
      {switch}
      <a class="btn nav-quote magnetic" href="{cta_href}">{cta_label}</a>
      <button class="btn ghost burger" type="button" aria-expanded="false" aria-controls="drawer">{t['menu']}</button>
    </div>
  </div>
  <div class="shell drawer" id="drawer">
    <p class="drawer-cta"><a class="btn" href="{cta_href}">{cta_label}</a></p>
    {"".join(drawer_team(d["key"]) for d in divisions(lang))}
    <div><p class="kicker">{t['company']}</p><ul>{drawer_more}</ul></div>
  </div>
</header>"""


HELLOS = ["Hello", "Hallo", "Bonjour", "こんにちは", "Hola", "你好", "Ciao", "안녕하세요", "Olá", "Cześć",
          "Merhaba", "Привіт", "مرحبا", "नमस्ते", "Hej", "Xin chào", "Salut", "Γεια σας"]


def marquee():
    words = "".join(f'<span lang="und">{w}</span><i>✦</i>' for w in HELLOS)
    return (f'<div class="marquee" aria-hidden="true"><div class="marquee-track">{words}{words}</div></div>'
            f'<div class="marquee rev" aria-hidden="true"><div class="marquee-track">{words}{words}</div></div>')


def phone_for(page):
    """The phone number for this page: the US number on Growth pages when there is one."""
    return settings.PHONE_US if lean(page) and settings.PHONE_US else settings.PHONE


def tel(number):
    return f'<a href="tel:{re.sub(r"[^0-9+]", "", number)}">{esc(number)}</a>' if number else ""


LINKEDIN_ICON = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 '
                 '2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5.2c0-1.2 0-2.8-1.7-2.8s-2 1.3-2 2.7V21h-4z"/></svg>')


def footer(lang, page=None, slug=""):
    t = UI[lang]
    plain = lean(page)
    # The "Let's talk" text and "How we work" points follow the division of the current page.
    d = TEAMS.get((page or {}).get("division") or team_of(slug))
    talk_text, talk_label, talk_href, points = t["talk_text"], t["quote"], path(lang, "contact"), t["creds"]
    if d and d.get("footer", {}).get(lang):
        talk_text, points = d["footer"][lang]
    if d and d.get("cta"):
        talk_label, talk_href = d["cta"][lang]
    phone = phone_for(page)
    contact = f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>' + (f'<p>{tel(phone)}</p>' if phone else "")
    contact += f'<p class="note">{t["place"]}</p>'
    if settings.LINKEDIN_URL:
        contact += f'<p><a class="social" href="{esc(settings.LINKEDIN_URL)}" rel="noopener">{LINKEDIN_ICON}<span>LinkedIn</span></a></p>'
    company_no = f' · {"Company number" if lang == "en" else "Handelsregisternummer"} {esc(settings.COMPANY_NO)}' if settings.COMPANY_NO else ""
    p = lambda s: path(lang, s)  # noqa: E731
    cols = ""
    for team in divisions(lang):
        links = "".join(f'<li><a href="{p(s)}">{esc(en if lang == "en" else de)}</a></li>' for s, en, de, *_ in team["items"])
        cols += f'<div class="team-{team["cls"]}"><p class="kicker"><a href="{p(team["hub"])}">{team[lang]}</a></p><ul>{links}</ul></div>'
    comp = "".join(f'<li><a href="{p(s)}">{esc(t[k])}</a></li>' for s, k in [
        ("about", "about"), ("process", "process"), ("industries", "industries"),
        ("pricing", "pricing"), ("work", "work"), ("faq", "faq"), ("insights", "insights"), ("contact", "contact")])
    legal = " · ".join(f'<a href="{p(s)}">{esc(t[s])}</a>' for s in ("privacy", "cookies", "terms"))
    standards = f'<div><p class="kicker">{t["standards"]}</p><ul class="ticks">{lis(points)}</ul></div>'
    return f"""{"" if plain else marquee()}<footer><div class="shell foot">
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
    <div><p class="kicker">{t['contact_h']}</p>{contact}</div>
    {standards}
    <div class="foot-talk"><p class="kicker">{t['talk']}</p><p class="note">{talk_text}</p><p><a class="btn magnetic" href="{talk_href}">{talk_label}</a></p></div>
  </div>
  <p class="shell wordmark" aria-hidden="true">Kayonne</p>
  <div class="shell foot-base note"><p>© {YEAR} Kayonne Creatives · {t['place']}{company_no}</p><p>{legal}</p></div>
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
  var tm=new URLSearchParams(location.search).get("team"),ts=document.getElementById("f-team");
  if(tm&&ts){[].slice.call(ts.options).forEach(function(o){if(o.value===tm)ts.value=tm;});}
  // Growth inquiries ask about the business instead of languages and files.
  if(ts){
    var form=ts.form,swap=[].slice.call(document.querySelectorAll(".intro [data-growth],#quote [data-growth]"));
    swap.forEach(function(el){el.dataset.base=el.tagName==="INPUT"?el.value:el.innerHTML;});
    var mode=function(){
      var g=ts.value==="growth";
      [].slice.call(form.querySelectorAll("[data-team],[data-team-not]")).forEach(function(box){
        var show=box.hasAttribute("data-team")?g:!g;box.hidden=!show;
        [].slice.call(box.querySelectorAll("input,select,textarea")).forEach(function(i){i.disabled=!show;});
      });
      var ph=document.getElementById("f-phone");if(ph)ph.required=g;
      swap.forEach(function(el){if(el.tagName==="INPUT")el.value=g?el.dataset.growth:el.dataset.base;else if(g)el.textContent=el.dataset.growth;else el.innerHTML=el.dataset.base;});
      document.documentElement.classList.toggle("team-growth",g);
    };
    ts.addEventListener("change",mode);mode();
  }
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
    "digital": "windows", "localize": "globe", "web-design-glasgow": "windows",
    "website-check": "lens", "certified-translation-glasgow": "seal", "apostille": "scales",
    "multilingual-seo": "bars", "international-launch": "plane", "ecommerce-localisation": "tiles",
    "readiness-check": "check",
    "insights/home-office-certified-translation": "seal", "insights/website-cost-glasgow": "windows",
    "insights/multilingual-seo-keywords": "bars",
}


REDIRECTS = {
    "language": "localize",
    "global": "localize",
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
    g1 = f' data-growth="{esc(page["growth_h1"])}"' if page.get("growth_h1") else ""
    g2 = f' data-growth="{esc(page["growth_lede"])}"' if page.get("growth_lede") else ""
    inner = f'<p class="kicker">{page.get("label", "")}</p><h1{g1}>{page["h1"]}</h1>'
    if page.get("lede"):
        inner += f'<p class="lede"{g2}>{page["lede"]}</p>'
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
        "contactPoint": [{"@type": "ContactPoint", "contactType": "customer service", "email": EMAIL,
                          **({"telephone": settings.PHONE} if settings.PHONE else {})}],
        **({"sameAs": [settings.LINKEDIN_URL]} if settings.LINKEDIN_URL else {}),
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
    if slug in EN_ONLY:
        alts = ""
    html_lang = page.get("html_lang", lang)
    schemas = list(page.get("schema", []))
    if slug in ("", "contact", "pricing"):
        schemas.insert(0, org_schema(lang))
    if slug == "contact":
        schemas.append({"@context": "https://schema.org", "@type": "ContactPage", "name": title, "url": url,
                        "about": {"@type": "Organization", "name": "Kayonne Creatives", "url": SITE + "/"}})
    if page.get("faq"):
        schemas.append(faq_schema(page["faq"]))
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    robots = '<meta name="robots" content="noindex" />' if page.get("noindex") else ""
    if page.get("noindex"):
        alts = ""
    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
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
<meta property="og:locale" content="{page.get('og_locale', UI[lang]['locale'])}" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="preload" href="/fonts/outfit-latin.woff2" as="font" type="font/woff2" crossorigin />
<link rel="preload" href="/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin />
<link rel="stylesheet" href="/css/site.css" />
{TEAM_STYLE}
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
        same = [it for it in team["items"] if (it[0] in LAUNCH) == (slug in LAUNCH)]
        picks = [it for it in same if it[0] not in NOT_SERVICES | {slug}][:3]
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
        gets = GETS["launch" if slug in LAUNCH else key][lang]
        parts.append(f'<section data-scene="orbit"><h2>{t["get"]}</h2><ul class="get-list{cls}">{lis(gets)}</ul></section>')
    if page.get("who"):
        parts.append(f'<section class="split" data-scene="shards"><h2>{t["who"]}</h2><p class="lede">{page["who"]}</p></section>')
    parts.append(faq_html(page.get("faq"), t))
    parts.append(related(lang, slug))
    parts.append(cta(lang))
    return "".join(parts)


def division_main(lang, page, slug):
    """Landing page for a division: hero, service cards, how it works, offer, FAQ, CTA.
    Optional "before" and "after" hold extra sections, placed before and after "how it works"."""
    t = UI[lang]
    d = TEAMS[page["division"]]
    cls = f' team-{d["cls"]}'
    page = dict(page, label=page.get("label") or d["brand"][lang], h1=page.get("h1") or d["tagline"][lang])
    actions = f'<a class="btn magnetic" href="{path(lang, "contact")}?team={d["key"]}">{t["quote"]}</a>'
    if page.get("secondary"):
        actions += f' <a class="btn ghost" href="{page["secondary"][1]}">{page["secondary"][0]}</a>'
    parts = [intro_html(page, slug, page.get("ticks"), actions)]
    # Service cards: all of the division's items, or named groups of them.
    for h, only, scene in page.get("groups") or [(page["services_h"], None, page.get("services_scene", "windows"))]:
        parts.append(f'<section data-scene="{scene}"><h2>{h}</h2>{team_cards(lang, d["key"], only)}</section>')
    parts.append(page.get("before", ""))
    if page.get("how"):
        steps = "".join(f'<li><h3>{a}</h3><p class="note">{b}</p></li>' for a, b in page["how"])
        parts.append(f'<section class="split band{cls}" data-scene="path"><h2>{page["how_h"]}</h2><ol class="num-list">{steps}</ol></section>')
    parts.append(page.get("after", ""))
    o = page.get("offer")
    if o:
        parts.append(f'<section data-scene="{o.get("scene", "check")}" class="offer card"><div><p class="kicker">{o["kicker"]}</p><h2>{o["title"]}</h2>'
                     f'<p>{o["text"]}</p></div><p><a class="btn magnetic" href="{o["href"]}">{o["button"]}</a></p></section>')
    parts.append(faq_html(page.get("faq"), t))
    parts.append(cta(lang))
    return "".join(parts)


# ---- Kayonne Growth ---------------------------------------------------------------------------
# Small stroke icons, drawn with currentColor so they take the Growth colour.
ICONS = {
    "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.6-3.4 8.3-8 9-4.6-.7-8-4.4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "phone": '<path d="M6 3h3l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v3a3 3 0 0 1-3 3A16 16 0 0 1 3 6a3 3 0 0 1 3-3z"/>',
    "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "drop": '<path d="M12 3s6 6.4 6 11a6 6 0 0 1-12 0c0-4.6 6-11 6-11z"/>',
    "badge": '<circle cx="12" cy="9" r="6"/><path d="M8.5 13.5L7 21l5-3 5 3-1.5-7.5"/>',
    "building": '<path d="M4 21V5l8-3v19M12 21h8V9l-8-3"/><path d="M7 8h2M7 12h2M7 16h2M15 12h2M15 16h2"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
    "x": '<circle cx="12" cy="12" r="9"/><path d="M9 9l6 6M15 9l-6 6"/>',
    "monitor": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
}


def icon(name, size=24):
    return (f'<svg class="ico" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def book_btn(label="Book a free 15-minute call", extra=""):
    return f'<a class="btn magnetic book{extra}" href="{GROWTH_BOOK_URL}">{label}</a>'


def phone_demo(ph):
    """Looping phone mockup: an ad, a short form, a new inquiry, a calendar filling. CSS only."""
    days = "".join(f"<i>{d}</i>" for d in "MTWTF")
    slots = "".join(f'<b style="--i:{i}"></b>' for i in range(25))
    label = ("Illustration: a social media ad for a local company, a homeowner filling in a short form, "
             f"a notification reading {ph['notice']}, {ph['notice_sub']}, and a calendar filling with booked jobs.")
    return f"""<figure class="phone-demo">
  <div class="phone" role="img" aria-label="{esc(label)}">
    <div class="screen s-ad" aria-hidden="true">
      <div class="ad-head"><span class="ad-avatar">{esc(ph['company'][:1])}</span><span><b>{esc(ph['company'])}</b><small>Sponsored · {esc(ph['sub'])}</small></span></div>
      <p class="ad-copy">{esc(ph['ad'])}</p>
      <div class="ad-img"><svg viewBox="0 0 160 90" aria-hidden="true"><rect width="160" height="90" fill="#dfe8f7"/><circle cx="128" cy="22" r="10" fill="#f6c453"/><path d="M0 70h160v20H0z" fill="#b9d3a5"/><path d="M38 70V46l26-20 26 20v24z" fill="#fff"/><path d="M32 48l32-26 32 26" fill="none" stroke="#1f5bb8" stroke-width="5" stroke-linejoin="round"/><rect x="56" y="54" width="14" height="16" fill="#1f5bb8"/><rect x="100" y="56" width="44" height="18" rx="4" fill="#fff"/><circle cx="110" cy="76" r="5" fill="#333"/><circle cx="134" cy="76" r="5" fill="#333"/></svg></div>
      <div class="ad-foot"><small>Local service · Book online</small><span class="ad-btn">Get a quote<span class="tap"></span></span></div>
      <div class="ad-ghost"><i></i><i></i><i></i></div>
    </div>
    <div class="screen s-form" aria-hidden="true">
      <p class="f-title">Get a quote from {esc(ph['company'])}</p>
      <span class="f-l">Name</span><span class="f-in"><i style="--w:55%"></i></span>
      <span class="f-l">ZIP code</span><span class="f-in"><i style="--w:30%"></i></span>
      <span class="f-l">What's the problem?</span><span class="f-in tall"><i style="--w:80%"></i></span>
      <span class="f-send">Send</span>
    </div>
    <div class="screen s-cal" aria-hidden="true">
      <p class="f-title">This week</p>
      <div class="cal-days">{days}</div>
      <div class="cal-grid">{slots}</div>
    </div>
    <div class="toast" aria-hidden="true">{icon("phone", 18)}<span><b>{esc(ph['notice'])}</b><small>{esc(ph['notice_sub'])}</small></span></div>
  </div>
  <figcaption>Illustration</figcaption>
</figure>"""


def trust_strip():
    items = "".join(f"<li>{icon(i, 20)}<span>{esc(x)}</span></li>" for i, x in content_growth.TRUST)
    return f'<section class="g-trust" aria-label="Why it is low risk"><ul>{items}</ul></section>'


def growth_hero(page):
    return (f'<header class="g-hero"><div class="g-copy"><p class="kicker">{page["label"]}</p><h1>{page["h1"]}</h1>'
            f'<p class="lede">{page["lede"]}</p><p class="actions">{book_btn()}</p></div>{phone_demo(page["phone"])}</header>')


def icon_cards(items):
    return '<ul class="g-cards">' + "".join(f'<li class="card"><span class="g-ico">{icon(i)}</span><p>{esc(x)}</p></li>' for i, x in items) + "</ul>"


def guarantee():
    return (f'<section class="g-guarantee"><span class="g-seal">{icon("shield", 34)}<b>30</b><small>days</small></span>'
            f'<div><p class="kicker">Low risk</p><p class="g-big">{esc(content_growth.GUARANTEE)}</p></div></section>')


def closing(page):
    small = f'<p class="note">{page["smallprint"]}</p>' if page.get("smallprint") else ""
    return (f'<section class="g-close" id="g-close"><h2>{esc(page["closing"])}</h2>'
            f'<p>{book_btn()}</p>{small}</section>')


def book_bar():
    return f'<div class="book-bar" id="book-bar"><a class="btn" href="{GROWTH_BOOK_URL}">Book a free call</a></div>'


def growth_faq(page):
    return faq_html(page.get("faq"), {"questions": "Questions"})


def growth_hub_main(lang, page, slug):
    trades = "".join(f'<li><a class="card g-trade" href="{path(lang, s_)}"><span class="g-ico">{icon(i)}</span>'
                     f'<strong>{esc(n)}</strong><span class="more">See how it works →</span></a></li>' for s_, n, i in page["trades"])
    parts = [growth_hero(page), trust_strip(),
             f'<section class="split"><h2>{page["who_h"]}</h2><div><p class="lede">{esc(page["who"])}</p>'
             f'<h3>{page["trades_h"]}</h3><ul class="g-trades">{trades}</ul></div></section>']
    v = page.get("video")
    if v:
        parts.append(f'<section class="g-video"><figure class="media"><video controls preload="none" poster="{v["poster"]}" width="1280" height="720">'
                     f'<source src="{v["src"]}" type="video/mp4"></video><figcaption>{esc(v["caption"])}</figcaption></figure></section>')
    parts.append(f'<section><h2>{page["get_h"]}</h2>{icon_cards(page["get"])}</section>')
    parts.append(person_block())
    parts.append(guarantee())
    parts.append(growth_faq(page))
    if page.get("results"):
        items = "".join(f'<li class="card"><h3>{esc(r["title"])}</h3><p>{esc(r["text"])}</p></li>' for r in page["results"])
        parts.append(f'<section><h2>Results</h2><ul class="grid-3 g-results">{items}</ul></section>')
    parts.append(closing(page))
    return "".join(parts)


def calendars(c):
    # Same 20 weekday slots in both months; the right one fills as it scrolls into view.
    left = {1, 4, 8, 13, 15, 18}
    right = {0, 1, 2, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19}
    def month(filled, extra):
        days = "".join(f"<i>{d}</i>" for d in "MTWTF")
        cells = "".join((f'<b class="job" style="--i:{n}"><span>Job</span></b>' if k in filled else "<b></b>")
                        for n, k in enumerate(range(20)))
        return f'<div class="g-month{extra}"><div class="cal-days">{days}</div><div class="cal-grid">{cells}</div></div>'
    label = "Illustration: a calendar with a few jobs booked from word of mouth only, next to a calendar mostly full of jobs with Kayonne Growth."
    return (f'<section class="g-cals"><h2>{c["h"]}</h2><figure><div class="g-cal-pair" role="img" aria-label="{label}">'
            f'<div><p class="g-cal-label">{c["left"]}</p>{month(left, "")}</div>'
            f'<div><p class="g-cal-label">{c["right"]}</p>{month(right, " busy")}</div></div>'
            f'<figcaption>Illustration</figcaption></figure></section>')


def example_card(page):
    rows = "".join(f"<li><span>{esc(k)}:</span> {esc(v)}</li>" for k, v in page["example"])
    return (f'<section class="split g-example"><h2>{page["example_h"]}</h2><div><figure class="g-notice">'
            f'<div class="g-notice-head">{icon("phone", 18)}<b>New inquiry</b><small>now</small></div><ul>{rows}</ul>'
            f'<figcaption>Example</figcaption></figure></div></section>')


def calculator(page):
    return f"""<section class="g-calc card" aria-labelledby="calc-h">
  <h2 id="calc-h">{page['calc_h']}</h2>
  <div class="g-calc-fields">
    <div><label for="calc-value">Your average job value ($)</label><input id="calc-value" type="number" inputmode="decimal" min="0" step="any" autocomplete="off"></div>
    <div><label for="calc-jobs">Extra jobs per month you could handle</label><input id="calc-jobs" type="number" inputmode="numeric" min="0" step="1" autocomplete="off"></div>
  </div>
  <p class="g-calc-out" aria-live="polite"><output id="calc-out" for="calc-value calc-jobs">Enter your numbers to see the total.</output></p>
  <p>{book_btn()}</p>
</section>"""


def growth_niche_main(lang, page, slug):
    pains = "".join(f'<li class="card">{icon("x")}<p>{esc(x)}</p></li>' for x in page["pains"])
    parts = [growth_hero(page), trust_strip(),
             f'<section><h2>{page["pains_h"]}</h2><ul class="g-pains">{pains}</ul></section>',
             calendars(page["calendars"]),
             f'<section><h2>{page["changes_h"]}</h2>{icon_cards(page["changes"])}</section>',
             example_card(page), calculator(page), guarantee(), growth_faq(page)]
    t = page.get("testimonial")
    if t:
        parts.append(f'<section class="g-quote"><blockquote><p>{esc(t["quote"])}</p><footer>{esc(t["name"])}, {esc(t["company"])}</footer></blockquote></section>')
    parts.append(closing(page))
    return "".join(parts)


def raw_main(lang, page, slug):
    t = UI[lang]
    body = page["body"]
    intro = intro_html(page, slug) if page.get("h1") else ""
    tail = faq_html(page.get("faq"), t) + ("" if page.get("no_cta") else cta(lang))
    return intro + body + tail


def team_cards(lang, key, only=None):
    team = TEAMS[key]
    out = []
    for s_, en, de, den, dde in team["items"]:
        if only is not None and s_ not in only:
            continue
        name, desc = (en, den) if lang == "en" else (de, dde)
        out.append(f'<li><a class="card img-card team-{team["cls"]}" href="{path(lang, s_)}">'
                   f'<img src="/img/scenes/{SCENES.get(s_, "default")}.webp" alt="" width="900" height="675" loading="lazy" decoding="async">'
                   f'<strong>{esc(name)}</strong><span class="note">{esc(desc)}</span></a></li>')
    return '<ul class="grid-3 link-cards img-cards">' + "".join(out) + "</ul>"


def service_card(lang, team, item, kicker=True):
    s_, en, de, den, dde = item
    name, desc = (en, den) if lang == "en" else (de, dde)
    k = f'<span class="kicker">{team[lang]}</span>' if kicker else ""
    return (f'<li><a class="card team-{team["cls"]}" href="{path(lang, s_)}">{k}'
            f'<strong>{esc(name)}</strong><span class="note">{esc(desc)}</span></a></li>')


def service_grid(lang):
    """Home page: one short row of service links per division."""
    out = []
    for d in divisions(lang):
        links = "".join(f'<li><a href="{path(lang, s_)}">{esc(en if lang == "en" else de)}</a></li>'
                        for s_, en, de, *_ in d["items"] if s_ not in NOT_SERVICES and s_ != d["slug"])
        out.append(f'<div class="svc-row team-{d["cls"]}"><h3><a href="{path(lang, d["slug"])}">{d["brand"][lang]}</a></h3>'
                   f'<ul>{links}</ul></div>')
    return "".join(out)


def services_by_division(lang):
    """The services page: one section per division."""
    out = []
    for d in divisions(lang):
        cards = "".join(service_card(lang, d, it, False) for it in d["items"] if it[0] not in NOT_SERVICES)
        out.append(f'<section class="team-{d["cls"]}"><div class="sec-head"><h2>{d["brand"][lang]}</h2>'
                   f'<a class="text-link" href="{path(lang, d["slug"])}">{esc(d["tagline"][lang])} →</a></div>'
                   f'<ul class="grid-3 link-cards accent-cards">{cards}</ul></section>')
    return "".join(out)


def division_cards(lang):
    """Home page cards for divisions that have one."""
    out = []
    for d in divisions(lang):
        c = d["card"] and d["card"].get(lang)
        if not c:
            continue
        out.append(f'<a class="team team-{d["cls"]}" href="{path(lang, d["slug"])}"><p class="kicker">{d["brand"][lang]}</p>'
                   f'<h2>{c["title"]}</h2><p>{c["text"]}</p>' + (f'<ul class="ticks">{lis(c["ticks"])}</ul>' if c["ticks"] else "") +
                   f'<span class="team-more">{c["button"]} →</span></a>')
    label = "Our teams" if lang == "en" else "Unsere Teams"
    return f'<section class="teams" data-scene="windows" aria-label="{label}">' + "".join(out) + "</section>"


def team_picker(lang):
    """The required team field on the quote form."""
    label, unsure = ("Which team do you need?", "Not sure") if lang == "en" else ("Welches Team brauchen Sie?", "Weiß ich noch nicht")
    opts = "".join(f'<option value="{d["key"]}">{d["brand"][lang]}</option>' for d in divisions(lang))
    choose = "Choose a team" if lang == "en" else "Team wählen"
    return (f'<div class="full"><label for="f-team">{label} *</label><select id="f-team" name="team" required>'
            f'<option value="">{choose}</option>{opts}<option value="unsure">{unsure}</option></select></div>')


def pricing(lang):
    """The pricing page: one table per division, in menu order."""
    mod = LANGS[lang]
    h = mod.PRICE_HEAD
    out = []
    for d in divisions(lang):
        rows = mod.PRICES.get(d["key"])
        if not rows:
            continue
        body = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows)
        out.append(f'<div class="price-group team-{d["cls"]}"><h2><a href="{path(lang, d["slug"])}">{d["brand"][lang]}</a></h2>'
                   f'<div class="table-wrap"><table><thead><tr><th scope="col">{h[0]}</th><th scope="col">{h[1]}</th>'
                   f'<th scope="col">{h[2]}</th></tr></thead><tbody>{body}</tbody></table></div></div>')
    return "".join(out)


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
    kind = page.get("kind")
    main = {"service": service_main, "division": division_main, "growth_hub": growth_hub_main,
            "growth_niche": growth_niche_main}.get(kind, raw_main)(lang, page, slug)
    main = main.replace("{{WEIGHTS}}", weights).replace("{{PAIRS}}", pair_cards(lang) if "{{PAIRS}}" in main else "")
    main = main.replace("{{SERVICES}}", service_grid(lang) if "{{SERVICES}}" in main else "")
    main = main.replace("{{SERVICES_BY_DIVISION}}", services_by_division(lang) if "{{SERVICES_BY_DIVISION}}" in main else "")
    main = main.replace("{{DIVISIONS}}", division_cards(lang) if "{{DIVISIONS}}" in main else "")
    main = main.replace("{{BOOK}}", GROWTH_BOOK_URL)
    main = main.replace("{{PERSON}}", person_block() if "{{PERSON}}" in main else "")
    main = main.replace("{{PHONE_LINE}}", phone_line(lang) if "{{PHONE_LINE}}" in main else "")
    main = main.replace("{{PRICING}}", pricing(lang) if "{{PRICING}}" in main else "")
    main = main.replace("{{CHOOSER}}", chooser(lang) if "{{CHOOSER}}" in main else "")
    main = main.replace("{{TEAMPICKER}}", team_picker(lang) if "{{TEAMPICKER}}" in main else "")
    main = main.replace("{{INSIGHTS3}}", insight_cards(lang, 3) if "{{INSIGHTS3}}" in main else "")
    main = main.replace("{{INSIGHTS}}", insight_cards(lang) if "{{INSIGHTS}}" in main else "")
    main = re.sub(r"\{\{TEAM:(\w+)\}\}", lambda m: team_cards(lang, m.group(1)), main)
    trail = crumbs(lang, slug, page)
    if trail:
        main = crumbs_html(trail) + main
        page = dict(page, schema=list(page.get("schema", [])) + [crumbs_schema(trail, lang, slug)])
    cls = "page" + (" home" if slug == "" else "")
    link_slug = "" if slug == "404" else slug
    body_attr = " data-no3d" if lean(page) else ""
    if kind and kind.startswith("growth"):
        cls += " growth"
    return (head(lang, slug, page) + f"\n<body{body_attr}>\n" + header(lang, link_slug, page) +
            f'\n<main id="content" class="shell {cls}">{main}</main>\n' + footer(lang, page, slug) +
            (book_bar() if kind and kind.startswith("growth") else "") + "\n" + SCRIPT +
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
    en_slugs = set(content_en.PAGES) - EN_ONLY
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
        alts = "" if slug in EN_ONLY else "".join(
            f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE + path(l, slug)}"/>' for l in ("en", "de"))
        urls.append(f"  <url><loc>{SITE + path(lang, slug)}</loc>{alts}</url>")
    with open("sitemap.xml", "w", encoding="utf-8") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                 'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
    print(f"Built {len(written)} pages, 404.html and sitemap.xml")


if __name__ == "__main__":
    main()
