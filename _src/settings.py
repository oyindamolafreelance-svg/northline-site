"""Contact details and the person shown on the site. Fill these in and rebuild.

Anything left empty is simply not shown: no placeholder ever appears on the site.
"""

# Phone, shown in the footer and on /contact/ as a tap-to-call link. International format, e.g. "+44 141 000 0000".
PHONE = ""
# A US phone number for the Kayonne Growth pages. When set, Growth pages show it instead of PHONE.
PHONE_US = ""
# Company registration number, shown as "Company no. ..." in the footer and on /contact/, e.g. "SC123456".
COMPANY_NO = ""
# LinkedIn company page, e.g. "https://www.linkedin.com/company/...". Adds the LinkedIn icon in the footer and on /contact/.
LINKEDIN_COMPANY_URL = ""
# LinkedIn profile of the person below, e.g. "https://www.linkedin.com/in/...". Adds a link on the person block.
LINKEDIN_URL = ""

# Kayonne Growth founding partner offer on /growth/ and every /growth/<trade>/ page.
# Raise FOUNDING_TAKEN by one each time a founding partner joins. Set FOUNDING_TOTAL to 0 to hide the banner.
FOUNDING_TOTAL = 5
FOUNDING_TAKEN = 0

# ---- Trust slots: hidden until filled. Only real, checkable details belong here. ----
# Google review rating, shown on the home page, e.g. dict(rating=4.9, count=12, url="https://g.page/...").
GOOGLE_REVIEWS = None
# Real testimonials, used only with the client's permission, shown on the home page.
# e.g. [dict(quote="...", name="Jane Smith", role="Owner, Smith Plumbing", team="growth")]
TESTIMONIALS = []
# Case studies, shown on the home page. e.g. [dict(title="...", text="...", team="localize", href="/work/")]
CASE_STUDIES = []
# Real photos of the team leads, by team: replaces the illustrated avatar. e.g. {"digital": "/img/team/digital.webp"}
LEAD_PHOTOS = {}

# The "Who you'll work with" block on /about/ and /growth/.
PERSON = dict(
    name="Oyindamola Ogunsanmi",
    role="Founder and project lead",
    # Photo path, e.g. "/img/team/oyindamola.webp" (square, at least 400 x 400). Until set, initials are shown.
    photo="",
    bio="Oyindamola runs Kayonne Creatives and leads every project from the first call to handover. "
        "You talk to the same person from start to finish.",
)
