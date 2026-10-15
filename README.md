# Kayonne Creatives website

Source for https://kayonnecreatives.com, hosted on GitHub Pages. Every push to `main` deploys.

## How to edit

The pages are generated. Do not edit the HTML files by hand.

1. Change the text in `_src/content_en.py` (English) and `_src/content_de.py` (German).
   Both files must contain the same pages.
2. Run `python3 _src/build.py` from the repo root. It writes every page, the 404 page and `sitemap.xml`.
3. Commit the content files and the generated HTML together.

Shared header, footer, menus and page head live in `_src/build.py`. Styles are in `css/site.css`.
Fonts are self-hosted in `fonts/`, so no visitor data goes to Google.

## Quote form

The form on `/contact/` posts to FormSubmit (formsubmit.co), which emails it to hello@kayonnecreatives.com.
The first time someone submits it, FormSubmit sends an activation email to that address. Click the link in it,
or the form will not deliver anything.

## Still needed from the owner

- Company details for the footer: registered name, legal form, company number and registered office
  (or the owner's name and business address if a sole trader), VAT number if registered
- Founder's name and photo for the About page
- Phone or WhatsApp number, if you want one shown
- Starting prices, if you want them on the pricing page
- A solicitor's review of the privacy notice and terms
