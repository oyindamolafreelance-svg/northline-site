"""English page content. Strings may contain HTML. Keys are URL slugs ("" is the home page)."""

EMAIL = "hello@kayonnecreatives.com"

EUROPE = ["German", "German (Switzerland)", "Dutch", "French", "Spanish", "Italian", "Portuguese", "Polish",
          "Swedish", "Danish", "Norwegian", "Finnish", "Czech", "Slovak", "Hungarian", "Romanian", "Greek",
          "Bulgarian", "Croatian", "Serbian", "Slovenian", "Ukrainian", "Estonian", "Latvian", "Lithuanian",
          "Catalan", "Turkish"]
ASIA = ["Japanese", "Chinese (Simplified)", "Chinese (Traditional)", "Cantonese", "Korean", "Hindi", "Bengali",
        "Tamil", "Telugu", "Urdu", "Punjabi", "Thai", "Vietnamese", "Indonesian", "Malay", "Tagalog", "Burmese",
        "Khmer", "Lao", "Nepali"]


def wall(items):
    return '<ul class="lang-wall">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


LANG_WALLS = (f"<h3>Europe</h3>{wall(EUROPE)}<h3>Asia</h3>{wall(ASIA)}"
              '<p class="note">Arabic and Persian are available on request. All languages are offered into and out of '
              "English. Live interpreting is not offered.</p>")

DIGITAL_CARDS = [
    ("websites", "Websites", "Business sites, shops and landing pages."),
    ("web-apps", "Web apps", "Custom tools and progressive web apps."),
    ("mobile-apps", "Mobile apps", "iOS and Android, through to the store listing."),
    ("domains-email", "Domains and business email", "Your domain, inbox and DNS set up properly."),
    ("seo", "SEO", "Technical, local and multilingual search."),
    ("speed", "Speed and accessibility", "Core Web Vitals and WCAG 2.2 AA, with a report."),
    ("care", "Care plans", "Updates, backups and someone watching."),
]
LANGUAGE_CARDS = [
    ("certified-translation", "Certified translation (UK)", "For the Home Office, courts and universities."),
    ("documents", "Document translation", "Certificates, statements and manuals, laid out to match."),
    ("localization", "Website and app localisation", "Your product, in your buyer's language."),
    ("games", "Game localisation", "Strings, store pages and subtitles, checked in context."),
    ("medical", "Medical translation", "Life sciences texts, with an NDA."),
    ("patents", "Patent translation", "Claims kept consistent across a family."),
    ("legal", "Legal translation", "Contracts and papers your counsel can review."),
    ("subtitling", "Subtitling and transcription", "Timed, readable and delivered in your format."),
    ("proofreading", "Proofreading and revision", "A second linguist checks a translation you already have."),
    ("quality", "MTPE and quality checks", "Post-editing, LQA and terminology care."),
]


def cards(items, prefix="/"):
    return '<ul class="grid-3 link-cards">' + "".join(
        f'<li><a class="card" href="{prefix}{s}/"><strong>{n}</strong><span class="note">{d}</span></a></li>'
        for s, n, d in items) + "</ul>"


def video(name, caption, w, h, label):
    return (f'<figure class="media"><video data-autoplay muted loop playsinline controls preload="none" '
            f'poster="/media/{name}.webp" width="{w}" height="{h}" aria-label="{label}">'
            f'<source src="/media/{name}.mp4" type="video/mp4"><source src="/media/{name}.webm" type="video/webm"></video><figcaption>{caption}</figcaption></figure>')


def shot(src, alt, w, h):
    return f'<figure class="media"><img src="{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async"></figure>'


LOC_VIDEO_EN = video("localisation", "One product card in English, German, Japanese and Arabic. The words, the date, the currency and the reading direction all change.", 1100, 482, "Localisation demo video")
REEL_EN = video("showreel", "The 3D scenes from this website, one for each service.", 1280, 720, "Showreel of the 3D scenes on this website")


def svc(**kw):
    kw["kind"] = "service"
    return kw


PAGES = {}

PAGES[""] = dict(
    title="Kayonne Creatives | Websites and translation, Glasgow",
    desc="Glasgow agency for websites, apps and translation. We build your site, then professional linguists "
         "take it into European and Asian languages. Hire one service or both.",
    body=f"""
<section class="hero" data-scene="hero">
  <div>
    <p class="kicker">Glasgow · worldwide</p>
    <h1>We build it. Then we take it to every market.</h1>
    <p class="lede">Kayonne Creatives is a digital and language agency in Glasgow. We build websites and apps, and professional linguists translate them into European and Asian languages. You can hire the build, the translation, or both.</p>
    <p class="actions"><a class="btn magnetic" href="/digital/">Build a site</a> <a class="btn magnetic" href="/language/">Translate a document</a> <a class="btn ghost magnetic" href="/global/">Launch abroad</a></p>
  </div>
  <div class="orbit" aria-hidden="true"><div class="ring"><span>ä</span><span>あ</span><span>中</span><span>é</span><span>ø</span></div></div>
</section>
<section data-scene="shards"><ul class="grid-4 creds">
  <li class="card note">MA in Translation Studies, Middlebury Institute at Monterey</li>
  <li class="card note">CIOL Diploma in Translation, Merit</li>
  <li class="card note">Professional linguists across Europe and Asia</li>
  <li class="card note">Processes aligned with ISO 17100 when a client requires it</li>
</ul></section>
<section class="teams" data-scene="windows" aria-label="Our two teams">
  <a class="team team-d" href="/digital/">
    <p class="kicker">Kayonne Digital</p>
    <h2>The build team</h2>
    <p>Websites, online shops and apps, the domain and email behind them, and the SEO that gets them found.</p>
    <ul class="ticks"><li>Websites and shops</li><li>Web and mobile apps</li><li>Domains and business email</li><li>SEO, speed and care</li></ul>
    <span class="team-more">Meet the build team →</span>
  </a>
  <a class="team team-l" href="/language/">
    <p class="kicker">Kayonne Language</p>
    <h2>The translation team</h2>
    <p>Qualified translators for certified, legal, medical and patent work, subtitles and proofreading, with a second check on every job.</p>
    <ul class="ticks"><li>Certified for the Home Office</li><li>Legal, medical, patents</li><li>Subtitling and transcription</li><li>Proofreading and revision</li></ul>
    <span class="team-more">Meet the translation team →</span>
  </a>
</section>
<section class="global-band card" data-scene="globe">
  <div>
    <p class="kicker">Kayonne Global</p>
    <h2>Both teams. One launch.</h2>
    <p>Most firms build the site or translate it. We do both on the same project, so your site is ready for the next market without a hand-off in the middle.</p>
    <ol class="mini-steps"><li>Audit</li><li>Research</li><li>Build</li><li>Translate</li><li>Check</li><li>Launch</li></ol>
    <p class="actions"><a class="btn magnetic" href="/global/">See how it works</a> <a class="btn ghost" href="/readiness-check/">Free readiness check</a></p>
  </div>
  {LOC_VIDEO_EN}
</section>
<section data-scene="network">
  <h2>Europe and Asia, with one team.</h2>
  <p class="lede">Professional linguists cover the languages below. You deal with one project lead in Glasgow.</p>
  {LANG_WALLS}
  <p><a class="btn ghost" href="/languages/">See all languages</a></p>
</section>
<section data-scene="path">
  <h2>How a project runs</h2>
  <ol class="grid-4 steps">
    <li class="card"><h3>Brief</h3><p class="note">We write down the job, the languages and the date.</p></li>
    <li class="card"><h3>Make</h3><p class="note">Design, build or translate, with you able to review.</p></li>
    <li class="card"><h3>Check</h3><p class="note">A speed report for a site, or a second linguist for a translation.</p></li>
    <li class="card"><h3>Hand over</h3><p class="note">You own the files. Ongoing care is optional.</p></li>
  </ol>
</section>""",
    faq=[
        ("Can one agency build and translate?", "Yes. You can also hire only the build, or only the translation."),
        ("Which languages do you cover?", "European and Asian languages, into and out of English. See the <a href=\"/languages/\">languages page</a>. The quote names who will work on your language pair."),
        ("Do you provide certified translations?", "Yes, for use in the UK. See <a href=\"/certified-translation/\">certified translation</a>."),
        ("Where are you based?", "Glasgow, United Kingdom. Clients can be anywhere."),
        ("Do you interpret live calls or events?", "No. We do written translation, subtitling and transcription only."),
    ],
)

PAGES["services"] = dict(
    title="Services | Kayonne Creatives",
    desc="Websites, apps, domains and email, SEO, certified translation, localisation and subtitling from one Glasgow agency.",
    label="Services", h1="Two sides. One agency.",
    lede="Kayonne Creatives builds the product, then prepares it in the European and Asian languages your buyers use. Professional linguists do the language work. You can hire one side or both.",
    body=f"<section><h2>Digital</h2>{cards(DIGITAL_CARDS)}</section><section><h2>Language</h2>{cards(LANGUAGE_CARDS)}</section>",
)

PAGES["websites"] = svc(
    title="Website design and development, Glasgow | Kayonne Creatives",
    desc="Business websites, online shops, landing pages and redesigns. Clear pages, fast loading and a speed report before launch.",
    label="Websites", h1="Websites that explain the offer and hold up.",
    lede="We design and build business sites, online shops and landing pages. A site is finished when it is clear, fast and ready to hand over, not when it only looks finished.",
    why=["A structure built around what you sell", "A design your team can update", "Speed and accessibility checked before launch"],
    incl=["Business and marketing websites", "Online shops (Shopify or WooCommerce)", "Landing pages", "Redesigns and moves from Wix or Squarespace",
          "CMS setup and training", "Domain, hosting and business email setup", "Page copy in English, and in other languages"],
    extra="""<section><h2>Packages</h2><ul class="grid-4 link-cards plain-cards">
<li class="card"><strong>One-page site</strong><span class="note">One page with your offer, contact form and map. For a launch or a sole trader.</span></li>
<li class="card"><strong>Business site</strong><span class="note">Five to eight pages, a blog if you want one, and local SEO setup.</span></li>
<li class="card"><strong>Online shop</strong><span class="note">Products, payments, delivery rules and order emails.</span></li>
<li class="card"><strong>Multilingual site</strong><span class="note">Any of the above in two or more languages, with hreflang and translated search terms.</span></li>
</ul><p class="note">Every package is quoted after a short brief, so you only pay for the pages you need.</p></section>""",
    steps=[("Brief", "We agree the audience, the offer and the pages that must exist."),
           ("Design", "You review the layout before the build starts."),
           ("Build", "We develop the site, the forms and the content model."),
           ("Check", "Every launch is tested against the Core Web Vitals thresholds. You receive the report.")],
    who="Companies and sole traders who need a site that sells a service, a product or a launch.",
    faq=[("Can we edit the site ourselves?", "Yes. CMS training is part of the handover. You own the site."),
         ("Do you redesign old sites?", "Yes. We keep the pages that already rank, set up redirects, and replace what does not help the buyer."),
         ("Who owns the domain?", "You do. We register it in your name or connect the one you have. See <a href=\"/domains-email/\">domains and business email</a>."),
         ("How long does a site take?", "It depends on the number of pages and how ready the content is. The quote gives a date.")],
)

PAGES["web-apps"] = svc(
    title="Custom web apps | Kayonne Creatives",
    desc="Web applications, progressive web apps and integrations. Built for the job, then handed over with the code.",
    label="Web apps", h1="Web apps built for the job, not a template.",
    lede="We build custom web applications and progressive web apps, and we connect them to the tools you already use.",
    why=["A product your team can run", "Integrations agreed before the build", "The code belongs to you"],
    incl=["Custom web applications", "Progressive web apps", "API and third-party integrations", "Design of the main screens", "Interfaces ready for translation"],
    steps=[("Scope", "We write down what the first version must do, and what it will not do."),
           ("Screens", "You approve the main flows before engineering starts."),
           ("Build", "We ship in stages you can click through."),
           ("Handover", "Repository, access and a short guide. Care is optional.")],
    who="Software companies, agencies and operators who have outgrown a spreadsheet or a plugin.",
    faq=[("Who owns the code?", "You do, once the agreed fees are paid."),
         ("Can a web app be installed on a phone?", "A progressive web app can. A store app is a separate service, see <a href=\"/mobile-apps/\">mobile apps</a>.")],
)

