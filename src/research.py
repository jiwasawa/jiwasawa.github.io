from fasthtml.common import *

from src.layout import page_shell


def research_project(title, description, related_publications=None):
    related_publications = related_publications or []
    body = description if not isinstance(description, str) else [P(p.strip()) for p in description.strip().split("\n\n")]
    return Article(
        H3(title),
        *(body if isinstance(body, list) else [body]),
        (
            Div(
                P("Related publications & models", cls="related-label"),
                Ul(*[Li(NotStr(pub)) for pub in related_publications], cls="plain-list"),
            )
            if related_publications
            else None
        ),
        cls="research-entry",
    )


def research_page():
    return page_shell(
        H1("Research", cls="page-title"),
        P(
            "My research spans several interdisciplinary areas, ranging from physics and biology to machine learning.",
            cls="page-lead",
        ),
        Section(
            research_project(
                "Large Language Models for Healthcare",
                [
                    P(
                        "As part of my work at Preferred Networks, I led projects focused on applying "
                        "Large Language Models (LLMs) to healthcare challenges. This includes developing "
                        "specialized medical LLMs that can understand and generate domain-specific "
                        "knowledge, assisting healthcare professionals in diagnosis, and enhancing "
                        "patient care through natural language processing."
                    ),
                    P(
                        "A major achievement was the development of medical domain-specialized LLMs, including ",
                        A(
                            "Llama3-Preferred-MedSwallow-70B",
                            href="https://huggingface.co/pfnet/Llama3-Preferred-MedSwallow-70B",
                        ),
                        " and ",
                        A(
                            "Preferred-MedLLM-Qwen-72B",
                            href="https://huggingface.co/pfnet/Preferred-MedLLM-Qwen-72B",
                        ),
                        ", which are the first open LLMs to surpass GPT-4 in the Japanese Medical Licensing "
                        "Exam (JMLE). These models demonstrate the potential for LLMs to serve as valuable "
                        "tools in healthcare settings, providing accurate medical information and supporting "
                        "clinical decision-making.",
                    ),
                ],
                [
                    '<a href="https://huggingface.co/pfnet/Preferred-MedLLM-Qwen-72B">Preferred-MedLLM-Qwen-72B</a>',
                    '<a href="https://huggingface.co/pfnet/Llama3-Preferred-MedSwallow-70B">Llama3-Preferred-MedSwallow-70B</a>',
                ],
            ),
            research_project(
                "Deciphering evolutionary constraints of Escherichia coli",
                """The prediction and control of evolution is a crucial topic for both evolutionary biology and tackling antibiotic resistance.
Although the lack of sufficient data has long hindered the mechanism of evolution, laboratory evolution experiments equipped with high-throughput sequencing/phenotyping are now gradually changing this situation. The emerging data from recent laboratory evolution experiments revealed repeatable features in evolutionary processes, suggesting the existence of constraints which could lead to actual predictions of evolutionary outcomes. These results also paint an upbeat picture of evolution: biologically feasible states and evolutionary trajectories could be distributed on a low-dimensional manifold within the high-dimensional space spanned by biological features.

By combining machine learning techniques with experimental data from high-throughput laboratory evolution experiments, we aim to decipher the constraints which cause the low-dimensional evolutionary dynamics.""",
                [
                    'Junichiro Iwasawa, Tomoya Maeda, Atsushi Shibai, Hazuki Kotani, Masako Kawada, and Chikara Furusawa, <a href="https://doi.org/10.1371/journal.pbio.3001920">Analysis of the evolution of resistance to multiple antibiotics enables prediction of the <em>Escherichia coli</em> phenotype-based fitness landscape</a>, <em>PLOS Biology</em> 20(12): e3001920 (2022).',
                    'Tomoya Maeda*, Junichiro Iwasawa*, Hazuki Kotani, Natsue Sakata, Masako Kawada, Takaaki Horinouchi, Aki Sakai, Kumi Tanabe, and Chikara Furusawa (*co-first authors), <a href="https://doi.org/10.1038/s41467-020-19713-w">High-throughput laboratory evolution reveals evolutionary constraints in <em>Escherichia coli</em></a>, <em>Nature Communications</em> 11, 5970 (2020).',
                ],
            ),
            research_project(
                "Collective phenomena of active colloidal particles (Janus particles)",
                """Collective motion can be observed in a wide variety of systems, from flocks of birds to the collective migration of living cells. The ubiquitousness of this collective phenomena strongly hints the existence of universal properties which can be explained from basic features of the system, and thus has motivated physicists for the past few decades leading to a field which is now called Active Matter.

Janus particles, which are asymmetric colloidal particles with distinct hemispheres with different physical properties, can function as self-propelled particles by dissipating energy to the surrounding fluid under an AC electric field. Since they provide a perfect test bed for active matter research, Janus particles have increasingly gained attention in the field of active matter through the past decade. We have explored universal features of collective motion through the active dynamics of Janus particles.""",
                [
                    'Junichiro Iwasawa, Daiki Nishiguchi, and Masaki Sano, <a href="https://doi.org/10.1103/PhysRevResearch.3.043104">Algebraic correlations and anomalous fluctuations in ordered flocks of Janus particles fueled by an AC electric field</a>, <em>Physical Review Research</em> 3, 043104 (2021).',
                    'Daiki Nishiguchi, Junichiro Iwasawa, Hong-Ren Jiang, and Masaki Sano, <a href="https://doi.org/10.1088/1367-2630/aa9b48">Flagellar dynamics of chains of active Janus particles fueled by an AC electric field</a>, <em>New Journal of Physics</em> 20, 015002 (2018).',
                ],
            ),
            research_project(
                "Medical image analysis in the small data regime",
                """Although neural networks are emerging in a wide range of topics, the preparation of sufficient data still remains as a hurdle to overcome, especially for biological/medical data. Recently, self-supervised learning has been suggested as an effective pre-training method for various fields such as natural language processing and image classification. The idea of self-supervised learning is to utilize unlabeled data to improve task performance when only a few labeled data is available through the utilization of pre-text tasks. However, self-supervised learning requires heavy computing before the main task, which could be a burden in certain scenarios.

We have been working on methods where pre-text tasks could be utilized as auxiliary tasks for regularizing segmentation models in the small labeled data regime, making the learning process more data and cost-efficient.""",
                [
                    'Junichiro Iwasawa, Yuichiro Hirano, and Yohei Sugawara, <a href="https://arxiv.org/abs/2009.11160">Label-Efficient Multi-Task Segmentation using Contrastive Learning</a>, <em>Brainlesion: Glioma, Multiple Sclerosis, Stroke and Traumatic Brain Injuries</em>, LNCS 12658, 101 (2021). arXiv:2009.11160.',
                ],
            ),
        ),
        active="research",
    )
