"""Build index.html from content.json.   Usage:  python3 build.py
Edit content.json (products, prices, WhatsApp number, email), run this, then publish."""

import json
import re
from pathlib import Path
from urllib.parse import quote

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent
c = json.loads((ROOT / "content.json").read_text(encoding="utf-8"))


def digits(s: str) -> str:
    return re.sub(r"\D", "", s or "")


def enquire(product=None):
    """(url, label): WhatsApp if a number is set, else email, else an Instagram message."""
    what = f"{product['name']} ({product['price']})" if product else "your candles"
    text = f"Hi Soulmade! I'd like to enquire about {what}."
    if digits(c.get("whatsapp")):
        return f"https://wa.me/{digits(c['whatsapp'])}?text={quote(text)}", "Enquire on WhatsApp"
    if c.get("email"):
        return f"mailto:{c['email']}?subject={quote('Enquiry: ' + (product['name'] if product else 'candles'))}&body={quote(text)}", "Enquire by email"
    return f"https://ig.me/m/{c['instagram']}", "Message us on Instagram"


products = [{**p, "url": enquire(p)[0], "label": enquire(p)[1]} for p in c["products"]]
general_url, general_label = enquire()
env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html", "j2"]))
html = env.get_template("index.html.j2").render(
    c=c, products=products, general_url=general_url, general_label=general_label,
    has_whatsapp=bool(digits(c.get("whatsapp"))), has_email=bool(c.get("email")),
)
(ROOT / "index.html").write_text(html, encoding="utf-8")
(ROOT / "CNAME").write_text(c["domain"].replace("https://", "").strip("/") + "\n", encoding="utf-8")
(ROOT / ".nojekyll").write_text("", encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {c['domain']}/sitemap.xml\n", encoding="utf-8")
(ROOT / "sitemap.xml").write_text(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{c["domain"]}/</loc></url></urlset>\n',
    encoding="utf-8")
print(f"built index.html with {len(products)} products; enquiries go to: {general_label}")
