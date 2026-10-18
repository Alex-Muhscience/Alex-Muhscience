#!/usr/bin/env python3
"""Build the profile README's SVG assets in light and dark variants.

Run from the repository root:  python3 scripts/build_assets.py
Standard library only. Edit the content below, re-run, commit the output.
"""
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "dark": dict(
        panel="#0f1622", inset="#0b1019", stroke="#273244", text="#e6edf3",
        muted="#8b98a9", accent="#5b9cf8", accent2="#f2605c", ok="#3fb950", warn="#d6a13a",
        blue="#5b9cf8", red="#f2605c", green="#3fb950", amber="#d6a13a", violet="#a78bfa", teal="#2dd4bf", cyan="#38bdf8",
    ),
    "light": dict(
        panel="#f7f9fc", inset="#ffffff", stroke="#d5dce6", text="#0f172a",
        muted="#566273", accent="#2563eb", accent2="#dc2626", ok="#15803d", warn="#a16207",
        blue="#2563eb", red="#dc2626", green="#15803d", amber="#a16207", violet="#7c3aed", teal="#0f766e", cyan="#0369a1",
    ),
}

# --- content -----------------------------------------------------------------

NAME = "Alex Murimi Kamau"
STATUS = "open to remote · Nairobi, Kenya · UTC+3"
ROLE = ("Full-stack developer", " · systems that run in production")
ROTATING = [
    "I build and run production platforms end to end",
    "Payments, multi-tenancy, RBAC and audit trails",
    "Linux, Docker, CI/CD and keeping it all running",
]
CLOSING = (
    "Let's build something that lasts",
    "Open to full-stack and backend engineering roles, technical partnerships and product work where reliability matters.",
    "alex.kamau.2558@gmail.com",
)
# Link buttons: solid colours that read on both light and dark pages. (slug, label, colour, icon)
BUTTONS = [
    ("portfolio", "Portfolio", "#2563eb",
     '<circle cx="9" cy="9" r="7.2"/><ellipse cx="9" cy="9" rx="3.1" ry="7.2"/><path d="M1.8,9 H16.2"/>'),
    ("linkedin", "LinkedIn", "#0a66c2",
     '<rect x="1.5" y="1.5" width="15" height="15" rx="3"/><path d="M5.6,8 V13 M5.6,5.2 V5.3 M8.8,13 V8 M8.8,10.4 C8.8,7.4 12.6,7.4 12.6,10.4 V13"/>'),
    ("resume", "Résumé", "#15803d",
     '<path d="M4,1.5 H11 L14.5,5 V16.5 H4 Z M11,1.5 V5 H14.5 M6.5,9 H12 M6.5,12 H12"/>'),
    ("email", "Email", "#dc2626",
     '<rect x="1.5" y="3.5" width="15" height="11" rx="2"/><path d="M2,4.5 L9,10 L16,4.5"/>'),
    ("whatsapp", "WhatsApp", "#1da851",
     '<path d="M3.4,13.6 A7.2,7.2 0 1 1 5.6,15.4 L1.9,16.3 Z"/><path d="M6.7,6.3 C6.7,9.2 8.9,11.4 11.7,11.4"/>'),
]

# The header draws the stack as four layers, top to bottom. (name, tools, colour)
LAYERS = [
    ("INTERFACE", "React · Next.js · TypeScript", "blue"),
    ("APPLICATION", "Node.js · Laravel · FastAPI · Flask", "violet"),
    ("DATA", "PostgreSQL · MySQL · MongoDB · Redis", "teal"),
    ("INFRASTRUCTURE", "Linux · Docker · nginx · CI/CD", "amber"),
]

