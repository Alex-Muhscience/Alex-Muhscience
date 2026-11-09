#!/usr/bin/env python3
"""Build the profile README's SVG assets in light and dark variants.

Run from the repository root:  python3 scripts/build_assets.py
Standard library only. Edit the content below, re-run, commit the output.
"""
import json
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
# Brand logos vendored from Simple Icons (CC0); see scripts/icons.json.
ICONS = json.loads((Path(__file__).resolve().parent / "icons.json").read_text(encoding="utf-8"))["icons"]
# Outline symbols for items that have no logo (24 x 24, stroked).
GLYPHS = {
    "shield": "M12 3l7 3v5c0 4.5-3 8.5-7 10-4-1.5-7-5.5-7-10V6z M9 12l2 2 4-4",
    "card": "M3 6.5h18v11H3z M3 10.5h18 M6.5 14.5h4",
    "check": "M12 3a9 9 0 1 0 0 18a9 9 0 1 0 0-18z M8 12.5l2.7 2.7L16.5 9.5",
    "gear": "M12 9a3 3 0 1 0 0 6a3 3 0 1 0 0-6z M12 2.5v3 M12 18.5v3 M2.5 12h3 M18.5 12h3 M5.3 5.3l2.1 2.1 M16.6 16.6l2.1 2.1 M5.3 18.7l2.1-2.1 M16.6 7.4l2.1-2.1",
}

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
ROLE = ("Full-stack engineer", " · technical owner")
ROTATING = [
    "I build and run production platforms end to end",
    "Payments, multi-tenancy, RBAC and audit trails",
    "Linux, Docker, CI/CD and keeping it all running",
    "Open source: Linux desktops, RPM packaging and QML",
]
# How I work: (title, explanation, colour)
PRINCIPLES = [
    ("Requirements first", "Architecture follows the problem. A content site and a multi-tenant ledger don't want the same design.", "blue"),
    ("Modular monolith first", "Services get extracted only when a domain proves it must scale or release on its own.", "violet"),
    ("Scale in measured steps", "Edge and Redis caching, indexes for real queries, queued slow work, stateless app servers. Scale out where load tests point.", "teal"),
    ("Every change through CI/CD", "Lint, static analysis, dependency audits, unit, E2E and load tests gate each deploy. Releases are scripted and repeatable.", "green"),
    ("Contain failure", "A slow PDF render or a dead webhook must never fail an unrelated checkout. Retries, backoff and an outbox.", "amber"),
    ("Money paths are idempotent", "Payments are confirmed only by signed provider callbacks, and recording one is always safe to retry.", "red"),
    ("Security is architecture", "Access control, MFA, row-level security and audit trails are designed into the first schema.", "red"),
    ("Measure, then optimise", "Find the real bottleneck with production-sized data, then fix that one thing. Query budgets fail the build.", "blue"),
    ("Built to be operated", "Health checks, correlated logs, verified backups and tested restores ship with the feature.", "green"),
]
# The stack, by layer: (layer, tools, colour)
STACK = [
    ("FRONTEND", [("React", "react"), ("Next.js", "nextdotjs"), ("TypeScript", "typescript"), ("Tailwind CSS", "tailwindcss"), ("Livewire", "livewire"), ("Alpine.js", "alpinedotjs")], "blue"),
    ("BACKEND", [("Laravel", "laravel"), ("PHP", "php"), ("Node.js", "nodedotjs"), ("Python", "python"), ("Django", "django"), ("FastAPI", "fastapi"), ("Flask", "flask")], "violet"),
    ("DATA", [("PostgreSQL", "postgresql"), ("MySQL", "mysql"), ("MongoDB", "mongodb"), ("Redis", "redis"), ("SQLite", "sqlite"), ("Algolia", "algolia")], "teal"),
    ("INFRASTRUCTURE", [("Linux", "linux"), ("Docker", "docker"), ("nginx", "nginx"), ("Cloudflare", "cloudflare"), ("Vercel", "vercel"), ("GitHub Actions", "githubactions")], "amber"),
    ("SECURITY", [("JWT", "jsonwebtokens"), ("RBAC", "shield"), ("TOTP MFA", "shield"), ("Row-level security", "shield"), ("Audit trails", "shield")], "red"),
    ("PAYMENTS & TESTING", [("Paystack", "card"), ("M-Pesa", "card"), ("PHPUnit", "check"), ("Playwright", "check"), ("k6", "k6")], "green"),
    ("SYSTEMS", [("Qt 6 / QML", "qt"), ("Hyprland", "hyprland"), ("Fedora RPM", "fedora"), ("systemd", "gear")], "cyan"),
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
    ("APPLICATION", "Laravel · Django · Node.js · FastAPI", "violet"),
    ("DATA", "PostgreSQL · MySQL · MongoDB · Redis", "teal"),
    ("INFRASTRUCTURE", "Linux · Docker · nginx · CI/CD", "amber"),
]

