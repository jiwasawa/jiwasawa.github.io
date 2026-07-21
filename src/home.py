from fasthtml.common import *
from monsterui.all import *

from src.sidebar import sidebar, navbar


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


def main_content():
    return Div(
        # Introduction section
        Section(
            H2("About", cls="text-3xl font-bold tracking-tight mb-6"),
            Div(
                P("As a Solutions Architect at NVIDIA, I work with Japanese enterprise customers on large language model training and inference, with a focus on the NeMo framework. I joined NVIDIA in February 2026."),
                P("Previously, as a Researcher at ",
                A("Preferred Networks Inc.",
                href="https://www.preferred.jp/en/",
                cls=AT.primary),
                ", I primarily engaged with clients in the healthcare and life sciences sectors and served as the tech lead for providing BtoB solutions using Large Language Models (LLMs)."),
                P("I led a research project to build a medical domain-specialized LLM, resulting in ",
                A("Llama3-Preferred-MedSwallow-70B",
                href="https://huggingface.co/pfnet/Llama3-Preferred-MedSwallow-70B",
                cls=AT.primary),
                " and ",
                A("Preferred-MedLLM-Qwen-72B",
                href="https://huggingface.co/pfnet/Preferred-MedLLM-Qwen-72B",
                cls=AT.primary),
                ", the first open LLMs that surpass GPT-4 in the Japanese Medical Licensing Exam (JMLE). I also led a project for developing a deep learning based solution aimed at enhancing the diagnosis of endometriosis through the analysis of MRIs, in collaboration with a leading pharmaceutical company."),
                P("I have experience formulating problems through consultations with clients and providing solutions based on deep learning / machine learning. I have also been the main mentor for four research interns and one part-time engineer."),
                P("During my PhD, I worked on the development of machine learning methods for gene expression/mutation data to tackle the problem of antibiotic resistance of bacteria."),
                cls="max-w-2xl space-y-4 leading-relaxed text-base"
            ),
            cls="mb-16"
        ),

        Section(
            H2("CV", cls="text-3xl font-bold tracking-tight mb-2"),
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
                cls="relative border-l border-border ml-2"
            ),
            cls="mb-16"
        ),
        cls="col-span-12 md:col-span-8 lg:col-span-9"
    )


def home():
    content = Container(
        Grid(
            sidebar(),
            main_content(),
            cols=12,
            cols_sm=1,  # Single column on small screens
            cls="gap-10 mt-12"
        ),
        cls=ContainerT.xl,
    )
    return Div(navbar(), content)