# Featured projects. Each card shows what the system does as a four-step flow.
# (slug, colour, status, title, description, flow steps, stack)
PROJECTS = [
    ("businessos", "blue", "in development · private", "BusinessOS",
     "Multi-tenant operating system for SMEs: CRM, sales, procurement, inventory, finance, HR and projects on one governed data model.",
     ["Tenant\nrequest", "Row-level\nsecurity", "Idempotent\nwrite", "Outbox +\nwebhooks"],
     ["Laravel 13", "Next.js 16", "PostgreSQL 18", "Redis", "Docker", "nginx"]),
    ("utdrs", "red", "live · Vercel + Render · Mozilla RCC Top 5", "UTDRS",
     "Unified threat detection and response: events run through ATT&CK-mapped rules, anomaly and ML detectors, and analysts triage alerts in a React dashboard.",
     ["Event", "ATT&CK\nrules", "Anomaly +\nML detectors", "Analyst\ntriage"],
     ["Python", "FastAPI", "React", "TypeScript", "MongoDB", "C", "Docker"]),
    ("secure-file-sharing", "cyan", "in development · private", "Secure File Sharing Platform",
     "Encrypted file sharing for teams: resumable uploads encrypted chunk by chunk, malware scanning before release and verified recipients.",
     ["Chunked\nupload", "AES-256-GCM\nat rest", "ClamAV\nquarantine", "Verified\ndownload"],
     ["Node.js", "Express", "MongoDB", "S3", "ClamAV", "libsodium", "Docker"]),
    ("euroafrique", "green", "in production · sole technical owner", "EuroAfrique Corporate Skills",
     "Corporate training platform: programme publishing, applications, M-Pesa and card payments, and automated enrolment documents.",
     ["Programme", "Application", "M-Pesa /\ncard payment", "Enrolment\ndocuments"],
     ["Laravel", "MySQL", "Redis", "Paystack", "M-Pesa", "Algolia", "Cloudflare"]),
    ("afriasia", "amber", "in production · sole technical owner", "AfriAsia Career Development Center",
     "Executive-training, booking and document platform with a public catalogue and an admin portal.",
     ["Catalogue", "Booking", "Paystack\nUSD / KES", "Invoice +\ncertificate"],
     ["Laravel 12", "Livewire", "Alpine.js", "Tailwind", "MySQL", "Redis"]),
    ("chania", "violet", "in production · sole technical owner", "Chania Publishers LMS",
     "Learning management system built from concept to production for an educational publisher.",
     ["Subscriber", "Verified\npayment", "Access\ncheck", "Video\nstream"],
     ["PHP", "MySQL", "JavaScript", "Linux"]),
    ("muhscience", "teal", "live on Vercel · open source", "Muhscience Tech Labs",
     "Company site on the Next.js App Router with server-handled enquiry forms, technical SEO and security headers.",
     ["Visitor", "App Router\npage", "Enquiry\nform", "Server\nhandler"],
     ["Next.js 15", "React 19", "TypeScript", "Tailwind", "shadcn/ui", "MongoDB"]),
]

# (when, role, where, kind) — newest first; kind is "now", "past" or "study"
JOURNEY = [
    ("Aug 2025 → now", "Full-Stack Developer & Technical Owner",
     "EuroAfrique Corporate Skills · Chania Publishers · AfriAsia Career Development Center", "now"),
    ("May – Aug 2025", "Freelance Web Development Tutor", "Self-employed", "past"),
    ("Aug 2024 – Feb 2025", "Network Technician", "Gicatech Enterprise Solutions", "past"),
    ("May – Aug 2024", "Software Development Intern", "Secunets Technologies", "past"),
    ("2021 – 2025", "BSc Computer Science, Second Class Honours (Upper)", "Kisii University", "study"),
]

# --- helpers -----------------------------------------------------------------


def svg(width, height, label, style, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" aria-label="{escape(label)}">\n'
        f"<style>{style}\n"
        "@media (prefers-reduced-motion: reduce){*{animation:none!important}.r1{opacity:1!important}}"
        f"</style>\n{body}\n</svg>\n"
    )


def base_style(t):
    return (
        f".s{{font-family:{SANS}}}.m{{font-family:{MONO}}}"
        f".t{{fill:{t['text']}}}.mu{{fill:{t['muted']}}}.ac{{fill:{t['accent']}}}"
        f".ok{{fill:{t['ok']}}}.warn{{fill:{t['warn']}}}"
    )


