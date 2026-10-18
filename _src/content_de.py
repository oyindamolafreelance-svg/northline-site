"""German page content. Same keys as content_en.PAGES. Strings may contain HTML."""
from content_en import DEMO_BODY, DEMO_STRINGS, EMAIL, demo_script, quote_form, shot, video  # noqa: F401

LOC_VIDEO = video("localisation", "Eine Produktkarte auf Englisch, Deutsch, Japanisch und Arabisch. Wörter, Datum, Währung und Leserichtung ändern sich.", 1100, 482, "Video zur Lokalisierungsdemo")
REEL = video("showreel", "Die 3D-Szenen dieser Website, eine für jede Leistung.", 1280, 720, "Showreel der 3D-Szenen dieser Website")

EUROPE = ["Deutsch", "Deutsch (Schweiz)", "Niederländisch", "Französisch", "Spanisch", "Italienisch", "Portugiesisch",
          "Polnisch", "Schwedisch", "Dänisch", "Norwegisch", "Finnisch", "Tschechisch", "Slowakisch", "Ungarisch",
          "Rumänisch", "Griechisch", "Bulgarisch", "Kroatisch", "Serbisch", "Slowenisch", "Ukrainisch", "Estnisch",
          "Lettisch", "Litauisch", "Katalanisch", "Türkisch"]
ASIA = ["Japanisch", "Chinesisch (vereinfacht)", "Chinesisch (traditionell)", "Kantonesisch", "Koreanisch", "Hindi",
        "Bengalisch", "Tamil", "Telugu", "Urdu", "Panjabi", "Thai", "Vietnamesisch", "Indonesisch", "Malaiisch",
        "Tagalog", "Birmanisch", "Khmer", "Laotisch", "Nepali"]


def wall(items):
    return '<ul class="lang-wall">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


LANG_WALLS = (f"<h3>Europa</h3>{wall(EUROPE)}<h3>Asien</h3>{wall(ASIA)}"
              '<p class="note">Arabisch und Persisch auf Anfrage. Alle Sprachen übersetzen wir aus dem Englischen und ins '
              "Englische.</p>")

DIGITAL_CARDS = [
    ("websites", "Websites", "Unternehmensseiten, Onlineshops und Landingpages."),
    ("web-apps", "Web-Apps", "Individuelle Anwendungen und Progressive Web Apps."),
    ("mobile-apps", "Mobile Apps", "iOS und Android, bis zum Store-Eintrag."),
    ("domains-email", "Domains und geschäftliche E-Mail", "Domain, Postfach und DNS richtig eingerichtet."),
    ("seo", "SEO", "Technische, lokale und mehrsprachige Suchmaschinenoptimierung."),
    ("speed", "Ladezeit und Barrierefreiheit", "Core Web Vitals und WCAG 2.2 AA, mit Bericht."),
    ("care", "Wartungspläne", "Updates, Backups und jemand, der aufpasst."),
]
LANGUAGE_CARDS = [
    ("documents", "Dokumentübersetzung", "Urkunden, Abschlüsse und Handbücher, im Layout des Originals."),
    ("localization", "Website- und App-Lokalisierung", "Ihr Produkt in der Sprache Ihrer Kunden."),
    ("games", "Spielelokalisierung", "Strings, Store-Seiten und Untertitel, im Kontext geprüft."),
    ("medical", "Medizinische Übersetzung", "Texte aus Medizin und Life Sciences, mit NDA."),
    ("patents", "Patentübersetzung", "Einheitliche Ansprüche über die ganze Patentfamilie."),
    ("legal", "Juristische Übersetzung", "Verträge und Schriftsätze, die Ihre Anwälte prüfen können."),
    ("subtitling", "Untertitelung und Transkription", "Getimt, lesbar und im gewünschten Format."),
    ("proofreading", "Korrektorat und Revision", "Eine zweite Fachkraft prüft Ihre vorhandene Übersetzung."),
    ("quality", "MTPE und Qualitätsprüfung", "Post-Editing, LQA und Terminologiepflege."),
]


def cards(items):
    return '<ul class="grid-3 link-cards">' + "".join(
        f'<li><a class="card" href="/de/{s}/"><strong>{n}</strong><span class="note">{d}</span></a></li>'
        for s, n, d in items) + "</ul>"


def svc(**kw):
    kw["kind"] = "service"
    return kw


PAGES = {}

PAGES[""] = dict(
    title="Kayonne Creatives | Websites und Übersetzungen aus Glasgow",
    desc="Agentur in Glasgow für Websites, Apps und Übersetzungen. Wir bauen Ihre Website, und professionelle Übersetzer "
         "bringen sie in europäische und asiatische Sprachen. Einzeln oder zusammen buchbar.",
    body=f"""
<section class="hero" data-scene="hero">
  <div>
    <p class="kicker">Glasgow · weltweit</p>
    <h1>Wir bauen es. Dann bringen wir es in jeden Markt.</h1>
    <p class="lede">Kayonne Creatives ist eine Digital- und Sprachagentur in Glasgow. Wir entwickeln Websites und Apps, und professionelle Übersetzer bringen sie in europäische und asiatische Sprachen. Sie buchen die Entwicklung, die Übersetzung oder beides.</p>
    <p class="actions"><a class="btn magnetic" href="/de/digital/">Website bauen</a> <a class="btn magnetic" href="/de/language/">Dokument übersetzen</a> <a class="btn ghost magnetic" href="/de/global/">Ins Ausland starten</a></p>
  </div>
  <div class="orbit" aria-hidden="true"><div class="ring"><span>ä</span><span>あ</span><span>中</span><span>é</span><span>ø</span></div></div>
</section>
<section data-scene="shards"><ul class="grid-4 creds">
  <li class="card note">MA in Translation Studies, Middlebury Institute in Monterey</li>
  <li class="card note">CIOL Diploma in Translation, mit Auszeichnung (Merit)</li>
  <li class="card note">Professionelle Übersetzer in Europa und Asien</li>
  <li class="card note">Abläufe nach ISO 17100, wenn ein Auftrag es verlangt</li>
</ul></section>
<section class="teams" data-scene="windows" aria-label="Unsere zwei Teams">
  <a class="team team-d" href="/de/digital/">
    <p class="kicker">Kayonne Digital</p>
    <h2>Das Entwicklungsteam</h2>
    <p>Websites, Onlineshops und Apps, Domain und E-Mail dahinter und die SEO, die für Auffindbarkeit sorgt.</p>
    <ul class="ticks"><li>Websites und Shops</li><li>Web- und Mobile-Apps</li><li>Domains und geschäftliche E-Mail</li><li>SEO, Ladezeit und Wartung</li></ul>
    <span class="team-more">Zum Entwicklungsteam →</span>
  </a>
  <a class="team team-l" href="/de/language/">
    <p class="kicker">Kayonne Language</p>
    <h2>Das Übersetzungsteam</h2>
    <p>Qualifizierte Übersetzer für Recht, Medizin, Patente und Geschäftstexte, Dokumente, Untertitel und Korrektorat, mit zweiter Prüfung bei jedem Auftrag.</p>
    <ul class="ticks"><li>Dokumente im Layout des Originals</li><li>Recht, Medizin, Patente</li><li>Untertitelung und Transkription</li><li>Korrektorat und Revision</li></ul>
    <span class="team-more">Zum Übersetzungsteam →</span>
  </a>
</section>
<section class="global-band card" data-scene="globe">
  <div>
    <p class="kicker">Kayonne Global</p>
    <h2>Beide Teams. Ein Marktstart.</h2>
    <p>Die meisten Anbieter bauen die Website oder übersetzen sie. Wir machen beides im selben Projekt, damit Ihre Website ohne Bruch für den nächsten Markt bereit ist.</p>
    <ol class="mini-steps"><li>Analyse</li><li>Recherche</li><li>Entwicklung</li><li>Übersetzung</li><li>Prüfung</li><li>Start</li></ol>
    <p class="actions"><a class="btn magnetic" href="/de/global/">So funktioniert es</a> <a class="btn ghost" href="/de/readiness-check/">Kostenloser Readiness-Check</a></p>
  </div>
  {LOC_VIDEO}
</section>
<section data-scene="network">
  <h2>Europa und Asien, mit einem Team.</h2>
  <p class="lede">Professionelle Übersetzer decken die folgenden Sprachen ab. Ihr Ansprechpartner ist eine Projektleitung in Glasgow.</p>
  {LANG_WALLS}
  <p><a class="btn ghost" href="/de/languages/">Alle Sprachen</a></p>
</section>
<section data-scene="path">
  <h2>So läuft ein Projekt</h2>
  <ol class="grid-4 steps">
    <li class="card"><h3>Briefing</h3><p class="note">Wir halten Auftrag, Sprachen und Termin schriftlich fest.</p></li>
    <li class="card"><h3>Umsetzung</h3><p class="note">Design, Entwicklung oder Übersetzung, und Sie können jederzeit prüfen.</p></li>
    <li class="card"><h3>Prüfung</h3><p class="note">Ein Ladezeitbericht für Websites, eine zweite Fachkraft für Übersetzungen.</p></li>
    <li class="card"><h3>Übergabe</h3><p class="note">Die Dateien gehören Ihnen. Laufende Betreuung ist optional.</p></li>
  </ol>
</section>""",
    faq=[
        ("Kann eine Agentur entwickeln und übersetzen?", "Ja. Sie können auch nur die Entwicklung oder nur die Übersetzung buchen."),
        ("Welche Sprachen übersetzen Sie?", "Europäische und asiatische Sprachen, aus dem und ins Englische. Siehe <a href=\"/de/languages/\">Sprachen</a>. Im Angebot steht, wer Ihr Sprachpaar übernimmt."),
        ("Wo sitzen Sie?", "In Glasgow, Vereinigtes Königreich. Unsere Kunden sitzen überall."),
    ],
)

PAGES["services"] = dict(
    title="Leistungen | Kayonne Creatives",
    desc="Websites, Apps, Domains und E-Mail, SEO, Übersetzung, Lokalisierung und Untertitelung aus einer Agentur in Glasgow.",
    label="Leistungen", h1="Zwei Säulen. Eine Agentur.",
    lede="Kayonne Creatives baut das Produkt und bereitet es in den europäischen und asiatischen Sprachen Ihrer Kunden auf. Professionelle Übersetzer übernehmen die Sprache. Sie buchen eine Säule oder beide.",
    body=f"<section><h2>Digital</h2>{cards(DIGITAL_CARDS)}</section><section><h2>Sprache</h2>{cards(LANGUAGE_CARDS)}</section>",
)

PAGES["websites"] = svc(
    title="Webdesign und Website-Entwicklung | Kayonne Creatives",
    desc="Unternehmenswebsites, Onlineshops, Landingpages und Relaunches. Klare Seiten, schnelle Ladezeiten und ein Ladezeitbericht vor dem Start.",
    label="Websites", h1="Websites, die Ihr Angebot erklären und halten.",
    lede="Wir gestalten und entwickeln Unternehmenswebsites, Onlineshops und Landingpages. Eine Website ist fertig, wenn sie klar, schnell und übergabebereit ist, nicht wenn sie nur fertig aussieht.",
    why=["Eine Struktur rund um Ihr Angebot", "Ein Design, das Ihr Team selbst pflegen kann", "Ladezeit und Barrierefreiheit vor dem Start geprüft"],
    incl=["Unternehmens- und Marketing-Websites", "Onlineshops (Shopify oder WooCommerce)", "Landingpages", "Relaunches und Umzüge von Wix oder Squarespace",
          "CMS-Einrichtung und Schulung", "Domain, Hosting und geschäftliche E-Mail", "Seitentexte auf Englisch und in weiteren Sprachen"],
    extra="""<section><h2>Pakete</h2><ul class="grid-4 link-cards plain-cards">
<li class="card"><strong>One-Pager</strong><span class="note">Eine Seite mit Angebot, Kontaktformular und Karte. Für einen Start oder für Selbstständige.</span></li>
<li class="card"><strong>Unternehmenswebsite</strong><span class="note">Fünf bis acht Seiten, auf Wunsch ein Blog, und lokale SEO.</span></li>
<li class="card"><strong>Onlineshop</strong><span class="note">Produkte, Zahlungen, Versandregeln und Bestellmails.</span></li>
<li class="card"><strong>Mehrsprachige Website</strong><span class="note">Jedes Paket in zwei oder mehr Sprachen, mit hreflang und übersetzten Suchbegriffen.</span></li>
</ul><p class="note">Jedes Paket wird nach einem kurzen Briefing angeboten. Sie zahlen nur die Seiten, die Sie brauchen.</p></section>""",
    steps=[("Briefing", "Wir legen Zielgruppe, Angebot und die nötigen Seiten fest."),
           ("Design", "Sie prüfen das Layout, bevor die Entwicklung beginnt."),
           ("Entwicklung", "Wir bauen die Website, die Formulare und das Inhaltsmodell."),
           ("Prüfung", "Jeder Start wird gegen die Core-Web-Vitals-Grenzwerte getestet. Sie erhalten den Bericht.")],
    who="Unternehmen und Selbstständige, die eine Website brauchen, die eine Leistung, ein Produkt oder einen Start verkauft.",
    faq=[("Können wir die Website selbst bearbeiten?", "Ja. Eine CMS-Schulung gehört zur Übergabe. Die Website gehört Ihnen."),
         ("Überarbeiten Sie bestehende Websites?", "Ja. Wir behalten Seiten, die bereits gut ranken, richten Weiterleitungen ein und ersetzen, was Ihren Kunden nicht hilft."),
         ("Wem gehört die Domain?", "Ihnen. Wir registrieren sie auf Ihren Namen oder binden Ihre bestehende ein. Siehe <a href=\"/de/domains-email/\">Domains und geschäftliche E-Mail</a>."),
         ("Wie lange dauert eine Website?", "Das hängt von der Seitenzahl ab und davon, wie weit die Inhalte vorbereitet sind. Im Angebot steht ein Termin.")],
)