# Project cards, shown two per row in the README. Deliberately plain, like
# GitHub's pinned-repository cards. (slug, dot colour, status, title, description, stack)
GROUPS = {
    "business": [
        ("euroafrique", "green", "In production", "EuroAfrique Corporate Skills",
         "Corporate training platform: programme publishing, applications, M-Pesa and card payments confirmed by signed callbacks, and automated enrolment documents.",
         "Laravel · MySQL · Redis · M-Pesa"),
        ("afriasia", "green", "In production", "AfriAsia Career Development Center",
         "Executive-training and booking platform with Paystack in USD and KES, idempotent payment recording, queued invoices and certificates, and admin MFA.",
         "Laravel · Livewire · MySQL · Redis"),
        ("chania", "green", "In production", "Chania Publishers LMS",
         "Learning management system for an educational publisher. Access only on verified payment, video streamed through an access-checked endpoint.",
         "PHP · MySQL · JavaScript · Linux"),
        ("chania-finance", "green", "In production", "Chania Finance Consultancy",
         "Finance-training platform built for catalogue scale: full-text search, calendar booking by venue, organisation invoicing, admin and trainer portals.",
         "Laravel · Livewire · MySQL · DomPDF"),
    ],
    "products": [
        ("businessos", "amber", "In development", "BusinessOS",
         "Multi-tenant operating system for SMEs: CRM, sales, procurement, inventory, finance and HR on one data model, isolated with PostgreSQL row-level security.",
         "Laravel · Next.js · PostgreSQL · Docker"),
        ("utdrs", "green", "Live", "UTDRS",
         "Threat detection and response: ATT&CK-mapped rules, anomaly and ML detectors, and analyst triage in React. Top 5, Mozilla Responsible Computing Challenge.",
         "Python · FastAPI · React · MongoDB"),
        ("secure-file-sharing", "amber", "In development", "Secure File Sharing",
         "Encrypted file sharing for teams: resumable uploads sealed chunk by chunk with AES-256-GCM, quarantined until ClamAV clears them.",
         "Node.js · MongoDB · S3 · ClamAV"),
        ("muhos", "blue", "Pre-release · open source", "MuhOS",
         "Desktop shell for Hyprland on Fedora, shipped as RPM packages with a GDM session. Idle shell CPU cut ~9×, measured in a VM.",
         "QML · Qt 6 · Quickshell · systemd"),
    ],
}

# (when, role, where, kind) — newest first; kind is "now", "past" or "study"
JOURNEY = [
    ("Aug 2025 → now", "Full-Stack Developer & Technical Owner",
     "EuroAfrique · Chania Publishers · AfriAsia Career Development Center · Chania Finance Consultancy", "now"),
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
    return svg(w, h, f"{NAME} — full-stack engineer and technical owner of production platforms. The stack, top to bottom: {layers}.", style, body)


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
    "app": (688, 56, 230, 92, "Application", "React · Next.js · Node.js\nLaravel · Django · FastAPI"),
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
        "Laravel, Django, FastAPI) and the database on the request path; Redis, queue workers, documents, signed webhooks and payment "
        "callbacks behind it; security, delivery and operations on every layer."
    )
    return svg(w, h, label, style, body)


# --- project cards -----------------------------------------------------------


def card(t, colour, status, title, description, stack):
    """A plain card: title, description, and one status line."""
    w, h = 600, 236
    lines = "".join(
        f'<text class="s mu" x="28" y="{98 + i * 26}" font-size="18">{escape(line)}</text>'
        for i, line in enumerate(textwrap.wrap(description, 54)[:3])
    )
    body = f"""<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="10" fill="{t['panel']}" stroke="{t['stroke']}"/>
<text class="s t" x="28" y="56" font-size="23" font-weight="600">{escape(title)}</text>
{lines}
<circle cx="35" cy="{h - 35}" r="6.5" fill="{t[colour]}"/>
<text class="s mu" x="50" y="{h - 29}" font-size="16">{escape(status)}  ·  {escape(stack)}</text>"""
    return svg(w, h, f"{title} ({status}). {description} {stack}.", base_style(t), body)