PAGES["mobile-apps"] = svc(
    title="Mobile app development, iOS and Android | Kayonne Creatives",
    desc="iOS and Android apps, from the first screens to the store listing. Localisation of the app and listing is available from the same team.",
    label="Mobile apps", h1="Mobile apps for iOS and Android.",
    lede="We design and build mobile apps, then we can translate the interface and the store listing. One team, from the first screen to the language your market reads.",
    why=["Screens designed for thumbs, not for a desktop slide", "Store listing text can be translated with the app", "You see a test build before it is submitted"],
    incl=["iOS apps", "Android apps", "Interface design", "Store listing copy", "App and store listing translation"],
    steps=[("Scope", "We name the first release and the screens it needs."),
           ("Design", "You review the flows on a phone-sized layout."),
           ("Build", "You install a test build."),
           ("Release", "We prepare the submission. Store review times are set by Apple and Google.")],
    who="Product teams and studios that need a phone app, not a stretched website.",
    faq=[("Do you publish under our account?", "Yes. The store accounts stay in your name."),
         ("Can you translate the app?", "Yes. Strings, screenshots and store text, see <a href=\"/localization/\">localisation</a>.")],
)

PAGES["domains-email"] = svc(
    title="Domain registration and business email setup | Kayonne Creatives",
    desc="Domain registration in your name, Google Workspace or Microsoft 365 email, SPF, DKIM and DMARC, and mailbox moves. Set up once and set up properly.",
    label="Domains and business email", h1="Your domain and your inbox, set up properly.",
    lede="We register your domain in your name, set up business email such as you@yourcompany.com, and configure the DNS records that keep your mail out of spam folders.",
    why=["The domain is registered to you, not to us", "Mail from your domain is authenticated, so it lands in the inbox", "Website, email and DNS work together from day one"],
    incl=["Domain registration and renewal reminders (.com, .co.uk, .de and more)", "Business email on Google Workspace or Microsoft 365",
          "SPF, DKIM and DMARC records", "Moving existing mailboxes and contacts", "Shared addresses such as info@ and quotes@",
          "Connecting the domain to your website, with HTTPS", "Email signatures"],
    steps=[("Check", "We look at what you have: domain, registrar, current email and website."),
           ("Register", "We register or transfer the domain in your name."),
           ("Set up", "Mailboxes, DNS records and the website connection."),
           ("Test", "We send test mail to Gmail and Outlook and confirm it is authenticated.")],
    who="New businesses, sole traders, and firms still using a personal Gmail or Hotmail address for work.",
    faq=[("Who pays for Google Workspace or Microsoft 365?", "You pay the provider directly, on your own account. We set it up and hand over the admin login."),
         ("Why does my email go to spam?", "Usually because SPF, DKIM or DMARC is missing or wrong. Since 2024 Gmail and Yahoo have required these records from bulk senders, and they help every sender."),
         ("Can you move us from another email provider?", "Yes. We move mailboxes and contacts and plan the switch so no mail is lost."),
         ("Do you hold our domain?", "No. The domain is registered to you. We only ask for access while we work.")],
)

PAGES["seo"] = svc(
    title="SEO services, Glasgow | Kayonne Creatives",
    desc="Technical, on-page, local and multilingual SEO. Search work happens during the build, not after the site is live.",
    label="SEO", h1="Search that matches the page you ship.",
    lede="We set up technical SEO, on-page SEO, local SEO and multilingual SEO. Content is written for what people search, not added at the end.",
    why=["A site search engines can read", "Language versions with hreflang and locale URLs", "Advice you can check yourself in Search Console"],
    incl=["Technical SEO", "On-page SEO", "Local SEO, including your Google Business Profile", "Multilingual SEO with hreflang and locale URLs",
          "Keyword research in each target language", "Content writing for SEO", "Conversion work on key pages"],
    steps=[("Audit", "We read the current site, the search terms and the list of markets."),
           ("Plan", "You approve the pages and the language structure."),
           ("Implement", "Titles, links, speed issues and locale tags are fixed in the build."),
           ("Review", "We show what changed. Rankings are never guaranteed.")],
    who="Businesses that need to be found in more than one city or more than one language.",
    faq=[("Do you guarantee a ranking?", "No. We fix what we control and we report on it. Nobody can sell you a position."),
         ("Is multilingual SEO just translation?", "No. Each language needs its own search terms, titles and URLs."),
         ("Do you set up Google Business Profile?", "Yes, along with Bing Places and Apple Business Connect if you want them.")],
)

PAGES["speed"] = svc(
    title="Website speed and accessibility audits | Kayonne Creatives",
    desc="Core Web Vitals and WCAG 2.2 AA audits with a written report. We test against the published thresholds and share the results.",
    label="Speed and accessibility", h1="Speed and access, with the report attached.",
    lede="We test every launch against the Core Web Vitals thresholds and against WCAG 2.2 AA. You get the report. We do not invent a score out of 100.",
    why=["A shared report, not a slogan", "Fixes for page weight, images and layout shift", "Accessibility issues named and repaired"],
    incl=["Core Web Vitals testing", "Speed fixes", "Accessibility audits and fixes", "Image and code weight review"],
    steps=[("Measure", "We test on mobile and desktop and keep the traces."),
           ("Fix", "We change whatever misses the threshold."),
           ("Retest", "You see the before and after."),
           ("Hand over", "The report stays with you.")],
    who="Teams whose site looks fine but feels slow, or who must meet an accessibility standard.",
    faq=[("What score do you promise?", "None out of 100. We test against the published Core Web Vitals thresholds and share the report."),
         ("Which accessibility standard?", "WCAG 2.2 AA for the pages in scope."),
         ("Can we see an example?", "Yes. <a href=\"/studio/\">This website</a> is our own example.")],
)

PAGES["care"] = svc(
    title="Website care and maintenance plans | Kayonne Creatives",
    desc="Website maintenance, security updates, backups, uptime checks and analytics. A monthly care plan keeps a site working after launch.",
    label="Care plans", h1="Care plans so the site keeps working.",
    lede="A site needs updates, backups and someone watching that it is up. Care is a monthly plan. Hosting, domain and analytics setup can also be booked on their own.",
    why=["Updates on a schedule", "A named contact when something breaks", "You still own the domain and the code"],
    incl=["Website maintenance", "Security updates", "Backups", "Uptime checks", "Hosting and domain management", "Analytics setup",
          "Small content edits", "Translation of new pages, if your site is multilingual"],
    steps=[("Access", "We list what we need. Accounts stay in your name."),
           ("Baseline", "We record the current speed, forms and backups."),
           ("Routine", "Updates follow the plan you chose."),
           ("Report", "You get a short note of what changed each month.")],
    who="Owners who do not want to be the one who notices the contact form has stopped working.",
    faq=[("Do you hold the domain?", "No. The domain and the code stay in your name."),
         ("Can we cancel?", "Yes. The notice period is written in your plan, and you keep everything when you leave."),
         ("Do you look after sites you did not build?", "Yes, after a short check of how the site is built and hosted.")],
)

PAGES["certified-translation"] = svc(
    title="Certified translation UK, Home Office and UKVI | Kayonne Creatives",
    desc="Certified translations for the Home Office, UKVI, courts, universities and banks. Birth and marriage certificates, transcripts, licences and statements.",
    label="Certified translation (UK)", h1="Certified translations for use in the UK.",
    lede="The UK has no sworn translators. A certified translation comes with a signed statement that it is a true and accurate translation of the original, with the date and the translator's name and contact details. We provide that statement with every certified translation.",
    why=["Includes the confirmation, date, name and contact details the Home Office asks for",
         "Translated by a qualified linguist, then checked by a second person",
         "Layout follows the original, so stamps and seals are easy to match"],
    incl=["Birth, marriage, divorce and death certificates", "Passports and identity documents", "Driving licences",
          "Degree certificates and academic transcripts", "Bank statements and payslips", "Police certificates",
          "Medical records and letters", "Court and solicitor papers"],
    extra="""<section><h2>Where certified translations are used</h2><ul class="ticks cols">
<li>Home Office and UK Visas and Immigration (UKVI)</li><li>HM Courts and Tribunals, and solicitors</li>
<li>Universities and UCAS</li><li>NHS and employers</li><li>DVLA</li><li>Banks and the Land Registry</li></ul>
<p class="note">Some bodies ask for more, such as a notarised translation or an apostille for use abroad. Tell us who will receive the document and we will tell you what they need. If a country requires a sworn translator, we arrange one through a vetted partner and say so in the quote. See <a href="/documents/">document translation</a>.</p></section>""",
    steps=[("Send", "Upload a clear photo or scan on the <a href=\"/contact/\">quote form</a>."),
           ("Quote", "You get a fixed price and a delivery date."),
           ("Translate", "Translation, then a check against the original by a second person."),
           ("Deliver", "A signed PDF by email, ready to upload or print.")],
    who="People applying for visas, settlement, citizenship, university places or jobs, and the solicitors who help them.",
    faq=[("Will the Home Office accept it?", "The Home Office asks for a confirmation from the translator that the translation is accurate, the date, and the translator's full name and contact details. Our certified translations include all of these."),
         ("Is a certified translation the same as a sworn translation?", "No. Sworn translations exist in countries such as Germany, France and Spain. For a UK authority, a certified translation is the usual requirement. For a foreign authority, check what it asks for."),
         ("How is it priced?", "Per document or per page, depending on how much text it has. Send the file and you get a fixed price before we start.")],
)

PAGES["documents"] = svc(
    title="Document translation services UK | Kayonne Creatives",
    desc="Document translation with the layout kept: certificates, statements, manuals and reports. Certified for UK use, or sworn through a partner abroad.",
    label="Document translation", h1="Documents translated, and formatted to match.",
    lede="We translate documents and format the result so it still looks like the original. For UK use we certify the translation ourselves. Where another country requires a sworn translator, we arrange one through a vetted partner.",
    why=["Clear handling of stamps, tables and scans", "Certified wording only where it is accurate", "Desktop publishing when the layout matters, including Asian scripts"],
    incl=["Document translation", "<a href=\"/certified-translation/\">Certified translation for UK use</a>", "Birth and marriage certificates",
          "Driving licences", "Academic transcripts", "Business statements and reports", "Technical manuals",
          "Multilingual desktop publishing", "Translation, editing and proofreading"],
    steps=[("File", "Upload a clear scan or the original file on the quote form. For very sensitive files, ask us for a private transfer link."),
           ("Use", "Tell us who will read it and whether a certified or sworn translation is required."),
           ("Work", "Translate, edit, then a final check."),
           ("Delivery", "You receive the file type we agreed.")],
    who="People and firms who need certificates, statements or manuals in another language.",
    faq=[("Are you sworn translators?", "No. The UK has no sworn translators. We certify translations for UK use. If an authority abroad requires a sworn translator, we work with a vetted partner and say so in the quote."),
         ("Which file formats do you accept?", "Word, Excel, PowerPoint, PDF, InDesign, and photos or scans. Ask about any other format."),
         ("Do you translate into English?", "Yes. Most document work is into English, from any of the languages we cover.")],
)