PAGES["web-apps"] = svc(
    title="Individuelle Web-Apps | Kayonne Creatives",
    desc="Webanwendungen, Progressive Web Apps und Integrationen. Für den Zweck gebaut und mit dem Quellcode übergeben.",
    label="Web-Apps", h1="Web-Apps für den Zweck gebaut, nicht aus der Vorlage.",
    lede="Wir entwickeln individuelle Webanwendungen und Progressive Web Apps und verbinden sie mit den Tools, die Sie bereits nutzen.",
    why=["Ein Produkt, das Ihr Team betreiben kann", "Integrationen vor der Entwicklung festgelegt", "Der Code gehört Ihnen"],
    incl=["Individuelle Webanwendungen", "Progressive Web Apps", "API- und Drittanbieter-Integrationen", "Design der wichtigsten Ansichten", "Oberflächen, die für Übersetzung vorbereitet sind"],
    steps=[("Umfang", "Wir halten fest, was die erste Version können muss und was nicht."),
           ("Ansichten", "Sie geben die wichtigsten Abläufe frei, bevor programmiert wird."),
           ("Entwicklung", "Wir liefern in Etappen, die Sie durchklicken können."),
           ("Übergabe", "Repository, Zugänge und eine kurze Anleitung. Betreuung ist optional.")],
    who="Softwarefirmen, Agenturen und Betriebe, denen eine Tabelle oder ein Plugin nicht mehr reicht.",
    faq=[("Wem gehört der Code?", "Ihnen, sobald die vereinbarten Honorare bezahlt sind."),
         ("Lässt sich eine Web-App auf dem Handy installieren?", "Eine Progressive Web App ja. Eine Store-App ist eine eigene Leistung, siehe <a href=\"/de/mobile-apps/\">Mobile Apps</a>.")],
)

PAGES["mobile-apps"] = svc(
    title="App-Entwicklung für iOS und Android | Kayonne Creatives",
    desc="Apps für iOS und Android, von den ersten Ansichten bis zum Store-Eintrag. Lokalisierung von App und Store-Text aus demselben Team.",
    label="Mobile Apps", h1="Mobile Apps für iOS und Android.",
    lede="Wir gestalten und entwickeln mobile Apps und können danach die Oberfläche und den Store-Eintrag übersetzen. Ein Team, von der ersten Ansicht bis zur Sprache Ihres Markts.",
    why=["Ansichten für den Daumen, nicht für eine Desktop-Folie", "Store-Texte können mit der App übersetzt werden", "Sie sehen einen Test-Build vor der Einreichung"],
    incl=["iOS-Apps", "Android-Apps", "Interface-Design", "Store-Texte", "Übersetzung von App und Store-Eintrag"],
    steps=[("Umfang", "Wir benennen das erste Release und die nötigen Ansichten."),
           ("Design", "Sie prüfen die Abläufe im Smartphone-Format."),
           ("Entwicklung", "Sie installieren einen Test-Build."),
           ("Release", "Wir bereiten die Einreichung vor. Die Prüfzeiten bestimmen Apple und Google.")],
    who="Produktteams und Studios, die eine echte App brauchen, keine gestreckte Website.",
    faq=[("Veröffentlichen Sie unter unserem Konto?", "Ja. Die Store-Konten bleiben auf Ihren Namen."),
         ("Können Sie die App übersetzen?", "Ja. Strings, Screenshots und Store-Texte, siehe <a href=\"/de/localization/\">Lokalisierung</a>.")],
)

PAGES["domains-email"] = svc(
    title="Domain registrieren und geschäftliche E-Mail einrichten | Kayonne Creatives",
    desc="Domainregistrierung auf Ihren Namen, E-Mail mit Google Workspace oder Microsoft 365, SPF, DKIM und DMARC sowie Postfachumzug.",
    label="Domains und geschäftliche E-Mail", h1="Ihre Domain und Ihr Postfach, richtig eingerichtet.",
    lede="Wir registrieren Ihre Domain auf Ihren Namen, richten geschäftliche E-Mail-Adressen wie sie@ihrefirma.de ein und setzen die DNS-Einträge, die Ihre Mails aus dem Spamordner halten.",
    why=["Die Domain gehört Ihnen, nicht uns", "Mails von Ihrer Domain sind authentifiziert und landen im Posteingang", "Website, E-Mail und DNS arbeiten vom ersten Tag an zusammen"],
    incl=["Domainregistrierung und Verlängerungserinnerungen (.de, .com, .co.uk und mehr)", "Geschäftliche E-Mail mit Google Workspace oder Microsoft 365",
          "SPF-, DKIM- und DMARC-Einträge", "Umzug bestehender Postfächer und Kontakte", "Sammeladressen wie info@ und angebote@",
          "Verbindung der Domain mit Ihrer Website, mit HTTPS", "E-Mail-Signaturen"],
    steps=[("Bestand", "Wir sehen uns an, was Sie haben: Domain, Registrar, E-Mail und Website."),
           ("Registrierung", "Wir registrieren oder übertragen die Domain auf Ihren Namen."),
           ("Einrichtung", "Postfächer, DNS-Einträge und die Verbindung zur Website."),
           ("Test", "Wir senden Testmails an Gmail und Outlook und prüfen die Authentifizierung.")],
    who="Neue Unternehmen, Selbstständige und Firmen, die beruflich noch eine private Gmail- oder GMX-Adresse nutzen.",
    faq=[("Wer zahlt Google Workspace oder Microsoft 365?", "Sie zahlen direkt beim Anbieter, auf Ihr eigenes Konto. Wir richten alles ein und übergeben den Admin-Zugang."),
         ("Warum landen meine Mails im Spam?", "Meist fehlen SPF, DKIM oder DMARC oder sind falsch gesetzt. Gmail und Yahoo verlangen diese Einträge seit 2024 von Massenversendern, und sie helfen jedem Absender."),
         ("Können Sie uns von einem anderen Anbieter umziehen?", "Ja. Wir ziehen Postfächer und Kontakte um und planen den Wechsel so, dass keine Mail verloren geht."),
         ("Verwalten Sie unsere Domain?", "Nein. Die Domain ist auf Sie registriert. Wir brauchen nur Zugang, solange wir daran arbeiten.")],
)

PAGES["seo"] = svc(
    title="SEO-Agentur für mehrsprachige Websites | Kayonne Creatives",
    desc="Technische, On-Page-, lokale und mehrsprachige SEO. Suchmaschinenoptimierung gehört in die Entwicklung, nicht ans Ende.",
    label="SEO", h1="Suchmaschinenoptimierung, die zur Seite passt.",
    lede="Wir übernehmen technische SEO, On-Page-SEO, lokale SEO und mehrsprachige SEO. Inhalte werden für die tatsächliche Suche geschrieben, nicht am Ende angehängt.",
    why=["Eine Website, die Suchmaschinen lesen können", "Sprachversionen mit hreflang und eigenen URLs", "Empfehlungen, die Sie in der Search Console selbst prüfen können"],
    incl=["Technische SEO", "On-Page-SEO", "Lokale SEO, inklusive Google-Unternehmensprofil", "Mehrsprachige SEO mit hreflang und Sprach-URLs",
          "Keyword-Recherche in jeder Zielsprache", "SEO-Texte", "Conversion-Optimierung wichtiger Seiten"],
    steps=[("Analyse", "Wir prüfen die Website, die Suchbegriffe und die Zielmärkte."),
           ("Plan", "Sie geben Seiten und Sprachstruktur frei."),
           ("Umsetzung", "Titel, Links, Ladezeit und Sprach-Tags werden im Code korrigiert."),
           ("Bericht", "Wir zeigen, was sich geändert hat. Rankings garantieren wir nie.")],
    who="Unternehmen, die in mehr als einer Stadt oder in mehr als einer Sprache gefunden werden müssen.",
    faq=[("Garantieren Sie ein Ranking?", "Nein. Wir beheben, was wir beeinflussen können, und berichten darüber. Eine Position kann niemand verkaufen."),
         ("Ist mehrsprachige SEO nur Übersetzung?", "Nein. Jede Sprache braucht eigene Suchbegriffe, Titel und URLs."),
         ("Richten Sie das Google-Unternehmensprofil ein?", "Ja, auf Wunsch auch Bing Places und Apple Business Connect.")],
)

PAGES["speed"] = svc(
    title="Ladezeit und Barrierefreiheit prüfen | Kayonne Creatives",
    desc="Audits zu Core Web Vitals und WCAG 2.2 AA mit schriftlichem Bericht. Wir testen gegen die veröffentlichten Grenzwerte.",
    label="Ladezeit und Barrierefreiheit", h1="Ladezeit und Barrierefreiheit, mit Bericht.",
    lede="Wir testen jeden Start gegen die Core-Web-Vitals-Grenzwerte und gegen WCAG 2.2 AA. Sie erhalten den Bericht. Eine erfundene Punktzahl von 100 gibt es bei uns nicht.",
    why=["Ein nachvollziehbarer Bericht statt eines Slogans", "Korrekturen für Seitengewicht, Bilder und Layoutverschiebungen", "Barrieren benannt und behoben"],
    incl=["Core-Web-Vitals-Tests", "Ladezeit-Optimierung", "Barrierefreiheits-Audits und Korrekturen", "Prüfung von Bild- und Codegewicht"],
    steps=[("Messen", "Wir testen auf Smartphone und Desktop und sichern die Messdaten."),
           ("Beheben", "Wir ändern, was den Grenzwert verfehlt."),
           ("Erneut testen", "Sie sehen den Vorher-nachher-Vergleich."),
           ("Übergabe", "Der Bericht bleibt bei Ihnen.")],
    who="Teams, deren Website gut aussieht, sich aber langsam anfühlt, oder die einen Barrierefreiheitsstandard erfüllen müssen.",
    faq=[("Welche Punktzahl versprechen Sie?", "Keine von 100. Wir testen gegen die veröffentlichten Core-Web-Vitals-Grenzwerte und teilen den Bericht."),
         ("Welcher Standard für Barrierefreiheit?", "WCAG 2.2 AA für die Seiten im Auftrag."),
         ("Gibt es ein Beispiel?", "Ja. <a href=\"/de/studio/\">Diese Website</a> ist unser eigenes Beispiel.")],
)

PAGES["care"] = svc(
    title="Website-Wartung und Betreuung | Kayonne Creatives",
    desc="Website-Wartung, Sicherheitsupdates, Backups, Verfügbarkeitsprüfung und Analytics. Ein monatlicher Wartungsplan hält die Website in Betrieb.",
    label="Wartungspläne", h1="Wartungspläne, damit die Website weiter funktioniert.",
    lede="Eine Website braucht Updates, Backups und jemanden, der prüft, ob sie erreichbar ist. Die Betreuung ist ein monatlicher Plan. Hosting, Domain und Analytics können Sie auch einzeln buchen.",
    why=["Updates nach Plan", "Eine feste Ansprechperson, wenn etwas ausfällt", "Domain und Code bleiben Ihr Eigentum"],
    incl=["Website-Wartung", "Sicherheitsupdates", "Backups", "Verfügbarkeitsprüfung", "Verwaltung von Hosting und Domain", "Einrichtung von Analytics",
          "Kleine Textänderungen", "Übersetzung neuer Seiten bei mehrsprachigen Websites"],
    steps=[("Zugang", "Wir listen auf, was wir brauchen. Die Konten bleiben auf Ihren Namen."),
           ("Ausgangslage", "Wir dokumentieren Ladezeit, Formulare und Backups."),
           ("Routine", "Updates folgen dem gewählten Plan."),
           ("Bericht", "Sie erhalten monatlich eine kurze Notiz, was sich geändert hat.")],
    who="Inhaber, die nicht selbst merken wollen, dass das Kontaktformular nicht mehr funktioniert.",
    faq=[("Verwalten Sie unsere Domain?", "Nein. Domain und Code bleiben auf Ihren Namen."),
         ("Können wir kündigen?", "Ja. Die Kündigungsfrist steht in Ihrem Plan, und Sie behalten alles."),
         ("Betreuen Sie auch Websites, die Sie nicht gebaut haben?", "Ja, nach einer kurzen Prüfung von Aufbau und Hosting.")],
)

PAGES["documents"] = svc(
    title="Dokumentübersetzung | Kayonne Creatives",
    desc="Übersetzung von Urkunden, Zeugnissen, Handbüchern und Berichten im Layout des Originals, in europäischen und asiatischen Sprachen.",
    label="Dokumentübersetzung", h1="Dokumente übersetzt und im Layout des Originals.",
    lede="Wir übersetzen Dokumente und gestalten das Ergebnis so, dass es wie das Original aussieht, mit Stempeln, Tabellen und Handschrift an Ort und Stelle übersetzt.",
    why=["Klarer Umgang mit Stempeln, Tabellen und Scans", "Bestätigungen nur, wo sie zutreffen", "Desktop-Publishing, wenn das Layout zählt, auch für asiatische Schriften"],
    incl=["Dokumentübersetzung", "Geburts- und Heiratsurkunden",
          "Führerscheine", "Zeugnisse und Notenübersichten", "Geschäftsberichte und Bilanzen", "Technische Handbücher",
          "Mehrsprachiges Desktop-Publishing", "Übersetzung, Lektorat und Korrektorat"],
    steps=[("Datei", "Laden Sie einen Scan oder die Originaldatei über das Formular hoch. Für sehr vertrauliche Dateien senden wir Ihnen einen privaten Upload-Link."),
           ("Zweck", "Sagen Sie uns, wer das Dokument liest und wie das Layout aussehen soll."),
           ("Arbeit", "Übersetzung, Lektorat, dann eine Schlussprüfung."),
           ("Lieferung", "Sie erhalten das vereinbarte Dateiformat.")],
    who="Privatpersonen und Unternehmen, die Urkunden, Abschlüsse oder Handbücher in einer anderen Sprache brauchen.",
    faq=[
         ("Welche Dateiformate nehmen Sie an?", "Word, Excel, PowerPoint, PDF, InDesign sowie Fotos oder Scans. Fragen Sie bei anderen Formaten nach."),
         ("Übersetzen Sie ins Englische?", "Ja. Die meisten Dokumente übersetzen wir ins Englische, aus allen Sprachen, die wir anbieten.")],
)