def slab(t, colour, cx, cy, a, b, depth):
    """One isometric layer: two side faces and a top face."""
    c = t[colour]
    top = f"{cx},{cy - b} {cx + a},{cy} {cx},{cy + b} {cx - a},{cy}"
    left = f"{cx - a},{cy} {cx},{cy + b} {cx},{cy + b + depth} {cx - a},{cy + depth}"
    right = f"{cx + a},{cy} {cx},{cy + b} {cx},{cy + b + depth} {cx + a},{cy + depth}"
    return (
        f'<polygon points="{left}" fill="{t["inset"]}" stroke="{c}" stroke-opacity=".55" stroke-linejoin="round"/>'
        f'<polygon points="{left}" fill="{c}" fill-opacity=".22"/>'
        f'<polygon points="{right}" fill="{t["inset"]}" stroke="{c}" stroke-opacity=".55" stroke-linejoin="round"/>'
        f'<polygon points="{right}" fill="{c}" fill-opacity=".1"/>'
        f'<polygon points="{top}" fill="{t["panel"]}" stroke="{c}" stroke-width="1.4" stroke-linejoin="round"/>'
        f'<polygon points="{top}" fill="{c}" fill-opacity=".14"/>'
    )


# --- hero --------------------------------------------------------------------


def hero(t):
    w, h = 1200, 320
    share = 100 // len(ROTATING)  # each line's slice of the cycle, in percent
    style = base_style(t) + (
        "@keyframes pulse{0%,100%{opacity:1}50%{opacity:.35}}"
        f"@keyframes rot{{0%{{opacity:0}}3%{{opacity:1}}{share - 3}%{{opacity:1}}{share}%,100%{{opacity:0}}}}"
        "@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}"
        ".p{animation:pulse 2.4s ease-in-out infinite}"
        f".r{{opacity:0;animation:rot {len(ROTATING) * 4}s linear infinite}}"
        ".b{animation:bob 5s ease-in-out infinite}"
    )
    rotating = "".join(
        f'<text class="m mu r{" r1" if i == 0 else ""}" style="animation-delay:{i * 4}s" '
        f'x="82" y="262" font-size="17">{escape(line)}</text>'
        for i, line in enumerate(ROTATING)
    )
    # Isometric stack: each layer is a slab (top face plus two sides), drawn bottom-up.
    cx, a, b, depth, first, step = 1036, 124, 62, 13, 88, 46
    slabs = ""
    for i in reversed(range(len(LAYERS))):
        name, tools, colour = LAYERS[i]
        c, cy = t[colour], first + i * step
        slabs += (
            f'<g class="b" style="animation-delay:{i * 0.35}s">'
            + slab(t, colour, cx, cy, a, b, depth)
            +
            f'<path d="M{cx - a - 6},{cy} H{cx - a - 34}" stroke="{c}" stroke-width="1.4"/>'
            f'<circle cx="{cx - a - 6}" cy="{cy}" r="2.6" fill="{c}"/>'
            f'<text class="m" x="{cx - a - 44}" y="{cy - 2}" font-size="12" font-weight="700" letter-spacing="1.3" text-anchor="end" fill="{c}">{name}</text>'
            f'<text class="s mu" x="{cx - a - 44}" y="{cy + 16}" font-size="13.5" text-anchor="end">{escape(tools)}</text>'
            + "</g>"
        )
    last = first + (len(LAYERS) - 1) * step
    # A request travelling down the stack's right edge, and the response coming back.
    wire = f"M{cx + a + 14},{first} V{last}"
    body = f"""<defs>
<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.1" fill="{t['muted']}" opacity=".4"/></pattern>
<linearGradient id="fade" x1="0" x2="1"><stop offset=".3" stop-color="#000"/><stop offset="1" stop-color="#fff"/></linearGradient>
<mask id="m"><rect width="{w}" height="{h}" fill="url(#fade)"/></mask>
<radialGradient id="glow" gradientUnits="userSpaceOnUse" cx="{cx}" cy="{h / 2}" r="330"><stop offset="0" stop-color="{t['accent']}" stop-opacity=".2"/><stop offset="1" stop-color="{t['accent']}" stop-opacity="0"/></radialGradient>
<linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{t['accent']}"/><stop offset="1" stop-color="{t['accent2']}"/></linearGradient>
<clipPath id="c"><rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#c)">
<rect width="{w}" height="{h}" fill="{t['panel']}"/>
<rect width="{w}" height="{h}" fill="url(#dots)" mask="url(#m)"/>
<rect width="{w}" height="{h}" fill="url(#glow)"/>
</g>
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18" fill="none" stroke="{t['stroke']}"/>
<circle class="ok p" cx="62" cy="77" r="5"/>
<text class="m mu" x="78" y="82" font-size="15">{escape(STATUS)}</text>
<text class="s t" x="54" y="158" font-size="58" font-weight="700" letter-spacing="-1.2">{escape(NAME)}</text>
<text class="s" x="56" y="202" font-size="21"><tspan class="t" font-weight="600">{escape(ROLE[0])}</tspan><tspan class="mu">{escape(ROLE[1])}</tspan></text>
<rect x="56" y="222" width="64" height="4" rx="2" fill="url(#bar)"/>
<text class="m ac" x="56" y="262" font-size="17" font-weight="700">›</text>
{rotating}
<ellipse cx="{cx}" cy="{last + b + depth + 8}" rx="{a * 0.8}" ry="8" fill="#000" opacity=".1"/>
<path d="{wire}" stroke="{t['stroke']}" stroke-width="1.6" stroke-dasharray="3 5"/>
<circle r="4" fill="{t['accent']}"><animateMotion dur="2.8s" repeatCount="indefinite" path="{wire}"/></circle>
<circle r="4" fill="{t['accent2']}"><animateMotion dur="2.8s" begin="-1.4s" repeatCount="indefinite" keyPoints="1;0" keyTimes="0;1" calcMode="linear" path="{wire}"/></circle>
{slabs}"""
    layers = "; ".join(f"{name.lower()}: {tools}" for name, tools, _ in LAYERS)
    return svg(w, h, f"{NAME} — full-stack developer, systems that run in production. The stack, top to bottom: {layers}.", style, body)