PAGES["localization"] = svc(
    title="Website and app localisation services | Kayonne Creatives",
    desc="Website, software and app store localisation into European and Asian languages. Glossary, in-context translation, layout checks and multilingual SEO.",
    label="Website and app localisation", h1="The same product, in their language.",
    lede="We localise websites, software interfaces and store listings. The glossary is agreed first, and a person reviews everything that ships.",
    why=["Layout checked when the text gets longer", "Search terms researched in the target language", "A quote from a URL or a file"],
    incl=["Website translation", "App and software localisation", "Store listing localisation", "Transcreation for lines that cannot be translated directly",
          "A glossary for your product", "Right-to-left layout checks for Arabic and Persian", "Translation of new content as you publish it"],
    extra="""<section data-scene="film"><h2>More than the words</h2><p>Localisation also covers dates, currencies, number formats, address forms, payment methods and legal pages. German buyers, for example, expect an Impressum page. <a href="/demo/">See a page change language</a> to watch what changes.</p>""" + LOC_VIDEO_EN + "</section>",
    steps=[("Files", "Send a URL, a string file or a page export."),
           ("Terms", "We agree names, tone and what must not change."),
           ("Translate", "A translator works in context, then an editor reviews."),
           ("Fit", "We check length, links and locale URLs.")],
    who="Software companies, online shops and agencies taking a product into a new market.",
    faq=[("Do you only translate the words?", "No. We also check buttons, metadata and how each language is structured on the site."),
         ("Can you quote from a URL?", "Yes. A URL or a file is enough to start."),
         ("Which CMS do you work with?", "WordPress with WPML or Polylang, Shopify Markets, Webflow Localization, and plain HTML or string files. Ask about others."),
         ("What happens when we add pages later?", "New content can be translated as you publish it, as part of a <a href=\"/care/\">care plan</a> or on request.")],
)

PAGES["games"] = svc(
    title="Game localisation services | Kayonne Creatives",
    desc="Game localisation for interface text, store listings and subtitles, with a glossary and a linguistic check in the build.",
    label="Game localisation", h1="Games that still make sense in the next language.",
    lede="We localise game interface text, store listings and on-screen lines. Jokes and tutorial steps are handled in context, not line by line in a blank spreadsheet.",
    why=["A glossary before the bulk of the words", "Length limits respected", "A linguistic check in the build when you can share one"],
    incl=["Interface strings", "Store listing text", "Subtitle files", "Style notes for tone"],
    steps=[("Kit", "Strings, limits and any build we are allowed to see."),
           ("Guide", "Names, tone and banned terms."),
           ("Translate", "Translation, then editing."),
           ("Play", "A linguistic check in context when a build is available.")],
    who="Game studios and publishers preparing a new language.",
    faq=[("Do you record voice?", "We coordinate voice-over with a recording partner. We do not run a studio."),
         ("Do you play the game?", "When you can share a build, yes. Context prevents bad line breaks.")],
)

PAGES["medical"] = svc(
    title="Medical translation services | Kayonne Creatives",
    desc="Medical and life sciences translation with agreed terminology, a second reader and an NDA before files are shared.",
    label="Medical translation", h1="Medical translation for readers who cannot guess.",
    lede="We translate medical and life sciences texts for companies that need accuracy and a careful process. An NDA is available before files are shared.",
    why=["Terminology agreed before the bulk of the work", "A second reader on the agreed scope", "Confidential handling, with an NDA on request"],
    incl=["Clinical and regulatory documents", "Patient-facing text", "Medical device instructions and leaflets", "Life sciences marketing that must stay accurate", "Glossary creation"],
    steps=[("NDA", "Ask for an NDA before you send sensitive files."),
           ("Terms", "We fix product names and units."),
           ("Translate", "Translation, editing and a final check."),
           ("Query", "Unclear source lines are queried, not guessed.")],
    who="Medical, life sciences and device companies, and the agencies who serve them.",
    faq=[("Do you give medical advice?", "No. We translate. If your process requires it, a clinician must approve text that will be used with patients."),
         ("Is the work confidential?", "Yes. Access is limited to the people on the job. We do not use your files to train a public AI model.")],
)

PAGES["patents"] = svc(
    title="Patent translation services | Kayonne Creatives",
    desc="Patent translation for firms that need consistent terms across a patent family. Claims kept precise, with queries instead of silent changes.",
    label="Patent translation", h1="Patent translation with the claims kept straight.",
    lede="We translate patent texts for firms that care about consistent terms. Claims language is kept precise, never smoothed into marketing.",
    why=["Terms kept stable across a family of documents", "Queries instead of silent changes", "An NDA before the specification is sent"],
    incl=["Patent specifications", "Claims", "Abstracts", "Office actions and related technical correspondence"],
    steps=[("Family", "Send related documents so terms stay consistent."),
           ("Lock", "We confirm the terms that must not change."),
           ("Translate", "A specialist translation, then an edit."),
           ("Check", "Numbers, references and claim order are checked.")],
    who="Patent firms and in-house teams filing or reading in another language.",
    faq=[("Are you a patent attorney?", "No. This is translation. Filing advice stays with your attorney."),
         ("Can you match an earlier translation?", "Yes, if you share it. That is what a glossary and a translation memory are for.")],
)

PAGES["legal"] = svc(
    title="Legal translation services | Kayonne Creatives",
    desc="Legal translation of contracts, policies and court papers. Close to the source, defined terms kept consistent, NDA available.",
    label="Legal translation", h1="Legal translation your counsel can review.",
    lede="We translate legal documents. We do not give legal advice and we do not replace your lawyer. The wording stays close to the source.",
    why=["Close translation, not a rewrite", "Defined terms kept consistent", "An NDA before confidential papers are sent"],
    incl=["Contracts", "Policies and terms", "Court and registry papers", "Legal correspondence", "<a href=\"/certified-translation/\">Certified translations</a> for UK courts"],
    steps=[("Counsel", "Tell us who must review the result."),
           ("Terms", "We list the defined terms."),
           ("Translate", "Translation and editing."),
           ("Return", "Queries are listed, not hidden.")],
    who="Law firms, in-house legal teams and companies with cross-border papers.",
    faq=[("Is this legal advice?", "No."),
         ("Do you certify the translation?", "Yes, for use in the UK. If an authority abroad requires a sworn translation, we arrange it through a partner.")],
)

PAGES["subtitling"] = svc(
    title="Subtitling and transcription services | Kayonne Creatives",
    desc="Subtitles, captions and transcription in European and Asian languages. SRT, WebVTT, EBU-STL and TTML, SDH and burned-in versions.",
    label="Subtitling and transcription", h1="Words on screen, timed and readable.",
    lede="We subtitle, caption and transcribe audio and video. Subtitles follow the reading speed and line length in your style guide, or a standard we agree with you.",
    why=["Reading speed kept in view", "Speaker labels when you need them", "Files you can import straight into your editor"],
    incl=["Translated subtitles", "Same-language captions", "Subtitles for the deaf and hard of hearing (SDH)", "Audio and video transcription, verbatim or clean",
          "Spotting and timing", "Burned-in subtitled video", "Voice-over coordination through a partner", "Audio and data annotation to your guidelines"],
    extra="""<section><h2>File formats</h2><p>SRT, WebVTT, EBU-STL, TTML/DFXP, SBV, and Word or Excel transcripts. Ask if your platform needs something else.</p></section>""",
    steps=[("Media", "Send the file or a link, and the language pair."),
           ("Rules", "Character limits, reading speed, tone and whether it is verbatim."),
           ("Time", "We spot the video, or translate your existing template."),
           ("Watch", "A linguistic check against the picture once the cut is final.")],
    who="Studios, training teams, YouTubers and product teams with video in more than one language.",
    faq=[("How is it priced?", "Per minute of video or audio. Language pair, speed of speech and turnaround change the price."),
         ("Do you interpret meetings?", "No. Live interpreting is not offered."),
         ("Can you book a voice?", "We coordinate it. The recording partner is named in the quote.")],
)

PAGES["proofreading"] = svc(
    title="Proofreading and translation revision | Kayonne Creatives",
    desc="Proofreading and bilingual revision of translations you already have. A second linguist checks accuracy, terminology and language, with tracked changes.",
    label="Proofreading and revision", h1="A second linguist checks the translation you already have.",
    lede="You have a translation from a freelancer, a colleague or a machine, and you need to know it is right. We check it and return tracked changes with a short summary.",
    why=["You know exactly what changed and why", "Errors are classed by type, not waved through", "The level of check is agreed before we start"],
    incl=["Proofreading: the translation is read alone for spelling, grammar, punctuation and style",
          "Revision: the translation is compared with the source for meaning, omissions and terminology",
          "Editing of machine translation output", "Checks of websites and apps in the browser or on a test build",
          "Tracked changes in Word, comments in a PDF, or edits in a bilingual file such as XLIFF"],
    steps=[("Send", "The translation, the source text and any glossary."),
           ("Level", "We agree proofreading or full revision."),
           ("Check", "A linguist works through the text and marks every change."),
           ("Report", "You get the corrected file and a short summary of the issues found.")],
    who="Businesses, agencies, students and authors who already have a translation and want it checked.",
    faq=[("What is the difference between proofreading and revision?", "Proofreading reads the translation on its own. Revision compares it line by line with the source, so it also catches mistranslations and missing text."),
         ("How is it priced?", "Per 1,000 words or per hour. Send both files and you get a fixed price."),
         ("What if the translation is too poor to fix?", "We tell you, and quote a new translation instead.")],
)

PAGES["quality"] = svc(
    title="Machine translation post-editing and LQA | Kayonne Creatives",
    desc="Machine translation post-editing (MTPE), linguistic quality assurance (LQA), localisation testing and terminology management.",
    label="MTPE and quality checks", h1="A human check, at the level the text needs.",
    lede="Some texts need a full translation, edit and proofread. Some need a careful post-edit of machine output. We name the level before we start, and we do not pretend they are the same job.",
    why=["The level of review is written down", "Glossaries and translation memories stay with your account", "Errors are classed, not waved through"],
    incl=["Translation, editing and proofreading", "Machine translation post-editing (MTPE)", "Linguistic quality assurance (LQA) with an error report",
          "Localisation testing", "Glossary and style guide creation", "Translation memory and terminology management"],
    steps=[("Level", "We agree full human translation or post-editing."),
           ("Assets", "Glossary, memory and style notes."),
           ("Work", "The passes you ordered, and no extra pass you did not."),
           ("Report", "On an LQA job, you get a short error report.")],
    who="Agencies and product teams who already have machine output, or who need a formal quality check. To have an existing translation checked, see <a href=\"/proofreading/\">proofreading and revision</a>.",
    faq=[("Is post-editing cheaper?", "Often, when the machine output is good enough. If it is not, we say so and quote a full translation."),
         ("Do you train public AI on our files?", "No.")],
)

PAGES["languages"] = dict(
    title="Languages we translate | Kayonne Creatives",
    desc="Translation into and out of English for European and Asian languages, from German, French and Polish to Japanese, Chinese and Korean.",
    label="Languages", h1="European and Asian languages, with one team.",
    lede="Professional linguists cover the languages below, into and out of English. You deal with one project lead in Glasgow, not a crowd of freelancers.",
    body=f"<section>{LANG_WALLS}</section>"
         "<section><h2>A note on two of them</h2><p><strong>German (Switzerland):</strong> written Swiss German follows Swiss Standard German. It uses ss instead of ß and has its own vocabulary. Spoken Swiss German dialect is covered for subtitles and transcription.</p>"
         "<p><strong>Cantonese:</strong> for subtitles and transcription of spoken Cantonese, and for Traditional Chinese written for Hong Kong readers.</p></section>"
         "<section data-scene=\"film\"><h2>Pages for the most requested languages</h2>{{PAIRS}}</section>"
         "<section><h2>Not on the list?</h2><p>Ask. The quote names the linguist, or we decline the pair.</p></section>",
)

PAGES["industries"] = dict(
    title="Industries | Kayonne Creatives",
    desc="Translation and web work for medical, legal, patent, gaming, software, ecommerce and public-sector clients.",
    label="Industries", h1="Industries we work with.",
    lede="We work with businesses, agencies, game studios, medical and legal companies, patent firms, online shops and software companies. The subject changes the process. The standard of care does not.",
    body="""<section><ul class="grid-3 link-cards">
<li><a class="card" href="/medical/"><strong>Medical and life sciences</strong></a></li>
<li><a class="card" href="/patents/"><strong>Patents</strong></a></li>
<li><a class="card" href="/legal/"><strong>Legal</strong></a></li>
<li><a class="card" href="/games/"><strong>Gaming</strong></a></li>
<li><a class="card" href="/localization/"><strong>Software and apps</strong></a></li>
<li><a class="card" href="/websites/"><strong>Ecommerce and marketing</strong></a></li>
<li><a class="card" href="/documents/"><strong>Technical manuals</strong></a></li>
<li><a class="card" href="/certified-translation/"><strong>Official documents</strong></a></li>
<li><a class="card" href="/subtitling/"><strong>Media and training video</strong></a></li>
</ul></section>""",
)

