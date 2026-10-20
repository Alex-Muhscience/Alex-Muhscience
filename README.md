<div align="center">

<a href="https://portfolio-alex-m-kamau.vercel.app">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg" />
  <img src="assets/hero-dark.svg" width="100%" alt="Alex Murimi Kamau — full-stack developer, systems that run in production" />
</picture>
</a>

<a href="https://portfolio-alex-m-kamau.vercel.app"><img src="assets/button-portfolio.svg" height="38" alt="Portfolio" /></a>&nbsp;&nbsp;<a href="https://www.linkedin.com/in/alex-m-kamau-20015b340"><img src="assets/button-linkedin.svg" height="38" alt="LinkedIn" /></a>&nbsp;&nbsp;<a href="https://flowcv.com/resume/t249m8own6"><img src="assets/button-resume.svg" height="38" alt="Résumé" /></a>&nbsp;&nbsp;<a href="mailto:alex.kamau.2558@gmail.com"><img src="assets/button-email.svg" height="38" alt="Email" /></a>&nbsp;&nbsp;<a href="https://wa.me/254746254055"><img src="assets/button-whatsapp.svg" height="38" alt="WhatsApp: +254 746 254 055" /></a>

</div>

<br/>

I design, build and **operate** business-critical web platforms from the first requirements conversation to the production server, and everything after it ships.

