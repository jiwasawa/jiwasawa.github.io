from fasthtml.common import *
from monsterui.all import *

from src.sidebar import navbar, _social_link


# Curated "Selected work" cards. Content is hand-picked, not auto-generated, so
# the band stays punchy; keep this to 3-4 entries.
HIGHLIGHTS = [
    {
        "tag": "Medical LLMs",
        "title": "Open medical LLMs that surpass GPT-4 on the Japanese Medical Licensing Exam",
        "result": "Led the research building the first open LLMs to beat GPT-4 on the JMLE.",
        "links": [
            ("Llama3-Preferred-MedSwallow-70B",
             "https://huggingface.co/pfnet/Llama3-Preferred-MedSwallow-70B"),
            ("Preferred-MedLLM-Qwen-72B",
             "https://huggingface.co/pfnet/Preferred-MedLLM-Qwen-72B"),
        ],
    },
    {
        "tag": "Medical imaging",
        "title": "AI-based MRI reading support (AMP) for deep endometriosis diagnosis",
        "result": "Deep-learning diagnostic support developed with a leading pharmaceutical company.",
        "links": [
            ("Scientific Reports (2025)",
             "https://doi.org/10.1038/s41598-025-30277-x"),
        ],
    },
    {
        "tag": "Evolutionary biology",
        "title": "High-throughput laboratory evolution reveals evolutionary constraints in E. coli",
        "result": "Predicting antibiotic-resistance fitness landscapes from large-scale evolution experiments.",
        "links": [
            ("Nature Communications",
             "https://doi.org/10.1038/s41467-020-19713-w"),
            ("PLOS Biology",
             "https://doi.org/10.1371/journal.pbio.3001920"),
        ],
    },
    {
        "tag": "Active matter",
        "title": "Collective motion of Janus particles under an AC electric field",
        "result": "Algebraic correlations and anomalous fluctuations in ordered flocks of active particles.",
        "links": [
            ("Physical Review Research",
             "https://doi.org/10.1103/PhysRevResearch.3.043104"),
        ],
    },
]


# Soft radial wash behind the hero. Uses the theme's primary token so it tracks
# the accent color and adapts to light/dark automatically.
_hero_glow = Style("""
    .hero-glow {
        background:
            radial-gradient(60rem 30rem at 15% -10%, hsl(var(--primary) / 0.10), transparent 60%),
            radial-gradient(50rem 28rem at 100% 0%, hsl(var(--primary) / 0.06), transparent 55%);
    }
""")


def _btn_primary(icon, label, href):
    return A(
        UkIcon(icon, height=16, width=16),
        Span(label),
        href=href,
        cls="inline-flex items-center gap-2 px-4 py-2.5 text-sm font-semibold "
            "rounded-lg bg-primary text-primary-foreground shadow-sm hover:opacity-90",
    )


def _btn_outline(icon, label, href):
    return A(
        UkIcon(icon, height=16, width=16),
        Span(label),
        href=href,
        cls="inline-flex items-center gap-2 px-4 py-2.5 text-sm font-semibold "
            "rounded-lg border border-border hover:border-primary hover:text-primary",
    )


def hero():
    text_col = Div(
        P("岩澤 諄一郎", cls="text-sm font-medium text-primary mb-3"),
        H1("Junichiro Iwasawa",
           cls="text-4xl sm:text-5xl font-extrabold tracking-tight leading-[1.05]"),
        P("Solutions Architect at NVIDIA. LLM training/inference for enterprise.",
          cls="mt-4 text-lg sm:text-xl font-medium text-muted-foreground"),
        P("I work with Japanese enterprise customers on large language model training "
          "and inference. Previously a researcher and tech lead at Preferred Networks, "
          "building medical LLMs and deep-learning solutions for healthcare.",
          cls="mt-4 max-w-xl mx-auto md:mx-0 leading-7 text-muted-foreground"),
        # Primary actions
        Div(
            _btn_primary("file-text", "Curriculum Vitae", "static/junichiro_iwasawa_cv.pdf"),
            _btn_outline("graduation-cap", "Scholar",
                         "https://scholar.google.co.jp/citations?user=LampCPIAAAAJ&hl=en"),
            _btn_outline("github", "GitHub", "https://github.com/jiwasawa"),
            _btn_outline("mail", "Email", "mailto:jiwasawa@nvidia.com"),
            cls="mt-7 flex flex-wrap items-center justify-center md:justify-start gap-3",
        ),
        # Secondary icon links
        Div(
            _social_link("twitter", "Twitter", "https://twitter.com/jiwasawa"),
            _social_link("linkedin", "LinkedIn",
                         "https://www.linkedin.com/in/junichiro-iwasawa-875b37130/"),
            _social_link("book-open", "researchmap",
                         "https://researchmap.jp/jiwasawa?lang=en"),
            cls="mt-5 flex flex-wrap items-center justify-center md:justify-start gap-1 -ml-1.5",
        ),
        cls="order-2 md:order-1 text-center md:text-left",
    )

    image_col = Div(
        Img(
            src="static/profile_img2.jpg",
            alt="Junichiro Iwasawa",
            cls="w-44 h-44 sm:w-52 sm:h-52 rounded-2xl object-cover "
                "ring-1 ring-border shadow-xl",
        ),
        cls="order-1 md:order-2 flex justify-center",
    )

    return Section(
        Div(
            text_col,
            image_col,
            cls="grid md:grid-cols-[1fr_auto] gap-10 md:gap-12 items-center",
        ),
        cls="hero-glow rounded-2xl px-6 sm:px-8 pt-12 pb-14 mb-16 "
            "border border-border/60",
    )


