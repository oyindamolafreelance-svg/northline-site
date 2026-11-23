"""The divisions of Kayonne Creatives, in menu order.

Everything that lists the divisions is generated from DIVISIONS: the mega menu, the mobile drawer,
the footer columns, the home page division cards, the "How we help you grow" grid and the team picker
on the quote form. To add a division, add one entry here, give it a landing page in content_en.py
(and content_de.py if "langs" includes "de") with kind="division", and add its service pages.

Fields
  key       short id, also used in ?team=<key> on the quote form
  slug      URL of the landing page
  cls       CSS class suffix (team-<cls>); color is the team color
  langs     languages the division's pages exist in
  name      menu label            brand    "Kayonne ..." name
  tagline   one-line tagline      line     one-line description (menu preview, footer)
  icon      icon name for the chooser card (see ICONS in build.py)
  need      the home page "What do you need?" card, e.g. "I need a website or app"
  card      home page card: title, text, ticks, button (None = no card)
  footer    footer "Let's talk" text and "How we work" points on this division's pages
  items     menu items: (slug, English name, German name, English description, German description)
  lean      optional: pages without the language switcher, greeting band, qualifications or 3D backdrop
  cta       optional: header button (label, link) in place of "Get a quote"
"""

# Every "Book a free 15-minute call" button on the Growth pages. Swap in a booking calendar here.
GROWTH_BOOK_URL = "/contact/?team=growth"

