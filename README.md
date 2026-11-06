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

I design, build and **operate** business-critical web platforms, from the first requirements conversation to the production server and everything after it ships.

I'm the full-stack developer and sole technical owner for **four companies**, and I build my own products and open-source software on the side. I pick the stack to fit the problem: **React** and **Next.js** on the front, **Laravel**, **Node.js** or **FastAPI** behind it, on **PostgreSQL** or **MySQL**, run on **Linux** and **Docker**.

<p align="center"><sub><b>4</b> companies I run tech for &nbsp;·&nbsp; <b>3</b> platforms in production &nbsp;·&nbsp; Mozilla RCC <b>Top 5</b> &nbsp;·&nbsp; open-source maintainer</sub></p>

## Platforms I run for businesses

<a href="https://www.euroafriquecorporateskills.com"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-euroafrique-dark.svg" /><source media="(prefers-color-scheme: light)" srcset="assets/card-euroafrique-light.svg" /><img src="assets/card-euroafrique-dark.svg" width="49%" alt="EuroAfrique Corporate Skills — corporate training platform, in production" /></picture></a>&nbsp;<a href="https://afriasiacareercenter.com"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-afriasia-dark.svg" /><source media="(prefers-color-scheme: light)" srcset="assets/card-afriasia-light.svg" /><img src="assets/card-afriasia-dark.svg" width="49%" alt="AfriAsia Career Development Center — executive-training and booking platform, in production" /></picture></a>

<a href="https://chaniapublishers.com"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-chania-dark.svg" /><source media="(prefers-color-scheme: light)" srcset="assets/card-chania-light.svg" /><img src="assets/card-chania-dark.svg" width="49%" alt="Chania Publishers LMS — learning management system, in production" /></picture></a>&nbsp;<a href="https://portfolio-alex-m-kamau.vercel.app/work/chania-finance-consultancy"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-chania-finance-dark.svg" /><source media="(prefers-color-scheme: light)" srcset="assets/card-chania-finance-light.svg" /><img src="assets/card-chania-finance-dark.svg" width="49%" alt="Chania Finance Consultancy — finance-training and booking platform, in development" /></picture></a>

## Products and open source

<a href="https://portfolio-alex-m-kamau.vercel.app/work/businessos"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-businessos-dark.svg" /><source media="(prefers-color-scheme: light)" srcset="assets/card-businessos-light.svg" /><img src="assets/card-businessos-dark.svg" width="49%" alt="BusinessOS — multi-tenant operating system for SMEs, in development" /></picture></a>&nbsp;<a href="https://portfolio-alex-m-kamau.vercel.app/work/unified-threat-detection-response"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-utdrs-dark.svg" /><source media="(prefers-color-scheme: light)" srcset="assets/card-utdrs-light.svg" /><img src="assets/card-utdrs-dark.svg" width="49%" alt="UTDRS — unified threat detection and response, live, Mozilla RCC Top 5" /></picture></a>

<a href="https://portfolio-alex-m-kamau.vercel.app/work/secure-file-sharing"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-secure-file-sharing-dark.svg" /><source media="(prefers-color-scheme: light)" srcset="assets/card-secure-file-sharing-light.svg" /><img src="assets/card-secure-file-sharing-dark.svg" width="49%" alt="Secure File Sharing — encrypted file sharing for teams, in development" /></picture></a>&nbsp;<a href="https://github.com/Alex-Muhscience/MuhOS"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-muhos-dark.svg" /><source media="(prefers-color-scheme: light)" srcset="assets/card-muhos-light.svg" /><img src="assets/card-muhos-dark.svg" width="49%" alt="MuhOS — open-source desktop shell for Hyprland on Fedora, pre-release" /></picture></a>

<sub>Also built: <a href="https://muhscience-tech-labs-website.vercel.app"><b>Muhscience Tech Labs</b></a>, a Next.js company site, and <a href="https://github.com/Alex-Muhscience/Pass-KeyGen"><b>KeyGen</b></a>, a Flutter password manager. Every project has a full case study on my <a href="https://portfolio-alex-m-kamau.vercel.app/work">portfolio</a>.</sub>

<details>
<summary><b>How I put a platform together</b></summary>

<br/>

Not one system, but the shape most of mine share: a boring, fast request path, with everything slow or failure-prone pushed behind it.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/architecture-light.svg" />
  <img src="assets/architecture-dark.svg" width="100%" alt="Request path: client, Cloudflare, nginx, the application and the database. Behind the request: Redis, queue workers, generated documents, signed webhooks and verified payment callbacks. On every layer: security, delivery and operations." />
</picture>

- **Architecture follows requirements.** A content site, a payment workflow and a multi-tenant ledger don't want the same design.
- **Modular monolith first.** Services get extracted when a domain proves it needs to scale or release on its own.
- **Contain failure.** A slow PDF render or a dead webhook should never fail an unrelated checkout.
- **Security and audit are architecture,** designed in from the first schema.
- **Measure, then optimise.** Find the bottleneck with real data volume, then fix that one thing.
- **Build systems that can be operated.** Health checks, correlated logs, repeatable deploys and tested restores are part of the feature.

</details>

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
  <img src="assets/journey-dark.svg" width="100%" alt="Aug 2025 to now: Full-Stack Developer and Technical Owner at EuroAfrique Corporate Skills, Chania Publishers, AfriAsia Career Development Center and Chania Finance Consultancy. May to Aug 2025: Freelance Web Development Tutor. Aug 2024 to Feb 2025: Network Technician at Gicatech Enterprise Solutions. May to Aug 2024: Software Development Intern at Secunets Technologies. 2021 to 2025: BSc Computer Science, Second Class Honours (Upper), Kisii University." />
</picture>

## Activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Alex-Muhscience/Alex-Muhscience/output/github-streak.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Alex-Muhscience/Alex-Muhscience/output/github-streak-light.svg" />
  <img src="https://raw.githubusercontent.com/Alex-Muhscience/Alex-Muhscience/output/github-streak.svg" width="49%" alt="GitHub streak" />
</picture>
<img src="https://github-stats-extended.vercel.app/api?username=Alex-Muhscience&rank_icon=percentile&show_icons=true&include_all_commits=true&hide_border=true&bg_color=00000000&title_color=2f81f7&text_color=8b949e&icon_color=2f81f7&disable_animations=true" width="49%" alt="GitHub stats" />

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

<sub>Every graphic on this page is generated by <a href="scripts/build_assets.py"><code>scripts/build_assets.py</code></a>.</sub>

</div>
