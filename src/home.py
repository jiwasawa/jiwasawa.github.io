from fasthtml.common import *

from src.layout import page_shell
from src.publications import publications_section


EXPERIENCE = [
    ("Feb. 2026 – present", "Solutions Architect", "NVIDIA"),
    ("Mar. 2025 – Jan. 2026", "Tech Lead", "Preferred Networks Inc."),
    ("Apr. 2021 – Jan. 2026", "Researcher", "Preferred Networks Inc."),
    (
        "Apr. 2018 – Mar. 2021",
        "Ph.D. in Physics",
        "Furusawa Laboratory, Dept. of Physics, The University of Tokyo",
    ),
    (
        "Apr. 2016 – Mar. 2018",
        "M.S. in Physics",
        "Sano Laboratory, Dept. of Physics, The University of Tokyo",
    ),
    (
        "Apr. 2012 – Mar. 2016",
        "B.S. in Physics",
        "Dept. of Physics, The University of Tokyo",
    ),
]


def _slash_links(links):
    nodes = []
    for idx, (label, href) in enumerate(links):
        if idx:
            nodes.append(Span("/", cls="sep"))
        nodes.append(A(label, href=href))
    return Div(*nodes, cls="bio-links")


def bio_header():
    links = [
        ("Email", "mailto:jiwasawa@nvidia.com"),
        ("CV", "static/junichiro_iwasawa_cv.pdf"),
        ("Google Scholar", "https://scholar.google.co.jp/citations?user=LampCPIAAAAJ&hl=en"),
        ("GitHub", "https://github.com/jiwasawa"),
        ("researchmap", "https://researchmap.jp/jiwasawa?lang=en"),
        ("LinkedIn", "https://www.linkedin.com/in/junichiro-iwasawa-875b37130/"),
        ("X", "https://twitter.com/jiwasawa"),
    ]
    return Header(
        Div(
            H1("Junichiro Iwasawa"),
            P("岩澤 諄一郎", cls="jp-name"),
            P(
                "I am a Solutions Architect at NVIDIA (since February 2026), working with "
                "Japanese enterprise customers on large language model training and inference, "
                "with a focus on the NeMo framework."
            ),
            P(
                "Previously, I was a Researcher and Tech Lead at ",
                A("Preferred Networks Inc.", href="https://www.preferred.jp/en/"),
                " (2021–2026), where I led BtoB machine learning solutions in healthcare and "
                "life sciences—including open medical LLMs surpassing GPT-4 on the Japanese "
                "Medical Licensing Exam and AI-based MRI diagnostic support—and mentored four "
                "research interns and one part-time engineer.",
            ),
            P(
                "I received my Ph.D. in Physics from the University of Tokyo (Furusawa Laboratory), "
                "studying evolutionary constraints and antibiotic resistance in ",
                Em("E. coli"),
                " with machine learning, and my M.S. in Physics (Sano Laboratory), studying "
                "active matter and collective motion of Janus colloidal particles.",
            ),
            _slash_links(links),
        ),
        Div(
            Img(
                src="static/profile_img2.jpg",
                alt="Junichiro Iwasawa",
                cls="portrait",
            ),
            cls="bio-photo-col",
        ),
        cls="bio",
        id="bio",
    )


def open_models_section():
    return Section(
        Div(H2("Open Models"), cls="sec-head"),
        Ul(
            Li(
                Div(
                    "Open Medical LLMs for the Japanese Medical Licensing Exam (JMLE)",
                    cls="models-title",
                ),
                Div(
                    "Led research at Preferred Networks building the first open LLMs to surpass GPT-4 on the JMLE.",
                    cls="pub-authors",
                ),
                Div(
                    A(
                        "[Llama3-Preferred-MedSwallow-70B]",
                        href="https://huggingface.co/pfnet/Llama3-Preferred-MedSwallow-70B",
                    ),
                    A(
                        "[Preferred-MedLLM-Qwen-72B]",
                        href="https://huggingface.co/pfnet/Preferred-MedLLM-Qwen-72B",
                    ),
                    cls="model-actions",
                ),
            ),
            cls="models-list",
        ),
        id="models",
    )


def experience_section():
    rows = [
        Tr(
            Td(period, cls="cv-period"),
            Td(Span(role, cls="cv-role"), ", ", Span(inst, cls="cv-inst")),
        )
        for period, role, inst in EXPERIENCE
    ]
    return Section(
        Div(
            H2("Experience & Education"),
            A("Full CV (PDF)", href="static/junichiro_iwasawa_cv.pdf", style="font-size:13.5px"),
            cls="sec-head",
        ),
        Table(Tbody(*rows), cls="cv-table"),
        id="experience",
    )


def home():
    return page_shell(
        bio_header(),
        open_models_section(),
        publications_section(standalone=False),
        experience_section(),
        active="home",
    )
