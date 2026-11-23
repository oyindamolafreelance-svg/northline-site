"""Kayonne Growth pages. US English, English only (no German version).

/growth/ uses kind="growth_hub" and every /growth/<niche>/ page uses kind="growth_niche".
To add a trade, copy the "growth/septic" entry, change its text, and add it to the Growth
items in divisions.py so it shows in the menu, the footer and the "Who we work with" list.

Sections set to None are hidden: fill "video", "results" or "testimonial" to show them.
"""

TRUST = [("badge", "30-day guarantee"), ("lock", "Your leads are never shared")]
GUARANTEE = "If we don't deliver in your first 30 days, you don't pay our fee."

PAGES = {}

PAGES["growth"] = dict(
    kind="growth_hub", division="growth",
    title="Kayonne Growth | More customers for local service businesses",
    desc="Kayonne Growth brings local service businesses a steady flow of new customers who are ready to book. Book a free 15-minute call.",
    label="Kayonne Growth",
    h1="More customers. Less guessing.",
    lede="Kayonne Growth brings local service businesses a steady flow of new customers who are ready to book.",
    phone=dict(company="Your Company", sub="Local home services",
               ad="Need it fixed this week? Friendly local crew, appointments this week.",
               notice="New inquiry", notice_sub="Homeowner, nearby"),
    who_h="Who we work with",
    who="We work with service businesses whose customers have a real, urgent need. We focus on one trade at a time, so we understand your customers before we start.",
    trades_h="Trades we currently work with",
    trades=[("growth/septic", "Septic companies", "drop")],
    video=None,  # e.g. dict(src="/media/growth-hello.mp4", poster="/media/growth-hello.webp", caption="A quick hello from the team.")
    get_h="What you get",
    get=[("pin", "New inquiries from homeowners in your area"),
         ("shield", "Only serious inquiries, checked before they reach you"),
         ("chart", "Clear updates, so you always know what's working")],
    faq=[("Do I need a website?", "No. We can get you customers whether you have a website or not."),
         ("Is there a long contract?", "No. We start with 30 days. If it works, we keep going month to month."),
         ("Who are you?", "Kayonne Growth is part of Kayonne Creatives, a UK company that also builds websites and handles translation for businesses.")],
    results=None,  # future case studies: list of dict(title=..., text=...)
    closing="Let's see if we're a good fit. It takes 15 minutes.",
    smallprint="",
)

PAGES["growth/septic"] = dict(
    kind="growth_niche", division="growth",
    title="Kayonne Growth | More jobs for septic companies",
    desc="More drain-field and replacement jobs for your septic company: homeowners in your area with real septic problems, ready to book an estimate.",
    label="Kayonne Growth · Septic companies", crumb="Septic companies",
    h1="More drain-field and replacement jobs for your septic company.",
    lede="We bring you homeowners in your area with real septic problems, ready to book an estimate.",
    phone=dict(company="Your Septic Co.", sub="Septic service and repair",
               ad="Septic backing up? Local septic pros. Estimates this week.",
               notice="New inquiry: septic backup", notice_sub="4 miles away"),
    pains_h="Sound familiar?",
    pains=["Most of your work comes from word of mouth, so some months are busy and others go quiet.",
           "Lead websites often share the same inquiry with other companies.",
           "You spend time on calls that go nowhere."],
    calendars=dict(h="Quiet month vs busy month", left="Word of mouth only", right="With Kayonne Growth"),
    changes_h="What changes when you work with us",
    changes=[("phone", "More calls from homeowners who need you now"),
             ("lock", "Inquiries that come only to you, never shared with competitors"),
             ("clock", "Less time wasted on people who were never going to book")],
    example_h="Example inquiry",
    example=[("Homeowner", "4 miles away"), ("Problem", "sewage backing up"), ("Owns the home", "Yes"), ("Wants it fixed", "this week")],
    calc_h="What would a few extra jobs be worth to you?",
    faq=[("Does this work for bigger jobs, not just pumping?", "Yes. We focus on the jobs you want most."),
         ("Is there a long contract?", "No. We start with 30 days, then go month to month.")],
    testimonial=None,  # dict(quote=..., name=..., company=...) once a septic client agrees to be quoted
    closing="Want to see if your area is a good fit? It takes 15 minutes.",
    smallprint="Kayonne Growth is part of Kayonne Creatives, UK.",
)

for _p in PAGES.values():
    _p.update(html_lang="en-US", og_locale="en_US", script='<script src="/js/growth.js" defer></script>')