PAGES["work"] = dict(
    title="Work and samples | Kayonne Creatives",
    desc="Anonymised translation samples, a live localisation demo and this website as our digital sample.",
    label="Work", h1="Samples, not a wall of borrowed logos.",
    lede="Client names appear here only with permission. Until then, these are anonymised samples and our own work, clearly labelled.",
    body="""<section><ul class="grid-2 link-cards plain-cards">
<li class="card"><strong>Medical sample</strong><span class="note">An anonymised medical device leaflet translated into German for a regulatory reader. Terms were fixed in a glossary before translation, and a second linguist revised the text against the source.</span></li>
<li class="card"><strong>Patent sample</strong><span class="note">Claims translated to stay aligned with an earlier English text in the same patent family. Every number, reference and claim order was checked.</span></li>
<li><a class="card" href="/studio/"><strong>This website</strong><span class="note">Built by us in English and German. See how it is built and how much each page weighs.</span></a></li>
<li><a class="card" href="/demo/"><strong>Localisation demo</strong><span class="note">Watch one page change language, date format, currency and reading direction.</span></a></li>
</ul></section>
<section data-scene="windows"><h2>This website</h2><div class="shots">""" + shot("/img/work/site-desktop.webp", "The Kayonne Creatives home page on a laptop, with the 3D scene beside the headline", 1280, 800) + shot("/img/work/site-phone-de.webp", "The German home page on a phone", 390, 844) + """</div></section>
<section data-scene="film"><h2>Localisation demo</h2>""" + LOC_VIDEO_EN + """</section>
<section data-scene="hero"><h2>3D showreel</h2>""" + REEL_EN + """</section>""",
)

PAGES["process"] = dict(
    title="Process and quality | Kayonne Creatives",
    desc="How a web or translation job runs at Kayonne Creatives: scope, build or translate, check, hand over. Translation follows translate, edit, proofread.",
    label="Process", h1="How a job runs.",
    lede="You see the work before it is called finished. Language jobs follow translation, editing and proofreading, then a final check, at the level you ordered.",
    body="""<section><ol class="grid-4 steps">
<li class="card"><h3>Scope</h3><p>We write down the job, the languages, the deadline and what is out of scope.</p></li>
<li class="card"><h3>Build or translate</h3><p>Design, engineering or the language passes. You can review along the way.</p></li>
<li class="card"><h3>Check</h3><p>A speed report for a launch. For language, a final read against the brief by a second person.</p></li>
<li class="card"><h3>Hand over</h3><p>Files, access and ownership. Ongoing care only if you want it.</p></li>
</ol></section>""",
    faq=[("What is the revision policy?", "One round of revisions is included on the files we delivered, within the period stated in your quote. New source text is a new job."),
         ("What if you miss the date?", "We tell you as soon as we see a risk, not on the day. The <a href=\"/terms/\">terms</a> explain what happens if we miss an agreed date.")],
)

PAGES["pricing"] = dict(
    title="Pricing | Kayonne Creatives",
    desc="How we price websites, care plans, certified translation, document translation, subtitling and proofreading. Every job gets a fixed written quote.",
    label="Pricing", h1="How we price.",
    lede="Every job gets a fixed written quote before work starts. Here is what each price is based on and what makes it go up or down.",
    body="""<section><div class="table-wrap"><table>
<thead><tr><th scope="col">Service</th><th scope="col">Priced by</th><th scope="col">What changes the price</th></tr></thead>
<tbody>
<tr><td><a href="/certified-translation/">Certified translation</a></td><td>Per document or page</td><td>Amount of text, language pair, deadline</td></tr>
<tr><td><a href="/documents/">Document translation</a></td><td>Per word</td><td>Language pair, subject, file format and layout work, deadline</td></tr>
<tr><td><a href="/proofreading/">Proofreading and revision</a></td><td>Per 1,000 words or per hour</td><td>Proofreading or full revision, quality of the existing translation</td></tr>
<tr><td><a href="/subtitling/">Subtitling and transcription</a></td><td>Per minute of video or audio</td><td>Language pair, speed of speech, timing from scratch or from a template, SDH</td></tr>
<tr><td><a href="/localization/">Website and app localisation</a></td><td>Per word, plus a fixed fee for checks</td><td>Number of languages, repeated text, CMS work, right-to-left layout</td></tr>
<tr><td><a href="/websites/">Website</a></td><td>Fixed project price</td><td>Number of pages, shop features, copywriting, number of languages</td></tr>
<tr><td><a href="/domains-email/">Domains and business email</a></td><td>Fixed setup fee</td><td>Number of mailboxes, moving existing mail</td></tr>
<tr><td><a href="/seo/">SEO</a></td><td>Monthly</td><td>Number of pages, markets and languages</td></tr>
<tr><td><a href="/care/">Care plan</a></td><td>Monthly</td><td>Size of the site, update frequency, editing hours</td></tr>
</tbody></table></div></section>
<section><h2>Getting a price</h2><p>Send the file, the URL or a short brief on the <a href="/contact/">quote form</a>. The quote states the price, the currency, the delivery date and how to pay. Nothing starts until you accept it.</p></section>""",
)

PAGES["about"] = dict(
    title="About Kayonne Creatives | Glasgow",
    desc="Kayonne Creatives is a Glasgow digital and language agency, led by a qualified translator, with professional linguists and digital specialists.",
    label="About", h1="An agency team. One project lead.",
    lede="Kayonne Creatives is led from Glasgow by its founder, a qualified translator. Professional linguists cover European and Asian languages, and digital specialists build the sites and apps. You speak to one project lead throughout.",
    body="""<section class="grid-2">
<div class="card"><h2>The founder</h2><p>MA in Translation Studies, Middlebury Institute of International Studies at Monterey.</p><p>CIOL Diploma in Translation, Merit.</p><p class="note">The founder leads every project and signs our certified translations.</p></div>
<div class="card"><h2>The team</h2><ul class="ticks"><li>Project lead in Glasgow</li><li>Professional linguists for European languages</li><li>Professional linguists for Asian languages</li><li>Editors and final readers</li><li>Digital specialists for sites, apps, search and speed</li></ul></div>
</section>
<section><h2>How we work</h2><ul class="ticks"><li>Every translation is checked by a second person before delivery.</li><li>Your files are seen only by the people on your job, and an NDA is available.</li><li>We do not use your files to train public AI models.</li><li>We say what we do not do: we are not sworn translators and we do not interpret live.</li></ul></section>""",
)

PAGES["faq"] = dict(
    title="FAQ | Kayonne Creatives",
    desc="Answers about languages, turnaround, file formats, certified translation, confidentiality, revisions, payment and ownership.",
    label="FAQ", h1="Questions clients ask.",
    lede="Short answers. If your case is different, the quote will say so.",
    body="",
    faq=[("Which languages do you cover?", "European and Asian languages, into and out of English. See the <a href=\"/languages/\">languages page</a>. The quote names who will work on your pair."),
         ("How fast is a translation?", "It depends on length, language and subject. A short, clear document often takes a few working days. A product localisation is scheduled. The quote gives a date."),
         ("Which formats do you accept?", "Word, Excel, PowerPoint, PDF, web exports, string files, subtitle files, and photos or scans. Design files such as InDesign by agreement."),
         ("Do you provide certified translations?", "Yes, for use in the UK. Where a foreign authority requires a sworn translator, we use a vetted partner. See <a href=\"/certified-translation/\">certified translation</a>."),
         ("Is the work confidential?", "Yes. We sign an NDA on request. Only the people on your job see the files. We do not train public AI models on your content."),
         ("How do revisions work?", "One round is included on the delivered files, within the period stated in the quote. New text is quoted again."),
         ("How do you take payment?", "The quote states the amount, the currency, any deposit, the due date and how to pay."),
         ("Who owns the website code and the translated text?", "You do, once the agreed fees are paid. See the <a href=\"/terms/\">terms</a>."),
         ("Can you set up our domain and email?", "Yes. See <a href=\"/domains-email/\">domains and business email</a>."),
         ("Do you interpret calls or events?", "No. Live interpreting is not offered.")],
)

PAGES["insights"] = dict(
    title="Insights | Kayonne Creatives",
    desc="Practical notes on website localisation, multilingual SEO and website speed, for people about to buy the work.",
    label="Insights", h1="Notes for people about to buy the work.",
    lede="Short, practical articles on localisation, search and speed.",
    body="""<section><ul class="grid-2 link-cards">
<li><a class="card" href="/insights/localise-a-website/"><strong>How to localise a website</strong><span class="note">Five decisions to make before the first page is translated.</span></a></li>
<li><a class="card" href="/insights/speed-mistakes/"><strong>Website speed mistakes</strong><span class="note">What usually makes a small business site slow on a phone.</span></a></li>
</ul></section>""",
)

PAGES["insights/localise-a-website"] = dict(
    title="How to localise a website | Kayonne Creatives",
    desc="Five steps to localise a website: locale URLs, a glossary, keyword research per language, room for longer text, and hreflang.",
    label="Insights", h1="How to localise a website",
    body="""<article class="prose">
<p>Start with the market, not the plugin. Choose locale URLs, such as one folder per language (<code>/de/</code>, <code>/fr/</code>), and keep one address as the default.</p>
<p>Write a glossary before the first page. Product names, buttons and claims should not change halfway through.</p>
<p>Research search terms in the target language. A direct translation of an English keyword is often not what people search for.</p>
<p>Leave room in buttons and headings. German and Dutch often run longer than English, and Japanese needs different line breaking.</p>
<p>Add hreflang, translate the titles and descriptions, and do not rely on the browser to redirect everyone automatically.</p>
</article>""",
)

PAGES["insights/speed-mistakes"] = dict(
    title="Website speed mistakes | Kayonne Creatives",
    desc="Common website speed mistakes: heavy hero images and 3D scenes, uncompressed photos, unused fonts, and testing only on a fast laptop.",
    label="Insights", h1="Website speed mistakes",
    body="""<article class="prose">
<p>A large hero image or a 3D scene that loads before the headline will delay the first paint on a phone.</p>
<p>Uncompressed photographs and unused fonts are usually where the weight comes from.</p>
<p>Test on a mid-range phone, not only on the office laptop.</p>
<p>Share the Core Web Vitals report. A single score out of 100 is not the threshold that matters.</p>
</article>""",
)

FORM_SERVICES = [
    ("Language", ["Certified translation (UK)", "Document translation", "Website or app localisation", "Game localisation",
                  "Medical translation", "Patent translation", "Legal translation", "Subtitling or transcription",
                  "Proofreading or revision", "MTPE or LQA"]),
    ("Digital", ["Website", "Online shop", "Web app", "Mobile app", "Domain and business email", "SEO", "Speed or accessibility audit", "Care plan"]),
    ("Both", ["Website and translation", "International launch", "Shop localisation", "Multilingual SEO", "Something else"]),
    ("Free", ["Free website check", "Free readiness check"]),
]