Today I'm the full-stack developer and sole technical owner for three companies: **EuroAfrique Corporate Skills**, **Chania Publishers** and **AfriAsia Career Development Center**. Each runs on a platform I architected, built, deployed and keep running. On the side, I'm building **BusinessOS**, a multi-tenant business operating system, and a **secure file sharing platform** for teams, and I maintain **[MuhOS](https://github.com/Alex-Muhscience/MuhOS)**, an open-source desktop shell for Hyprland on Fedora. I was a **Top 5 finalist** in the Mozilla Responsible Computing Challenge.

I pick the stack to fit the problem: **React** and **Next.js** on the front, **Node.js**, **Laravel**, **FastAPI** or **Flask** behind it, and **TypeScript**, **Python** and **PHP** as the working languages.

## How I put a platform together

Not one system, but the shape most of mine share: a boring, fast request path, with everything slow or failure-prone pushed behind it.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/architecture-light.svg" />
  <img src="assets/architecture-dark.svg" width="100%" alt="Request path: client, Cloudflare, nginx, the application (React, Next.js, Node.js, Laravel, FastAPI, Flask) and the database. Behind the request: Redis, queue workers fed by an outbox, generated documents, signed webhooks and verified payment callbacks. On every layer: security, delivery and operations." />
</picture>

**The rules behind it**

- **Architecture follows requirements.** A content site, a payment workflow and a multi-tenant ledger don't want the same design.
- **Modular monolith first.** Services get extracted when a domain proves it needs to scale or release on its own.
- **Contain failure.** A slow PDF render or a dead webhook should never fail an unrelated checkout.
- **Security and audit are architecture,** designed in from the first schema — not bolted on later.
- **Measure, then optimise.** Find the bottleneck with real data volume, then fix that one thing.
- **Build systems that can be operated.** Health checks, correlated logs, repeatable deploys and tested restores are part of the feature.

## Featured work

Each card traces what the system does, left to right. Click one to open it.

<a href="https://portfolio-alex-m-kamau.vercel.app/work/businessos">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/project-businessos-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/project-businessos-light.svg" />
  <img src="assets/project-businessos-dark.svg" width="100%" alt="BusinessOS — multi-tenant operating system for SMEs, in development. Laravel, Next.js, PostgreSQL, Redis, Docker, nginx." />
</picture>
</a>

<a href="https://portfolio-alex-m-kamau.vercel.app/work/unified-threat-detection-response">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/project-utdrs-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/project-utdrs-light.svg" />
  <img src="assets/project-utdrs-dark.svg" width="100%" alt="UTDRS — unified threat detection and response, live on Vercel and Render, Mozilla RCC Top 5. Python, FastAPI, React, TypeScript, MongoDB, C, Docker." />
</picture>
</a>

<a href="https://portfolio-alex-m-kamau.vercel.app/work/secure-file-sharing">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/project-secure-file-sharing-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/project-secure-file-sharing-light.svg" />
  <img src="assets/project-secure-file-sharing-dark.svg" width="100%" alt="Secure File Sharing Platform — encrypted file sharing for teams, in development, private. Node.js, Express, MongoDB, S3, ClamAV, libsodium, Docker." />
</picture>
</a>

<a href="https://github.com/Alex-Muhscience/MuhOS">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/project-muhos-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/project-muhos-light.svg" />
  <img src="assets/project-muhos-dark.svg" width="100%" alt="MuhOS — open-source desktop shell for Hyprland on Fedora, pre-release, AGPL-3.0. QML, Qt 6, Quickshell, Hyprland, Fedora RPM, systemd, Python." />
</picture>
</a>

<a href="https://www.euroafriquecorporateskills.com">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/project-euroafrique-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/project-euroafrique-light.svg" />
  <img src="assets/project-euroafrique-dark.svg" width="100%" alt="EuroAfrique Corporate Skills — corporate training platform, in production. Laravel, MySQL, Redis, Paystack, M-Pesa, Algolia, Cloudflare." />
</picture>
</a>

<a href="https://afriasiacareercenter.com">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/project-afriasia-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/project-afriasia-light.svg" />
  <img src="assets/project-afriasia-dark.svg" width="100%" alt="AfriAsia Career Development Center — executive-training, booking and document platform, in production. Laravel, Livewire, Alpine.js, Tailwind, MySQL, Redis." />
</picture>
</a>

<a href="https://chaniapublishers.com">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/project-chania-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/project-chania-light.svg" />
  <img src="assets/project-chania-dark.svg" width="100%" alt="Chania Publishers LMS — learning management system, in production. PHP, MySQL, JavaScript, Linux." />
</picture>
</a>

<a href="https://muhscience-tech-labs-website.vercel.app">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/project-muhscience-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/project-muhscience-light.svg" />
  <img src="assets/project-muhscience-dark.svg" width="100%" alt="Muhscience Tech Labs — company site on the Next.js App Router, live on Vercel. Next.js, React, TypeScript, Tailwind, shadcn/ui, MongoDB." />
</picture>
</a>

<details>
<summary><b>Engineering notes for each project</b></summary>

<br/>

**[BusinessOS](https://portfolio-alex-m-kamau.vercel.app/work/businessos)** — in development, private
- Postgres **row-level security** + app-level authorization
- Transactional **outbox**, signed webhooks, idempotent writes
- JWT with rotating refresh tokens, TOTP 2FA
- CI with Playwright E2E and **k6** load tests

**[UTDRS](https://portfolio-alex-m-kamau.vercel.app/work/unified-threat-detection-response)** — live, private repository, Mozilla RCC Top 5 · [dashboard](https://utdrs-capstone-project.vercel.app)
- Every event runs through MITRE ATT&CK-mapped rules, anomaly and ML detectors
- Analysts triage the alerts in a React dashboard
- Built to keep AI explainable
- Dashboard on **Vercel**, gateway and engine on **Render**, data in MongoDB Atlas

**[Secure File Sharing Platform](https://portfolio-alex-m-kamau.vercel.app/work/secure-file-sharing)** — in development, private
- Per-file keys, every chunk sealed with **AES-256-GCM**
- **Resumable** chunked uploads, streamed range downloads
- Quarantined until **ClamAV** clears it; fails closed
- Workspace roles, email-verified recipients, revocable links

**[MuhOS](https://github.com/Alex-Muhscience/MuhOS)** — open source (AGPL-3.0), pre-release · [case study](https://portfolio-alex-m-kamau.vercel.app/work/muhos) · [releases](https://github.com/Alex-Muhscience/MuhOS/releases)
- Fedora fork of the Serpantinum shell: **RPM packages** and a **GDM session** instead of a `curl | bash` installer
- Redesigned menu bar and control centre in **QML**: GNOME layout, macOS-style glass, Adwaita icons
- Every number measured in a **VM benchmark**: idle shell CPU 0.62% → 0.07% of a core
- Every bundled font, sound and image **licence-checked** in CI

**[EuroAfrique Corporate Skills](https://www.euroafriquecorporateskills.com)** — in production, sole technical owner
- Faster responses via **Redis + Cloudflare** caching
- Manual operations replaced with **automation**
- Enrolment documents generated automatically
- Deploys gated on lint, audits and tests

**[AfriAsia Career Development Center](https://afriasiacareercenter.com)** — in production, sole technical owner
- Paystack in **USD/KES**, idempotent payment recording
- Queued PDF/DOCX invoices, letters and certificates
- Admin **TOTP MFA**, single-session enforcement
- Spatie roles & permissions, audit logs

**[Chania Publishers LMS](https://chaniapublishers.com)** — in production, sole technical owner
- Access granted only on **verified payment**
- Video streamed through an **access-checked** endpoint
- Layered auth / admin / subscriber middleware
- Pages optimised for speed

**[Muhscience Tech Labs](https://muhscience-tech-labs-website.vercel.app)** — live on Vercel, open source · [repository](https://github.com/Alex-Muhscience/Muhscience-Tech-Labs-Website)
- Next.js App Router with server-handled enquiry forms
- Technical SEO and security headers

</details>

<sub>Also built: <a href="https://github.com/Alex-Muhscience/Pass-KeyGen"><b>KeyGen</b></a> — a Flutter password manager with AES-encrypted storage, PBKDF2 and biometric unlock. Full case studies live on my <a href="https://portfolio-alex-m-kamau.vercel.app/work">portfolio</a>.</sub>

## Toolbox

<div align="center">

**Languages & frameworks**<br/>
<img src="https://skillicons.dev/icons?i=ts,js,react,nextjs,nodejs,python,fastapi,flask,php,laravel,tailwind,dart,flutter,qt&perline=14" alt="TypeScript, JavaScript, React, Next.js, Node.js, Python, FastAPI, Flask, PHP, Laravel, Tailwind, Dart, Flutter, Qt" />

**Data & infrastructure**<br/>
<img src="https://skillicons.dev/icons?i=postgres,mysql,redis,mongodb,sqlite,docker,nginx,linux,bash,githubactions,cloudflare,vercel,git&perline=13" alt="PostgreSQL, MySQL, Redis, MongoDB, SQLite, Docker, nginx, Linux, Bash, GitHub Actions, Cloudflare, Vercel, Git" />

<sub>Also: Livewire · Alpine.js · Playwright · k6 · JWT · TOTP MFA · RBAC · Row-level security · M-Pesa · Paystack · Algolia · QML / Qt · Hyprland · RPM packaging · systemd</sub>

</div>

## Journey

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/journey-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/journey-light.svg" />
  <img src="assets/journey-dark.svg" width="100%" alt="Aug 2025 to now: Full-Stack Developer and Technical Owner at EuroAfrique Corporate Skills, Chania Publishers and AfriAsia Career Development Center. May to Aug 2025: Freelance Web Development Tutor. Aug 2024 to Feb 2025: Network Technician at Gicatech Enterprise Solutions. May to Aug 2024: Software Development Intern at Secunets Technologies. 2021 to 2025: BSc Computer Science, Second Class Honours (Upper), Kisii University." />
</picture>

## Activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Alex-Muhscience/Alex-Muhscience/output/github-streak.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Alex-Muhscience/Alex-Muhscience/output/github-streak-light.svg" />
  <img src="https://raw.githubusercontent.com/Alex-Muhscience/Alex-Muhscience/output/github-streak.svg" alt="GitHub streak" />
</picture>

[![GitHub Stats](https://github-stats-extended.vercel.app/api/top-langs?username=Alex-Muhscience&layout=pie&langs_count=10&theme=transparent)](https://github-stats-extended.vercel.app/api/top-langs?username=Alex-Muhscience&layout=pie&langs_count=10&theme=transparent)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Alex-Muhscience/Alex-Muhscience/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Alex-Muhscience/Alex-Muhscience/output/github-contribution-grid-snake.svg" />
  <img src="https://raw.githubusercontent.com/Alex-Muhscience/Alex-Muhscience/output/github-contribution-grid-snake-dark.svg" width="100%" alt="Contribution graph" />
</picture>

</div>

<br/>

<div align="center">

<a href="mailto:alex.kamau.2558@gmail.com">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/footer-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/footer-light.svg" />
  <img src="assets/footer-dark.svg" width="100%" alt="Let's build something that lasts. Open to full-stack and backend engineering roles, technical partnerships and product work where reliability matters. alex.kamau.2558@gmail.com" />
</picture>
</a>

<a href="https://portfolio-alex-m-kamau.vercel.app"><img src="assets/button-portfolio.svg" height="38" alt="Portfolio" /></a>&nbsp;&nbsp;<a href="https://www.linkedin.com/in/alex-m-kamau-20015b340"><img src="assets/button-linkedin.svg" height="38" alt="LinkedIn" /></a>&nbsp;&nbsp;<a href="https://flowcv.com/resume/t249m8own6"><img src="assets/button-resume.svg" height="38" alt="Résumé" /></a>&nbsp;&nbsp;<a href="mailto:alex.kamau.2558@gmail.com"><img src="assets/button-email.svg" height="38" alt="Email" /></a>&nbsp;&nbsp;<a href="https://wa.me/254746254055"><img src="assets/button-whatsapp.svg" height="38" alt="WhatsApp: +254 746 254 055" /></a>

<br/>

<sub>Every graphic on this page is generated by <a href="scripts/build_assets.py"><code>scripts/build_assets.py</code></a>.</sub>

</div>
