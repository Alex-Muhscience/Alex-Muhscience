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
        blue="#5b9cf8", red="#f2605c", green="#3fb950", amber="#d6a13a", violet="#a78bfa", teal="#2dd4bf",
    ),
    "light": dict(
        panel="#f7f9fc", inset="#ffffff", stroke="#d5dce6", text="#0f172a",
        muted="#566273", accent="#2563eb", accent2="#dc2626", ok="#15803d", warn="#a16207",
        blue="#2563eb", red="#dc2626", green="#15803d", amber="#a16207", violet="#7c3aed", teal="#0f766e",
    ),
}

# --- content -----------------------------------------------------------------

NAME = "Alex Murimi Kamau"
STATUS = "open to remote · Nairobi, Kenya · UTC+3"
ROLE = ("Full-stack developer", " · systems that run in production")
ROTATING = [
    "TypeScript · React · Next.js · Node.js",
    "Python · FastAPI · Flask · PHP · Laravel",
    "Payments, multi-tenancy, RBAC and audit trails",
    "Linux, Docker, CI/CD and keeping it all running",
]
PLATFORMS = [
    ("EuroAfrique Corporate Skills", "production", "ok"),
    ("Chania Publishers LMS", "production", "ok"),
    ("AfriAsia Career Development Center", "production", "ok"),
    ("BusinessOS", "in development", "warn"),
]

# Featured projects. Each card shows what the system does as a four-step flow.
# (slug, colour, status, title, description, flow steps, stack)
PROJECTS = [
    ("businessos", "blue", "in development · private", "BusinessOS",
     "Multi-tenant operating system for SMEs: CRM, sales, procurement, inventory, finance, HR and projects on one governed data model.",
     ["Tenant\nrequest", "Row-level\nsecurity", "Idempotent\nwrite", "Outbox +\nwebhooks"],
     ["Laravel 13", "Next.js 16", "PostgreSQL 18", "Redis", "Docker", "nginx"]),
    ("utdrs", "red", "in development · private · Mozilla RCC Top 5", "UTDRS",
     "Unified threat detection and response: events run through ATT&CK-mapped rules, anomaly and ML detectors, and analysts triage alerts in a React dashboard.",
     ["Event", "ATT&CK\nrules", "Anomaly +\nML detectors", "Analyst\ntriage"],
     ["Python", "FastAPI", "React", "TypeScript", "MongoDB", "C", "Docker"]),
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


# --- hero --------------------------------------------------------------------


def hero(t):
    w, h = 1200, 300
    share = 100 // len(ROTATING)  # each line's slice of the cycle, in percent
    style = base_style(t) + (
        "@keyframes pulse{0%,100%{opacity:1}50%{opacity:.35}}"
        f"@keyframes rot{{0%{{opacity:0}}3%{{opacity:1}}{share - 3}%{{opacity:1}}{share}%,100%{{opacity:0}}}}"
        ".p{animation:pulse 2.4s ease-in-out infinite}"
        f".r{{opacity:0;animation:rot {len(ROTATING) * 4}s linear infinite}}"
    )
    rows = []
    for i, (name, state, tone) in enumerate(PLATFORMS):
        y = 132 + i * 34
        rows.append(
            f'<circle class="{tone} p" style="animation-delay:{i * 0.4}s" cx="730" cy="{y - 5}" r="4.5"/>'
            f'<text class="s t" x="748" y="{y}" font-size="16">{escape(name)}</text>'
            f'<text class="m {tone}" x="1126" y="{y}" font-size="13" text-anchor="end">{state}</text>'
        )
    rotating = "".join(
        f'<text class="m mu r{" r1" if i == 0 else ""}" style="animation-delay:{i * 4}s" '
        f'x="82" y="250" font-size="17">{escape(line)}</text>'
        for i, line in enumerate(ROTATING)
    )
    body = f"""<defs>
<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.1" fill="{t['muted']}" opacity=".45"/></pattern>
<linearGradient id="fade" x1="0" x2="1"><stop offset=".25" stop-color="#000"/><stop offset="1" stop-color="#fff"/></linearGradient>
<mask id="m"><rect width="{w}" height="{h}" fill="url(#fade)"/></mask>
<radialGradient id="glow" cx="1" cy="0" r="1"><stop offset="0" stop-color="{t['accent']}" stop-opacity=".22"/><stop offset=".6" stop-color="{t['accent']}" stop-opacity="0"/></radialGradient>
<linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{t['accent']}"/><stop offset="1" stop-color="{t['accent2']}"/></linearGradient>
<clipPath id="c"><rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#c)">
<rect width="{w}" height="{h}" fill="{t['panel']}"/>
<rect width="{w}" height="{h}" fill="url(#dots)" mask="url(#m)"/>
<rect width="{w}" height="{h}" fill="url(#glow)"/>
</g>
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18" fill="none" stroke="{t['stroke']}"/>
<circle class="ok p" cx="62" cy="67" r="5"/>
<text class="m mu" x="78" y="72" font-size="15">{escape(STATUS)}</text>
<text class="s t" x="54" y="146" font-size="58" font-weight="700" letter-spacing="-1.2">{escape(NAME)}</text>
<text class="s" x="56" y="190" font-size="21"><tspan class="t" font-weight="600">{escape(ROLE[0])}</tspan><tspan class="mu">{escape(ROLE[1])}</tspan></text>
<rect x="56" y="210" width="64" height="4" rx="2" fill="url(#bar)"/>
<text class="m ac" x="56" y="250" font-size="17" font-weight="700">›</text>
{rotating}
<rect x="700" y="62" width="450" height="188" rx="14" fill="{t['inset']}" stroke="{t['stroke']}"/>
<text class="m mu" x="724" y="96" font-size="12.5" letter-spacing="1.4">PLATFORMS I OWN END TO END</text>
{''.join(rows)}"""
    return svg(w, h, f"{NAME} — full-stack developer, systems that run in production", style, body)


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


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for theme, tokens in THEMES.items():
        for name, build in (("hero", hero), ("architecture", architecture)):
            path = OUT / f"{name}-{theme}.svg"
            path.write_text(build(tokens), encoding="utf-8")
            print(f"wrote {path.relative_to(OUT.parent)}")
        for index, (slug, *card) in enumerate(PROJECTS, 1):
            path = OUT / f"project-{slug}-{theme}.svg"
            path.write_text(project(tokens, index, *card), encoding="utf-8")
            print(f"wrote {path.relative_to(OUT.parent)}")
