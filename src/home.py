from fasthtml.common import *
from monsterui.all import *

from src.sidebar import sidebar, navbar


def cv_timeline_item(period, title, institution):
    return Card(
        DivLAligned(
            Span(period, cls=TextPresets.muted_sm),
            Div(
                H4(title, cls=TextT.bold),
                P(institution, cls=TextPresets.muted_sm)
            ),
            cls="space-x-4"
        ),
        cls="mb-4 p-4"
    )


def main_content():
    return Div(
        # Introduction section
        Section(
            H2("About Junichiro", cls="text-3xl font-semibold mb-4"),
            P("""As a Researcher at """,
            A("Preferred Networks Inc.", 
            href="https://www.preferred.jp/en/", 
            cls=AT.primary), 
            """, I primarily engage with clients 
            in the healthcare and life sciences sectors.
            Currently, I serve as the tech lead for providing BtoB solutions using Large Language Models (LLMs) .""",
            cls="mb-3 leading-relaxed text-base"),
            P("""I led a research project to build a medical domain-specialized LLM, 
            resulting in """, 
            A("Llama3-Preferred-MedSwallow-70B", 
            href="https://huggingface.co/pfnet/Llama3-Preferred-MedSwallow-70B", 
            cls=AT.primary), 
            """ and """,
            A("Preferred-MedLLM-Qwen-72B", 
            href="https://huggingface.co/pfnet/Preferred-MedLLM-Qwen-72B", 
            cls=AT.primary),
            """, the first open LLMs that 
            surpass GPT-4 in the Japanese Medical Licensing Exam (JMLE).
            Over the past few years, I have also been leading a project for developing a deep learning based solution 
            aimed at enhancing the diagnosis of endometriosis through the analysis of MRIs, 
            in collaboration with a leading pharmaceutical company.""",
            cls="mb-3 leading-relaxed text-base"),
            P("""I have experience formulating problems through consultations with clients and 
            providing solutions based on deep learning / machine learning.
            Additionally, I have been the main mentor for four research interns and one part-time engineer.""",
            cls="mb-3 leading-relaxed text-base"),
            P("""During my PhD, I have been working on the development of machine learning methods 
            for gene expression/mutation data to tackle the problem of antibiotic resistance of bacteria.""",
            cls="mb-3 leading-relaxed text-base"),
            Div(
                Label("Large Language Models", cls="mr-2 mb-2"),
                Label("Machine Learning", cls="mr-2 mb-2"),
                Label("Healthcare", cls="mr-2 mb-2"),
                Label("Biophysics", cls="mr-2 mb-2"),
                Label("Statistical Physics", cls="mr-2 mb-2"),
                cls="mt-6 flex flex-wrap"
            ),
            cls="mb-12"
        ),
        
        Section(
            H2("CV", cls="text-3xl font-semibold mb-4"),
            P("Junichiro Iwasawa (岩澤 諄一郎)", cls=TextPresets.muted_lg + " mb-4"),
            DivLAligned(
                UkIcon("file-text", cls="mr-2"),
                A("Link to CV (pdf)", href="junichiro_iwasawa_cv.pdf", cls=AT.primary),
                cls="mb-6"
            ),
            cv_timeline_item("Mar. 2025–present", "Tech Lead", "Preferred Networks Inc."),
            cv_timeline_item("Apr. 2021–present", "Researcher", "Preferred Networks Inc."),
            cv_timeline_item("Apr. 2018–Mar. 2021", "Doctor of Philosophy", "Furusawa Laboratory, Dept. of Physics, The University of Tokyo"),
            cv_timeline_item("Apr. 2016–Mar. 2018", "Master of Science", "Sano Laboratory, Dept. of Physics, The University of Tokyo"),
            cv_timeline_item("Apr. 2012–Mar. 2016", "Bachelor of Science", "Dept. of Physics, The University of Tokyo"),
            cls="mb-8"
        ),
        cls="col-span-7"  # Added col-span-9 to take up 9/12 columns
    )

def home():
    content = Container(
        Grid(
            sidebar(),
            main_content(),
            cols=12,  # Use a 12-column grid
            cls="gap-8 mt-8"
        ),
        cls=ContainerT.xl,
    )
    return Div(navbar(), content)