DIVISIONS = [
    dict(
        key="digital", slug="digital", cls="d", color="#a8582a", langs=("en", "de"),
        icon="monitor", need={"en": "I need a website or app", "de": "Ich brauche eine Website oder App"},
        footer={
            "en": ("Need a website, shop or app? Send the brief and we reply by email with a quote or questions.",
                   ["A written quote before work starts", "A layout to review before the build",
                    "Sites tested against Core Web Vitals and WCAG 2.2 AA", "The site and domain in your name"]),
            "de": ("Sie brauchen eine Website, einen Shop oder eine App? Schicken Sie uns das Briefing, wir antworten per E-Mail mit Angebot oder Rückfragen.",
                   ["Ein schriftliches Angebot vor Arbeitsbeginn", "Ein Layout zur Prüfung vor der Entwicklung",
                    "Websites geprüft nach Core Web Vitals und WCAG 2.2 AA", "Website und Domain auf Ihren Namen"]),
        },
        name={"en": "Digital", "de": "Digital"},
        brand={"en": "Kayonne Digital", "de": "Kayonne Digital"},
        tagline={"en": "The build team.", "de": "Das Entwicklungsteam."},
        line={"en": "The build team: sites, shops, apps and the plumbing behind them.",
              "de": "Das Entwicklungsteam: Websites, Shops, Apps und die Technik dahinter."},
        card={
            "en": dict(title="The build team",
                       text="Websites, online shops and apps, the domain and email behind them, and the SEO that gets them found.",
                       ticks=["Websites and shops", "Web and mobile apps", "Domains and business email", "SEO, speed and care"],
                       button="Meet the build team"),
            "de": dict(title="Das Entwicklungsteam",
                       text="Websites, Onlineshops und Apps, Domain und E-Mail dahinter und die SEO, die für Auffindbarkeit sorgt.",
                       ticks=["Websites und Shops", "Web- und Mobile-Apps", "Domains und geschäftliche E-Mail", "SEO, Ladezeit und Wartung"],
                       button="Zum Entwicklungsteam"),
        },
        items=[
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
    ),
    dict(
        key="localize", slug="localize", cls="l", color="#127569", langs=("en", "de"),
        icon="globe", need={"en": "I need translation, or to launch abroad", "de": "Ich brauche eine Übersetzung oder will ins Ausland"},
        footer={
            "en": ("Need a translation or a launch abroad? Send the file or the brief and we reply by email with a quote or questions.",
                   ["Every translation checked by a second linguist", "A written quote before work starts",
                    "Processes aligned with ISO 17100 on request", "Your files seen only by the people on your job"]),
            "de": ("Sie brauchen eine Übersetzung oder wollen ins Ausland? Schicken Sie Datei oder Briefing, wir antworten per E-Mail mit Angebot oder Rückfragen.",
                   ["Jede Übersetzung von einer zweiten Fachkraft geprüft", "Ein schriftliches Angebot vor Arbeitsbeginn",
                    "Abläufe nach ISO 17100 auf Wunsch", "Ihre Dateien sehen nur die Personen im Auftrag"]),
        },
        name={"en": "Localize", "de": "Localize"},
        brand={"en": "Kayonne Localize", "de": "Kayonne Localize"},
        tagline={"en": "The translation and localisation team.", "de": "Das Übersetzungs- und Lokalisierungsteam."},
        line={"en": "The translation and localisation team: qualified linguists, and launches in new markets.",
              "de": "Das Übersetzungs- und Lokalisierungsteam: qualifizierte Fachleute und Marktstarts im Ausland."},
        card={
            "en": dict(title="The translation and localisation team",
                       text="Qualified translators for documents, legal, medical and patent work, subtitles and proofreading, with a second check on every job. Then your website or shop, launched in new markets.",
                       ticks=["Documents laid out like the original", "Legal, medical, patents", "Subtitling and proofreading", "Website and shop localisation"],
                       button="Meet the Localize team"),
            "de": dict(title="Das Übersetzungs- und Lokalisierungsteam",
                       text="Qualifizierte Übersetzer für Dokumente, Recht, Medizin und Patente, Untertitel und Korrektorat, mit zweiter Prüfung bei jedem Auftrag. Dazu Ihre Website oder Ihr Shop, gestartet in neuen Märkten.",
                       ticks=["Dokumente im Layout des Originals", "Recht, Medizin, Patente", "Untertitelung und Korrektorat", "Website- und Shop-Lokalisierung"],
                       button="Zum Team Localize"),
        },
        # Translation services first, international launch services second.
        items=[
            ("documents", "Document translation", "Dokumentübersetzung", "Certificates, statements, manuals", "Urkunden, Zeugnisse, Handbücher"),
            ("legal", "Legal translation", "Juristische Übersetzung", "Contracts and court papers", "Verträge und Gerichtsunterlagen"),
            ("medical", "Medical translation", "Medizinische Übersetzung", "Life sciences, under NDA", "Life Sciences, mit NDA"),
            ("patents", "Patent translation", "Patentübersetzung", "Claims kept consistent", "Einheitliche Ansprüche"),
            ("subtitling", "Subtitling and transcription", "Untertitelung und Transkription", "SRT, VTT, SDH, burned-in", "SRT, VTT, SDH, eingebrannt"),
            ("proofreading", "Proofreading and revision", "Korrektorat und Revision", "Check a translation you have", "Vorhandene Übersetzung prüfen"),
            ("quality", "MTPE and quality checks", "MTPE und Qualitätsprüfung", "Post-editing and LQA", "Post-Editing und LQA"),
            ("languages", "All languages", "Alle Sprachen", "Into and out of English", "Aus dem und ins Englische"),
            ("international-launch", "International launch", "Internationaler Marktstart", "One team, one launch plan", "Ein Team, ein Startplan"),
            ("localization", "Website and app localisation", "Website- und App-Lokalisierung", "Your product, in their language", "Ihr Produkt in ihrer Sprache"),
            ("multilingual-seo", "Multilingual SEO", "Mehrsprachige SEO", "Found in every market", "In jedem Markt gefunden"),
            ("ecommerce-localisation", "Shop localisation", "Shop-Lokalisierung", "Shopify and WooCommerce", "Shopify und WooCommerce"),
            ("games", "Game localisation", "Spielelokalisierung", "Strings, stores, subtitles", "Strings, Stores, Untertitel"),
            ("readiness-check", "Free readiness check", "Kostenloser Readiness-Check", "Is your site ready to translate?", "Ist Ihre Website übersetzungsbereit?"),
            ("demo", "Live localisation demo", "Live-Lokalisierungsdemo", "Watch a page change language", "Eine Seite wechselt die Sprache"),
        ],
    ),
    dict(
        key="growth", slug="growth", cls="g", color="#1f5bb8", langs=("en",), lean=True,
        icon="chart", need={"en": "I need more customers"},
        footer={"en": ("Want more customers? Book a free 15-minute call.", ["30-day guarantee", "Your leads are never shared"])},
        cta={"en": ("Book a call", GROWTH_BOOK_URL)},
        name={"en": "Growth"},
        brand={"en": "Kayonne Growth"},
        tagline={"en": "More customers for local service businesses."},
        line={"en": "We bring local service businesses a steady flow of new customers."},
        card={
            "en": dict(title="More customers. Less guessing.",
                       text="We bring local service businesses a steady flow of new customers.",
                       ticks=["New inquiries from homeowners in your area", "Only serious inquiries", "30-day guarantee",
                              "Built for one trade at a time"],
                       button="See how it works"),
        },
        items=[
            ("growth", "How it works", "", "More customers. Less guessing.", ""),
            # Shown as "Local service businesses" in menus and lists; the page itself is for septic companies.
            ("growth/septic", "Local service businesses", "", "One trade at a time", ""),
        ],
    ),
]

# Menu items that are free offers or pages about a place or a list, not paid services.
# They stay in the menus but are left out of service grids and "Related services".
NOT_SERVICES = {"website-check", "readiness-check", "demo", "languages", "web-design-glasgow"}