def quote_form(lang, L):
    opts = "".join(f'<optgroup label="{g}">' + "".join(f"<option>{o}</option>" for o in items) + "</optgroup>"
                   for g, items in L["services"])
    next_url = "https://kayonnecreatives.com" + ("/de" if lang == "de" else "") + "/thanks/"
    return f"""<form class="card form" id="quote" action="https://formsubmit.co/{EMAIL}" method="POST" enctype="multipart/form-data">
  <h2>{L['heading']}</h2>
  <input type="hidden" name="_subject" value="{L['subject']}" />
  <input type="hidden" name="_next" value="{next_url}" />
  <input type="hidden" name="_template" value="table" />
  <input type="hidden" name="_autoresponse" value="{L['auto']}" />
  <div class="hp" aria-hidden="true"><label for="f-honey">Leave empty</label><input id="f-honey" type="text" name="_honey" tabindex="-1" autocomplete="off" /></div>
  <div class="fields">
    <div><label for="f-name">{L['name']} *</label><input id="f-name" name="name" required autocomplete="name" /></div>
    <div><label for="f-email">{L['email']} *</label><input id="f-email" name="email" type="email" required autocomplete="email" /></div>
    <div><label for="f-phone">{L['phone']}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" /></div>
    <div><label for="f-company">{L['company']}</label><input id="f-company" name="company" autocomplete="organization" /></div>
    <div class="full"><label for="f-service">{L['service']} *</label><select id="f-service" name="service" required><option value="">{L['choose']}</option>{opts}</select></div>
    <div><label for="f-source">{L['source']}</label><input id="f-source" name="source_language" list="langs" placeholder="{L['source_ph']}" /></div>
    <div><label for="f-target">{L['target']}</label><input id="f-target" name="target_languages" placeholder="{L['target_ph']}" /></div>
    <div><label for="f-deadline">{L['deadline']}</label><input id="f-deadline" name="deadline" type="date" /></div>
    <div><label for="f-size">{L['size']}</label><input id="f-size" name="size" placeholder="{L['size_ph']}" /></div>
    <div class="full"><label for="f-file">{L['file']}</label><input id="f-file" name="attachment" type="file" accept=".pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.txt,.rtf,.odt,.srt,.vtt,.xliff,.xlf,.json,.csv,.jpg,.jpeg,.png,.heic,.zip" /><p class="note">{L['file_note']}</p></div>
    <div class="full"><label for="f-message">{L['message']}</label><textarea id="f-message" name="message" placeholder="{L['message_ph']}"></textarea></div>
  </div>
  <p class="check"><input type="checkbox" id="f-consent" name="consent" value="yes" required /><label for="f-consent">{L['consent']} *</label></p>
  <p><button class="btn" type="submit">{L['send']}</button></p>
  <p class="note">{L['after']}</p>
</form>
<datalist id="langs">{''.join(f'<option value="{x}"></option>' for x in L['datalist'])}</datalist>"""


FORM_EN = dict(
    heading="Request a quote", subject="New quote request from kayonnecreatives.com",
    auto="Thank you for contacting Kayonne Creatives. We have received your request and will reply by email with a quote or any questions. If you need to add files, reply to this email.",
    name="Your name", email="Email", phone="Phone (optional)", company="Company (optional)", service="What do you need?",
    choose="Choose a service", source="From language", source_ph="e.g. Polish", target="Into language(s)", target_ph="e.g. English, German",
    deadline="Deadline", size="Size", size_ph="e.g. 3 pages, 2,000 words, 12 minutes", file="Attach a file",
    file_note="One file, up to 10 MB in total. For larger or more files, paste a WeTransfer or Google Drive link in the message.",
    message="Message", message_ph="Who will read it, where it will be used, the website address, anything we should know.",
    consent='I agree that Kayonne Creatives may use these details to reply to my request. See the <a href="/privacy/">privacy notice</a>.',
    send="Send request", after=f"The form is delivered to {EMAIL} by our form provider. You can also email us directly.",
    services=FORM_SERVICES, datalist=["English"] + EUROPE + ASIA + ["Arabic", "Persian"],
)

PAGES["contact"] = dict(
    title="Get a quote | Kayonne Creatives",
    desc="Ask for a quote for translation, certified translation, subtitling, a website, or domain and email setup. Attach your file and get a fixed price.",
    label="Contact", h1="Tell us the job.",
    lede=f'Tell us the service, the languages and the deadline, and attach the file if you have one. We reply by email with a fixed quote or any questions. You can also write to <a href="mailto:{EMAIL}">{EMAIL}</a>.',
    body=quote_form("en", FORM_EN), no_cta=True,
)

PAGES["thanks"] = dict(
    title="Request sent | Kayonne Creatives", desc="Your request has been sent to Kayonne Creatives.", noindex=True,
    label="Contact", h1="Thank you. Your request has been sent.",
    lede=f"We will reply by email with a quote or any questions. A confirmation has been sent to your inbox. If it is not there, check your spam folder, or write to {EMAIL}.",
    body='<p><a class="btn ghost" href="/">Back to the home page</a></p>', no_cta=True,
)

PAGES["privacy"] = dict(
    title="Privacy notice | Kayonne Creatives",
    desc="How Kayonne Creatives collects, uses and protects personal data under UK GDPR.",
    label="Legal", h1="Privacy notice",
    body=f"""<article class="prose">
<p>This notice explains how Kayonne Creatives ("we") uses personal data when you visit this website, ask for a quote or become a client. We follow the UK General Data Protection Regulation (UK GDPR) and the Data Protection Act 2018.</p>
<h2>Who we are</h2>
<p>Kayonne Creatives, Glasgow, United Kingdom. Contact for privacy questions: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>What we collect</h2>
<ul><li><strong>Quote requests:</strong> your name, email address, phone number and company if given, the service and languages you need, your message, and any file you attach.</li>
<li><strong>Client work:</strong> the documents, media and website content you send us, which may contain personal data about you or other people.</li>
<li><strong>Billing:</strong> your name, address and payment details needed to issue invoices.</li>
<li><strong>Website visits:</strong> our hosting provider records technical data such as IP address and browser type in server logs. This website does not use analytics or advertising cookies.</li></ul>
<h2>Why we use it, and our legal basis</h2>
<ul><li>To reply to your request and prepare a quote: steps taken at your request before entering a contract.</li>
<li>To carry out the work you ordered: performance of a contract.</li>
<li>To keep accounting records: legal obligation.</li>
<li>To keep the website secure and working: our legitimate interests.</li></ul>
<h2>Who we share it with</h2>
<ul><li>The linguists and specialists working on your job, who are bound by confidentiality.</li>
<li>FormSubmit, which delivers the quote form to our inbox.</li>
<li>Our email provider and file storage provider.</li>
<li>GitHub, which hosts this website.</li>
<li>Our accountant, and authorities where the law requires it.</li></ul>
<p>Some of these providers process data outside the UK, including in the United States. Where they do, the transfer is covered by the UK's adequacy regulations or by standard contractual clauses. We never sell personal data and we do not use your files to train AI models.</p>
<h2>How long we keep it</h2>
<ul><li>Quote requests that do not become a job: up to 12 months.</li>
<li>Files you send for a job: deleted within 90 days of delivery unless you ask us to keep them, for example as a translation memory.</li>
<li>Invoices and accounting records: 6 years, as required by HMRC.</li></ul>
<h2>Your rights</h2>
<p>You can ask for a copy of your data, ask us to correct or delete it, object to or restrict how we use it, and ask for it in a portable format. Write to <a href="mailto:{EMAIL}">{EMAIL}</a>. We reply within one month.</p>
<p>If you are unhappy with how we handle your data, you can complain to the Information Commissioner's Office (ICO) at <a href="https://ico.org.uk/make-a-complaint/">ico.org.uk</a>.</p>
<h2>Changes</h2>
<p>We will update this notice when our practices change. Last updated: October 2026.</p>
</article>""",
)

PAGES["cookies"] = dict(
    title="Cookie policy | Kayonne Creatives",
    desc="This website does not set cookies or use analytics or advertising trackers.",
    label="Legal", h1="Cookie policy",
    body=f"""<article class="prose">
<p>This website does not set any cookies and does not use analytics, advertising or social media trackers. That is why there is no cookie banner.</p>
<p>Fonts and scripts are served from our own website, so your visit is not shared with font or script providers.</p>
<p>When you send the quote form, it is delivered by FormSubmit. FormSubmit may show a spam check, which can use its own cookies. See the <a href="/privacy/">privacy notice</a> for how we handle your data.</p>
<p>If we add analytics in the future, we will update this page and ask for your consent first where the law requires it.</p>
<p>Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>. Last updated: October 2026.</p>
</article>""",
)

PAGES["terms"] = dict(
    title="Terms of service | Kayonne Creatives",
    desc="Terms for translation, localisation, subtitling, website and care plan work by Kayonne Creatives.",
    label="Legal", h1="Terms of service",
    body=f"""<article class="prose">
<p>These terms apply to all work by Kayonne Creatives ("we") for you ("the client"). Your quote may add specific terms, and where it does, the quote takes priority.</p>
<h2>1. Quotes and orders</h2>
<p>A quote is valid for 30 days. It states the scope, price, currency, delivery date and payment terms. A job starts when you accept the quote in writing and pay any deposit it names.</p>
<h2>2. Your responsibilities</h2>
<p>You confirm you have the right to send us the material and to have it translated or published. You give us final source text, files that can be read, and timely answers to our questions. Delays in these move the delivery date.</p>
<h2>3. Changes</h2>
<p>New or changed source text, extra languages or extra pages are outside the original scope and are quoted separately.</p>
<h2>4. Delivery and revisions</h2>
<p>We deliver in the format agreed in the quote. One round of revisions on the delivered work is included within 14 days of delivery, unless the quote says otherwise. Changes of style or preference to a correct translation, and new requests, are charged separately.</p>
<h2>5. Late delivery</h2>
<p>If we see a risk to an agreed date, we tell you straight away. If we miss an agreed date for a reason within our control, you may cancel the undelivered part without charge, or agree a reduced price with us.</p>
<h2>6. Payment</h2>
<p>Invoices are due within 14 days unless the quote says otherwise. Larger projects may require a deposit and staged payments. We may pause work on overdue accounts.</p>
<h2>7. Ownership</h2>
<p>Once the agreed fees are paid in full, you own the translations, website code and designs made for you, except third-party software, fonts, plugins and stock assets, which stay under their own licences. We may keep translation memories and glossaries for your future jobs and will delete them if you ask.</p>
<h2>8. Confidentiality</h2>
<p>We keep your material confidential and share it only with the people working on your job, who are bound by confidentiality. We sign a separate NDA on request.</p>
<h2>9. Certified and specialist translations</h2>
<p>A certified translation confirms that the translation is accurate. It does not guarantee that a third party will accept it, as each authority sets its own rules. We do not give legal, medical or patent filing advice.</p>
<h2>10. Websites, hosting and care plans</h2>
<p>Domains, hosting and email accounts are registered in your name and paid by you to the provider. Care plans run monthly and can be cancelled with the notice stated in the plan. We are not responsible for outages or changes made by third-party providers.</p>
<h2>11. Liability</h2>
<p>Our total liability for any job is limited to the fees paid for that job. We are not liable for indirect losses such as lost profit. Nothing in these terms limits liability that cannot be limited by law.</p>
<h2>12. Cancellation</h2>
<p>If you cancel a job after it has started, you pay for the work done so far. If you are a consumer and order at a distance, you have a 14-day right to cancel under the Consumer Contracts Regulations 2013. If you ask us to start within those 14 days, you pay for the work done before you cancel.</p>
<h2>13. Complaints</h2>
<p>Write to <a href="mailto:{EMAIL}">{EMAIL}</a>. We reply within 5 working days.</p>
<h2>14. Law</h2>
<p>These terms are governed by the law of Scotland, and the Scottish courts have jurisdiction. Consumers keep any rights they have under the law where they live.</p>
<p class="note">Last updated: October 2026.</p>
</article>""",
)

PAGES["studio"] = dict(
    title="How this website is built | Kayonne Creatives",
    desc="This website is our digital sample: plain HTML and CSS, self-hosted fonts, no cookies, no trackers, in English and German.",
    label="Our own site", h1="This website is the digital sample.",
    lede="We sell speed, search and build quality, so this site is built the way we build for clients. Here are the facts you can check yourself.",
    body="""<section><h2>What is in it</h2><ul class="ticks">
<li>Plain HTML and CSS. Scripts only run the menu, the animations and the 3D scenes</li>
<li>3D scenes built with three.js and served from this site. They load after the page is ready and switch off when your device asks for reduced motion or to save data</li>
<li>Two font files, served from this site, not from Google</li>
<li>No cookies, no analytics and no third-party trackers</li>
<li>Every page in English and German, linked with hreflang</li>
<li>Labelled form fields, keyboard navigation and a skip link</li>
<li>Hosted on GitHub Pages, with HTTPS</li></ul></section>
<section><h2>What each page weighs</h2><p>The size of the HTML for a selection of pages. The stylesheet and fonts are shared and are only downloaded once.</p>{{WEIGHTS}}</section>
<section><p>Check it yourself with <a href="https://pagespeed.web.dev/analysis?url=https%3A%2F%2Fkayonnecreatives.com%2F">PageSpeed Insights</a>.</p></section>""",
)

