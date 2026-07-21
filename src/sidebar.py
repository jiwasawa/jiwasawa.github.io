from fasthtml.common import *
from monsterui.all import *


_NAV_LINK_CLS = (
    "px-3 py-2 rounded-md text-muted-foreground "
    "hover:text-primary hover:bg-muted transition-colors"
)
_ICON_BTN_CLS = (
    "p-1.5 rounded-lg text-muted-foreground "
    "hover:text-primary hover:bg-muted transition-colors"
)


def _social_link(icon, label, href):
    return A(
        UkIcon(icon, height=18, width=18),
        href=href,
        title=label,
        aria_label=label,
        cls=_ICON_BTN_CLS,
    )


def sidebar():
    return Div(
        Div(
            Img(
                src="static/profile_img2.jpg",
                alt="Junichiro Iwasawa",
                cls="w-40 h-40 rounded-full object-cover mx-auto md:mx-0 "
                    "ring-4 ring-primary/25 shadow-sm mb-5",
            ),
            H4("Junichiro Iwasawa", cls="text-lg font-semibold tracking-tight"),
            P("Solutions Architect at NVIDIA", cls=TextPresets.muted_sm),
            # Icon-button social row. Blog lives in the navbar, so it is omitted
            # here to keep the row inside the sidebar column. -ml-1.5 cancels the
            # first icon's padding so the row aligns flush with the heading above.
            Div(
                _social_link("twitter", "Twitter", "https://twitter.com/jiwasawa"),
                _social_link(
                    "linkedin",
                    "LinkedIn",
                    "https://www.linkedin.com/in/junichiro-iwasawa-875b37130/",
                ),
                _social_link(
                    "graduation-cap",
                    "Google Scholar",
                    "https://scholar.google.co.jp/citations?user=LampCPIAAAAJ&hl=en",
                ),
                _social_link("github", "GitHub", "https://github.com/jiwasawa"),
                _social_link(
                    "book-open",
                    "researchmap",
                    "https://researchmap.jp/jiwasawa?lang=en",
                ),
                cls="flex flex-wrap items-center gap-1 -ml-1.5 mt-5 "
                    "justify-center md:justify-start",
            ),
            A(
                DivLAligned(
                    UkIcon("file-text", height=16, width=16, cls="mr-2"),
                    Span("Curriculum Vitae"),
                ),
                href="static/junichiro_iwasawa_cv.pdf",
                cls="inline-flex items-center mt-6 px-3.5 py-2 text-sm font-medium "
                    "rounded-lg border border-border hover:border-primary "
                    "hover:text-primary transition-colors",
            ),
            cls="text-center md:text-left p-4",
        ),
        cls="col-span-12 md:col-span-4 lg:col-span-3 md:sticky md:top-24",
    )


def _theme_toggle():
    return Button(
        UkIcon("moon", height=18, width=18, cls="block dark:hidden"),
        UkIcon("sun", height=18, width=18, cls="hidden dark:block"),
        onclick="__toggleMode()",
        title="Toggle dark mode",
        aria_label="Toggle dark mode",
        cls="p-2 rounded-md text-muted-foreground "
            "hover:text-primary hover:bg-muted transition-colors",
    )


def navbar():
    links = [
        A(label, href=href, cls=_NAV_LINK_CLS)
        for label, href in [
            ("About", "/"),
            ("Publications", "/publications"),
            ("Research", "/research"),
            ("Talks", "/talks"),
            ("Blog", "/blog"),
            ("ブログ", "/blog_jp"),
        ]
    ]
    return NavBar(
        *links,
        _theme_toggle(),
        brand=H3("Junichiro Iwasawa", cls="text-xl font-semibold tracking-tight"),
        sticky=True,
        cls="px-4 py-2 mb-4",
    )
