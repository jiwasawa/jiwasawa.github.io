from fasthtml.common import *


SITE_CSS = """
  *, *::before, *::after { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    margin: 0;
    background: #ffffff;
    color: #222222;
    font-family: 'Lato', 'Noto Sans JP', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 15px;
    line-height: 1.65;
    -webkit-font-smoothing: antialiased;
  }
  a {
    color: #1772d0;
    text-decoration: none;
  }
  a:hover, a:focus-visible {
    color: #f09228;
    text-decoration: underline;
    text-underline-offset: 2px;
  }
  :focus-visible {
    outline: 2px solid #1772d0;
    outline-offset: 2px;
  }

  .wrap {
    max-width: 820px;
    margin: 0 auto;
    padding: 28px 24px 64px;
  }

  /* Navigation */
  .topnav {
    display: flex;
    justify-content: flex-end;
    align-items: baseline;
    flex-wrap: wrap;
    gap: 18px;
    font-size: 13.5px;
    color: #666666;
    margin-bottom: 34px;
  }
  .topnav.with-brand {
    justify-content: space-between;
    border-bottom: 1px solid #ececec;
    padding-bottom: 12px;
    margin-bottom: 30px;
  }
  .topnav-brand {
    font-size: 15px;
    font-weight: 700;
    color: #111111;
  }
  .topnav-brand:hover { color: #1772d0; text-decoration: none; }
  .topnav-links {
    display: flex;
    flex-wrap: wrap;
    gap: 18px;
  }
  .topnav a { color: #555555; }
  .topnav a:hover { color: #1772d0; }
  .topnav a.active {
    color: #111111;
    font-weight: 700;
  }

  /* Bio header */
  .bio {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 196px;
    gap: 36px;
    align-items: start;
    margin-bottom: 42px;
  }
  .bio > * { min-width: 0; }
  h1 {
    margin: 0 0 4px;
    font-size: 31px;
    font-weight: 400;
    line-height: 1.2;
    color: #111111;
    letter-spacing: -0.01em;
  }
  .jp-name {
    font-size: 14.5px;
    color: #666666;
    margin: 0 0 18px;
    font-weight: 400;
  }
  .bio p { margin: 0 0 13px; }
  .bio-links {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    row-gap: 4px;
    margin-top: 18px;
    font-size: 14.5px;
    color: #999999;
    line-height: 1.7;
  }
  .bio-links a { white-space: nowrap; }
  .bio-links .sep { margin: 0 7px; color: #cccccc; }
  .portrait {
    width: 186px;
    height: 186px;
    border-radius: 50%;
    object-fit: cover;
    object-position: center 15%;
    display: block;
    margin: 8px auto 0;
  }

  /* Section headings */
  section { margin-bottom: 40px; }
  .sec-head {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
    border-bottom: 1px solid #e6e6e6;
    padding-bottom: 6px;
    margin-bottom: 16px;
  }
  h2 {
    margin: 0;
    font-size: 21px;
    font-weight: 400;
    color: #111111;
  }
  h3 {
    margin: 0 0 8px;
    font-size: 17px;
    font-weight: 700;
    color: #111111;
  }
  .page-title {
    margin: 0 0 10px;
    font-size: 26px;
    font-weight: 400;
    color: #111111;
  }
  .page-lead {
    margin: 0 0 26px;
    color: #444444;
    max-width: 68ch;
  }

  /* Filter bar & legend */
  .filter-links {
    font-size: 13.5px;
    color: #777777;
  }
  .filter-links button {
    background: none;
    border: none;
    padding: 0;
    font: inherit;
    color: #1772d0;
    cursor: pointer;
  }
  .filter-links button:hover {
    color: #f09228;
    text-decoration: underline;
  }
  .filter-links button.active {
    color: #111111;
    font-weight: 700;
    cursor: default;
    text-decoration: none;
  }
  .legend {
    font-size: 13px;
    color: #666666;
    margin: -6px 0 14px;
  }
  .swatch {
    display: inline-block;
    width: 11px;
    height: 11px;
    background: #fdf9e7;
    border: 1px solid #e5dcaa;
    vertical-align: -1px;
    margin-right: 4px;
  }

  /* Open models block */
  .models-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .models-list li {
    padding: 10px 12px;
    margin: 0 -12px 6px;
    border-radius: 3px;
    background: #fdf9e7;
  }
  .models-title { font-weight: 700; color: #111111; }

  /* Publications & BibTeX (Design 1 + Design 4) */
  .pub-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .pub-item {
    display: grid;
    grid-template-columns: 52px minmax(0, 1fr);
    gap: 12px;
    padding: 11px 12px;
    margin: 0 -12px 4px;
    border-radius: 3px;
  }
  .pub-item > * { min-width: 0; }
  .pub-item.highlight { background: #fdf9e7; }
  .pub-item.hidden { display: none; }
  .pub-year {
    font-size: 13.5px;
    color: #666666;
    font-variant-numeric: tabular-nums;
    padding-top: 1px;
  }
  .pub-title { font-weight: 700; color: #111111; overflow-wrap: break-word; }
  .pub-authors {
    font-size: 14px;
    color: #444444;
    margin-top: 2px;
    overflow-wrap: break-word;
  }
  .pub-authors u {
    text-decoration: underline;
    text-underline-offset: 2px;
    color: #111111;
  }
  .pub-venue {
    font-size: 14px;
    margin-top: 2px;
    color: #444444;
    overflow-wrap: break-word;
  }
  .pub-venue em { color: #222222; }
  .pub-actions {
    margin-left: 6px;
    font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, monospace;
    font-size: 12.5px;
    white-space: nowrap;
  }
  .model-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 2px 12px;
    margin-top: 3px;
    font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, monospace;
    font-size: 12.5px;
  }
  .model-actions a { overflow-wrap: anywhere; }
  .bib-btn {
    background: none;
    border: none;
    padding: 0;
    margin-left: 6px;
    font: inherit;
    color: #6b1d1d;
    cursor: pointer;
  }
  .bib-btn:hover {
    color: #f09228;
    text-decoration: underline;
    text-underline-offset: 2px;
  }
  .bib-box {
    display: none;
    max-width: 100%;
    margin: 8px 0 2px;
    padding: 10px 58px 10px 12px;
    background: #f7f7f5;
    border: 1px solid #d8d8d4;
    border-radius: 2px;
    font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, monospace;
    font-size: 11.5px;
    line-height: 1.5;
    color: #222222;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    overflow-x: auto;
    position: relative;
  }
  .bib-box.open { display: block; }
  .copy-btn {
    position: absolute;
    top: 7px;
    right: 8px;
    background: #ffffff;
    border: 1px solid #cccccc;
    border-radius: 2px;
    font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, monospace;
    font-size: 11px;
    padding: 2px 7px;
    cursor: pointer;
    color: #333333;
  }
  .copy-btn:hover {
    border-color: #1772d0;
    color: #1772d0;
  }

  /* CV table */
  .cv-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14.5px;
  }
  .cv-table td {
    padding: 7px 0;
    vertical-align: top;
    border-bottom: 1px solid #f0f0f0;
  }
  .cv-table tr:last-child td { border-bottom: none; }
  .cv-period {
    width: 175px;
    color: #595959;
    font-size: 13.5px;
    font-variant-numeric: tabular-nums;
    padding-right: 16px;
  }
  .cv-role { font-weight: 700; color: #111111; }
  .cv-inst { color: #444444; }

  /* Research subpage */
  .research-entry {
    padding-bottom: 24px;
    margin-bottom: 24px;
    border-bottom: 1px solid #ececec;
  }
  .research-entry:last-child { border-bottom: none; margin-bottom: 0; }
  .research-entry p { margin: 0 0 12px; color: #2d2d2d; }
  .related-label {
    font-size: 13.5px;
    font-weight: 700;
    color: #555555;
    margin: 14px 0 6px;
  }
  .plain-list {
    margin: 0;
    padding-left: 20px;
  }
  .plain-list li {
    margin-bottom: 8px;
    font-size: 14.5px;
    overflow-wrap: break-word;
  }

  /* Talks subpage */
  .jump-bar {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    row-gap: 4px;
    font-size: 13.5px;
    color: #888888;
    margin: -10px 0 28px;
    line-height: 1.7;
  }
  .jump-bar .sep { margin: 0 7px; color: #cccccc; }
  .talk-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .talk-list li {
    padding: 9px 0;
    border-bottom: 1px solid #f0f0f0;
    font-size: 14.5px;
    overflow-wrap: break-word;
  }
  .talk-list li:last-child { border-bottom: none; }
  .talk-title { font-weight: 700; color: #111111; }
  .talk-jp { color: #555555; font-size: 14px; }
  .talk-meta { color: #444444; font-size: 14px; margin-top: 2px; }
  .sub-h {
    font-size: 15.5px;
    font-weight: 700;
    color: #444444;
    margin: 0 0 10px;
  }

  /* Footer */
  footer {
    margin-top: 44px;
    padding-top: 14px;
    border-top: 1px solid #ececec;
    font-size: 12.5px;
    color: #777777;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 8px;
  }
  footer a { color: #555555; }
  footer a:hover { color: #1772d0; }

  @media (max-width: 680px) {
    .wrap { padding: 18px 16px 48px; }
    .topnav {
      justify-content: flex-start;
      gap: 6px 12px;
      font-size: 13px;
      margin-bottom: 24px;
    }
    .topnav.with-brand {
      gap: 8px 12px;
      margin-bottom: 24px;
    }
    .topnav-links { gap: 6px 12px; }
    .bio { grid-template-columns: minmax(0, 1fr); gap: 20px; margin-bottom: 34px; }
    .bio-photo-col { order: -1; }
    .portrait { width: 148px; height: 148px; margin: 0 auto; }
    h1 { font-size: 27px; }
    .bio-links { gap: 6px 14px; }
    .bio-links .sep { display: none; }
    .models-list li { padding: 10px 12px; margin: 0 -4px 6px; }
    .pub-item { grid-template-columns: minmax(0, 1fr); gap: 2px; padding: 10px 12px; margin: 0 -4px 4px; }
    .pub-year { font-size: 12.5px; color: #777777; }
    .bib-box { padding: 34px 10px 10px 10px; font-size: 11px; }
    .cv-table td { display: block; padding: 2px 0; border: none; }
    .cv-table tr { display: block; padding: 7px 0; border-bottom: 1px solid #f0f0f0; }
    .cv-period { width: auto; }
  }
"""