DEMO_STRINGS = {
    "en": {"label": "English", "dir": "ltr", "locale": "en-GB", "currency": "GBP", "price": 49.99,
           "title": "Spring sale: 20% off every plan", "body": "Your order ships on {date}.", "total": "Total", "button": "Add to basket"},
    "de": {"label": "Deutsch", "dir": "ltr", "locale": "de-DE", "currency": "EUR", "price": 57.99,
           "title": "Frühjahrsaktion: 20 % Rabatt auf alle Tarife", "body": "Ihre Bestellung wird am {date} versendet.", "total": "Gesamt", "button": "In den Warenkorb"},
    "ja": {"label": "日本語", "dir": "ltr", "locale": "ja-JP", "currency": "JPY", "price": 9500,
           "title": "春のセール：全プラン20%オフ", "body": "ご注文の商品は{date}に発送されます。", "total": "合計", "button": "カートに入れる"},
    "ar": {"label": "العربية", "dir": "rtl", "locale": "ar-AE", "currency": "AED", "price": 229,
           "title": "تخفيضات الربيع: خصم ٢٠٪ على جميع الباقات", "body": "سيتم شحن طلبك في {date}.", "total": "الإجمالي", "button": "أضف إلى السلة"},
}


def demo_script(ltr="left to right", rtl="right to left", start="en"):
    import json
    return """<script>
(function(){
  var S=""" + json.dumps(DEMO_STRINGS, ensure_ascii=False) + """;
  var when=new Date(Date.UTC(2026,10,3,12));
  var box=document.getElementById("demo-card"),info=document.getElementById("demo-info");
  function show(k){
    var s=S[k],en=S.en;
    box.setAttribute("dir",s.dir);box.setAttribute("lang",k);
    var date=new Intl.DateTimeFormat(s.locale,{dateStyle:"full",timeZone:"UTC"}).format(when);
    var price=new Intl.NumberFormat(s.locale,{style:"currency",currency:s.currency}).format(s.price);
    box.querySelector("h3").textContent=s.title;
    box.querySelector(".d-body").textContent=s.body.replace("{date}",date);
    box.querySelector(".d-total").textContent=s.total+": "+price;
    box.querySelector("button").textContent=s.button;
    var diff=Math.round((s.title.length-en.title.length)/en.title.length*100);
    info.querySelector(".i-len").textContent=s.title.length+" ("+(diff>0?"+":"")+diff+"%)";
    info.querySelector(".i-date").textContent=date;
    info.querySelector(".i-cur").textContent=price;
    info.querySelector(".i-dir").textContent=s.dir==="rtl"?""" + json.dumps(rtl) + """:""" + json.dumps(ltr) + """;
    document.querySelectorAll(".demo-tabs button").forEach(function(b){b.setAttribute("aria-pressed",b.dataset.k===k?"true":"false");});
  }
  document.querySelectorAll(".demo-tabs button").forEach(function(b){b.addEventListener("click",function(){show(b.dataset.k);});});
  show(""" + json.dumps(start) + """);
})();
</script>"""


DEMO_BODY = """<section class="demo">
<div class="demo-tabs" role="group" aria-label="Language">""" + "".join(
    f'<button type="button" class="btn ghost" data-k="{k}" lang="{k}">{v["label"]}</button>' for k, v in DEMO_STRINGS.items()) + """</div>
<div class="grid-2">
  <div class="card demo-card" id="demo-card" aria-live="polite"><h3></h3><p class="d-body"></p><p class="d-total"></p><button type="button" class="btn" tabindex="-1">.</button></div>
  <dl class="card demo-info" id="demo-info">
    <dt>{len}</dt><dd class="i-len"></dd><dt>{date}</dt><dd class="i-date"></dd><dt>{cur}</dt><dd class="i-cur"></dd><dt>{dir}</dt><dd class="i-dir"></dd>
  </dl>
</div>
<p class="note">{note}</p>
</section>"""

PAGES["demo"] = dict(
    title="Localisation demo | Kayonne Creatives",
    desc="See one product card change language: text length, date format, currency and reading direction in English, German, Japanese and Arabic.",
    label="Localisation demo", h1="See a page change language.",
    lede="This sample is not a client. It shows what localisation changes besides the words: text length, dates, currency and reading direction. Pick a language.",
    body=DEMO_BODY.format(len="Headline length in characters (vs English)", date="Date format", cur="Currency format", dir="Reading direction",
                          note="Sample prices. Dates and currencies are formatted by your browser for each locale, the same way a localised site does it."),
    script=demo_script(),
)

NOT_FOUND = dict(
    title="Page not found | Kayonne Creatives", desc="This page does not exist.", noindex=True,
    label="404", h1="That page is not here.",
    lede='The link may be old or mistyped. <span lang="de">Diese Seite gibt es nicht.</span>',
    body='<p class="actions"><a class="btn" href="/">Home</a> <a class="btn ghost" href="/de/" lang="de">Startseite (Deutsch)</a> <a class="btn ghost" href="/contact/">Contact</a></p>',
    no_cta=True,
)


# ---------------------------------------------------------------------------
# Team hubs, new money pages, language pages and articles
# ---------------------------------------------------------------------------

def team_video(key, caption, label):
    return video(f"team-{key}", caption, 1280, 720, label)


STATEMENT_EN = """<figure class="statement" aria-label="Example of the statement attached to a certified translation">
<p class="kicker">Example statement</p>
<p class="st-title">Certificate of translation accuracy</p>
<p>I confirm that the attached document is a true and accurate translation of the original birth certificate from Polish into English.</p>
<dl><dt>Translator</dt><dd>Full name and signature</dd><dt>Date</dt><dd>Date of translation</dd><dt>Contact</dt><dd>hello@kayonnecreatives.com</dd><dt>Company</dt><dd>Kayonne Creatives, Glasgow</dd></dl>
<figcaption class="note">These are the four things the Home Office asks to see: confirmation of accuracy, the date, the translator's full name and signature, and contact details.</figcaption>
</figure>"""

PAGES["digital"] = dict(
    title="Kayonne Digital | Web design, apps and SEO, Glasgow",
    desc="The Kayonne Digital team builds websites, online shops and apps, sets up domains and business email, and handles SEO, speed and care.",
    label="Kayonne Digital", h1="The build team.",
    lede="Designers and developers who build websites, shops and apps, set up the domain and email behind them, and keep them fast and found. Based in Glasgow, working with businesses across the UK.",
    body="""<section data-scene="windows"><h2>What the team builds</h2>{{TEAM:digital}}</section>
<section data-scene="tiles" class="grid-2 split-copy"><div><h2>Who you work with</h2><p>A project lead in Glasgow, a designer and a developer on every build. You see designs before anything is coded, a test site before launch, and a speed report at handover.</p><p>When your site needs another language, the <a href="/language/">language team</a> sits next door. No second agency, no hand-off by email.</p></div>"""
    + team_video("digital", "The Digital team's work in 3D: browser windows, an app grid and phones.", "Kayonne Digital reel") + """</section>
<section data-scene="bars"><h2>Packages</h2><ul class="grid-4 link-cards plain-cards">
<li class="card"><strong>One-page site</strong><span class="note">Offer, contact form, map. For a launch or a sole trader.</span></li>
<li class="card"><strong>Business site</strong><span class="note">Five to eight pages, blog, local SEO setup.</span></li>
<li class="card"><strong>Online shop</strong><span class="note">Shopify or WooCommerce, payments, delivery rules.</span></li>
<li class="card"><strong>Multilingual site</strong><span class="note">Any package in two or more languages.</span></li>
</ul><p><a class="btn ghost" href="/pricing/">How we price</a></p></section>
<section data-scene="lens" class="offer card"><div><p class="kicker">Free</p><h2>Website check</h2><p>Send your address. We look at speed on a phone, mobile layout, search basics and the contact form, and email you a short written list of what to fix first.</p></div><p><a class="btn magnetic" href="/website-check/">Get a free check</a></p></section>""",
    faq=[("Do you only work in Glasgow?", "No. The team is in Glasgow and works with clients across the UK and abroad. Local clients can meet in person."),
         ("Who owns the site?", "You do, once the agreed fees are paid. Domain, hosting and email accounts are in your name."),
         ("Can you translate the site too?", "Yes. That is what the <a href=\"/global/\">Global</a> service is for.")],
)

PAGES["language"] = dict(
    title="Kayonne Language | Certified and specialist translation, UK",
    desc="The Kayonne Language team: qualified translators for certified, legal, medical and patent translation, subtitling and proofreading, with a second check on every job.",
    label="Kayonne Language", h1="The translation team.",
    lede="Qualified translators led from Glasgow by a translator with an MA in Translation Studies and the CIOL Diploma in Translation. Every job is checked by a second linguist before it leaves us.",
    body="""<section data-scene="sheets"><h2>What the team translates</h2>{{TEAM:language}}</section>
<section data-scene="seal" class="grid-2 split-copy"><div><h2>Certified for the Home Office</h2><p>The UK has no sworn translators. A certified translation carries a signed statement that it is accurate, with the date and the translator's details. Ours include everything the Home Office asks for.</p><p><a class="btn magnetic" href="/certified-translation/">Certified translation</a></p></div>""" + STATEMENT_EN + """</section>
<section data-scene="path"><h2>How a translator joins the team</h2><ol class="grid-4 steps">
<li class="card"><h3>Qualified</h3><p>A translation degree or a professional qualification such as the CIOL Diploma.</p></li>
<li class="card"><h3>Native</h3><p>They translate into their own first language.</p></li>
<li class="card"><h3>Specialist</h3><p>Legal, medical and patent work goes only to linguists with experience in that field.</p></li>
<li class="card"><h3>Checked</h3><p>A second linguist revises every job before delivery.</p></li>
</ol></section>
<section data-scene="film" class="grid-2 split-copy"><div><h2>Languages</h2><p>European and Asian languages, into and out of English. The most requested have their own pages: <a href="/languages/polish/">Polish</a>, <a href="/languages/romanian/">Romanian</a>, <a href="/languages/arabic/">Arabic</a>, <a href="/languages/urdu/">Urdu</a>, <a href="/languages/chinese/">Chinese</a>, <a href="/languages/spanish/">Spanish</a>, <a href="/languages/french/">French</a>, <a href="/languages/german/">German</a>, <a href="/languages/ukrainian/">Ukrainian</a> and <a href="/languages/portuguese/">Portuguese</a>.</p><p><a class="btn ghost" href="/languages/">All languages</a></p></div>"""
    + team_video("language", "The Language team's work in 3D: a certified seal, documents and subtitles.", "Kayonne Language reel") + """</section>
<section data-scene="shield"><h2>Your documents stay private</h2><ul class="ticks"><li>Only the people on your job see the files.</li><li>NDA on request, before you send anything.</li><li>Files deleted within 90 days of delivery unless you ask us to keep them.</li><li>Never used to train public AI models.</li></ul></section>""",
    faq=[("Do you translate into English or out of it?", "Both. Most certified work is into English, for UK authorities."),
         ("Is a certified translation the same as a sworn one?", "No. See <a href=\"/certified-translation/\">certified translation</a> and <a href=\"/apostille/\">apostille and legalisation</a>."),
         ("How do I get a price?", "Upload the document on the <a href=\"/contact/\">quote form</a>. You get a fixed price before we start.")],
)

