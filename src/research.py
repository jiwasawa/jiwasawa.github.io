from fasthtml.common import *
from monsterui.all import *

from src.sidebar import sidebar, navbar


def research_project(title, description, related_publications=None):
    related_publications = related_publications or []
    return Div(
        H3(title, cls="text-2xl font-semibold mb-3"),
        description if not isinstance(description, str) else P(description, cls="mb-4 leading-relaxed text-base"),
        Div(
            H4("Related Publications:", cls="text-lg font-semibold mb-2") if related_publications else None,
            Ul(*[Li(Safe(pub), cls="mb-2") for pub in related_publications], cls="list-disc pl-5"),
            cls="mt-4 text-base"
        ) if related_publications else None,
        cls="mb-12 pb-8 border-b border-gray-200 last:border-0"
    )


def research_content():
    return Div(
        # Introduction
        Section(
            H2("Research", cls="text-3xl font-semibold mb-6"),
            P("My research spans several interdisciplinary areas, ranging from physics, biology to machine learning.", 
              cls="mb-6 text-lg"),
            cls="mb-8"
        ),
        
        # Research Projects
        Section(
            research_project(
                "Large Language Models for Healthcare",
                P("""As part of my work at Preferred Networks, I've been leading projects focused on applying Large Language Models (LLMs) to healthcare challenges. 
                This includes developing specialized medical LLMs that can understand and generate domain-specific knowledge, assisting healthcare professionals 
                in diagnosis, and enhancing patient care through natural language processing.
                
                A major achievement was the development of medical domain-specialized LLMs, including """,
                A("Llama3-Preferred-MedSwallow-70B", 
                  href="https://huggingface.co/pfnet/Llama3-Preferred-MedSwallow-70B", 
                  cls=AT.primary),
                """ and """,
                A("Preferred-MedLLM-Qwen-72B", 
                  href="https://huggingface.co/pfnet/Preferred-MedLLM-Qwen-72B", 
                  cls=AT.primary),
                """, which are the first open LLMs to surpass GPT-4 in the Japanese Medical Licensing Exam (JMLE). These models demonstrate the potential for LLMs to 
                serve as valuable tools in healthcare settings, providing accurate medical information and supporting clinical decision-making.""",
                cls="mb-4 leading-relaxed text-base"
                ),
                [
                    """<a href="https://huggingface.co/pfnet/Preferred-MedLLM-Qwen-72B" class="text-primary hover:underline">Preferred-MedLLM-Qwen-72B</a>""",
                    """<a href="https://huggingface.co/pfnet/Llama3-Preferred-MedSwallow-70B" class="text-primary hover:underline">Llama3-Preferred-MedSwallow-70B</a>"""
                ]
            ),
            research_project(
                "Deciphering evolutionary constraints of Escherichia coli",
                """The prediction and control of evolution is a crucial topic for both evolutionary biology and tackling antibiotic resistance. 
                Although the lack of sufficient data has long hindered the mechanism of evolution, laboratory evolution experiments equipped 
                with high-throughput sequencing/phenotyping are now gradually changing this situation. The emerging data from recent laboratory 
                evolution experiments revealed repeatable features in evolutionary processes, suggesting the existence of constraints which could 
                lead to actual predictions of evolutionary outcomes. These results also paint an upbeat picture of evolution: biologically feasible 
                states and evolutionary trajectories could be distributed on a low-dimensional manifold within the high-dimensional space spanned 
                by biological features.
                
                By combining machine learning techniques with experimental data from high-throughput laboratory evolution experiments, we aim to 
                decipher the constraints which cause the low-dimensional evolutionary dynamics.""",
                [
                    """Junichiro Iwasawa, Tomoya Maeda, Atsushi Shibai, Hazuki Kotani, Masako Kawada, and Chikara Furusawa,
                    <a href="https://doi.org/10.1371/journal.pbio.3001920" class="text-primary hover:underline">Analysis of the evolution of resistance to multiple antibiotics enables prediction of the Escherichia coli phenotype-based fitness landscape</a>, 
                    PLOS Biology 20(12): e3001920 (2022).""",
                    
                    """Tomoya Maeda*, Junichiro Iwasawa*, Hazuki Kotani, Natsue Sakata, Masako Kawada, Takaaki Horinouchi, Aki Sakai, Kumi Tanabe, 
                    and Chikara Furusawa (*first co-authors), <a href="https://doi.org/10.1038/s41467-020-19713-w" class="text-primary hover:underline">High-throughput laboratory evolution and evolutionary constraints in Escherichia coli</a>, 
                    Nature Communications 11, 5970 (2020)."""
                ]
            ),
            
            research_project(
                "Collective phenomena of active colloidal particles (Janus particles)",
                """Collective motion can be observed in a wide variety of systems, from flocks of birds to the collective migration of living cells. 
                The ubiquitousness of this collective phenomena strongly hints the existence of universal properties which can be explained from basic 
                features of the system, and thus has motivated physicists for the past few decades leading to a field which is now called Active Matter.
                
                Janus particles, which are asymmetric colloidal particles with distinct hemispheres with different physical properties, can function as 
                self-propelled particles by dissipating energy to the surrounding fluid under an AC electric field. Since they provide a perfect test bed 
                for active matter research, Janus particles have increasingly gained attention in the field of active matter through the past decade. 
                We have explored universal features of collective motion through the active dynamics of Janus particles.""",
                [
                    """Junichiro Iwasawa, Daiki Nishiguchi, and Masaki Sano, <a href="https://doi.org/10.1103/PhysRevResearch.3.043104" class="text-primary hover:underline">Algebraic correlations and anomalous fluctuations in ordered flocks of 
                    Janus particles fueled by an AC electric field</a>, Physical Review Research 3, 043104 (2021).""",
                    
                    """Daiki Nishiguchi, Junichiro Iwasawa, Hong-Ren Jiang, and Masaki Sano, <a href="https://doi.org/10.1088/1367-2630/aa9b5b" class="text-primary hover:underline">Flagellar dynamics of chains of active Janus particles 
                    fueled by an AC electric field</a>, New Journal of Physics 20, 015002 (2018)."""
                ]
            ),
            
            research_project(
                "Medical image analysis in the small data regime",
                """Although neural networks are emerging in a wide range of topics, the preparation of sufficient data still remains as a hurdle to overcome, 
                especially for biological/medical data. Recently, self-supervised learning has been suggested as an effective pre-training method for various 
                fields such as natural language processing and image classification. The idea of self-supervised learning is to utilize unlabeled data to improve 
                task performance when only a few labeled data is available through the utilization of pre-text tasks. However, self-supervised learning requires 
                heavy computing before the main task, which could be a burden in certain scenarios.
                
                We have been working on methods where pre-text tasks could be utilized as auxillary tasks for regularizing segmentation models in the small labeled 
                data regime, making the learning process more data and cost-efficient.""",
                [
                    """Junichiro Iwasawa, Yuichiro Hirano, and Yohei Sugawara, <a href="https://arxiv.org/abs/2009.11160" class="text-primary hover:underline">Label-Efficient Multi-Task Segmentation using Contrastive Learning</a>, 
                    Brainlesion: Glioma, Multiple Sclerosis, Stroke and Traumatic Brain Injuries, LNCS 12658, 101 (2021). arXiv: 2009.11160."""
                ]
            ),
            cls="space-y-8"
        ),
        cls="col-span-7"
    )



def research_page():
    content = Container(
        Grid(
            sidebar(),
            research_content(),
            cols=12,
            cls="gap-8 mt-8"
        ),
        cls=ContainerT.xl
    )
    
    return Div(navbar(), content)