# --- link buttons and footer -------------------------------------------------


def button(label, colour, icon):
    w, h = round(len(label) * 8.6) + 62, 38
    body = (
        f'<rect width="{w}" height="{h}" rx="9" fill="{colour}"/>'
        f'<g transform="translate(16,10)" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{icon}</g>'
        f'<text x="{44 + (w - 60) / 2}" y="24.5" font-family="{SANS}" font-size="15" font-weight="600" fill="#fff" text-anchor="middle">{escape(label)}</text>'
    )
    return svg(w, h, label, "", body)


def footer(t):
    w, h = 1200, 220
    title, pitch, email = CLOSING
    style = base_style(t) + (
        "@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}"
        ".b{animation:bob 5s ease-in-out infinite}"
    )
    lines = "".join(
        f'<text class="s mu" x="56" y="{118 + i * 24}" font-size="17">{escape(line)}</text>'
        for i, line in enumerate(textwrap.wrap(pitch, 74)[:2])
    )
    cx, a, b, depth, first, step = 1040, 92, 46, 10, 66, 32
    slabs = "".join(
        f'<g class="b" style="animation-delay:{i * 0.35}s">{slab(t, LAYERS[i][2], cx, first + i * step, a, b, depth)}</g>'
        for i in reversed(range(len(LAYERS)))
    )
    body = f"""<defs>
<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.1" fill="{t['muted']}" opacity=".4"/></pattern>
<linearGradient id="fade" x1="0" x2="1"><stop offset=".3" stop-color="#000"/><stop offset="1" stop-color="#fff"/></linearGradient>
<mask id="m"><rect width="{w}" height="{h}" fill="url(#fade)"/></mask>
<radialGradient id="glow" gradientUnits="userSpaceOnUse" cx="{cx}" cy="{h / 2}" r="300"><stop offset="0" stop-color="{t['accent']}" stop-opacity=".2"/><stop offset="1" stop-color="{t['accent']}" stop-opacity="0"/></radialGradient>
<linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{t['accent']}"/><stop offset="1" stop-color="{t['accent2']}"/></linearGradient>
<clipPath id="c"><rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#c)">
<rect width="{w}" height="{h}" fill="{t['panel']}"/>
<rect width="{w}" height="{h}" fill="url(#dots)" mask="url(#m)"/>
<rect width="{w}" height="{h}" fill="url(#glow)"/>
</g>
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18" fill="none" stroke="{t['stroke']}"/>
<rect x="56" y="38" width="64" height="4" rx="2" fill="url(#bar)"/>
<text class="s t" x="54" y="86" font-size="36" font-weight="700" letter-spacing="-.8">{escape(title)}</text>
{lines}
<text class="m" x="56" y="186" font-size="16"><tspan class="ac" font-weight="700">›</tspan><tspan class="t" dx="10">{escape(email)}</tspan></text>
{slabs}"""
    return svg(w, h, f"{title}. {pitch} {email}", style, body)