PAGES["localization"] = svc(
    title="Website- und App-Lokalisierung | Kayonne Creatives",
    desc="Lokalisierung von Websites, Software und App-Store-Einträgen in europäische und asiatische Sprachen. Glossar, Übersetzung im Kontext, Layoutprüfung und SEO.",
    label="Website- und App-Lokalisierung", h1="Dasselbe Produkt, in ihrer Sprache.",
    lede="Wir lokalisieren Websites, Software-Oberflächen und Store-Einträge. Zuerst wird das Glossar abgestimmt, und ein Mensch prüft alles, was veröffentlicht wird.",
    why=["Layout geprüft, wenn der Text länger wird", "Suchbegriffe in der Zielsprache recherchiert", "Ein Angebot auf Basis einer URL oder Datei"],
    incl=["Website-Übersetzung", "App- und Software-Lokalisierung", "Lokalisierung von Store-Einträgen", "Transkreation für Sätze, die sich nicht direkt übersetzen lassen",
          "Ein Glossar für Ihr Produkt", "Prüfung von Rechts-nach-links-Layouts für Arabisch und Persisch", "Übersetzung neuer Inhalte, sobald Sie sie veröffentlichen"],
    extra="""<section data-scene="film"><h2>Mehr als die Wörter</h2><p>Zur Lokalisierung gehören auch Datumsformate, Währungen, Zahlenformate, Adressen, Zahlungsarten und rechtliche Seiten. Deutsche Kunden erwarten zum Beispiel ein Impressum. <a href="/de/demo/">Sehen Sie, wie eine Seite die Sprache wechselt</a>.</p>""" + LOC_VIDEO + "</section>",
    steps=[("Dateien", "Senden Sie eine URL, eine String-Datei oder einen Seitenexport."),
           ("Begriffe", "Wir legen Namen, Tonalität und unveränderliche Begriffe fest."),
           ("Übersetzung", "Eine Fachkraft übersetzt im Kontext, dann folgt das Lektorat."),
           ("Anpassung", "Wir prüfen Längen, Links und Sprach-URLs.")],
    who="Softwarefirmen, Onlineshops und Agenturen, die ein Produkt in einen neuen Markt bringen.",
    faq=[("Übersetzen Sie nur die Wörter?", "Nein. Wir prüfen auch Schaltflächen, Metadaten und die Sprachstruktur der Website."),
         ("Können Sie anhand einer URL ein Angebot machen?", "Ja. Eine URL oder eine Datei genügt für den Start."),
         ("Mit welchen CMS arbeiten Sie?", "WordPress mit WPML oder Polylang, Shopify Markets, Webflow Localization sowie reines HTML oder String-Dateien. Fragen Sie bei anderen Systemen nach."),
         ("Was passiert, wenn wir später Seiten ergänzen?", "Neue Inhalte übersetzen wir laufend, im Rahmen eines <a href=\"/de/care/\">Wartungsplans</a> oder auf Anfrage.")],
)

PAGES["games"] = svc(
    title="Spielelokalisierung | Kayonne Creatives",
    desc="Lokalisierung von Spieltexten, Store-Einträgen und Untertiteln, mit Glossar und sprachlicher Prüfung im Build.",
    label="Spielelokalisierung", h1="Spiele, die auch in der nächsten Sprache Sinn ergeben.",
    lede="Wir lokalisieren Interface-Texte, Store-Einträge und Bildschirmtexte. Witze und Tutorial-Schritte übersetzen wir im Kontext, nicht Zeile für Zeile in einer leeren Tabelle.",
    why=["Ein Glossar vor dem Großteil der Arbeit", "Längenbegrenzungen eingehalten", "Sprachliche Prüfung im Build, wenn Sie einen bereitstellen"],
    incl=["Interface-Strings", "Store-Texte", "Untertiteldateien", "Stilhinweise zur Tonalität"],
    steps=[("Paket", "Strings, Längenlimits und jeder Build, den wir sehen dürfen."),
           ("Leitfaden", "Namen, Tonalität und verbotene Begriffe."),
           ("Übersetzung", "Übersetzung, dann Lektorat."),
           ("Spielen", "Sprachliche Prüfung im Kontext, sobald ein Build verfügbar ist.")],
    who="Spielestudios und Publisher, die eine neue Sprache vorbereiten.",
    faq=[("Nehmen Sie Sprachaufnahmen auf?", "Wir koordinieren Voice-over mit einem Tonstudio als Partner. Ein eigenes Studio betreiben wir nicht."),
         ("Spielen Sie das Spiel?", "Wenn Sie einen Build teilen, ja. Kontext verhindert falsche Zeilenumbrüche.")],
)

PAGES["medical"] = svc(
    title="Medizinische Fachübersetzung | Kayonne Creatives",
    desc="Übersetzungen für Medizin und Life Sciences mit abgestimmter Terminologie, zweiter Prüfung und NDA vor dem Dateiaustausch.",
    label="Medizinische Übersetzung", h1="Medizinische Übersetzung für Leser, die nicht raten dürfen.",
    lede="Wir übersetzen Texte aus Medizin und Life Sciences für Unternehmen, die Genauigkeit und einen sorgfältigen Ablauf brauchen. Vor dem Dateiaustausch unterzeichnen wir auf Wunsch eine Geheimhaltungsvereinbarung.",
    why=["Terminologie vor dem Großteil der Arbeit abgestimmt", "Eine zweite Prüfung im vereinbarten Umfang", "Vertrauliche Bearbeitung, auf Wunsch mit NDA"],
    incl=["Klinische und regulatorische Dokumente", "Texte für Patientinnen und Patienten", "Gebrauchsanweisungen und Beipackzettel für Medizinprodukte", "Life-Sciences-Marketing, das korrekt bleiben muss", "Glossarerstellung"],
    steps=[("NDA", "Fordern Sie eine NDA an, bevor Sie vertrauliche Dateien senden."),
           ("Begriffe", "Wir legen Produktnamen und Einheiten fest."),
           ("Übersetzung", "Übersetzung, Lektorat und Schlussprüfung."),
           ("Rückfragen", "Unklare Stellen im Ausgangstext klären wir nach, statt zu raten.")],
    who="Unternehmen aus Medizin, Life Sciences und Medizintechnik sowie die Agenturen, die für sie arbeiten.",
    faq=[("Geben Sie medizinischen Rat?", "Nein. Wir übersetzen. Wenn Ihr Prozess es vorsieht, muss eine Ärztin oder ein Arzt Texte für Patienten freigeben."),
         ("Ist die Arbeit vertraulich?", "Ja. Nur die Personen im Auftrag haben Zugriff. Wir nutzen Ihre Dateien nicht zum Training öffentlicher KI-Modelle.")],
)

PAGES["patents"] = svc(
    title="Patentübersetzung | Kayonne Creatives",
    desc="Patentübersetzungen mit einheitlicher Terminologie über die gesamte Patentfamilie. Präzise Ansprüche und Rückfragen statt stiller Änderungen.",
    label="Patentübersetzung", h1="Patentübersetzung mit sauber geführten Ansprüchen.",
    lede="Wir übersetzen Patenttexte für Kanzleien, denen einheitliche Begriffe wichtig sind. Die Sprache der Ansprüche bleibt präzise und wird nie zu Werbetext geglättet.",
    why=["Begriffe über eine ganze Dokumentfamilie stabil", "Rückfragen statt stiller Änderungen", "NDA vor dem Versand der Patentschrift"],
    incl=["Patentschriften", "Patentansprüche", "Zusammenfassungen", "Amtsbescheide und zugehörige technische Korrespondenz"],
    steps=[("Familie", "Senden Sie zugehörige Dokumente, damit die Begriffe einheitlich bleiben."),
           ("Festlegung", "Wir bestätigen die Begriffe, die sich nicht ändern dürfen."),
           ("Übersetzung", "Fachübersetzung, dann Lektorat."),
           ("Prüfung", "Zahlen, Bezugszeichen und Reihenfolge der Ansprüche werden geprüft.")],
    who="Patentanwaltskanzleien und Patentabteilungen, die in einer anderen Sprache anmelden oder lesen.",
    faq=[("Sind Sie Patentanwälte?", "Nein. Wir übersetzen. Die Beratung zur Anmeldung bleibt bei Ihrer Kanzlei."),
         ("Können Sie sich an eine frühere Übersetzung anlehnen?", "Ja, wenn Sie sie uns geben. Genau dafür gibt es Glossar und Translation Memory.")],
)

PAGES["legal"] = svc(
    title="Juristische Fachübersetzung | Kayonne Creatives",
    desc="Übersetzung von Verträgen, Richtlinien und Gerichtsunterlagen. Nah am Ausgangstext, definierte Begriffe einheitlich, NDA auf Wunsch.",
    label="Juristische Übersetzung", h1="Juristische Übersetzung, die Ihre Anwälte prüfen können.",
    lede="Wir übersetzen juristische Dokumente. Wir geben keine Rechtsberatung und ersetzen nicht Ihre Kanzlei. Die Formulierung bleibt nah am Ausgangstext.",
    why=["Genaue Übersetzung statt Umformulierung", "Definierte Begriffe einheitlich", "NDA, bevor vertrauliche Unterlagen gesendet werden"],
    incl=["Verträge", "Richtlinien und AGB", "Gerichts- und Registerunterlagen", "Juristische Korrespondenz"],
    steps=[("Prüfer", "Sagen Sie uns, wer das Ergebnis prüfen muss."),
           ("Begriffe", "Wir listen die definierten Begriffe auf."),
           ("Übersetzung", "Übersetzung und Lektorat."),
           ("Rückgabe", "Rückfragen werden aufgelistet, nicht versteckt.")],
    who="Kanzleien, Rechtsabteilungen und Unternehmen mit grenzüberschreitenden Unterlagen.",
    faq=[("Ist das Rechtsberatung?", "Nein."),
         ("Behalten Sie die Formatierung bei?", "Ja. Klauselnummern, definierte Begriffe und Layout folgen dem Ausgangstext.")],
)

PAGES["subtitling"] = svc(
    title="Untertitelung und Transkription | Kayonne Creatives",
    desc="Untertitel, Captions und Transkription in europäischen und asiatischen Sprachen. SRT, WebVTT, EBU-STL und TTML, SDH und eingebrannte Untertitel.",
    label="Untertitelung und Transkription", h1="Text im Bild, getimt und lesbar.",
    lede="Wir untertiteln, erstellen Captions und transkribieren Audio und Video. Untertitel folgen der Lesegeschwindigkeit und Zeilenlänge aus Ihrem Styleguide oder einem Standard, den wir mit Ihnen vereinbaren.",
    why=["Lesegeschwindigkeit im Blick", "Sprecherkennzeichnung, wenn Sie sie brauchen", "Dateien, die Sie direkt in Ihren Editor importieren"],
    incl=["Übersetzte Untertitel", "Untertitel in der Originalsprache", "Untertitel für Hörgeschädigte (SDH)", "Audio- und Videotranskription, wörtlich oder geglättet",
          "Spotting und Timing", "Video mit eingebrannten Untertiteln", "Voice-over-Koordination über einen Partner", "Audio- und Datenannotation nach Ihren Richtlinien"],
    extra="""<section><h2>Dateiformate</h2><p>SRT, WebVTT, EBU-STL, TTML/DFXP, SBV sowie Transkripte in Word oder Excel. Fragen Sie, wenn Ihre Plattform ein anderes Format braucht.</p></section>""",
    steps=[("Medien", "Senden Sie die Datei oder einen Link und das Sprachpaar."),
           ("Regeln", "Zeichenlimits, Lesegeschwindigkeit, Tonalität und ob wörtlich transkribiert wird."),
           ("Timing", "Wir spotten das Video oder übersetzen Ihr bestehendes Template."),
           ("Sichtung", "Sprachliche Prüfung am Bild, sobald der Schnitt final ist.")],
    who="Studios, Schulungsteams, Creator und Produktteams mit Videos in mehr als einer Sprache.",
    faq=[("Wie wird der Preis berechnet?", "Pro Minute Video oder Audio. Sprachpaar, Sprechtempo und Lieferzeit beeinflussen den Preis."),
         ("Können Sie eine Sprecherin oder einen Sprecher buchen?", "Wir koordinieren das. Das Partnerstudio steht im Angebot.")],
)

PAGES["proofreading"] = svc(
    title="Korrektorat und Revision von Übersetzungen | Kayonne Creatives",
    desc="Korrektorat und zweisprachige Revision vorhandener Übersetzungen. Eine zweite Fachkraft prüft Richtigkeit, Terminologie und Sprache, mit Änderungsverfolgung.",
    label="Korrektorat und Revision", h1="Eine zweite Fachkraft prüft Ihre vorhandene Übersetzung.",
    lede="Sie haben eine Übersetzung von einer freien Übersetzerin, einem Kollegen oder einer Maschine und wollen sicher sein, dass sie stimmt. Wir prüfen sie und liefern die Änderungen nachverfolgbar, mit einer kurzen Zusammenfassung.",
    why=["Sie sehen genau, was geändert wurde und warum", "Fehler werden nach Art eingeordnet, nicht übergangen", "Der Prüfumfang wird vorher festgelegt"],
    incl=["Korrektorat: Die Übersetzung wird allein auf Rechtschreibung, Grammatik, Zeichensetzung und Stil gelesen",
          "Revision: Die Übersetzung wird mit dem Ausgangstext auf Sinn, Auslassungen und Terminologie abgeglichen",
          "Überarbeitung maschineller Übersetzungen", "Prüfung von Websites und Apps im Browser oder im Test-Build",
          "Änderungen in Word, Kommentare im PDF oder Bearbeitung in zweisprachigen Dateien wie XLIFF"],
    steps=[("Senden", "Die Übersetzung, den Ausgangstext und ein vorhandenes Glossar."),
           ("Umfang", "Wir vereinbaren Korrektorat oder vollständige Revision."),
           ("Prüfung", "Eine Fachkraft arbeitet den Text durch und markiert jede Änderung."),
           ("Bericht", "Sie erhalten die korrigierte Datei und eine kurze Übersicht der Fehler.")],
    who="Unternehmen, Agenturen, Studierende und Autoren, die eine Übersetzung haben und sie prüfen lassen wollen.",
    faq=[("Was ist der Unterschied zwischen Korrektorat und Revision?", "Beim Korrektorat wird nur die Übersetzung gelesen. Bei der Revision wird sie Satz für Satz mit dem Ausgangstext verglichen, sodass auch Fehlübersetzungen und fehlende Stellen auffallen."),
         ("Wie wird der Preis berechnet?", "Pro 1.000 Wörter oder pro Stunde. Senden Sie beide Dateien, und Sie erhalten einen Festpreis."),
         ("Und wenn die Übersetzung nicht zu retten ist?", "Dann sagen wir es Ihnen und bieten eine neue Übersetzung an.")],
)

