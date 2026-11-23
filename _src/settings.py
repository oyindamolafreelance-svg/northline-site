"""Contact details and the person shown on the site. Fill these in and rebuild.

Anything left empty is simply not shown: no placeholder ever appears on the site.
"""

# Phone, shown in the footer and on /contact/ as a tap-to-call link. International format, e.g. "+44 141 000 0000".
PHONE = ""
# A US phone number for the Kayonne Growth pages. When set, Growth pages show it instead of PHONE.
PHONE_US = ""
# Company registration number, shown in the footer, e.g. "SC123456".
COMPANY_NO = ""
# LinkedIn profile or company page, e.g. "https://www.linkedin.com/in/...". Adds the footer icon and the link on the person block.
LINKEDIN_URL = ""

# The "Who you'll work with" block on /about/ and /growth/.
PERSON = dict(
    name="Oyindamola Ogunsanmi",
    role="Founder and project lead",
    # Photo path, e.g. "/img/team/oyindamola.webp" (square, at least 400 x 400). Until set, initials are shown.
    photo="",
    bio="Oyindamola runs Kayonne Creatives and leads every project from the first call to handover. "
        "You talk to the same person from start to finish.",
)
