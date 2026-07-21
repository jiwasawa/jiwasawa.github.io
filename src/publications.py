import re

from fasthtml.common import *
from monsterui.all import *

from src.sidebar import sidebar, navbar


def _authors_with_self_underlined(authors):
    parts = re.split(r"(Junichiro Iwasawa\*?)", authors)
    return [U(p) if p.startswith("Junichiro Iwasawa") else p for p in parts]


def publication_item(authors, title, journal, link=""):
    return Li(
        *_authors_with_self_underlined(authors),
        ". ",
        Strong(f"{title}."),
        " ",
        Em(f"{journal}."),
        " ",
        A("[link]", href=link, cls=AT.primary) if link else None,
    )


def publications_content():
    return Div(
        # Introduction
        Section(
            H2("Publications", cls="text-3xl font-bold tracking-tight mb-4"),
            DivLAligned(
                UkIcon("graduation-cap", cls="mr-2"),
                A("Google Scholar Profile",
                  href="https://scholar.google.co.jp/citations?user=LampCPIAAAAJ&hl=en",
                  cls=AT.primary + " text-base")
            ),
            cls="mb-12"
        ),

        # Publications and Preprints
        Section(
            H3("Publications and Preprints", cls="text-2xl font-semibold mb-4"),
            Ul(
                publication_item(
                    "Rie Shiokawa, Junichiro Iwasawa, Yumiko Oishi Tanaka, Yuta Tokuoka, Yohei Sugawara, Yuichiro Hirano, Ryo Takaji, Yayoi Hayakawa, Keita Oda, Yasunori Kudo, Miho Li, Kazue Mizuno, Kazuhisa Ozeki, Ayako Nishimoto-Kakiuchi, and Kimio Terao",
                    "Development of an AI-based magnetic resonance imaging reading support program (AMP) for deep endometriosis diagnosis",
                    "Scientific Reports 16, 790 (2025)",
                    "https://doi.org/10.1038/s41598-025-30277-x",
                ),
                publication_item(
                    "Wataru Kawakami, Keita Suzuki, and Junichiro Iwasawa",
                    "Stabilizing Reasoning in Medical LLMs with Continued Pretraining and Reasoning Preference Optimization",
                    "NeurIPS 2025 Workshop GenAI4Health",
                    "https://openreview.net/forum?id=bGkyFZVyRL",
                ),
                publication_item(
                    "Naoto Iwase, Hiroki Okuyama, and Junichiro Iwasawa",
                    "MedRECT: A Medical Reasoning Benchmark for Error Correction in Clinical Texts",
                    "arXiv preprint arXiv:2511.00421 (2025)",
                    "https://arxiv.org/abs/2511.00421",
                ),
                publication_item(
                    "Xinkai Zhao, Yuta Tokuoka, Junichiro Iwasawa, and Keita Oda",
                    "Frequency-calibrated membership inference attacks on medical image diffusion models",
                    "MICCAI 2025 Workshop on Deep Generative Models",
                    "https://link.springer.com/chapter/10.1007/978-3-032-05472-2_29",
                ),
                publication_item(
                    "Enzhi Zhang, Junichiro Iwasawa, Keita Oda, and Yuta Tokuoka",
                    "SAM2v-BTR: Accelerating SAM 2 Training for 3D Medical Image Segmentation Through Bootstrap and Memory Annealing",
                    "2025 IEEE International Conference on Systems, Man, and Cybernetics (SMC), 4456-4461 (2025)",
                    "https://doi.org/10.1109/SMC58881.2025.11343367",
                ),
                publication_item(
                    "Junichiro Iwasawa and Kenta Oono",
                    "Advancements and Challenges in Japanese Medical Large Language Models",
                    "Journal of the Japanese Society for Artificial Intelligence 40(5), 726-734 (2025)",
                    "https://doi.org/10.11517/jjsai.40.5_726",
                ),
                publication_item(
                    "Junichiro Iwasawa, Tomoya Maeda, Atsushi Shibai, Hazuki Kotani, Masako Kawada, and Chikara Furusawa",
                    "Analysis of the evolution of resistance to multiple antibiotics enables prediction of the Escherichia coli phenotype-based fitness landscape",
                    "PLOS Biology 20(12): e3001920 (2022)",
                    "https://doi.org/10.1371/journal.pbio.3001920",
                ),
                publication_item(
                    "Junichiro Iwasawa, Daiki Nishiguchi, and Masaki Sano",
                    "Algebraic correlations and anomalous fluctuations in ordered flocks of Janus particles fueled by an AC electric field",
                    "Physical Review Research 3, 043104 (2021)",
                    "https://doi.org/10.1103/PhysRevResearch.3.043104",
                ),
                publication_item(
                    "Junichiro Iwasawa, Yuichiro Hirano, and Yohei Sugawara",
                    "Label-Efficient Multi-Task Segmentation using Contrastive Learning",
                    "Brainlesion: Glioma, Multiple Sclerosis, Stroke and Traumatic Brain Injuries, LNCS 12658, 101 (2021)",
                    "https://arxiv.org/abs/2009.11160",
                ),
                publication_item(
                    "Tomoya Maeda*, Junichiro Iwasawa*, Hazuki Kotani, Natsue Sakata, Masako Kawada, Takaaki Horinouchi, Aki Sakai, Kumi Tanabe, and Chikara Furusawa (*co-first authors)",
                    "High-throughput laboratory evolution reveals evolutionary constraints in Escherichia coli",
                    "Nature Communications 11, 5970 (2020)",
                    "https://doi.org/10.1038/s41467-020-19713-w",
                ),
                publication_item(
                    "Daiki Nishiguchi, Junichiro Iwasawa, Hong-Ren Jiang, and Masaki Sano",
                    "Flagellar dynamics of chains of active Janus particles fueled by an AC electric field",
                    "New Journal of Physics 20, 015002 (2018)",
                    "http://doi.org/10.1088/1367-2630/aa9b48",
                ),
                publication_item(
                    "Tomoyuki Mano, Jean-Baptiste Delfau, Junichiro Iwasawa and Masaki Sano",
                    "Optimal run-and-tumble-based transportation of a Janus particle with active steering",
                    "Proceedings of the National Academy of Sciences 114 (13), E2580-E2589 (2017)",
                    "https://doi.org/10.1073/pnas.1616013114",
                ),
                cls="list-disc pl-5 space-y-3"
            ),
            cls="mb-12"
        ),
        cls="col-span-12 md:col-span-8 lg:col-span-9"
    )


def publications_page():

    content = Container(
        Grid(
            sidebar(),
            publications_content(),
            cols=12,
            cls="gap-10 mt-12"
        ),
        cls=ContainerT.xl
    )

    return Div(navbar(), content)