PAGES["quality"] = svc(
    title="MT-Post-Editing und LQA | Kayonne Creatives",
    desc="Post-Editing maschineller Übersetzung (MTPE), sprachliche Qualitätssicherung (LQA), Lokalisierungstests und Terminologiemanagement.",
    label="MTPE und Qualitätsprüfung", h1="Menschliche Prüfung, in der Tiefe, die der Text braucht.",
    lede="Manche Texte brauchen Übersetzung, Lektorat und Korrektorat. Andere brauchen ein sorgfältiges Post-Editing maschineller Übersetzung. Wir legen die Stufe vorher fest und tun nicht so, als wäre beides dasselbe.",
    why=["Die Prüfstufe wird schriftlich festgehalten", "Glossare und Translation Memories bleiben bei Ihrem Konto", "Fehler werden eingeordnet, nicht übergangen"],
    incl=["Übersetzung, Lektorat und Korrektorat", "Post-Editing maschineller Übersetzung (MTPE)", "Sprachliche Qualitätssicherung (LQA) mit Fehlerbericht",
          "Lokalisierungstests", "Glossare und Styleguides", "Translation Memory und Terminologiemanagement"],
    steps=[("Stufe", "Wir vereinbaren Humanübersetzung oder Post-Editing."),
           ("Ressourcen", "Glossar, Translation Memory und Stilhinweise."),
           ("Arbeit", "Die bestellten Durchgänge, und kein zusätzlicher, den Sie nicht bestellt haben."),
           ("Bericht", "Bei LQA-Aufträgen erhalten Sie einen kurzen Fehlerbericht.")],
    who="Agenturen und Produktteams mit maschinellen Übersetzungen oder mit Bedarf an einer formalen Qualitätsprüfung. Für die Prüfung einer vorhandenen Übersetzung siehe <a href=\"/de/proofreading/\">Korrektorat und Revision</a>.",
    faq=[("Ist Post-Editing günstiger?", "Oft, wenn die maschinelle Übersetzung gut genug ist. Wenn nicht, sagen wir es und bieten eine vollständige Übersetzung an."),
         ("Trainieren Sie öffentliche KI mit unseren Dateien?", "Nein.")],
)

PAGES["languages"] = dict(
    title="Sprachen | Kayonne Creatives",
    desc="Übersetzungen aus dem und ins Englische für europäische und asiatische Sprachen, von Deutsch, Französisch und Polnisch bis Japanisch, Chinesisch und Koreanisch.",
    label="Sprachen", h1="Europäische und asiatische Sprachen, mit einem Team.",
    lede="Professionelle Übersetzer decken die folgenden Sprachen ab, aus dem und ins Englische. Ihr Ansprechpartner ist eine Projektleitung in Glasgow, keine Gruppe einzelner Freelancer.",
    body=f"<section>{LANG_WALLS}</section>"
         "<section><h2>Zwei Hinweise</h2><p><strong>Deutsch (Schweiz):</strong> Geschriebenes Schweizerdeutsch folgt dem Schweizer Hochdeutsch. Es verwendet ss statt ß und hat einen eigenen Wortschatz. Gesprochener Dialekt ist für Untertitel und Transkription abgedeckt.</p>"
         "<p><strong>Kantonesisch:</strong> für Untertitel und Transkription von gesprochenem Kantonesisch sowie für traditionelles Chinesisch für Leser in Hongkong.</p></section>"
         "<section data-scene=\"film\"><h2>Eigene Seiten für die meistgefragten Sprachen</h2>{{PAIRS}}</section>"
         "<section><h2>Ihre Sprache fehlt?</h2><p>Fragen Sie. Im Angebot steht die Fachkraft, oder wir lehnen das Sprachpaar ab.</p></section>",
)

PAGES["industries"] = dict(
    title="Branchen | Kayonne Creatives",
    desc="Übersetzung und Webentwicklung für Medizin, Recht, Patente, Gaming, Software, E-Commerce und Behördendokumente.",
    label="Branchen", h1="Branchen, für die wir arbeiten.",
    lede="Wir arbeiten für Unternehmen, Agenturen, Spielestudios, Medizin- und Rechtsunternehmen, Patentkanzleien, Onlineshops und Softwarefirmen. Das Fachgebiet ändert den Ablauf, nicht die Sorgfalt.",
    body="""<section><ul class="grid-3 link-cards">
<li><a class="card" href="/de/medical/"><strong>Medizin und Life Sciences</strong></a></li>
<li><a class="card" href="/de/patents/"><strong>Patente</strong></a></li>
<li><a class="card" href="/de/legal/"><strong>Recht</strong></a></li>
<li><a class="card" href="/de/games/"><strong>Gaming</strong></a></li>
<li><a class="card" href="/de/localization/"><strong>Software und Apps</strong></a></li>
<li><a class="card" href="/de/websites/"><strong>E-Commerce und Marketing</strong></a></li>
<li><a class="card" href="/de/documents/"><strong>Technische Dokumentation</strong></a></li>
<li><a class="card" href="/de/documents/"><strong>Amtliche Dokumente</strong></a></li>
<li><a class="card" href="/de/subtitling/"><strong>Medien und Schulungsvideos</strong></a></li>
</ul></section>""",
)

PAGES["work"] = dict(
    title="Arbeiten und Beispiele | Kayonne Creatives",
    desc="Anonymisierte Übersetzungsbeispiele, eine Lokalisierungsdemo und diese Website als digitales Beispiel.",
    label="Arbeiten", h1="Beispiele statt geliehener Logos.",
    lede="Kundennamen zeigen wir nur mit Erlaubnis. Bis dahin sehen Sie hier anonymisierte Beispiele und unsere eigene Arbeit, klar gekennzeichnet.",
    body="""<section><ul class="grid-2 link-cards plain-cards">
<li class="card"><strong>Beispiel Medizin</strong><span class="note">Eine anonymisierte Gebrauchsinformation für ein Medizinprodukt, für eine Zulassungsbehörde ins Deutsche übersetzt. Die Begriffe wurden vorab im Glossar festgelegt, und eine zweite Fachkraft hat den Text mit dem Original abgeglichen.</span></li>
<li class="card"><strong>Beispiel Patent</strong><span class="note">Ansprüche, die mit einer früheren englischen Fassung derselben Patentfamilie übereinstimmen mussten. Alle Zahlen, Bezugszeichen und die Reihenfolge der Ansprüche wurden geprüft.</span></li>
<li><a class="card" href="/de/studio/"><strong>Diese Website</strong><span class="note">Von uns gebaut, auf Englisch und Deutsch. Sehen Sie, wie sie aufgebaut ist und wie viel jede Seite wiegt.</span></a></li>
<li><a class="card" href="/de/demo/"><strong>Lokalisierungsdemo</strong><span class="note">Eine Seite wechselt Sprache, Datumsformat, Währung und Leserichtung.</span></a></li>
</ul></section>
<section data-scene="windows"><h2>Diese Website</h2><div class="shots">""" + shot("/img/work/site-desktop.webp", "Die Startseite von Kayonne Creatives auf einem Laptop, mit der 3D-Szene neben der Überschrift", 1280, 800) + shot("/img/work/site-phone-de.webp", "Die deutsche Startseite auf einem Smartphone", 390, 844) + """</div></section>
<section data-scene="film"><h2>Lokalisierungsdemo</h2>""" + LOC_VIDEO + """</section>
<section data-scene="hero"><h2>3D-Showreel</h2>""" + REEL + """</section>""",
)

PAGES["process"] = dict(
    title="Ablauf und Qualität | Kayonne Creatives",
    desc="So läuft ein Web- oder Übersetzungsauftrag bei Kayonne Creatives: Umfang, Umsetzung, Prüfung, Übergabe. Übersetzung mit Lektorat und Korrektorat.",
    label="Ablauf", h1="So läuft ein Auftrag.",
    lede="Sie sehen die Arbeit, bevor sie als fertig gilt. Sprachaufträge durchlaufen Übersetzung, Lektorat und Korrektorat und dann eine Schlussprüfung, in der von Ihnen bestellten Stufe.",
    body="""<section><ol class="grid-4 steps">
<li class="card"><h3>Umfang</h3><p>Wir halten Auftrag, Sprachen, Termin und Ausschlüsse schriftlich fest.</p></li>
<li class="card"><h3>Umsetzung</h3><p>Design, Entwicklung oder die Sprachdurchgänge. Sie können unterwegs prüfen.</p></li>
<li class="card"><h3>Prüfung</h3><p>Ein Ladezeitbericht für Websites. Bei Sprache eine Schlussprüfung gegen das Briefing durch eine zweite Person.</p></li>
<li class="card"><h3>Übergabe</h3><p>Dateien, Zugänge und Eigentum. Laufende Betreuung nur, wenn Sie sie wünschen.</p></li>
</ol></section>""",
    faq=[("Wie funktionieren Korrekturen?", "Eine Korrekturrunde an den gelieferten Dateien ist innerhalb der im Angebot genannten Frist enthalten. Neuer Ausgangstext ist ein neuer Auftrag."),
         ("Was passiert, wenn Sie einen Termin verpassen?", "Wir melden uns, sobald wir ein Risiko sehen, nicht erst am Liefertag. Die <a href=\"/de/terms/\">AGB</a> regeln, was gilt, wenn wir einen vereinbarten Termin verfehlen.")],
)

PAGES["pricing"] = dict(
    title="Preise | Kayonne Creatives",
    desc="Wie wir Websites, Wartung, Dokumentübersetzung, Untertitelung und Korrektorat berechnen. Jeder Auftrag erhält ein schriftliches Festpreisangebot.",
    label="Preise", h1="So berechnen wir.",
    lede="Jeder Auftrag erhält ein schriftliches Festpreisangebot, bevor die Arbeit beginnt. Hier sehen Sie, worauf der Preis basiert und was ihn verändert.",
    body="""<section><div class="table-wrap"><table>
<thead><tr><th scope="col">Leistung</th><th scope="col">Abrechnung</th><th scope="col">Was den Preis verändert</th></tr></thead>
<tbody>
<tr><td><a href="/de/documents/">Dokumentübersetzung</a></td><td>Pro Wort</td><td>Sprachpaar, Fachgebiet, Dateiformat und Layoutarbeit, Termin</td></tr>
<tr><td><a href="/de/proofreading/">Korrektorat und Revision</a></td><td>Pro 1.000 Wörter oder pro Stunde</td><td>Korrektorat oder Revision, Qualität der vorhandenen Übersetzung</td></tr>
<tr><td><a href="/de/subtitling/">Untertitelung und Transkription</a></td><td>Pro Minute Video oder Audio</td><td>Sprachpaar, Sprechtempo, Timing neu oder aus Template, SDH</td></tr>
<tr><td><a href="/de/localization/">Website- und App-Lokalisierung</a></td><td>Pro Wort, plus Pauschale für Prüfungen</td><td>Anzahl der Sprachen, Wiederholungen, CMS-Arbeit, Rechts-nach-links-Layout</td></tr>
<tr><td><a href="/de/websites/">Website</a></td><td>Projektfestpreis</td><td>Seitenzahl, Shopfunktionen, Texterstellung, Anzahl der Sprachen</td></tr>
<tr><td><a href="/de/domains-email/">Domains und geschäftliche E-Mail</a></td><td>Einrichtungspauschale</td><td>Anzahl der Postfächer, Umzug bestehender Mails</td></tr>
<tr><td><a href="/de/seo/">SEO</a></td><td>Monatlich</td><td>Anzahl der Seiten, Märkte und Sprachen</td></tr>
<tr><td><a href="/de/care/">Wartungsplan</a></td><td>Monatlich</td><td>Größe der Website, Update-Häufigkeit, Stunden für Änderungen</td></tr>
</tbody></table></div></section>
<section><h2>So erhalten Sie einen Preis</h2><p>Senden Sie die Datei, die URL oder ein kurzes Briefing über das <a href="/de/contact/">Anfrageformular</a>. Im Angebot stehen Preis, Währung, Liefertermin und Zahlungsweise. Nichts beginnt, bevor Sie zustimmen.</p></section>""",
)

PAGES["about"] = dict(
    title="Über Kayonne Creatives | Glasgow",
    desc="Kayonne Creatives ist eine Digital- und Sprachagentur in Glasgow, geleitet von einer qualifizierten Übersetzerin bzw. einem qualifizierten Übersetzer, mit professionellen Übersetzern und Digitalspezialisten.",
    label="Über uns", h1="Ein Agenturteam. Eine Projektleitung.",
    lede="Kayonne Creatives wird von Glasgow aus von der Gründungsperson geleitet, einer qualifizierten Fachkraft für Übersetzung. Professionelle Übersetzer decken europäische und asiatische Sprachen ab, Digitalspezialisten bauen Websites und Apps. Sie sprechen die ganze Zeit mit einer Projektleitung.",
    body="""<section class="grid-2">
<div class="card"><h2>Gründung und Leitung</h2><p>MA in Translation Studies, Middlebury Institute of International Studies in Monterey.</p><p>CIOL Diploma in Translation, mit Auszeichnung (Merit).</p><p class="note">Die Gründungsperson leitet jedes Projekt.</p></div>
<div class="card"><h2>Das Team</h2><ul class="ticks"><li>Projektleitung in Glasgow</li><li>Professionelle Übersetzer für europäische Sprachen</li><li>Professionelle Übersetzer für asiatische Sprachen</li><li>Lektorat und Schlussprüfung</li><li>Digitalspezialisten für Websites, Apps, Suche und Ladezeit</li></ul></div>
</section>
<section><h2>Wie wir arbeiten</h2><ul class="ticks"><li>Jede Übersetzung wird vor der Lieferung von einer zweiten Person geprüft.</li><li>Ihre Dateien sehen nur die Personen in Ihrem Auftrag, und eine NDA ist möglich.</li><li>Wir nutzen Ihre Dateien nicht zum Training öffentlicher KI-Modelle.</li></ul></section>""",
)