PAGES["global"] = dict(
    title="Kayonne Global | Website localisation and international launch",
    desc="Kayonne Global brings the build and translation teams together: localised websites and shops, multilingual SEO and international launches, from one Glasgow team.",
    label="Kayonne Global", h1="Both teams. One launch.",
    lede="Most firms do one half: they build the site, or they translate it. Kayonne Global puts the build team and the translation team on the same project, so your site is ready for the next market without a hand-off in the middle.",
    body="""<section data-scene="globe"><h2>What we take abroad</h2>{{TEAM:global}}</section>
<section data-scene="plane"><h2>How a launch runs</h2><ol class="grid-3 steps">
<li class="card"><h3>Audit</h3><p>Is the site ready to translate? Text in images, fixed-width buttons, hard-coded dates.</p></li>
<li class="card"><h3>Research</h3><p>Search terms researched in each market by a native speaker, not translated from English.</p></li>
<li class="card"><h3>Build</h3><p>Language folders, hreflang, local currency and dates, layout that survives longer words.</p></li>
<li class="card"><h3>Translate</h3><p>A specialist translates in context. A second linguist revises.</p></li>
<li class="card"><h3>Check</h3><p>Every page checked in the browser, in every language, on a phone.</p></li>
<li class="card"><h3>Launch</h3><p>Sitemaps and Search Console for each market, plus a report on what to watch.</p></li>
</ol></section>
<section data-scene="film" class="grid-2 split-copy"><div><h2>See it happen</h2><p>One product card in English, German, Japanese and Arabic. The words change, and so do the date, the currency and the reading direction.</p><p><a class="btn ghost" href="/demo/">Try the live demo</a></p></div>""" + LOC_VIDEO_EN + """</section>
<section data-scene="check"><h2>Why not just use a translation plugin?</h2><div class="table-wrap"><table>
<thead><tr><th scope="col"></th><th scope="col">Machine plugin alone</th><th scope="col">Kayonne Global</th></tr></thead>
<tbody>
<tr><td>Speed to first draft</td><td>Minutes</td><td>Days</td></tr>
<tr><td>Search terms per market</td><td>Translated from English</td><td>Researched by a native speaker</td></tr>
<tr><td>Brand names, tone, legal claims</td><td>Not checked</td><td>Glossary agreed first, revised by a second linguist</td></tr>
<tr><td>Layout with longer words</td><td>Not checked</td><td>Checked on desktop and phone</td></tr>
<tr><td>Best for</td><td>Low-risk pages, internal tools</td><td>Pages that sell, legal pages, checkout</td></tr>
</tbody></table></div><p class="note">A plugin can be the right first step. We can also review and fix machine output instead of starting again. See <a href="/quality/">MTPE</a>.</p></section>
<section data-scene="check" class="offer card"><div><p class="kicker">Free</p><h2>International readiness check</h2><p>We look at your site and tell you what would break in translation, which market to start with, and roughly what it would take.</p></div><p><a class="btn magnetic" href="/readiness-check/">Check my site</a></p></section>""",
    faq=[("Which markets do you know best?", "Europe and Asia. Germany and the German-speaking countries are a particular focus."),
         ("Can you work with our existing developer?", "Yes. We can supply translations, keyword research and hreflang specifications to your team."),
         ("Do you handle the shop too?", "Yes. See <a href=\"/ecommerce-localisation/\">shop localisation</a>.")],
)

PAGES["web-design-glasgow"] = svc(
    title="Web design Glasgow | Kayonne Creatives",
    desc="Web design in Glasgow from a local team: business websites, online shops and redesigns, fast and found, with the option to add other languages.",
    label="Web design Glasgow", h1="Web design in Glasgow, by a team you can meet.",
    lede="We design and build websites for Glasgow businesses: trades, clinics, shops, consultants and startups. Clear pages, fast on a phone, set up for local search, and ready for another language if you sell abroad.",
    why=["A local team you can meet in person", "Local SEO and Google Business Profile set up with the site", "Translation in-house when you need a second language"],
    incl=["Business websites", "Online shops", "Redesigns of slow or outdated sites", "Domain and business email", "Google Business Profile setup", "Care plans after launch"],
    steps=[("Meet", "A call or a coffee in Glasgow to agree what the site must do."),
           ("Design", "You approve the look before anything is built."),
           ("Build", "We build, connect the domain and set up email."),
           ("Launch", "Speed report, local SEO checklist and training.")],
    who="Glasgow and West of Scotland businesses that want a site that brings in enquiries.",
    faq=[("How much does a website cost in Glasgow?", "Local prices run from a few hundred pounds for a template to several thousand for a custom build. See our <a href=\"/insights/website-cost-glasgow/\">guide to website costs</a>."),
         ("Can you help with Google Maps?", "Yes. We set up and tidy your Google Business Profile so you show up in local searches."),
         ("Can we meet?", "Yes. Tell us in the quote form and we'll arrange it.")],
)

PAGES["website-check"] = dict(
    title="Free website check | Kayonne Digital",
    desc="Send your website address and get a free written check of speed on a phone, mobile layout, search basics and your contact form.",
    label="Kayonne Digital · Free", h1="A free check of your website.",
    lede="Send us your website address. A developer looks at it the way a customer and Google would, then emails you a short list of what to fix first. No obligation.",
    body="""<section data-scene="lens"><h2>What we check</h2><ul class="grid-4 link-cards plain-cards">
<li class="card"><strong>Speed on a phone</strong><span class="note">Core Web Vitals, with the numbers.</span></li>
<li class="card"><strong>Mobile layout</strong><span class="note">Text, buttons and menus at phone width.</span></li>
<li class="card"><strong>Search basics</strong><span class="note">Titles, descriptions, headings, indexing.</span></li>
<li class="card"><strong>Contact form</strong><span class="note">We send a test and see if it arrives.</span></li>
</ul></section>
<section data-scene="ring" class="offer card"><div><h2>Request your check</h2><p>Choose "Free website check" on the form and put your website address in the message.</p></div><p><a class="btn magnetic" href="/contact/?service=Free+website+check">Request a check</a></p></section>""",
)

PAGES["readiness-check"] = dict(
    title="Free international readiness check | Kayonne Global",
    desc="Find out what would break when your website is translated, which market to start with, and what it would take. Free check from Kayonne Global.",
    label="Kayonne Global · Free", h1="Is your website ready for another language?",
    lede="We look at your site with a developer's eyes and a translator's eyes, then tell you what would break in translation and which market makes sense first.",
    body="""<section data-scene="check"><h2>What we look at</h2><ul class="grid-4 link-cards plain-cards">
<li class="card"><strong>Text in images</strong><span class="note">Words baked into pictures can't be translated.</span></li>
<li class="card"><strong>Layout</strong><span class="note">Buttons and menus that break when German runs 30% longer.</span></li>
<li class="card"><strong>Platform</strong><span class="note">Whether your CMS or shop handles languages well.</span></li>
<li class="card"><strong>Market fit</strong><span class="note">Search demand, currency, payment and legal pages.</span></li>
</ul></section>
<section data-scene="plane" class="offer card"><div><h2>Request your check</h2><p>Choose "Free readiness check" on the form, add your website address and the markets you're thinking about.</p></div><p><a class="btn magnetic" href="/contact/?service=Free+readiness+check">Request a check</a></p></section>""",
)

PAGES["certified-translation-glasgow"] = svc(
    title="Certified translation Glasgow | Kayonne Language",
    desc="Certified translation in Glasgow for the Home Office, UKVI, Scottish courts, universities and banks. Signed statement, checked by a second linguist.",
    label="Certified translation Glasgow", h1="Certified translation in Glasgow.",
    lede="Certified translations from a Glasgow team, for visas, settlement, citizenship, Scottish courts, universities, employers and banks. Each one comes with a signed statement of accuracy, the date and the translator's details.",
    why=["Led by a CIOL-qualified translator in Glasgow", "A second linguist checks every certified translation", "Upload a photo or scan from anywhere in Scotland"],
    incl=["Birth, marriage and divorce certificates", "Passports and ID", "Driving licences", "Degrees and transcripts", "Bank statements", "Court and solicitor papers"],
    extra=f"<section data-scene=\"seal\" class=\"grid-2 split-copy\"><div><h2>What you receive</h2><p>A translation laid out like the original, and a signed statement like this one. Delivered as a PDF you can upload or print.</p></div>{STATEMENT_EN}</section>",
    steps=[("Upload", "A clear photo or scan on the <a href=\"/contact/?service=Certified+translation+(UK)\">quote form</a>."),
           ("Quote", "A fixed price and a delivery date."),
           ("Translate", "Translated, then checked against the original by a second linguist."),
           ("Deliver", "Signed PDF by email.")],
    who="People in Glasgow and across Scotland applying to the Home Office, universities or employers, and the solicitors who help them.",
    faq=[("Will it be accepted by the Home Office?", "It includes the confirmation of accuracy, date, full name and signature, and contact details that the Home Office asks for. Read <a href=\"/insights/home-office-certified-translation/\">what the Home Office needs</a>."),
         ("Do Scottish courts accept it?", "Courts usually accept a certified translation. Some cases need a sworn affidavit or notarisation; your solicitor will know, and we can arrange it."),
         ("Can I drop the document off?", "Send a scan or photo; you keep your original.")],
)

PAGES["apostille"] = dict(
    title="Apostille and legalisation for UK documents | Kayonne Language",
    desc="How to use UK documents and translations abroad: what an apostille is, who issues it, when a translation needs notarising, and when embassy legalisation is needed.",
    label="Kayonne Language · Guide", h1="Apostille and legalisation, in plain words.",
    lede="If a UK document or translation will be used abroad, the receiving country may want proof that the signature or stamp on it is genuine. That proof is usually an apostille.",
    body="""<article class="prose">
<h2>What an apostille is</h2>
<p>An apostille is a certificate attached to a public document that confirms the signature, seal or stamp on it is genuine. In the UK, apostilles are issued by the Legalisation Office of the Foreign, Commonwealth and Development Office (FCDO).</p>
<h2>Which countries accept it</h2>
<p>Countries that have joined the Hague Apostille Convention accept an apostille without further steps. Countries outside the Convention may also ask for the document to be legalised by their embassy or consulate.</p>
<h2>Where translation comes in</h2>
<p>An apostille confirms a signature, not a translation. If the receiving country needs a translation, it may ask for the translation to be certified and then notarised by a UK solicitor or notary public, so that the apostille can be attached to the notary's signature.</p>
<h2>A typical order of steps</h2>
<ol><li>Ask the receiving authority exactly what it needs.</li><li>Get the translation certified.</li><li>Have it notarised if required.</li><li>Get the apostille from the FCDO.</li><li>Legalise at the embassy if the country is outside the Convention.</li></ol>
<p>We can produce the certified translation and arrange the notary and apostille steps through partners. The quote lists each step and who does it.</p>
<p class="note">Rules and fees change. Check the current guidance on gov.uk before you apply.</p>
</article>""",
)

PAGES["multilingual-seo"] = svc(
    title="Multilingual SEO agency | Kayonne Global",
    desc="Multilingual and international SEO: keyword research by native speakers in each market, hreflang, translated metadata and locale URLs, from a team that builds and translates.",
    label="Multilingual SEO", h1="Found in every language you sell in.",
    lede="People in Germany don't search for what people in Glasgow search for, even when they want the same thing. We research search terms in each market with native speakers, then build the pages to match.",
    why=["Keyword research by native speakers, not translated keywords", "The same team fixes the code, writes the pages and translates them", "Reports per market from Search Console"],
    incl=["International keyword research", "Hreflang and language folders", "Translated titles, descriptions and URLs", "Local content briefs", "Technical audits for multilingual sites", "Market-by-market reporting"],
    steps=[("Markets", "Which countries, which languages, which pages first."),
           ("Research", "Native speakers research what people actually type."),
           ("Build", "Folders, hreflang, metadata and internal links."),
           ("Report", "Search Console per market, every month.")],
    who="Businesses already selling in the UK that want to be found in Germany, Europe or Asia.",
    faq=[("Can't we just translate our keywords?", "Usually not. See <a href=\"/insights/multilingual-seo-keywords/\">why translated keywords fail</a>."),
         ("Do you guarantee rankings?", "No one can. We fix what we control and report on it.")],
)

