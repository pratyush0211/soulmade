# Soulmade website

A static site: no server, no database. Hosted free on GitHub Pages.

**Change products, prices, WhatsApp number or email:** edit `content.json`, then run
`python3 build.py` (needs `pip install jinja2`) and commit. It rebuilds `index.html`.

- `images/`: web-sized photos. Put new product photos here and reference them in `content.json`.
- Enquiry buttons use WhatsApp if `whatsapp` is set (digits with country code, e.g. `919XXXXXXXXX`),
  else email if `email` is set, else an Instagram message.
- Fonts (Cormorant Garamond, Allura, Jost) are self-hosted under the SIL Open Font License.
