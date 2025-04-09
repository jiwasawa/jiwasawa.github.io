from fasthtml.common import *
from monsterui.all import *

from src.sidebar import sidebar, navbar


def publication_item(authors, title, journal, link="", labels=None):
    labels = labels or []
    return Card(
        Div(
            P(authors, cls=TextPresets.muted_sm),
            H4(title, cls=TextT.bold),
            P(journal, cls=TextT.italic),
            Div(*[Label(l, cls="mr-2 mb-2") for l in labels], cls="mt-2 flex flex-wrap"),
            A("View Publication", href=link, cls=AT.primary) if link else None,
            cls="space-y-2"
        ),
        cls="mb-6 p-4 hover:bg-secondary"
    )


def publications_content():
    return Div(
        # Introduction
        Section(
            H2("Publications", cls="text-3xl font-semibold mb-4"),
            DivLAligned(
                UkIcon("graduation-cap", cls="mr-2"),
                A("Google Scholar Profile", 
                  href="https://scholar.google.co.jp/citations?user=LampCPIAAAAJ&hl=en", 
                  cls=AT.primary + " text-base")
            ),
            cls="mb-8"
        ),
        
        # Publications and Preprints
        Section(
            H3("Publications and Preprints", cls="text-2xl font-semibold mb-4"),
            Div(
                publication_item(
                    "Junichiro Iwasawa, Tomoya Maeda, Atsushi Shibai, Hazuki Kotani, Masako Kawada, and Chikara Furusawa",
                    "Analysis of the evolution of resistance to multiple antibiotics enables prediction of the Escherichia coli phenotype-based fitness landscape",
                    "PLOS Biology 20(12): e3001920 (2022)",
                    "https://doi.org/10.1371/journal.pbio.3001920",
                    ["Biophysics", "Machine Learning", "Antibiotic Resistance"]
                ),
                publication_item(
                    "Junichiro Iwasawa, Daiki Nishiguchi, and Masaki Sano",
                    "Algebraic correlations and anomalous fluctuations in ordered flocks of Janus particles fueled by an AC electric field",
                    "Physical Review Research 3, 043104 (2021)",
                    "https://doi.org/10.1103/PhysRevResearch.3.043104",
                    ["Statistical Physics", "Active Matter"]
                ),
                publication_item(
                    "Junichiro Iwasawa, Yuichiro Hirano, and Yohei Sugawara",
                    "Label-Efficient Multi-Task Segmentation using Contrastive Learning",
                    "Brainlesion: Glioma, Multiple Sclerosis, Stroke and Traumatic Brain Injuries, LNCS 12658, 101 (2021)",
                    "https://arxiv.org/abs/2009.11160",
                    ["Deep Learning", "Medical Imaging"]
                ),
                publication_item(
                    "Tomoya Maeda*, Junichiro Iwasawa*, Hazuki Kotani, Natsue Sakata, Masako Kawada, Takaaki Horinouchi, Aki Sakai, Kumi Tanabe, and Chikara Furusawa (*co-first authors)",
                    "High-throughput laboratory evolution reveals evolutionary constraints in Escherichia coli",
                    "Nature Communications 11, 5970 (2020)",
                    "https://doi.org/10.1038/s41467-020-19713-w",
                    ["Biophysics", "Machine Learning", "Antibiotic Resistance"]
                ),
                publication_item(
                    "Daiki Nishiguchi, Junichiro Iwasawa, Hong-Ren Jiang, and Masaki Sano",
                    "Flagellar dynamics of chains of active Janus particles fueled by an AC electric field",
                    "New Journal of Physics 20, 015002 (2018)",
                    "https://doi.org/10.1088/1367-2630/aa9b5b",
                    ["Statistical Physics", "Active Matter"]
                ),
                publication_item(
                    "Tomoyuki Mano, Jean-Baptiste Delfau, Junichiro Iwasawa and Masaki Sano",
                    "Optimal run-and-tumble-based transportation of a Janus particle with active steering",
                    "Proceedings of the National Academy of Sciences 114 (13), E2580-E2589 (2017)",
                    "https://doi.org/10.1073/pnas.1616013114",
                    ["Statistical Physics", "Active Matter"]
                ),
                cls="space-y-4"
            ),
            cls="mb-12"
        ),
        cls="col-span-7"
    )


def publications_page():
    
    content = Container(
        Grid(
            sidebar(),
            publications_content(),
            cols=12,
            cls="gap-8 mt-8"
        ),
        cls=ContainerT.xl
    )
    
    return Div(navbar(), content)