def highlight_card(tag, title, result, links):
    return Div(
        Span(
            tag,
            cls="inline-block text-[11px] font-semibold uppercase tracking-wide "
                "text-primary bg-primary/10 rounded px-2 py-0.5",
        ),
        H3(title, cls="mt-3 font-semibold text-lg leading-snug"),
        P(result, cls="mt-2 text-sm leading-6 text-muted-foreground"),
        Div(
            *[A(label, href=href, cls=AT.primary) for label, href in links],
            cls="mt-4 flex flex-wrap gap-x-4 gap-y-1 text-sm font-medium",
        ),
        cls="rounded-xl border border-border bg-muted/30 p-5 "
            "hover:border-primary/50 hover:shadow-md transition-colors",
    )


def highlights():
    return Section(
        Div(
            H2("Selected work", cls="text-2xl font-bold tracking-tight"),
            A("All publications →", href="/publications",
              cls=AT.primary + " text-sm font-medium"),
            cls="flex items-end justify-between gap-4 mb-6",
        ),
        Div(
            *[highlight_card(h["tag"], h["title"], h["result"], h["links"])
              for h in HIGHLIGHTS],
            cls="grid sm:grid-cols-2 gap-4",
        ),
        cls="mb-16",
    )


def about_condensed():
    return Section(
        H2("About", cls="text-2xl font-bold tracking-tight mb-5"),
        Div(
            P("As a Solutions Architect at NVIDIA, I work with Japanese enterprise "
              "customers on large language model training and inference, with a focus on "
              "the NeMo framework. I joined NVIDIA in February 2026."),
            P("Previously, as a Researcher and Tech Lead at ",
              A("Preferred Networks Inc.", href="https://www.preferred.jp/en/", cls=AT.primary),
              ", I engaged with clients in the healthcare and life sciences sectors and "
              "led BtoB solutions built on large language models."),
            P("I have experience formulating problems through consultation with clients and "
              "delivering deep-learning / machine-learning solutions, and I was the main "
              "mentor for four research interns and one part-time engineer."),
            P("During my PhD in the Department of Physics at the University of Tokyo, I "
              "developed machine-learning methods for gene expression and mutation data to "
              "tackle antibiotic resistance in bacteria."),
            cls="space-y-4 leading-relaxed text-base",
        ),
        cls="mb-16 max-w-2xl",
    )


def cv_entry(period, title, institution, current=False):
    dot_cls = "bg-primary" if current else "bg-muted-foreground/40"
    period_cls = "text-primary" if current else "text-muted-foreground"
    return Li(
        Span(
            cls=f"absolute -left-[30px] top-1.5 w-3 h-3 rounded-full {dot_cls} ring-4 ring-background"
        ),
        P(period, cls=f"text-xs font-semibold uppercase tracking-wide {period_cls}"),
        P(title, cls="font-medium mt-0.5"),
        P(institution.rstrip("."), cls="text-sm text-muted-foreground"),
        cls="ml-6 pb-7 last:pb-0 relative",
    )


def cv_section():
    return Section(
        H2("CV", cls="text-2xl font-bold tracking-tight mb-1"),
        P("Junichiro Iwasawa (岩澤 諄一郎)", cls=TextPresets.muted_lg + " mb-8"),
        Ol(
            cv_entry("Feb. 2026 – present", "Solutions Architect", "NVIDIA", current=True),
            cv_entry("Mar. 2025 – Jan. 2026", "Tech Lead", "Preferred Networks Inc."),
            cv_entry("Apr. 2021 – Jan. 2026", "Researcher", "Preferred Networks Inc."),
            cv_entry(
                "Apr. 2018 – Mar. 2021",
                "Doctor of Philosophy",
                "Furusawa Laboratory, Dept. of Physics, The University of Tokyo",
            ),
            cv_entry(
                "Apr. 2016 – Mar. 2018",
                "Master of Science",
                "Sano Laboratory, Dept. of Physics, The University of Tokyo",
            ),
            cv_entry("Apr. 2012 – Mar. 2016", "Bachelor of Science", "Dept. of Physics, The University of Tokyo"),
            cls="relative border-l border-border ml-2",
        ),
        cls="mb-16 max-w-2xl",
    )


def home():
    content = Container(
        _hero_glow,
        hero(),
        highlights(),
        about_condensed(),
        cv_section(),
        cls=ContainerT.xl + " mt-12",
    )
    return Div(navbar(), content)