PAGES["faq"] = dict(
    title="FAQ | Kayonne Creatives",
    desc="Antworten zu Sprachen, Lieferzeit, Dateiformaten, Vertraulichkeit, Korrekturen, Zahlung und Eigentum.",
    label="FAQ", h1="Fragen unserer Kunden.",
    lede="Kurze Antworten. Wenn Ihr Fall anders liegt, steht es im Angebot.",
    body="",
    faq=[("Welche Sprachen übersetzen Sie?", "Europäische und asiatische Sprachen, aus dem und ins Englische. Siehe <a href=\"/de/languages/\">Sprachen</a>. Im Angebot steht, wer Ihr Sprachpaar übernimmt."),
         ("Wie schnell ist eine Übersetzung fertig?", "Das hängt von Umfang, Sprache und Fachgebiet ab. Ein kurzes, klares Dokument dauert oft einige Werktage. Eine Produktlokalisierung wird geplant. Im Angebot steht ein Termin."),
         ("Welche Formate nehmen Sie an?", "Word, Excel, PowerPoint, PDF, Web-Exporte, String-Dateien, Untertiteldateien sowie Fotos und Scans. Designdateien wie InDesign nach Absprache."),
         ("Ist die Arbeit vertraulich?", "Ja. Auf Wunsch unterzeichnen wir eine NDA. Nur die Personen in Ihrem Auftrag sehen die Dateien. Wir trainieren keine öffentlichen KI-Modelle mit Ihren Inhalten."),
         ("Wie funktionieren Korrekturen?", "Eine Runde an den gelieferten Dateien ist innerhalb der im Angebot genannten Frist enthalten. Neuer Text wird neu angeboten."),
         ("Wie bezahle ich?", "Im Angebot stehen Betrag, Währung, eine eventuelle Anzahlung, Fälligkeit und Zahlungsweise."),
         ("Wem gehören der Website-Code und die übersetzten Texte?", "Ihnen, sobald die vereinbarten Honorare bezahlt sind. Siehe <a href=\"/de/terms/\">AGB</a>."),
         ("Können Sie Domain und E-Mail einrichten?", "Ja. Siehe <a href=\"/de/domains-email/\">Domains und geschäftliche E-Mail</a>.")],
)

PAGES["insights"] = dict(
    title="Ratgeber | Kayonne Creatives",
    desc="Praktische Hinweise zu Website-Lokalisierung, mehrsprachiger SEO und Ladezeit, für alle, die solche Leistungen einkaufen.",
    label="Ratgeber", h1="Hinweise für alle, die diese Arbeit einkaufen.",
    lede="Kurze, praktische Artikel zu Lokalisierung, Suche und Ladezeit.",
    body="""<section><ul class="grid-2 link-cards">
<li><a class="card" href="/de/insights/localise-a-website/"><strong>Eine Website lokalisieren</strong><span class="note">Fünf Entscheidungen vor der ersten übersetzten Seite.</span></a></li>
<li><a class="card" href="/de/insights/speed-mistakes/"><strong>Typische Ladezeit-Fehler</strong><span class="note">Was eine kleine Unternehmenswebsite auf dem Smartphone meist langsam macht.</span></a></li>
</ul></section>""",
)

PAGES["insights/localise-a-website"] = dict(
    title="Eine Website lokalisieren | Kayonne Creatives",
    desc="Fünf Schritte zur Website-Lokalisierung: Sprach-URLs, Glossar, Keyword-Recherche pro Sprache, Platz für längere Texte und hreflang.",
    label="Ratgeber", h1="Eine Website lokalisieren",
    body="""<article class="prose">
<p>Beginnen Sie mit dem Markt, nicht mit dem Plugin. Wählen Sie Sprach-URLs, etwa einen Ordner pro Sprache (<code>/de/</code>, <code>/fr/</code>), und legen Sie eine Standardadresse fest.</p>
<p>Schreiben Sie vor der ersten Seite ein Glossar. Produktnamen, Schaltflächen und Werbeaussagen dürfen sich nicht mittendrin ändern.</p>
<p>Recherchieren Sie Suchbegriffe in der Zielsprache. Die direkte Übersetzung eines englischen Keywords ist oft nicht das, wonach Menschen suchen.</p>
<p>Lassen Sie Platz in Schaltflächen und Überschriften. Deutsch und Niederländisch laufen oft länger als Englisch, und Japanisch bricht Zeilen anders um.</p>
<p>Setzen Sie hreflang, übersetzen Sie Titel und Beschreibungen, und verlassen Sie sich nicht darauf, dass der Browser alle automatisch umleitet.</p>
</article>""",
)

PAGES["insights/speed-mistakes"] = dict(
    title="Typische Ladezeit-Fehler | Kayonne Creatives",
    desc="Typische Fehler bei der Ladezeit: schwere Titelbilder und 3D-Szenen, unkomprimierte Fotos, ungenutzte Schriften und Tests nur am schnellen Laptop.",
    label="Ratgeber", h1="Typische Ladezeit-Fehler",
    body="""<article class="prose">
<p>Ein großes Titelbild oder eine 3D-Szene, die vor der Überschrift lädt, verzögert auf dem Smartphone die erste Darstellung.</p>
<p>Unkomprimierte Fotos und ungenutzte Schriften sind meist der Grund für das Gewicht.</p>
<p>Testen Sie auf einem Mittelklasse-Smartphone, nicht nur am Laptop im Büro.</p>
<p>Teilen Sie den Core-Web-Vitals-Bericht. Eine einzelne Punktzahl von 100 ist nicht der Grenzwert, auf den es ankommt.</p>
</article>""",
)

FORM_DE = dict(
    heading="Angebot anfragen", subject="Neue Angebotsanfrage über kayonnecreatives.com/de",
    auto="Vielen Dank für Ihre Anfrage bei Kayonne Creatives. Wir haben sie erhalten und antworten per E-Mail mit einem Angebot oder Rückfragen. Weitere Dateien können Sie einfach als Antwort auf diese Mail senden.",
    name="Ihr Name", email="E-Mail", phone="Telefon (optional)", company="Firma (optional)", service="Was brauchen Sie?",
    choose="Leistung wählen", source="Aus der Sprache", source_ph="z. B. Englisch", target="In die Sprache(n)", target_ph="z. B. Deutsch, Japanisch",
    deadline="Termin", size="Umfang", size_ph="z. B. 3 Seiten, 2.000 Wörter, 12 Minuten", file="Datei anhängen",
    file_note="Eine Datei, insgesamt bis 10 MB. Für größere oder mehrere Dateien fügen Sie einen WeTransfer- oder Google-Drive-Link in die Nachricht ein.",
    message="Nachricht", message_ph="Wer liest den Text, wo wird er verwendet, Website-Adresse, alles, was wir wissen sollten.",
    consent='Ich bin einverstanden, dass Kayonne Creatives diese Angaben verwendet, um auf meine Anfrage zu antworten. Siehe <a href="/de/privacy/">Datenschutzerklärung</a>.',
    send="Anfrage senden", after=f"Das Formular wird über unseren Formulardienst an {EMAIL} zugestellt. Sie können uns auch direkt schreiben.",
    services=[
        ("Sprache", ["Dokumentübersetzung", "Website- oder App-Lokalisierung", "Spielelokalisierung",
                     "Medizinische Übersetzung", "Patentübersetzung", "Juristische Übersetzung", "Untertitelung oder Transkription",
                     "Korrektorat oder Revision", "MTPE oder LQA"]),
        ("Digital", ["Website", "Onlineshop", "Web-App", "Mobile App", "Domain und geschäftliche E-Mail", "SEO", "Ladezeit- oder Barrierefreiheits-Audit", "Wartungsplan"]),
        ("Beides", ["Website und Übersetzung", "Internationaler Marktstart", "Shop-Lokalisierung", "Mehrsprachige SEO", "Etwas anderes"]),
        ("Kostenlos", ["Kostenloser Website-Check", "Kostenloser Readiness-Check"]),
    ],
    datalist=["Englisch"] + EUROPE + ASIA + ["Arabisch", "Persisch"],
)

PAGES["contact"] = dict(
    title="Angebot anfragen | Kayonne Creatives",
    desc="Angebot für Übersetzung, Untertitelung, Website oder Domain und E-Mail anfragen. Datei anhängen und Festpreis erhalten.",
    label="Kontakt", h1="Beschreiben Sie den Auftrag.",
    lede=f'Nennen Sie Leistung, Sprachen und Termin und hängen Sie die Datei an, falls vorhanden. Wir antworten per E-Mail mit einem Festpreisangebot oder Rückfragen. Sie erreichen uns auch unter <a href="mailto:{EMAIL}">{EMAIL}</a>.',
    body=quote_form("de", FORM_DE), no_cta=True,
)

PAGES["thanks"] = dict(
    title="Anfrage gesendet | Kayonne Creatives", desc="Ihre Anfrage wurde an Kayonne Creatives gesendet.", noindex=True,
    label="Kontakt", h1="Vielen Dank. Ihre Anfrage ist angekommen.",
    lede=f"Wir antworten per E-Mail mit einem Angebot oder Rückfragen. Eine Bestätigung ist unterwegs. Falls sie fehlt, sehen Sie bitte im Spamordner nach oder schreiben Sie an {EMAIL}.",
    body='<p><a class="btn ghost" href="/de/">Zur Startseite</a></p>', no_cta=True,
)

PAGES["privacy"] = dict(
    title="Datenschutzerklärung | Kayonne Creatives",
    desc="Wie Kayonne Creatives personenbezogene Daten nach UK GDPR und DSGVO erhebt, nutzt und schützt.",
    label="Rechtliches", h1="Datenschutzerklärung",
    body=f"""<article class="prose">
<p>Diese Erklärung beschreibt, wie Kayonne Creatives („wir“) personenbezogene Daten verarbeitet, wenn Sie diese Website besuchen, ein Angebot anfragen oder Kunde werden. Wir halten uns an die UK General Data Protection Regulation (UK GDPR) und den Data Protection Act 2018. Für Kunden in der EU gelten die entsprechenden Rechte der DSGVO.</p>
<h2>Verantwortlicher</h2>
<p>Kayonne Creatives, Glasgow, Vereinigtes Königreich. Kontakt für Datenschutzfragen: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Welche Daten wir erheben</h2>
<ul><li><strong>Anfragen:</strong> Name, E-Mail-Adresse, Telefonnummer und Firma, falls angegeben, die gewünschte Leistung und Sprachen, Ihre Nachricht und angehängte Dateien.</li>
<li><strong>Aufträge:</strong> die Dokumente, Medien und Website-Inhalte, die Sie uns senden. Sie können personenbezogene Daten über Sie oder andere Personen enthalten.</li>
<li><strong>Abrechnung:</strong> Name, Anschrift und Zahlungsdaten für die Rechnungsstellung.</li>
<li><strong>Websitebesuche:</strong> Unser Hosting-Anbieter speichert technische Daten wie IP-Adresse und Browsertyp in Server-Logs. Diese Website nutzt keine Analyse- oder Werbe-Cookies.</li></ul>
<h2>Zwecke und Rechtsgrundlagen</h2>
<ul><li>Beantwortung Ihrer Anfrage und Angebotserstellung: vorvertragliche Maßnahmen auf Ihre Anfrage (Art. 6 Abs. 1 lit. b).</li>
<li>Durchführung des Auftrags: Vertragserfüllung (Art. 6 Abs. 1 lit. b).</li>
<li>Buchhaltung: rechtliche Verpflichtung (Art. 6 Abs. 1 lit. c).</li>
<li>Sicherheit und Betrieb der Website: berechtigtes Interesse (Art. 6 Abs. 1 lit. f).</li></ul>
<h2>Empfänger</h2>
<ul><li>Die Übersetzer und Fachkräfte in Ihrem Auftrag, die zur Vertraulichkeit verpflichtet sind.</li>
<li>FormSubmit, das das Anfrageformular an unser Postfach zustellt.</li>
<li>Unser E-Mail- und Speicheranbieter.</li>
<li>GitHub, das diese Website hostet.</li>
<li>Unsere Steuerberatung und Behörden, soweit gesetzlich vorgeschrieben.</li></ul>
<p>Einige Anbieter verarbeiten Daten außerhalb des Vereinigten Königreichs und der EU, auch in den USA. Solche Übermittlungen stützen sich auf Angemessenheitsbeschlüsse oder Standardvertragsklauseln. Wir verkaufen keine Daten und nutzen Ihre Dateien nicht zum Training von KI-Modellen.</p>
<h2>Speicherdauer</h2>
<ul><li>Anfragen ohne Auftrag: bis zu 12 Monate.</li>
<li>Dateien zu einem Auftrag: Löschung innerhalb von 90 Tagen nach Lieferung, sofern Sie nicht wünschen, dass wir sie aufbewahren, etwa als Translation Memory.</li>
<li>Rechnungen und Buchhaltungsunterlagen: 6 Jahre, wie von der britischen Steuerbehörde HMRC verlangt.</li></ul>
<h2>Ihre Rechte</h2>
<p>Sie können Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung und Datenübertragbarkeit verlangen und der Verarbeitung widersprechen. Schreiben Sie an <a href="mailto:{EMAIL}">{EMAIL}</a>. Wir antworten innerhalb eines Monats.</p>
<p>Sie können sich beim britischen Information Commissioner's Office (ICO) beschweren, <a href="https://ico.org.uk/make-a-complaint/">ico.org.uk</a>, oder bei der Datenschutzaufsichtsbehörde in Ihrem Land.</p>
<h2>Änderungen</h2>
<p>Wir passen diese Erklärung an, wenn sich unsere Abläufe ändern. Stand: Oktober 2026.</p>
</article>""",
)

PAGES["cookies"] = dict(
    title="Cookie-Richtlinie | Kayonne Creatives",
    desc="Diese Website setzt keine Cookies und nutzt keine Analyse- oder Werbetracker.",
    label="Rechtliches", h1="Cookie-Richtlinie",
    body=f"""<article class="prose">
<p>Diese Website setzt keine Cookies und verwendet keine Analyse-, Werbe- oder Social-Media-Tracker. Deshalb gibt es kein Cookie-Banner.</p>
<p>Schriften und Skripte werden von unserer eigenen Website geladen. Ihr Besuch wird also nicht an Schrift- oder Skriptanbieter übermittelt.</p>
<p>Wenn Sie das Anfrageformular absenden, stellt FormSubmit es zu. FormSubmit kann eine Spam-Prüfung anzeigen, die eigene Cookies verwenden kann. Wie wir mit Ihren Daten umgehen, steht in der <a href="/de/privacy/">Datenschutzerklärung</a>.</p>
<p>Falls wir künftig Analysen einsetzen, aktualisieren wir diese Seite und holen vorher Ihre Einwilligung ein, wo das Gesetz es verlangt.</p>
<p>Fragen: <a href="mailto:{EMAIL}">{EMAIL}</a>. Stand: Oktober 2026.</p>
</article>""",
)