SITE_SCRIPT = """
document.addEventListener('DOMContentLoaded', () => {
  const filterBtns = document.querySelectorAll('[data-pub-filter]');
  const pubItems = document.querySelectorAll('.pub-item');
  if (filterBtns.length) {
    const applyFilter = (mode) => {
      filterBtns.forEach((b) => {
        const active = b.dataset.pubFilter === mode;
        b.classList.toggle('active', active);
        b.setAttribute('aria-pressed', active ? 'true' : 'false');
      });
      pubItems.forEach((li) => {
        li.classList.toggle('hidden', mode === 'highlight' && !li.classList.contains('highlight'));
      });
    };
    filterBtns.forEach((b) => b.addEventListener('click', () => applyFilter(b.dataset.pubFilter)));
  }

  document.querySelectorAll('.bib-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      const box = document.getElementById(btn.getAttribute('aria-controls'));
      if (!box) return;
      const open = box.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  document.querySelectorAll('.copy-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      const code = btn.parentElement && btn.parentElement.querySelector('code');
      if (!code) return;
      const text = code.textContent;
      const done = () => {
        btn.textContent = 'copied';
        setTimeout(() => { btn.textContent = 'copy'; }, 1200);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done).catch(() => {
          const ta = document.createElement('textarea');
          ta.value = text;
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.select();
          try { document.execCommand('copy'); } catch (e) {}
          document.body.removeChild(ta);
          done();
        });
      } else {
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand('copy'); } catch (e) {}
        document.body.removeChild(ta);
        done();
      }
    });
  });
});
"""


