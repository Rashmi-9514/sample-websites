import os

EXCLUDE = {"index.html"}

def get_icon(filename):
    f = filename.lower()
    if "push" in f:     return "🔔"
    if "inbox" in f:    return "📬"
    if "visual" in f:   return "🎨"
    if "display" in f:  return "🖥️"
    if "rudder" in f:   return "🔀"
    if "axis" in f:     return "🎯"
    if "pe" in f:       return "⚡"
    if "sample" in f:   return "⚡"
    return "🌐"

def get_tag(filename):
    f = filename.lower()
    if "push" in f:     return "Push"
    if "inbox" in f:    return "Inbox"
    if "visual" in f:   return "Builder"
    if "display" in f:  return "Display"
    if "rudder" in f:   return "Integration"
    if "axis" in f:     return "PE · Axis"
    if "pe" in f:       return "Web SDK"
    if "sample" in f:   return "Demo"
    return "Demo"

def get_title(filename):
    name = filename.replace(".html", "").replace("_", " ").replace("-", " ")
    return " ".join(word.capitalize() for word in name.split())

def get_desc(filename):
    f = filename.lower()
    if "push" in f:         return "Web push notification setup and integration demo."
    if "inbox" in f:        return "Web inbox messaging feature demo and implementation."
    if "visual" in f:       return "Visual builder for creating web campaigns and layouts."
    if "display2" in f:     return "Banner & carousel display demo with CleverTap event tracking."
    if "display" in f:      return "Core web native display component showcase."
    if "rudder" in f:       return "Sample integration connecting RudderStack with CleverTap."
    if "axis" in f:         return "Product Experiences demo tailored for the Axis use case."
    if "pe" in f:           return "Product Experiences demo via the CleverTap Web SDK."
    if "sample" in f:       return "Sample demo page with CleverTap integration."
    return "Demo page hosted on GitHub Pages."

html_files = sorted([
    f for f in os.listdir(".")
    if f.endswith(".html") and f not in EXCLUDE
])

cards = ""
for i, f in enumerate(html_files, 1):
    cards += f"""
      <a class="card" href="{f}" target="_blank">
        <span class="card-number">{str(i).zfill(2)}</span>
        <span class="card-tag">{get_tag(f)}</span>
        <div class="card-icon">{get_icon(f)}</div>
        <div class="card-title">{get_title(f)}</div>
        <div class="card-desc">{get_desc(f)}</div>
        <div class="card-arrow">Open demo →</div>
      </a>
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Rashmi's Demo Websites</title>
  <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap" rel="stylesheet"/>
  <style>
    :root {{
      --bg: #f5f0eb;
      --card: #fff;
      --border: #e0d8d0;
      --accent: #c0392b;
      --text: #1a1412;
      --muted: #8a7f78;
    }}

    * {{ margin: 0; padding: 0; box-sizing: border-box; }}

    body {{
      background: var(--bg);
      color: var(--text);
      font-family: 'Syne', sans-serif;
      min-height: 100vh;
    }}

    .container {{
      max-width: 960px;
      margin: 0 auto;
      padding: 60px 24px 80px;
    }}

    header {{ margin-bottom: 52px; }}

    .eyebrow {{
      font-family: 'Space Mono', monospace;
      font-size: 11px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 12px;
    }}

    h1 {{
      font-size: clamp(2.2rem, 5vw, 3.5rem);
      font-weight: 800;
      line-height: 1.05;
      letter-spacing: -0.02em;
      color: var(--text);
    }}

    .subtitle {{
      margin-top: 10px;
      font-family: 'Space Mono', monospace;
      font-size: 12px;
      color: var(--muted);
    }}

    .section-label {{
      font-family: 'Space Mono', monospace;
      font-size: 10px;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 20px;
    }}

    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 16px;
    }}

    .card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 24px;
      text-decoration: none;
      color: var(--text);
      display: flex;
      flex-direction: column;
      gap: 10px;
      position: relative;
      transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }}

    .card:hover {{
      transform: translateY(-4px);
      border-color: var(--accent);
      box-shadow: 0 12px 32px rgba(0,0,0,0.08);
    }}

    .card-number {{
      font-family: 'Space Mono', monospace;
      font-size: 10px;
      color: var(--muted);
    }}

    .card-tag {{
      position: absolute;
      top: 24px;
      right: 20px;
      font-family: 'Space Mono', monospace;
      font-size: 9px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--muted);
      border: 1px solid var(--border);
      padding: 3px 8px;
      border-radius: 99px;
    }}

    .card-icon {{ font-size: 1.8rem; }}

    .card-title {{
      font-size: 1rem;
      font-weight: 700;
      letter-spacing: -0.01em;
    }}

    .card-desc {{
      font-family: 'Space Mono', monospace;
      font-size: 11px;
      color: var(--muted);
      line-height: 1.6;
      flex: 1;
    }}

    .card-arrow {{
      font-family: 'Space Mono', monospace;
      font-size: 10px;
      color: var(--accent);
      margin-top: 4px;
    }}

    footer {{
      margin-top: 60px;
      display: flex;
      justify-content: space-between;
      font-family: 'Space Mono', monospace;
      font-size: 11px;
      color: var(--muted);
      border-top: 1px solid var(--border);
      padding-top: 24px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="eyebrow">Rashmi-9514 · GitHub Pages</div>
      <h1>Demo<br>Websites</h1>
      <p class="subtitle">// Click any card to open the demo</p>
    </header>

    <p class="section-label">// All pages — {len(html_files)} demos</p>

    <div class="grid">
{cards}
    </div>

    <footer>
      <span>Rashmi · Demo Collection</span>
      <span>{len(html_files)} demos</span>
    </footer>
  </div>
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(html)

print(f"✅ index.html generated with {len(html_files)} demos!")