PAGES["terms"] = dict(
    title="Allgemeine Geschäftsbedingungen | Kayonne Creatives",
    desc="Bedingungen für Übersetzung, Lokalisierung, Untertitelung, Websites und Wartungspläne von Kayonne Creatives.",
    label="Rechtliches", h1="Allgemeine Geschäftsbedingungen",
    body=f"""<article class="prose">
<p class="note">Diese Übersetzung dient der Information. Maßgeblich ist die <a href="/terms/">englische Fassung</a>.</p>
<p>Diese Bedingungen gelten für alle Leistungen von Kayonne Creatives („wir“) für Sie („Kunde“). Ihr Angebot kann ergänzende Bedingungen enthalten, die dann vorgehen.</p>
<h2>1. Angebote und Aufträge</h2>
<p>Ein Angebot gilt 30 Tage. Es nennt Umfang, Preis, Währung, Liefertermin und Zahlungsbedingungen. Ein Auftrag beginnt, wenn Sie das Angebot schriftlich annehmen und eine eventuell genannte Anzahlung leisten.</p>
<h2>2. Ihre Pflichten</h2>
<p>Sie bestätigen, dass Sie berechtigt sind, uns das Material zu senden und übersetzen oder veröffentlichen zu lassen. Sie liefern finale Ausgangstexte, lesbare Dateien und zeitnahe Antworten auf Rückfragen. Verzögerungen verschieben den Liefertermin.</p>
<h2>3. Änderungen</h2>
<p>Neuer oder geänderter Ausgangstext, zusätzliche Sprachen oder Seiten liegen außerhalb des ursprünglichen Umfangs und werden gesondert angeboten.</p>
<h2>4. Lieferung und Korrekturen</h2>
<p>Wir liefern im vereinbarten Format. Eine Korrekturrunde an der gelieferten Arbeit ist innerhalb von 14 Tagen nach Lieferung enthalten, sofern das Angebot nichts anderes sagt. Stilistische Wunschänderungen an einer korrekten Übersetzung und neue Anforderungen werden gesondert berechnet.</p>
<h2>5. Verspätete Lieferung</h2>
<p>Sehen wir ein Risiko für einen vereinbarten Termin, melden wir uns sofort. Verfehlen wir einen vereinbarten Termin aus Gründen, die wir zu vertreten haben, können Sie den nicht gelieferten Teil kostenfrei stornieren oder mit uns einen reduzierten Preis vereinbaren.</p>
<h2>6. Zahlung</h2>
<p>Rechnungen sind innerhalb von 14 Tagen fällig, sofern das Angebot nichts anderes sagt. Größere Projekte können eine Anzahlung und Teilzahlungen erfordern. Bei überfälligen Rechnungen können wir die Arbeit unterbrechen.</p>
<h2>7. Eigentum</h2>
<p>Nach vollständiger Zahlung gehören Ihnen die für Sie erstellten Übersetzungen, der Website-Code und die Designs, mit Ausnahme von Software, Schriften, Plugins und Stockmaterial Dritter, die unter ihren eigenen Lizenzen bleiben. Translation Memories und Glossare dürfen wir für Ihre künftigen Aufträge aufbewahren und löschen sie auf Ihren Wunsch.</p>
<h2>8. Vertraulichkeit</h2>
<p>Wir behandeln Ihr Material vertraulich und geben es nur an die Personen in Ihrem Auftrag weiter, die zur Vertraulichkeit verpflichtet sind. Auf Wunsch unterzeichnen wir eine gesonderte NDA.</p>
<h2>9. Fachübersetzungen</h2>
<p>Wir übersetzen juristische, medizinische und Patenttexte. Wir geben keine Rechts-, Medizin- oder Patentberatung, und ob eine Stelle eine Übersetzung annimmt, richtet sich nach deren eigenen Regeln.</p>
<h2>10. Websites, Hosting und Wartung</h2>
<p>Domains, Hosting und E-Mail-Konten werden auf Ihren Namen registriert und von Ihnen direkt beim Anbieter bezahlt. Wartungspläne laufen monatlich und sind mit der im Plan genannten Frist kündbar. Für Ausfälle oder Änderungen durch Drittanbieter haften wir nicht.</p>
<h2>11. Haftung</h2>
<p>Unsere Gesamthaftung je Auftrag ist auf das für diesen Auftrag gezahlte Honorar begrenzt. Für mittelbare Schäden wie entgangenen Gewinn haften wir nicht. Gesetzlich nicht beschränkbare Haftung bleibt unberührt.</p>
<h2>12. Stornierung</h2>
<p>Stornieren Sie einen begonnenen Auftrag, zahlen Sie die bis dahin erbrachte Arbeit. Verbraucher, die aus der Ferne bestellen, haben ein 14-tägiges Widerrufsrecht. Verlangen Sie den Beginn innerhalb dieser Frist, zahlen Sie die bis zum Widerruf erbrachte Arbeit.</p>
<h2>13. Beschwerden</h2>
<p>Schreiben Sie an <a href="mailto:{EMAIL}">{EMAIL}</a>. Wir antworten innerhalb von 5 Werktagen.</p>
<h2>14. Recht</h2>
<p>Es gilt schottisches Recht, zuständig sind die schottischen Gerichte. Verbraucher behalten die zwingenden Rechte ihres Wohnsitzlandes.</p>
<p class="note">Stand: Oktober 2026.</p>
</article>""",
)

PAGES["studio"] = dict(
    title="So ist diese Website gebaut | Kayonne Creatives",
    desc="Diese Website ist unser digitales Beispiel: reines HTML und CSS, selbst gehostete Schriften, keine Cookies, keine Tracker, auf Englisch und Deutsch.",
    label="Unsere eigene Website", h1="Diese Website ist das digitale Beispiel.",
    lede="Wir verkaufen Ladezeit, Auffindbarkeit und saubere Entwicklung, also ist diese Website so gebaut wie für unsere Kunden. Hier die Fakten, die Sie selbst prüfen können.",
    body="""<section><h2>Was drinsteckt</h2><ul class="ticks">
<li>Reines HTML und CSS. Skripte steuern nur das Menü, die Animationen und die 3D-Szenen</li>
<li>3D-Szenen mit three.js, von dieser Website geladen. Sie starten erst, wenn die Seite bereit ist, und schalten sich ab, wenn Ihr Gerät reduzierte Bewegung oder Datensparen verlangt</li>
<li>Zwei Schriftdateien, von dieser Website geladen, nicht von Google</li>
<li>Keine Cookies, keine Analyse, keine Tracker von Dritten</li>
<li>Jede Seite auf Englisch und Deutsch, verknüpft mit hreflang</li>
<li>Beschriftete Formularfelder, Tastaturbedienung und ein Link zum Inhalt</li>
<li>Gehostet auf GitHub Pages, mit HTTPS</li></ul></section>
<section><h2>Was jede Seite wiegt</h2><p>Die Größe des HTML für eine Auswahl von Seiten. Stylesheet und Schriften werden nur einmal geladen.</p>{{WEIGHTS}}</section>
<section><p>Prüfen Sie es selbst mit <a href="https://pagespeed.web.dev/analysis?url=https%3A%2F%2Fkayonnecreatives.com%2Fde%2F">PageSpeed Insights</a>.</p></section>""",
)

PAGES["demo"] = dict(
    title="Lokalisierungsdemo | Kayonne Creatives",
    desc="Eine Produktkarte wechselt die Sprache: Textlänge, Datumsformat, Währung und Leserichtung auf Englisch, Deutsch, Japanisch und Arabisch.",
    label="Lokalisierungsdemo", h1="Sehen Sie, wie eine Seite die Sprache wechselt.",
    lede="Dieses Beispiel ist kein Kundenprojekt. Es zeigt, was Lokalisierung neben den Wörtern ändert: Textlänge, Datum, Währung und Leserichtung. Wählen Sie eine Sprache.",
    body=DEMO_BODY.format(len="Länge der Überschrift in Zeichen (ggü. Englisch)", date="Datumsformat", cur="Währungsformat", dir="Leserichtung",
                          note="Beispielpreise. Datum und Währung formatiert Ihr Browser für jede Sprache, so wie es eine lokalisierte Website tut."),
    script=demo_script(ltr="links nach rechts", rtl="rechts nach links", start="de"),
)


# ---------------------------------------------------------------------------
# Team-Seiten, neue Leistungsseiten, Sprachseiten und Artikel
# ---------------------------------------------------------------------------
from content_en import LANG_PAIRS  # noqa: E402


def team_video(key, caption, label):
    return video(f"team-{key}", caption, 1280, 720, label)


PAGES["digital"] = dict(
    title="Kayonne Digital | Webdesign, Apps und SEO aus Glasgow",
    desc="Das Team Kayonne Digital entwickelt Websites, Onlineshops und Apps, richtet Domains und geschäftliche E-Mail ein und kümmert sich um SEO, Ladezeit und Wartung.",
    label="Kayonne Digital", h1="Das Entwicklungsteam.",
    lede="Designer und Entwickler, die Websites, Shops und Apps bauen, Domain und E-Mail dahinter einrichten und dafür sorgen, dass alles schnell und auffindbar bleibt. In Glasgow, für Unternehmen in ganz Großbritannien und Europa.",
    body="""<section data-scene="windows"><h2>Was das Team baut</h2>{{TEAM:digital}}</section>
<section data-scene="tiles" class="grid-2 split-copy"><div><h2>Mit wem Sie arbeiten</h2><p>Eine Projektleitung in Glasgow, ein Designer und ein Entwickler bei jedem Projekt. Sie sehen das Design, bevor programmiert wird, eine Testseite vor dem Start und einen Ladezeitbericht bei der Übergabe.</p><p>Braucht Ihre Website eine weitere Sprache, sitzt das <a href="/de/language/">Sprachteam</a> nebenan. Keine zweite Agentur, keine Übergabe per E-Mail.</p></div>"""
    + team_video("digital", "Die Arbeit des Digital-Teams in 3D: Browserfenster, App-Raster und Smartphones.", "Kayonne Digital Showreel") + """</section>
<section data-scene="bars"><h2>Pakete</h2><ul class="grid-4 link-cards plain-cards">
<li class="card"><strong>One-Pager</strong><span class="note">Angebot, Kontaktformular, Karte. Für einen Start oder Selbstständige.</span></li>
<li class="card"><strong>Unternehmenswebsite</strong><span class="note">Fünf bis acht Seiten, Blog, lokale SEO.</span></li>
<li class="card"><strong>Onlineshop</strong><span class="note">Shopify oder WooCommerce, Zahlungen, Versandregeln.</span></li>
<li class="card"><strong>Mehrsprachige Website</strong><span class="note">Jedes Paket in zwei oder mehr Sprachen.</span></li>
</ul><p><a class="btn ghost" href="/de/pricing/">So berechnen wir</a></p></section>
<section data-scene="lens" class="offer card"><div><p class="kicker">Kostenlos</p><h2>Website-Check</h2><p>Senden Sie uns Ihre Adresse. Wir prüfen Ladezeit auf dem Smartphone, mobile Ansicht, SEO-Grundlagen und Kontaktformular und schicken Ihnen eine kurze Liste, was zuerst zu tun ist.</p></div><p><a class="btn magnetic" href="/de/website-check/">Kostenlosen Check anfordern</a></p></section>""",
    faq=[("Arbeiten Sie nur in Glasgow?", "Nein. Das Team sitzt in Glasgow und arbeitet für Kunden in Großbritannien und im Ausland."),
         ("Wem gehört die Website?", "Ihnen, sobald die vereinbarten Honorare bezahlt sind. Domain, Hosting und E-Mail laufen auf Ihren Namen."),
         ("Können Sie die Website auch übersetzen?", "Ja. Dafür gibt es <a href=\"/de/global/\">Global</a>.")],
)

PAGES["language"] = dict(
    title="Kayonne Language | Professionelle Fachübersetzungen",
    desc="Das Team Kayonne Language: qualifizierte Übersetzer für Dokumente, Recht, Medizin, Patente, Untertitel und Korrektorat, mit zweiter Prüfung bei jedem Auftrag.",
    label="Kayonne Language", h1="Das Übersetzungsteam.",
    lede="Qualifizierte Übersetzer, geleitet von Glasgow aus von einer Fachkraft mit MA in Translation Studies und CIOL Diploma in Translation. Jeder Auftrag wird vor der Lieferung von einer zweiten Fachkraft geprüft.",
    body="""<section data-scene="sheets"><h2>Was das Team übersetzt</h2>{{TEAM:language}}</section>
<section data-scene="sheets" class="grid-2 split-copy"><div><h2>Dokumente wie das Original</h2><p>Urkunden, Kontoauszüge, Verträge und Handbücher kommen im Layout des Ausgangstexts zurück, mit Stempeln, Tabellen und handschriftlichen Vermerken dort übersetzt, wo sie stehen.</p><p><a class="btn magnetic" href="/de/documents/">Dokumentübersetzung</a></p></div><figure class="media"><img src="/img/scenes/sheets.webp" alt="" width="900" height="675" loading="lazy" decoding="async"></figure></section>
<section data-scene="path"><h2>Wer bei uns übersetzt</h2><ol class="grid-4 steps">
<li class="card"><h3>Qualifiziert</h3><p>Studium der Übersetzung oder eine Berufsqualifikation wie das CIOL Diploma.</p></li>
<li class="card"><h3>Muttersprachlich</h3><p>Übersetzt wird in die eigene Muttersprache.</p></li>
<li class="card"><h3>Fachkundig</h3><p>Recht, Medizin und Patente nur mit Erfahrung im Fachgebiet.</p></li>
<li class="card"><h3>Geprüft</h3><p>Eine zweite Fachkraft revidiert jeden Auftrag.</p></li>
</ol></section>
<section data-scene="film" class="grid-2 split-copy"><div><h2>Sprachen</h2><p>Europäische und asiatische Sprachen, aus dem und ins Englische. Die meistgefragten haben eigene Seiten: <a href="/de/languages/polish/">Polnisch</a>, <a href="/de/languages/romanian/">Rumänisch</a>, <a href="/de/languages/arabic/">Arabisch</a>, <a href="/de/languages/urdu/">Urdu</a>, <a href="/de/languages/chinese/">Chinesisch</a>, <a href="/de/languages/spanish/">Spanisch</a>, <a href="/de/languages/french/">Französisch</a>, <a href="/de/languages/german/">Deutsch</a>, <a href="/de/languages/ukrainian/">Ukrainisch</a> und <a href="/de/languages/portuguese/">Portugiesisch</a>.</p><p><a class="btn ghost" href="/de/languages/">Alle Sprachen</a></p></div>"""
    + team_video("language", "Die Arbeit des Sprachteams in 3D: Dokumente, Waage und Untertitel.", "Kayonne Language Showreel") + """</section>
<section data-scene="shield"><h2>Ihre Dokumente bleiben vertraulich</h2><ul class="ticks"><li>Nur die Personen im Auftrag sehen die Dateien.</li><li>NDA auf Wunsch, bevor Sie etwas senden.</li><li>Löschung innerhalb von 90 Tagen nach Lieferung, außer Sie wünschen etwas anderes.</li><li>Nie zum Training öffentlicher KI-Modelle genutzt.</li></ul></section>""",
    faq=[("Übersetzen Sie ins Englische oder aus dem Englischen?", "Beides, für alle Sprachen, die wir anbieten."),
         ("Können Sie eine vorhandene Übersetzung prüfen?", "Ja. Siehe <a href=\"/de/proofreading/\">Korrektorat und Revision</a>."),
         ("Wie erhalte ich einen Preis?", "Laden Sie das Dokument über das <a href=\"/de/contact/\">Anfrageformular</a> hoch. Sie erhalten einen Festpreis vor Beginn.")],
)