# --- architecture ------------------------------------------------------------

# (x, y, width, height, title, subtitle lines)
BOXES = {
    "client": (24, 56, 160, 92, "Client", "browser · mobile"),
    "edge": (232, 56, 190, 92, "Cloudflare", "edge caching"),
    "nginx": (470, 56, 170, 92, "nginx", "reverse proxy · TLS"),
    "app": (688, 56, 230, 92, "Application", "React · Next.js · Node.js\nLaravel · FastAPI · Flask"),
    "pg": (966, 56, 210, 92, "Database", "PostgreSQL · MySQL\nMongoDB"),
    "pay": (232, 250, 190, 92, "Paystack · M-Pesa", "verified callbacks"),
    "redis": (688, 250, 230, 92, "Redis", "cache · sessions · queues"),
    "work": (966, 250, 210, 92, "Queue workers", "idempotent jobs"),
    "docs": (688, 432, 230, 92, "Documents", "PDF · DOCX, off-request"),
    "hooks": (966, 432, 210, 92, "Signed webhooks", "outbound · retried"),
}
# (path, has arrowhead)
LINKS = [
    ("M184,102 H232", True), ("M422,102 H470", True), ("M640,102 H688", True), ("M918,102 H966", True),
    ("M327,250 V148", True),
    ("M803,148 V250", True),
    ("M1071,148 V250", True),
    ("M918,296 H966", True),
    ("M1071,342 V432", True),
    ("M1010,342 V388 H803 V432", True),
]
# (path, duration s, head start s, colour key)
PACKETS = [
    ("M184,102 H966", 4.2, 0, "accent"), ("M184,102 H966", 4.2, 2.1, "accent"),
    ("M327,250 V148", 2.6, 0.6, "accent2"),
    ("M803,148 V250", 2.2, 1.0, "accent"),
    ("M1071,148 V250 M1071,342 V432", 3.4, 0.3, "accent2"),
    ("M918,296 H966", 1.8, 1.4, "accent"),
    ("M1010,342 V388 H803 V432", 3.0, 1.8, "accent2"),
]
BANDS = [
    ("Security", "JWT · TOTP 2FA · RBAC · row-level security · audit log"),
    ("Delivery", "CI gates: lint · audits · tests · Playwright · k6"),
    ("Operations", "health checks · correlated logs · tested restores"),
]