SITE_HEADERS = (
    Meta(charset="utf-8"),
    Meta(name="viewport", content="width=device-width, initial-scale=1"),
    Meta(
        name="description",
        content="Junichiro Iwasawa — Solutions Architect at NVIDIA, previously Researcher and Tech Lead at Preferred Networks, Ph.D. in Physics (The University of Tokyo).",
    ),
    Link(rel="preconnect", href="https://fonts.googleapis.com"),
    Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
    Link(
        rel="stylesheet",
        href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Lato:ital,wght@0,400;0,700;1,400&family=Noto+Sans+JP:wght@400;500&display=swap",
    ),
    Style(SITE_CSS),
    Script(SITE_SCRIPT),
)


def topnav(active="home"):
    if active == "home":
        items = [
            ("Bio", "#bio"),
            ("Publications", "#publications"),
            ("Experience", "#experience"),
            ("Research", "/research"),
            ("Talks", "/talks"),
            ("Blog", "/blog"),
            ("ブログ", "/blog_jp"),
        ]
        return Nav(
            *[A(label, href=href) for label, href in items],
            cls="topnav",
            aria_label="Site navigation",
        )

    items = [
        ("About", "/", "home"),
        ("Publications", "/publications", "publications"),
        ("Research", "/research", "research"),
        ("Talks", "/talks", "talks"),
        ("Blog", "/blog", "blog"),
        ("ブログ", "/blog_jp", "blog_jp"),
    ]
    return Nav(
        A("Junichiro Iwasawa", href="/", cls="topnav-brand"),
        Div(
            *[
                A(label, href=href, cls="active" if key == active else None)
                for label, href, key in items
            ],
            cls="topnav-links",
        ),
        cls="topnav with-brand",
        aria_label="Site navigation",
    )


def site_footer():
    return Footer(
        Span("Junichiro Iwasawa · Tokyo, Japan"),
        Span(
            A("Research", href="/research"),
            " · ",
            A("Talks", href="/talks"),
            " · ",
            A("Blog", href="/blog"),
            " · ",
            A("ブログ", href="/blog_jp"),
        ),
    )


def page_shell(*children, active="home"):
    return Div(
        topnav(active=active),
        *children,
        site_footer(),
        cls="wrap",
    )