PAGES["global"] = dict(
    title="Kayonne Global | Website-Lokalisierung und internationaler Marktstart",
    desc="Kayonne Global vereint Entwicklungs- und Übersetzungsteam: lokalisierte Websites und Shops, mehrsprachige SEO und internationale Markteinführungen aus einer Hand.",
    label="Kayonne Global", h1="Beide Teams. Ein Marktstart.",
    lede="Die meisten Anbieter machen eine Hälfte: Sie bauen die Website oder sie übersetzen sie. Bei Kayonne Global arbeiten Entwicklungs- und Übersetzungsteam am selben Projekt, damit Ihre Website ohne Bruch in der Mitte für den nächsten Markt bereit ist.",
    body="""<section data-scene="globe"><h2>Was wir ins Ausland bringen</h2>{{TEAM:global}}</section>
<section data-scene="plane"><h2>So läuft ein Marktstart</h2><ol class="grid-3 steps">
<li class="card"><h3>Analyse</h3><p>Ist die Website übersetzungsbereit? Text in Bildern, feste Schaltflächenbreiten, fest codierte Daten.</p></li>
<li class="card"><h3>Recherche</h3><p>Suchbegriffe von Muttersprachlern im Zielmarkt recherchiert, nicht aus dem Englischen übersetzt.</p></li>
<li class="card"><h3>Entwicklung</h3><p>Sprachordner, hreflang, lokale Währung und Formate, Layout für längere Wörter.</p></li>
<li class="card"><h3>Übersetzung</h3><p>Eine Fachkraft übersetzt im Kontext, eine zweite revidiert.</p></li>
<li class="card"><h3>Prüfung</h3><p>Jede Seite in jeder Sprache im Browser und auf dem Smartphone geprüft.</p></li>
<li class="card"><h3>Start</h3><p>Sitemaps und Search Console je Markt, dazu ein Bericht, worauf zu achten ist.</p></li>
</ol></section>
<section data-scene="film" class="grid-2 split-copy"><div><h2>Sehen Sie selbst</h2><p>Eine Produktkarte auf Englisch, Deutsch, Japanisch und Arabisch. Es ändern sich die Wörter, aber auch Datum, Währung und Leserichtung.</p><p><a class="btn ghost" href="/de/demo/">Live-Demo ausprobieren</a></p></div>""" + LOC_VIDEO + """</section>
<section data-scene="check"><h2>Warum nicht einfach ein Übersetzungs-Plugin?</h2><div class="table-wrap"><table>
<thead><tr><th scope="col"></th><th scope="col">Nur maschinelles Plugin</th><th scope="col">Kayonne Global</th></tr></thead>
<tbody>
<tr><td>Zeit bis zum ersten Entwurf</td><td>Minuten</td><td>Tage</td></tr>
<tr><td>Suchbegriffe je Markt</td><td>Aus dem Englischen übersetzt</td><td>Von Muttersprachlern recherchiert</td></tr>
<tr><td>Markennamen, Tonalität, rechtliche Aussagen</td><td>Nicht geprüft</td><td>Glossar vorab, Revision durch eine zweite Fachkraft</td></tr>
<tr><td>Layout bei längeren Wörtern</td><td>Nicht geprüft</td><td>Auf Desktop und Smartphone geprüft</td></tr>
<tr><td>Geeignet für</td><td>Unkritische Seiten, interne Tools</td><td>Verkaufsseiten, Rechtstexte, Checkout</td></tr>
</tbody></table></div><p class="note">Ein Plugin kann ein guter erster Schritt sein. Wir können maschinelle Übersetzungen auch überarbeiten, statt neu anzufangen. Siehe <a href="/de/quality/">MTPE</a>.</p></section>
<section data-scene="check" class="offer card"><div><p class="kicker">Kostenlos</p><h2>Readiness-Check</h2><p>Wir prüfen Ihre Website und sagen Ihnen, was bei einer Übersetzung kaputtgehen würde, mit welchem Markt Sie beginnen sollten und was es ungefähr braucht.</p></div><p><a class="btn magnetic" href="/de/readiness-check/">Website prüfen lassen</a></p></section>""",
    faq=[("Welche Märkte kennen Sie am besten?", "Europa und Asien, mit besonderem Fokus auf Deutschland, Österreich und die Schweiz."),
         ("Arbeiten Sie mit unserem Entwickler zusammen?", "Ja. Wir liefern Übersetzungen, Keyword-Recherche und hreflang-Vorgaben an Ihr Team."),
         ("Übernehmen Sie auch den Shop?", "Ja. Siehe <a href=\"/de/ecommerce-localisation/\">Shop-Lokalisierung</a>.")],
)

PAGES["web-design-glasgow"] = svc(
    title="Webdesign Glasgow | Kayonne Creatives",
    desc="Webdesign in Glasgow von einem Team vor Ort: Unternehmenswebsites, Onlineshops und Relaunches, schnell und auffindbar, auf Wunsch mehrsprachig.",
    label="Webdesign Glasgow", h1="Webdesign in Glasgow, von einem Team, das Sie treffen können.",
    lede="Wir gestalten und entwickeln Websites für Unternehmen in Glasgow: Handwerk, Praxen, Läden, Beratung und Start-ups. Klare Seiten, schnell auf dem Smartphone, für die lokale Suche eingerichtet und bereit für eine weitere Sprache.",
    why=["Ein Team vor Ort, das Sie persönlich treffen können", "Lokale SEO und Google-Unternehmensprofil gleich mit eingerichtet", "Übersetzung im Haus, wenn Sie eine zweite Sprache brauchen"],
    incl=["Unternehmenswebsites", "Onlineshops", "Relaunches langsamer oder veralteter Websites", "Domain und geschäftliche E-Mail", "Google-Unternehmensprofil", "Wartung nach dem Start"],
    steps=[("Treffen", "Ein Gespräch oder ein Kaffee in Glasgow, um festzulegen, was die Website leisten muss."),
           ("Design", "Sie geben das Design frei, bevor gebaut wird."),
           ("Entwicklung", "Wir bauen, verbinden die Domain und richten E-Mail ein."),
           ("Start", "Ladezeitbericht, Checkliste für lokale SEO und Schulung.")],
    who="Unternehmen in Glasgow und im Westen Schottlands, die mit ihrer Website Anfragen gewinnen wollen.",
    faq=[("Was kostet eine Website in Glasgow?", "Von einigen hundert Pfund für eine Vorlage bis zu mehreren tausend für eine individuelle Entwicklung. Siehe unseren <a href=\"/de/insights/website-cost-glasgow/\">Ratgeber zu Website-Kosten</a>."),
         ("Helfen Sie bei Google Maps?", "Ja. Wir richten Ihr Google-Unternehmensprofil ein und pflegen es."),
         ("Können wir uns treffen?", "Ja. Schreiben Sie es ins Anfrageformular.")],
)

PAGES["website-check"] = dict(
    title="Kostenloser Website-Check | Kayonne Digital",
    desc="Senden Sie Ihre Website-Adresse und erhalten Sie eine kostenlose schriftliche Prüfung von Ladezeit, mobiler Ansicht, SEO-Grundlagen und Kontaktformular.",
    label="Kayonne Digital · Kostenlos", h1="Ein kostenloser Check Ihrer Website.",
    lede="Senden Sie uns Ihre Website-Adresse. Ein Entwickler sieht sie sich an, wie Kunden und Google sie sehen, und schickt Ihnen eine kurze Liste, was zuerst zu tun ist. Unverbindlich.",
    body="""<section data-scene="lens"><h2>Was wir prüfen</h2><ul class="grid-4 link-cards plain-cards">
<li class="card"><strong>Ladezeit auf dem Smartphone</strong><span class="note">Core Web Vitals, mit Zahlen.</span></li>
<li class="card"><strong>Mobile Ansicht</strong><span class="note">Texte, Schaltflächen und Menüs in Smartphone-Breite.</span></li>
<li class="card"><strong>SEO-Grundlagen</strong><span class="note">Titel, Beschreibungen, Überschriften, Indexierung.</span></li>
<li class="card"><strong>Kontaktformular</strong><span class="note">Wir senden einen Test und prüfen, ob er ankommt.</span></li>
</ul></section>
<section data-scene="ring" class="offer card"><div><h2>Check anfordern</h2><p>Wählen Sie im Formular „Kostenloser Website-Check“ und tragen Sie Ihre Website-Adresse in die Nachricht ein.</p></div><p><a class="btn magnetic" href="/de/contact/?service=Kostenloser+Website-Check">Check anfordern</a></p></section>""",
)

PAGES["readiness-check"] = dict(
    title="Kostenloser Readiness-Check für den Auslandsstart | Kayonne Global",
    desc="Erfahren Sie, was bei der Übersetzung Ihrer Website kaputtgehen würde, mit welchem Markt Sie beginnen sollten und was es braucht. Kostenloser Check von Kayonne Global.",
    label="Kayonne Global · Kostenlos", h1="Ist Ihre Website bereit für eine weitere Sprache?",
    lede="Wir sehen uns Ihre Website mit den Augen eines Entwicklers und eines Übersetzers an und sagen Ihnen, was bei einer Übersetzung kaputtgehen würde und welcher Markt sich zuerst lohnt.",
    body="""<section data-scene="check"><h2>Was wir prüfen</h2><ul class="grid-4 link-cards plain-cards">
<li class="card"><strong>Text in Bildern</strong><span class="note">Wörter in Grafiken lassen sich nicht übersetzen.</span></li>
<li class="card"><strong>Layout</strong><span class="note">Schaltflächen und Menüs, die bei 30 % längerem Deutsch brechen.</span></li>
<li class="card"><strong>Plattform</strong><span class="note">Ob Ihr CMS oder Shop mehrere Sprachen gut unterstützt.</span></li>
<li class="card"><strong>Markt</strong><span class="note">Suchnachfrage, Währung, Zahlungsarten und rechtliche Seiten.</span></li>
</ul></section>
<section data-scene="plane" class="offer card"><div><h2>Check anfordern</h2><p>Wählen Sie im Formular „Kostenloser Readiness-Check“, fügen Sie Ihre Website-Adresse und die geplanten Märkte hinzu.</p></div><p><a class="btn magnetic" href="/de/contact/?service=Kostenloser+Readiness-Check">Check anfordern</a></p></section>""",
)

PAGES["multilingual-seo"] = svc(
    title="Mehrsprachige SEO-Agentur | Kayonne Global",
    desc="Mehrsprachige und internationale SEO: Keyword-Recherche durch Muttersprachler in jedem Markt, hreflang, übersetzte Metadaten und Sprach-URLs, von einem Team, das baut und übersetzt.",
    label="Mehrsprachige SEO", h1="Gefunden in jeder Sprache, in der Sie verkaufen.",
    lede="In Deutschland sucht man anders als in Glasgow, auch wenn man dasselbe will. Wir recherchieren Suchbegriffe in jedem Markt mit Muttersprachlern und bauen die Seiten passend dazu.",
    why=["Keyword-Recherche durch Muttersprachler statt übersetzter Keywords", "Dasselbe Team korrigiert den Code, schreibt die Seiten und übersetzt sie", "Berichte je Markt aus der Search Console"],
    incl=["Internationale Keyword-Recherche", "Hreflang und Sprachordner", "Übersetzte Titel, Beschreibungen und URLs", "Lokale Content-Briefings", "Technische Audits mehrsprachiger Websites", "Berichte je Markt"],
    steps=[("Märkte", "Welche Länder, welche Sprachen, welche Seiten zuerst."),
           ("Recherche", "Muttersprachler recherchieren, was Menschen tatsächlich eintippen."),
           ("Umsetzung", "Ordner, hreflang, Metadaten und interne Links."),
           ("Bericht", "Search Console je Markt, jeden Monat.")],
    who="Unternehmen, die bereits in Großbritannien verkaufen und in Deutschland, Europa oder Asien gefunden werden wollen.",
    faq=[("Können wir nicht einfach unsere Keywords übersetzen?", "Meist nicht. Siehe <a href=\"/de/insights/multilingual-seo-keywords/\">warum übersetzte Keywords scheitern</a>."),
         ("Garantieren Sie Rankings?", "Das kann niemand. Wir beheben, was wir beeinflussen können, und berichten darüber.")],
)

