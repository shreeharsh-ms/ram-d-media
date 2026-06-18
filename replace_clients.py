import re

with open("portfolio.html", "r") as f:
    content = f.read()

clients = [
    {
        "id": "Sirimirii",
        "url": "https://www.instagram.com/sirimiriirestaurant?igsh=eThjNDlvaGxmMTZp",
        "img": "LOGOS/sirimirii logo.png"
    },
    {
        "id": "Plan your home",
        "url": "https://www.instagram.com/planyourhome.in?igsh=cDk1dGo4OTlwcWd6",
        "img": "LOGOS/plan your home.png"
    },
    {
        "id": "Easy living",
        "url": "https://www.instagram.com/easy_living_official_?igsh=MWtmNWF0N2tjcjUxNg==",
        "img": "portfolio_data/images/EL Logo.png"
    },
    {
        "id": "Shree electricals",
        "url": "https://www.instagram.com/shree_electricals1974?igsh=MW84dmhjd3ExdnI4bQ==",
        "img": "portfolio_data/images/shree elctrcal white.png"
    },
    {
        "id": "ensure_to_insure",
        "url": None,
        "img": "ensure_to_insure.png",
        "bg_size": "contain"
    },
    {
        "id": "Rekha beauty parlour",
        "url": None,
        "img": "LOGOS/images.jpg"
    },
    {
        "id": "Sakarya",
        "url": None,
        "img": "portfolio_data/images/sakarya logo white.png",
        "bg_size": "contain"
    }
]

def make_card(c, is_mobile=False):
    click = f"onclick=\"window.open('{c['url']}', '_blank')\"" if c['url'] else ""
    cursor = "cursor: pointer;" if c['url'] else ""
    cls = "mobile-client-card" if is_mobile else "carousel-card"
    bg_size = c.get("bg_size", "contain")
    return f"""                <div class="{cls}"
                    {click}
                    style="background-image: url('{c['img']}'); background-size: {bg_size}; background-position: center; background-repeat: no-repeat; background-color: transparent; {cursor}">
                </div>"""

# Desktop Col 1
col1_html = '\n'.join([make_card(c) for c in clients] + [make_card(c) for c in clients])

# Desktop Col 2 (Reversed)
col2_html = '\n'.join([make_card(c) for c in reversed(clients)] + [make_card(c) for c in reversed(clients)])

# Mobile
mobile_html = '\n'.join([make_card(c, is_mobile=True) for c in clients] + [make_card(c, is_mobile=True) for c in clients])

# Replace clientsCol1
content = re.sub(
    r'(<div class="carousel-col carousel-up" id="clientsCol1">).*?(</div>\s*<div class="carousel-col carousel-down" id="clientsCol2">)',
    rf'\1\n{col1_html}\n            \2',
    content,
    flags=re.DOTALL
)

# Replace clientsCol2
content = re.sub(
    r'(<div class="carousel-col carousel-down" id="clientsCol2">).*?(</div>\s*</div>\s*</section>)',
    rf'\1\n{col2_html}\n            \2',
    content,
    flags=re.DOTALL
)

# Replace mobileCarousel
content = re.sub(
    r'(<div class="mobile-carousel-container" id="mobileCarousel">).*?(</div>\s*</section>\s*</div>)',
    rf'\1\n{mobile_html}\n            \2',
    content,
    flags=re.DOTALL
)

with open("portfolio.html", "w") as f:
    f.write(content)