PAGES["international-launch"] = svc(
    title="International website launch | Kayonne Global",
    desc="Take your website into a new market with one team: audit, keyword research, build, translation, checks and launch, managed from Glasgow.",
    label="International launch", h1="Your next market, launched by one team.",
    lede="A fixed plan to take your site or shop into a new language: the build team prepares the site, the translation team writes it in the new language, and one project lead runs both.",
    why=["One project lead instead of an agency plus a translator", "Search terms researched before a word is translated", "Every page checked on a phone in every language"],
    incl=["Readiness audit", "Market keyword research", "Language folders, hreflang and local formats", "Translation and second-linguist revision", "Legal page checks such as an Impressum for Germany", "Launch report and 30-day review"],
    steps=[("Plan", "Markets, pages and launch date agreed in writing."),
           ("Prepare", "The site is made translation-ready."),
           ("Localise", "Translation, revision and in-context checks."),
           ("Launch", "Go live, submit sitemaps, review after 30 days.")],
    who="UK businesses entering Germany, Europe or Asia for the first time.",
    faq=[("How long does a launch take?", "It depends on the number of pages and languages. The quote gives a date for each stage."),
         ("Do you need access to our site?", "Yes, or to your developer. Accounts stay in your name.")],
)

PAGES["ecommerce-localisation"] = svc(
    title="Shopify and WooCommerce store localisation | Kayonne Global",
    desc="Translate and localise your Shopify or WooCommerce store: products, checkout, emails, currency and SEO, with human translation and a second-linguist check.",
    label="Shop localisation", h1="Your shop, open in another language.",
    lede="We localise Shopify and WooCommerce stores end to end: product pages, collections, checkout, order emails, currency and the search terms people use to find you.",
    why=["Products, checkout and emails all translated, not just the home page", "Prices, currency and formats set per market", "Product titles researched for search in each market"],
    incl=["Shopify Markets setup", "WooCommerce with WPML or Polylang", "Product and collection translation", "Checkout and email templates", "Currency, tax display and formats", "Multilingual SEO for products"],
    steps=[("Review", "We check your theme, apps and catalogue size."),
           ("Set up", "Markets, languages, currencies and URLs."),
           ("Translate", "Products first, then pages, checkout and emails."),
           ("Test", "A test order in every language before launch.")],
    who="Online shops ready to sell in Germany, France, Spain or further afield.",
    faq=[("Do you translate thousands of products?", "Yes. Large catalogues can use machine translation with human post-editing on your best sellers."),
         ("Will it slow the shop down?", "No. We check speed before and after.")],
)

# ---------- language pair pages ----------
LANG_PAIRS = {
    "polish": dict(name="Polish", native="Polski",
        note="Names and places keep their Polish letters (ą, ć, ę, ł, ń, ó, ś, ź, ż) exactly as on the original, so they match passports and records.",
        docs=["Birth certificates (odpis aktu urodzenia)", "Marriage certificates", "Driving licences", "School and university certificates", "Police certificates"]),
    "romanian": dict(name="Romanian", native="Română",
        note="We keep ș and ț in names exactly as written, and translate stamps and handwritten notes on civil status certificates.",
        docs=["Birth certificates (certificat de naștere)", "Marriage certificates", "Criminal record certificates", "Diplomas and transcripts", "Bank statements"]),
    "arabic": dict(name="Arabic", native="العربية",
        note="Arabic reads right to left and some documents use Hijri dates. We give the Gregorian date where the reader needs it and spell names to match the passport.",
        docs=["Birth and marriage certificates", "Family registers", "Degrees and transcripts", "Court papers", "Medical reports"]),
    "urdu": dict(name="Urdu", native="اردو",
        note="Urdu is written right to left in Nastaliq script. Names can be spelled differently across documents, so tell us the spelling on your passport and we will use it throughout.",
        docs=["Birth certificates (NADRA)", "Marriage certificates (nikah nama)", "Family registration certificates", "Educational certificates", "Bank statements"]),
    "chinese": dict(name="Chinese", native="中文",
        note="Simplified Chinese is used in mainland China and Singapore, Traditional in Hong Kong and Taiwan. Chinese names put the family name first; we keep the order used on the passport.",
        docs=["Household registers (hukou)", "Notarial certificates", "Degree certificates and transcripts", "Business licences", "Bank statements"]),
    "spanish": dict(name="Spanish", native="Español",
        note="Spain and Latin America differ in vocabulary and formats, so tell us the country. Spanish documents often show two surnames, and we keep both.",
        docs=["Birth certificates (partida de nacimiento)", "Marriage certificates", "Academic records", "Contracts", "Medical reports"]),
    "french": dict(name="French", native="Français",
        note="French from France, Belgium, Switzerland, Canada and Africa differs in terms and formats. We follow the country of the document or its reader.",
        docs=["Birth certificates (acte de naissance)", "Marriage certificates", "Diplomas", "Contracts", "Company documents"]),
    "german": dict(name="German", native="Deutsch",
        note="Swiss documents use ss instead of ß. For German authorities that need a sworn translation (beglaubigte Übersetzung), we arrange an authorised partner.",
        docs=["Birth certificates (Geburtsurkunde)", "Marriage certificates", "Certificates of good conduct", "Degrees and transcripts", "Employment references"]),
    "ukrainian": dict(name="Ukrainian", native="Українська",
        note="Names are transliterated exactly as in the Ukrainian passport so every document matches. We also translate Russian-language documents issued in Ukraine.",
        docs=["Birth certificates", "Marriage certificates", "Diplomas and transcripts", "Driving licences", "Medical records"]),
    "portuguese": dict(name="Portuguese", native="Português",
        note="Portuguese from Portugal and from Brazil differ in spelling and terms, so tell us which. Long Portuguese and Brazilian names are kept in full.",
        docs=["Birth certificates (certidão de nascimento)", "Marriage certificates", "Diplomas", "Criminal record certificates", "Bank statements"]),
}

for _slug, _l in LANG_PAIRS.items():
    PAGES[f"languages/{_slug}"] = svc(
        title=f"{_l['name']} translation services UK | {_l['name']} to English | Kayonne",
        desc=f"Certified and professional {_l['name']} translation, into and out of English: documents for the Home Office, legal, medical and business texts, websites and subtitles.",
        label=f"{_l['name']} · <span lang=\"und\">{_l['native']}</span>", h1=f"{_l['name']} translation, into and out of English.",
        lede=f"Qualified {_l['name']} translators for certified documents, legal and medical texts, business content, websites and subtitles. Every job checked by a second linguist.",
        why=[_l["note"], "Certified translations with the statement the Home Office asks for", "A second linguist checks every job"],
        incl=[f"{_l['name']} to English certified translation", f"English to {_l['name']} translation"] + _l["docs"],
        steps=[("Upload", "Send a photo, scan or file on the quote form."),
               ("Quote", "A fixed price and a date."),
               ("Translate", f"A native {_l['name']} translator works on it."),
               ("Check", "A second linguist revises before delivery.")],
        who=f"People and businesses who need {_l['name']} documents in English, or English content in {_l['name']}.",
        faq=[(f"Do you provide certified {_l['name']} translations?", f"Yes. Certified {_l['name']} to English translations come with a signed statement of accuracy. See <a href=\"/certified-translation/\">certified translation</a>."),
             ("How do I get a price?", f"Upload the document on the <a href=\"/contact/\">quote form</a> and choose {_l['name']} as the language.")],
    )

# ---------- articles ----------
PAGES["insights/home-office-certified-translation"] = dict(
    title="What the Home Office needs from a certified translation | Kayonne",
    desc="What a certified translation for a UK visa or settlement application must include, common mistakes that cause problems, and an example statement.",
    label="Insights · Certified translation", h1="What the Home Office needs from a certified translation",
    lede="If a document for your visa, settlement or citizenship application is not in English or Welsh, you need a translation that the Home Office can check. Here is what it should include.",
    body="""<article class="prose">
<p class="byline">By the Kayonne Language team, led by a CIOL-qualified translator.</p>
<h2>The short answer</h2>
<p>Home Office guidance asks for a translation that includes: confirmation from the translator that it is an accurate translation of the original document, the date of the translation, the translator's full name and signature, and the translator's contact details.</p>
<h2>Who can translate it</h2>
<p>The UK has no sworn translators, so a professional translator or translation company certifies the translation. You cannot translate and certify your own documents.</p>
<h2>Mistakes that cause delays</h2>
<ul><li><b>Names spelled differently</b> from the passport. Give your translator the passport spelling.</li><li><b>Stamps and handwriting left out.</b> Everything on the page should be translated or described.</li><li><b>Missing pages</b>, including the back of a certificate.</li><li><b>No contact details</b>, so the translation cannot be verified.</li></ul>
<h2>An example statement</h2>
""" + STATEMENT_EN + """
<h2>How we handle it</h2>
<p>We translate the full document, keep the layout close to the original, check names against your passport, and have a second linguist review it. You receive a signed PDF. See <a href="/certified-translation/">certified translation</a>.</p>
<p class="note">Guidance can change. Check the current requirements on gov.uk for your application.</p>
</article>""",
)

PAGES["insights/website-cost-glasgow"] = dict(
    title="How much does a website cost in Glasgow in 2026? | Kayonne",
    desc="Website prices in Glasgow in 2026: templates, small business sites, custom builds and shops, what changes the price, and the running costs people forget.",
    label="Insights · Websites", h1="How much does a website cost in Glasgow in 2026?",
    lede="Prices for a website in Glasgow range from a few hundred pounds to well over ten thousand. Here is what you get at each level and what moves the price.",
    body="""<article class="prose">
<p class="byline">By the Kayonne Digital team.</p>
<h2>Typical ranges we found</h2>
<div class="table-wrap"><table><thead><tr><th scope="col">Type</th><th scope="col">Typical Glasgow price</th></tr></thead><tbody>
<tr><td>Template site</td><td class="n">from about £300</td></tr>
<tr><td>Small business site, up to 5 pages</td><td class="n">about £400 to £1,500</td></tr>
<tr><td>Custom design from a studio</td><td class="n">usually from £2,000 to £5,000</td></tr>
<tr><td>Larger builds and shops</td><td class="n">£5,000 to £10,000 and up</td></tr>
<tr><td>Pay-monthly sites</td><td class="n">about £25 to £50 a month</td></tr>
</tbody></table></div>
<p class="note">Based on prices Glasgow studios published in 2026. Check current prices with each studio.</p>
<h2>What changes the price</h2>
<ul><li>Number of pages and how much writing you need.</li><li>A shop: products, payments and delivery rules.</li><li>Custom design versus a template.</li><li>Bookings, logins or integrations with other software.</li><li>More than one language.</li></ul>
<h2>Running costs people forget</h2>
<ul><li>Domain renewal every year.</li><li>Hosting.</li><li>Business email, such as Google Workspace or Microsoft 365, per user per month.</li><li>Updates and backups, either your time or a care plan.</li></ul>
<h2>How we price</h2>
<p>Every site gets a fixed written quote after a short brief. See <a href="/pricing/">pricing</a> or <a href="/website-check/">get a free check</a> of your current site first.</p>
</article>""",
)

PAGES["insights/multilingual-seo-keywords"] = dict(
    title="Multilingual SEO: why you can't just translate your keywords | Kayonne",
    desc="Why translated keywords fail in international SEO, with examples, and how to research search terms in each market properly.",
    label="Insights · Multilingual SEO", h1="Multilingual SEO: why you can't just translate your keywords",
    lede="A keyword that brings you customers in the UK can bring nobody in Germany once it is translated word for word. Here is why, and what to do instead.",
    body="""<article class="prose">
<p class="byline">By the Kayonne Global team.</p>
<h2>People search in their own words</h2>
<p>A British shopper looks for <i>trainers</i>, an American for <i>sneakers</i>. In Germany a mobile phone is a <i>Handy</i>, a word a dictionary would never give you. A direct translation is often correct and still not what anyone types.</p>
<h2>The same intent, different searches</h2>
<p>Even when the meaning lines up, search habits differ: some markets use shorter queries, some add the city, some search in English for technical products. Each market needs its own research.</p>
<h2>How to do it properly</h2>
<ol><li>List the pages that sell, not every page.</li><li>Have a native speaker research what people search for in that market.</li><li>Check search intent: does the term bring buyers or students?</li><li>Write titles, headings and URLs around those terms.</li><li>Add hreflang so each market sees the right version.</li><li>Track each market separately in Search Console.</li></ol>
<p>That is how we run <a href="/multilingual-seo/">multilingual SEO</a>.</p>
</article>""",
)