# --- how I work and the stack -------------------------------------------------


def principles(t):
    w, cols, tw, th, gap = 1200, 3, 384, 176, 24
    rows = (len(PRINCIPLES) + cols - 1) // cols
    h = rows * th + (rows - 1) * gap
    body = ""
    for i, (title, text, colour) in enumerate(PRINCIPLES):
        x, y, c = (i % cols) * (tw + gap), (i // cols) * (th + gap), t[colour]
        lines = "".join(
            f'<text class="s mu" x="{x + 28}" y="{y + 92 + j * 22}" font-size="15.5">{escape(line)}</text>'
            for j, line in enumerate(textwrap.wrap(text, 42)[:3])
        )
        body += (
            f'<rect x="{x + 1}" y="{y + 1}" width="{tw - 2}" height="{th - 2}" rx="16" fill="{t["panel"]}" stroke="{t["stroke"]}"/>'
            f'<rect x="{x + 28}" y="{y + 1}" width="48" height="3" rx="1.5" fill="{c}"/>'
            f'<text class="m" x="{x + 28}" y="{y + 40}" font-size="13" font-weight="700" letter-spacing="1.2" fill="{c}">{i + 1:02d}</text>'
            f'<text class="s t" x="{x + 28}" y="{y + 66}" font-size="20" font-weight="700" letter-spacing="-.3">{escape(title)}</text>'
            + lines
        )
    label = "How I work. " + " ".join(f"{a}: {b}" for a, b, _ in PRINCIPLES)
    return svg(w, h, label, base_style(t), body)


def luminance(hex_colour):
    def channel(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hex_colour.lstrip("#")[k:k + 2], 16) for k in (0, 2, 4))
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def logo_colour(t, hex_colour):
    """Brand colour, unless it would vanish against the card (then the text colour)."""
    a, b = luminance(hex_colour), luminance(t["panel"])
    contrast = (max(a, b) + 0.05) / (min(a, b) + 0.05)
    return f"#{hex_colour}" if contrast >= 2.2 else t["text"]


def stack(t):
    w, row = 1200, 56
    h = len(STACK) * row + 36
    body = f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18" fill="{t["panel"]}" stroke="{t["stroke"]}"/>'
    for i, (layer, tools, colour) in enumerate(STACK):
        y, c = 18 + i * row, t[colour]
        if i:
            body += f'<line x1="32" x2="{w - 32}" y1="{y}" y2="{y}" stroke="{t["stroke"]}" stroke-dasharray="2 6"/>'
        body += (
            f'<text class="m" x="40" y="{y + row / 2 + 5}" font-size="13.5" font-weight="700" letter-spacing="1.3" fill="{c}">{escape(layer)}</text>'
        )
        cx = 290
        for name, icon in tools:
            cw = len(name) * 8.6 + 58
            ix, iy = cx + 14, y + 17
            if icon in ICONS:
                mark = (
                    f'<g transform="translate({ix},{iy}) scale(.9167)">'
                    f'<path d="{ICONS[icon]["path"]}" fill="{logo_colour(t, ICONS[icon]["hex"])}"/></g>'
                )
            else:
                mark = (
                    f'<g transform="translate({ix},{iy}) scale(.9167)" fill="none" stroke="{t["muted"]}" '
                    f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="{GLYPHS[icon]}"/></g>'
                )
            body += (
                f'<rect x="{cx}" y="{y + 10}" width="{cw:.1f}" height="36" rx="18" fill="{t["inset"]}" stroke="{t["stroke"]}"/>'
                + mark
                + f'<text class="s t" x="{cx + 44}" y="{y + 33}" font-size="15" font-weight="500">{escape(name)}</text>'
            )
            cx += cw + 9
    label = "Stack by layer. " + " ".join(f"{a.title()}: {', '.join(n for n, _ in b)}." for a, b, _ in STACK)
    return svg(w, h, label, base_style(t), body)


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
        for name, build in (("hero", hero), ("architecture", architecture), ("principles", principles), ("stack", stack), ("journey", journey), ("footer", footer)):
            path = OUT / f"{name}-{theme}.svg"
            path.write_text(build(tokens), encoding="utf-8")
            print(f"wrote {path.relative_to(OUT.parent)}")
        for projects in GROUPS.values():
            for slug, *spec in projects:
                path = OUT / f"card-{slug}-{theme}.svg"
                path.write_text(card(tokens, *spec), encoding="utf-8")
                print(f"wrote {path.relative_to(OUT.parent)}")