def architecture(t):
    w, h = 1200, 540
    style = base_style(t) + (
        "@keyframes flow{to{stroke-dashoffset:-20}}"
        f".l{{fill:none;stroke:{t['muted']};stroke-width:1.6;stroke-dasharray:4 6;animation:flow 1.2s linear infinite}}"
    )
    links = "".join(
        f'<path class="l" d="{d}"{" marker-end=\'url(#a)\'" if arrow else ""}/>' for d, arrow in LINKS
    ).replace("'", '"')
    packets = "".join(
        f'<circle r="4.5" fill="{t[c]}"><animateMotion dur="{dur}s" begin="-{delay}s" repeatCount="indefinite" path="{d}"/></circle>'
        for d, dur, delay, c in PACKETS
    )
    boxes = ""
    for x, y, bw, bh, title, sub in BOXES.values():
        lines = sub.split("\n")
        top = y + (42 if len(lines) == 1 else 33)
        boxes += (
            f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="12" fill="{t["panel"]}" stroke="{t["stroke"]}"/>'
            f'<text class="s t" x="{x + bw / 2}" y="{top}" font-size="18" font-weight="600" text-anchor="middle">{escape(title)}</text>'
        )
        for i, line in enumerate(lines):
            boxes += (
                f'<text class="s mu" x="{x + bw / 2}" y="{top + 24 + i * 20}" font-size="14.5" text-anchor="middle">{escape(line)}</text>'
            )
    bands = "".join(
        f'<text class="s t" x="48" y="{452 + i * 28}" font-size="15" font-weight="600">{escape(k)}</text>'
        f'<text class="s mu" x="150" y="{452 + i * 28}" font-size="14.5">{escape(v)}</text>'
        for i, (k, v) in enumerate(BANDS)
    )
    body = f"""<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="{t['muted']}" stroke-width="1.6"/></marker></defs>
<text class="m mu" x="24" y="34" font-size="12.5" letter-spacing="1.4">REQUEST PATH</text>
<text class="m mu" x="24" y="228" font-size="12.5" letter-spacing="1.4">BEHIND THE REQUEST</text>
<text class="m mu" x="1090" y="204" font-size="12.5">outbox</text>
{links}
{packets}
{boxes}
<rect x="24" y="388" width="616" height="136" rx="12" fill="none" stroke="{t['stroke']}" stroke-dasharray="3 5"/>
<text class="m mu" x="48" y="420" font-size="12.5" letter-spacing="1.4">ON EVERY LAYER</text>
{bands}"""
    label = (
        "How the platforms are put together: client, Cloudflare, nginx, the application (React, Next.js, Node.js, "
        "Laravel, FastAPI, Flask) and the database on the request path; Redis, queue workers, documents, signed webhooks and payment "
        "callbacks behind it; security, delivery and operations on every layer."
    )
    return svg(w, h, label, style, body)


# --- project cards -----------------------------------------------------------


def project(t, index, colour, status, title, description, steps, stack):
    w, h = 1000, 176
    c = t[colour]
    style = base_style(t) + (
        "@keyframes flow{to{stroke-dashoffset:-20}}"
        f".l{{fill:none;stroke:{t['muted']};stroke-width:1.6;stroke-dasharray:4 6;animation:flow 1.2s linear infinite}}"
    )
    lines = textwrap.wrap(description, 58)[:3]
    desc = "".join(
        f'<text class="s mu" x="30" y="{104 + i * 20}" font-size="14.5">{escape(line)}</text>'
        for i, line in enumerate(lines)
    )
    # Flow: nodes sit on top of one animated line, so the packet shows only in the gaps.
    nw, gap, x0, y0, nh = 113, 16, 474, 30, 52
    nodes = ""
    for i, step in enumerate(steps):
        x = x0 + i * (nw + gap)
        last = i == len(steps) - 1
        parts = step.split("\n")
        top = y0 + (31 if len(parts) == 1 else 23)
        nodes += f'<rect x="{x}" y="{y0}" width="{nw}" height="{nh}" rx="9" fill="{t["inset"]}" stroke="{c if last else t["stroke"]}"/>'
        for j, part in enumerate(parts):
            nodes += (
                f'<text class="s t" x="{x + nw / 2}" y="{top + j * 16}" font-size="12.5" '
                f'font-weight="{600 if last else 500}" text-anchor="middle">{escape(part)}</text>'
            )
    x1, mid = x0 + len(steps) * (nw + gap) - gap, y0 + nh / 2
    chips, cx = "", x0
    for name in stack:
        cw = len(name) * 7.2 + 16
        chips += (
            f'<rect x="{cx}" y="112" width="{cw:.1f}" height="26" rx="13" fill="none" stroke="{t["stroke"]}"/>'
            f'<text class="m mu" x="{cx + cw / 2:.1f}" y="129.5" font-size="12" text-anchor="middle">{escape(name)}</text>'
        )
        cx += cw + 5
    body = f"""<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="14" fill="{t['panel']}" stroke="{t['stroke']}"/>
<rect x="1" y="26" width="4" height="{h - 52}" rx="2" fill="{c}"/>
<text class="m" x="30" y="42" font-size="12.5" letter-spacing="1.2"><tspan fill="{c}" font-weight="700">{index:02d}</tspan><tspan class="mu">  {escape(status.upper())}</tspan></text>
<text class="s t" x="30" y="76" font-size="24" font-weight="700" letter-spacing="-.4">{escape(title)}</text>
{desc}
<path class="l" d="M{x0},{mid} H{x1}"/>
<circle r="4" fill="{c}"><animateMotion dur="3.6s" begin="-{index * 0.5}s" repeatCount="indefinite" path="M{x0},{mid} H{x1}"/></circle>
{nodes}
{chips}"""
    label = f"{title} ({status}). {description} Flow: {', '.join(s.replace(chr(10), ' ') for s in steps)}. Stack: {', '.join(stack)}."
    return svg(w, h, label, style, body)


