# Kayonne Creatives website

Source for https://kayonnecreatives.com, hosted on GitHub Pages. Every push to `main` deploys.

## How to edit

The pages are generated. Do not edit the HTML files by hand.

1. Change the text in `_src/content_en.py` (English) and `_src/content_de.py` (German).
   Both files must contain the same pages.
2. Run `python3 _src/build.py` from the repo root. It writes every page, the 404 page and `sitemap.xml`.
3. Commit the content files and the generated HTML together.

Shared header, footer, menus and page head live in `_src/build.py`. Styles are in `css/site.css`.

## Your details (phone, LinkedIn, company number, photo)

Fill them in `_src/settings.py` and rebuild. Each one appears on the site only once it is filled in:
phone in the footer and on /contact/ (a US number for Growth pages if you set `PHONE_US`), the company
number in the footer, the LinkedIn icon in the footer and on the person block, and the photo on the
"Who you'll work with" block on /about/ and /growth/ (initials are shown until a photo is set).

## Divisions (Digital, Localize, Growth)

The divisions are listed once, in `_src/divisions.py`. The menus, footer columns, home page chooser and
cards, service grids, pricing tables and the quote form's team picker are all generated from that list.
To add a "Kayonne Something" division: add an entry there, add its landing page with `kind="division"`
(and its rows to `PRICES`), then add its service pages.

- Kayonne Growth is English only (US English). Its pages are in `_src/content_growth.py`; a new trade is a
  copy of the `growth/septic` entry plus a menu item in `divisions.py`. Sections set to `None` (video,
  results, testimonial) stay hidden until filled.
- Every Growth booking button uses `GROWTH_BOOK_URL` in `_src/divisions.py`. Change it there to switch to a
  booking calendar.
- Old addresses that moved (`REDIRECTS` in `_src/build.py`) get a forwarding page. GitHub Pages cannot send
  real 301 redirects; the forwarding page tells browsers and search engines where the page went.
Fonts are self-hosted in `fonts/`, so no visitor data goes to Google.

## 3D, images and video

- `js/motion.js` runs the section animations, card tilt and video playback, then loads the 3D backdrop.
- `js/scene.js` holds every 3D scene. A section picks its scene with `data-scene="name"`; the page-top
  scene for each page is set in `SCENES` in `_src/build.py`. three.js is served from `js/` (MIT licence in
  `js/three-LICENSE.txt`).
- Visitors who ask for reduced motion or to save data get no 3D and no autoplay; they see the still images
  in `img/scenes/` instead.
- Videos are in `media/`. How to re-render stills and videos: `_src/media/README.md`.

## Quote form

The form on `/contact/` posts to FormSubmit (formsubmit.co), which emails it to hello@kayonnecreatives.com.
The first time someone submits it, FormSubmit sends an activation email to that address. Click the link in it,
or the form will not deliver anything.

## Still needed from the owner

- Company details for the footer: registered name, legal form, company number and registered office
  (or the owner's name and business address if a sole trader), VAT number if registered
- Phone or WhatsApp number, if you want one shown
- Starting prices, if you want them on the pricing page
- A solicitor's review of the privacy notice and terms