PAGES["international-launch"] = svc(
    title="Internationaler Website-Start | Kayonne Global",
    desc="Bringen Sie Ihre Website mit einem Team in einen neuen Markt: Analyse, Keyword-Recherche, Entwicklung, Übersetzung, Prüfung und Start, gesteuert aus Glasgow.",
    label="Internationaler Marktstart", h1="Ihr nächster Markt, gestartet von einem Team.",
    lede="Ein fester Plan, um Ihre Website oder Ihren Shop in eine neue Sprache zu bringen: Das Entwicklungsteam bereitet die Website vor, das Übersetzungsteam schreibt sie in der neuen Sprache, und eine Projektleitung steuert beides.",
    why=["Eine Projektleitung statt Agentur plus Übersetzer", "Suchbegriffe recherchiert, bevor ein Wort übersetzt wird", "Jede Seite in jeder Sprache auf dem Smartphone geprüft"],
    incl=["Readiness-Analyse", "Keyword-Recherche je Markt", "Sprachordner, hreflang und lokale Formate", "Übersetzung und Revision durch eine zweite Fachkraft", "Prüfung rechtlicher Seiten wie des Impressums für Deutschland", "Startbericht und Review nach 30 Tagen"],
    steps=[("Plan", "Märkte, Seiten und Starttermin schriftlich vereinbart."),
           ("Vorbereitung", "Die Website wird übersetzungsbereit gemacht."),
           ("Lokalisierung", "Übersetzung, Revision und Prüfung im Kontext."),
           ("Start", "Livegang, Sitemaps einreichen, Review nach 30 Tagen.")],
    who="Britische Unternehmen, die erstmals nach Deutschland, Europa oder Asien gehen.",
    faq=[("Wie lange dauert ein Marktstart?", "Das hängt von Seiten- und Sprachanzahl ab. Im Angebot steht ein Termin für jede Phase."),
         ("Brauchen Sie Zugang zu unserer Website?", "Ja, oder zu Ihrem Entwickler. Die Konten bleiben auf Ihren Namen.")],
)

PAGES["ecommerce-localisation"] = svc(
    title="Shopify- und WooCommerce-Shop lokalisieren | Kayonne Global",
    desc="Übersetzen und lokalisieren Sie Ihren Shopify- oder WooCommerce-Shop: Produkte, Checkout, E-Mails, Währung und SEO, mit menschlicher Übersetzung und zweiter Prüfung.",
    label="Shop-Lokalisierung", h1="Ihr Shop, geöffnet in einer weiteren Sprache.",
    lede="Wir lokalisieren Shopify- und WooCommerce-Shops vollständig: Produktseiten, Kategorien, Checkout, Bestellmails, Währung und die Suchbegriffe, mit denen man Sie findet.",
    why=["Produkte, Checkout und E-Mails übersetzt, nicht nur die Startseite", "Preise, Währung und Formate je Markt", "Produkttitel für die Suche im jeweiligen Markt recherchiert"],
    incl=["Shopify Markets einrichten", "WooCommerce mit WPML oder Polylang", "Produkt- und Kategorieübersetzung", "Checkout- und E-Mail-Vorlagen", "Währung, Steueranzeige und Formate", "Mehrsprachige SEO für Produkte"],
    steps=[("Prüfung", "Wir prüfen Theme, Apps und Katalogumfang."),
           ("Einrichtung", "Märkte, Sprachen, Währungen und URLs."),
           ("Übersetzung", "Zuerst Produkte, dann Seiten, Checkout und E-Mails."),
           ("Test", "Eine Testbestellung in jeder Sprache vor dem Start.")],
    who="Onlineshops, die in Deutschland, Frankreich, Spanien oder weiter weg verkaufen wollen.",
    faq=[("Übersetzen Sie tausende Produkte?", "Ja. Große Kataloge können maschinell übersetzt und bei Bestsellern von Menschen nachbearbeitet werden."),
         ("Wird der Shop dadurch langsamer?", "Nein. Wir messen die Ladezeit vorher und nachher.")],
)

LANG_DE = {
    "polish": ("Polnisch", "Namen und Orte behalten ihre polnischen Buchstaben (ą, ć, ę, ł, ń, ó, ś, ź, ż) genau wie im Original, damit sie mit Pässen und Registern übereinstimmen.",
               ["Geburtsurkunden (odpis aktu urodzenia)", "Heiratsurkunden", "Führerscheine", "Schul- und Hochschulzeugnisse", "Führungszeugnisse"]),
    "romanian": ("Rumänisch", "Wir übernehmen ș und ț in Namen genau wie geschrieben und übersetzen Stempel und handschriftliche Vermerke auf Personenstandsurkunden.",
                 ["Geburtsurkunden (certificat de naștere)", "Heiratsurkunden", "Führungszeugnisse", "Diplome und Notenübersichten", "Kontoauszüge"]),
    "arabic": ("Arabisch", "Arabisch wird von rechts nach links gelesen, manche Dokumente nutzen Hidschri-Daten. Wir ergänzen das gregorianische Datum, wo nötig, und schreiben Namen wie im Pass.",
               ["Geburts- und Heiratsurkunden", "Familienregister", "Abschlüsse und Notenübersichten", "Gerichtsunterlagen", "Arztberichte"]),
    "urdu": ("Urdu", "Urdu wird von rechts nach links in Nastaliq geschrieben. Namen werden in Dokumenten oft unterschiedlich geschrieben; nennen Sie uns die Schreibweise im Pass, und wir verwenden sie durchgehend.",
             ["Geburtsurkunden (NADRA)", "Heiratsurkunden (nikah nama)", "Familienregisterauszüge", "Bildungsnachweise", "Kontoauszüge"]),
    "chinese": ("Chinesisch", "Vereinfachtes Chinesisch gilt in Festlandchina und Singapur, traditionelles in Hongkong und Taiwan. Chinesische Namen stehen mit dem Familiennamen zuerst; wir übernehmen die Reihenfolge aus dem Pass.",
                ["Haushaltsregister (hukou)", "Notarielle Bescheinigungen", "Abschlusszeugnisse und Notenübersichten", "Gewerbelizenzen", "Kontoauszüge"]),
    "spanish": ("Spanisch", "Spanien und Lateinamerika unterscheiden sich in Wortschatz und Formaten, nennen Sie uns das Land. Spanische Dokumente führen oft zwei Nachnamen, und wir behalten beide.",
                ["Geburtsurkunden (partida de nacimiento)", "Heiratsurkunden", "Studiennachweise", "Verträge", "Arztberichte"]),
    "french": ("Französisch", "Französisch aus Frankreich, Belgien, der Schweiz, Kanada und Afrika unterscheidet sich in Begriffen und Formaten. Wir richten uns nach dem Land des Dokuments oder der Leser.",
               ["Geburtsurkunden (acte de naissance)", "Heiratsurkunden", "Diplome", "Verträge", "Unternehmensdokumente"]),
    "german": ("Deutsch", "Schweizer Dokumente verwenden ss statt ß, und wir halten deutsche, österreichische und Schweizer Begriffe auseinander.",
               ["Geburtsurkunden", "Heiratsurkunden", "Führungszeugnisse", "Abschlüsse und Notenübersichten", "Arbeitszeugnisse"]),
    "ukrainian": ("Ukrainisch", "Namen werden genau wie im ukrainischen Pass transliteriert, damit alle Dokumente übereinstimmen. Wir übersetzen auch russischsprachige Dokumente aus der Ukraine.",
                  ["Geburtsurkunden", "Heiratsurkunden", "Diplome und Notenübersichten", "Führerscheine", "Krankenakten"]),
    "portuguese": ("Portugiesisch", "Portugiesisch aus Portugal und Brasilien unterscheidet sich in Schreibung und Begriffen, nennen Sie uns die Variante. Lange portugiesische und brasilianische Namen bleiben vollständig.",
                   ["Geburtsurkunden (certidão de nascimento)", "Heiratsurkunden", "Diplome", "Führungszeugnisse", "Kontoauszüge"]),
}

for _slug, (_name, _note, _docs) in LANG_DE.items():
    _native = LANG_PAIRS[_slug]["native"]
    PAGES[f"languages/{_slug}"] = svc(
        title=f"Übersetzung {_name}–Englisch | Kayonne Language",
        desc=f"Fachübersetzungen {_name}–Englisch und Englisch–{_name}: Dokumente, Recht, Medizin, Business, Websites und Untertitel.",
        label=f"{_name} · <span lang=\"und\">{_native}</span>", h1=f"{_name}, ins Englische und aus dem Englischen.",
        lede=f"Qualifizierte Übersetzer für {_name}: Dokumente, Recht und Medizin, Geschäftstexte, Websites und Untertitel. Jeder Auftrag wird von einer zweiten Fachkraft geprüft.",
        why=[_note, "Layout nah am Originaldokument", "Eine zweite Fachkraft prüft jeden Auftrag"],
        incl=[f"Übersetzung {_name}–Englisch", f"Übersetzung Englisch–{_name}"] + _docs,
        steps=[("Hochladen", "Foto, Scan oder Datei über das Anfrageformular senden."),
               ("Angebot", "Festpreis und Termin."),
               ("Übersetzung", f"Eine muttersprachliche Fachkraft für {_name} übernimmt."),
               ("Prüfung", "Eine zweite Fachkraft revidiert vor der Lieferung.")],
        who=f"Menschen und Unternehmen, die {_name.lower()}e Dokumente auf Englisch oder englische Inhalte auf {_name} brauchen." if _name.endswith("isch") else f"Menschen und Unternehmen, die Dokumente auf {_name} ins Englische oder englische Inhalte auf {_name} brauchen.",
        faq=[(f"Welche Dokumente auf {_name} übersetzen Sie?", f"Private, juristische, medizinische, geschäftliche und technische Dokumente, in beide Richtungen. Siehe <a href=\"/de/documents/\">Dokumentübersetzung</a>."),
             ("Wie erhalte ich einen Preis?", f"Laden Sie das Dokument über das <a href=\"/de/contact/\">Anfrageformular</a> hoch und wählen Sie {_name} als Sprache.")],
    )

PAGES["insights/website-cost-glasgow"] = dict(
    title="Was kostet eine Website in Glasgow 2026? | Kayonne",
    desc="Website-Preise in Glasgow 2026: Vorlagen, kleine Unternehmensseiten, individuelle Entwicklung und Shops, was den Preis verändert und welche laufenden Kosten man vergisst.",
    label="Ratgeber · Websites", h1="Was kostet eine Website in Glasgow 2026?",
    lede="Eine Website in Glasgow kostet zwischen einigen hundert und weit über zehntausend Pfund. Das bekommen Sie auf jeder Stufe, und das verändert den Preis.",
    body="""<article class="prose">
<p class="byline">Vom Team Kayonne Digital.</p>
<h2>Typische Preisspannen</h2>
<div class="table-wrap"><table><thead><tr><th scope="col">Art</th><th scope="col">Typischer Preis in Glasgow</th></tr></thead><tbody>
<tr><td>Vorlagen-Website</td><td class="n">ab etwa £300</td></tr>
<tr><td>Kleine Unternehmensseite, bis 5 Seiten</td><td class="n">etwa £400 bis £1.500</td></tr>
<tr><td>Individuelles Design vom Studio</td><td class="n">meist £2.000 bis £5.000</td></tr>
<tr><td>Größere Projekte und Shops</td><td class="n">£5.000 bis £10.000 und mehr</td></tr>
<tr><td>Website im Monatsabo</td><td class="n">etwa £25 bis £50 im Monat</td></tr>
</tbody></table></div>
<p class="note">Auf Basis von Preisen, die Studios in Glasgow 2026 veröffentlicht haben. Prüfen Sie aktuelle Preise beim jeweiligen Studio.</p>
<h2>Was den Preis verändert</h2>
<ul><li>Seitenzahl und wie viel Text geschrieben werden muss.</li><li>Ein Shop: Produkte, Zahlungen, Versandregeln.</li><li>Individuelles Design oder Vorlage.</li><li>Buchungen, Logins oder Anbindungen an andere Software.</li><li>Mehr als eine Sprache.</li></ul>
<h2>Laufende Kosten, die man vergisst</h2>
<ul><li>Jährliche Domainverlängerung.</li><li>Hosting.</li><li>Geschäftliche E-Mail wie Google Workspace oder Microsoft 365, pro Person und Monat.</li><li>Updates und Backups, als eigene Zeit oder Wartungsplan.</li></ul>
<h2>So berechnen wir</h2>
<p>Jede Website erhält nach einem kurzen Briefing ein schriftliches Festpreisangebot. Siehe <a href="/de/pricing/">Preise</a> oder lassen Sie zuerst Ihre aktuelle Website <a href="/de/website-check/">kostenlos prüfen</a>.</p>
</article>""",
)

PAGES["insights/multilingual-seo-keywords"] = dict(
    title="Mehrsprachige SEO: Warum Sie Keywords nicht einfach übersetzen können | Kayonne",
    desc="Warum übersetzte Keywords in der internationalen SEO scheitern, mit Beispielen, und wie man Suchbegriffe je Markt richtig recherchiert.",
    label="Ratgeber · Mehrsprachige SEO", h1="Mehrsprachige SEO: Warum Sie Keywords nicht einfach übersetzen können",
    lede="Ein Keyword, das Ihnen in Großbritannien Kunden bringt, kann in Deutschland wortwörtlich übersetzt niemanden bringen. Hier ist der Grund und was Sie stattdessen tun sollten.",
    body="""<article class="prose">
<p class="byline">Vom Team Kayonne Global.</p>
<h2>Menschen suchen mit ihren eigenen Wörtern</h2>
<p>Britische Käufer suchen nach <i>trainers</i>, amerikanische nach <i>sneakers</i>. In Deutschland heißt ein Mobiltelefon <i>Handy</i>, ein Wort, das kein englisches Wörterbuch liefert. Eine direkte Übersetzung ist oft richtig und trotzdem nicht das, was jemand eintippt.</p>
<h2>Gleiche Absicht, andere Suche</h2>
<p>Selbst wenn die Bedeutung übereinstimmt, unterscheiden sich die Gewohnheiten: Manche Märkte suchen kürzer, manche ergänzen die Stadt, manche suchen bei technischen Produkten auf Englisch. Jeder Markt braucht eigene Recherche.</p>
<h2>So geht es richtig</h2>
<ol><li>Listen Sie die Seiten, die verkaufen, nicht jede Seite.</li><li>Lassen Sie Muttersprachler recherchieren, wonach im Markt gesucht wird.</li><li>Prüfen Sie die Suchabsicht: Bringt der Begriff Käufer oder Studierende?</li><li>Schreiben Sie Titel, Überschriften und URLs um diese Begriffe.</li><li>Setzen Sie hreflang, damit jeder Markt die richtige Version sieht.</li><li>Verfolgen Sie jeden Markt getrennt in der Search Console.</li></ol>
<p>So arbeiten wir bei der <a href="/de/multilingual-seo/">mehrsprachigen SEO</a>.</p>
</article>""",
)