# --- journey -----------------------------------------------------------------


def journey(t):
    w, row, top = 1000, 68, 34
    h = top + row * len(JOURNEY) - 8
    rail = 222
    style = base_style(t) + (
        "@keyframes ring{0%{r:6px;opacity:.7}100%{r:16px;opacity:0}}"
        ".g{animation:ring 2.4s ease-out infinite}"
    )
    body = f'<path d="M{rail},{top} V{top + row * (len(JOURNEY) - 1)}" stroke="{t["stroke"]}" stroke-width="2"/>'
    for i, (when, role, where, kind) in enumerate(JOURNEY):
        y = top + i * row
        if kind == "now":
            mark = (
                f'<circle class="g" cx="{rail}" cy="{y}" r="6" fill="{t["accent"]}"/>'
                f'<circle cx="{rail}" cy="{y}" r="6" fill="{t["accent"]}"/>'
            )
        elif kind == "study":
            mark = f'<rect x="{rail - 6}" y="{y - 6}" width="12" height="12" rx="2" transform="rotate(45 {rail} {y})" fill="{t["panel"]}" stroke="{t["muted"]}" stroke-width="2"/>'
        else:
            mark = f'<circle cx="{rail}" cy="{y}" r="5" fill="{t["panel"]}" stroke="{t["muted"]}" stroke-width="2"/>'
        body += (
            f'{mark}<text class="m {"ac" if kind == "now" else "mu"}" x="{rail - 28}" y="{y + 5}" font-size="13.5" text-anchor="end">{escape(when)}</text>'
            f'<text class="s t" x="{rail + 30}" y="{y + 5}" font-size="17" font-weight="600">{escape(role)}</text>'
            f'<text class="s mu" x="{rail + 30}" y="{y + 27}" font-size="14.5">{escape(where)}</text>'
        )
    label = "Journey. " + " ".join(f"{when}: {role}, {where}." for when, role, where, _ in JOURNEY)
    return svg(w, h, label, style, body)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for slug, *spec in BUTTONS:
        path = OUT / f"button-{slug}.svg"
        path.write_text(button(*spec), encoding="utf-8")
        print(f"wrote {path.relative_to(OUT.parent)}")
    for theme, tokens in THEMES.items():
        for name, build in (("hero", hero), ("architecture", architecture), ("journey", journey), ("footer", footer)):
            path = OUT / f"{name}-{theme}.svg"
            path.write_text(build(tokens), encoding="utf-8")
            print(f"wrote {path.relative_to(OUT.parent)}")
        for index, (slug, *card) in enumerate(PROJECTS, 1):
            path = OUT / f"project-{slug}-{theme}.svg"
            path.write_text(project(tokens, index, *card), encoding="utf-8")
            print(f"wrote {path.relative_to(OUT.parent)}")
