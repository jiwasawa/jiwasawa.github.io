import re

from fasthtml.common import *

from src.layout import page_shell


PUBLICATIONS = [
    {
        "key": "shiokawa2025amp",
        "year": "2025",
        "highlight": True,
        "authors": (
            "Rie Shiokawa, Junichiro Iwasawa, Yumiko Oishi Tanaka, Yuta Tokuoka, "
            "Yohei Sugawara, Yuichiro Hirano, Ryo Takaji, Yayoi Hayakawa, Keita Oda, "
            "Yasunori Kudo, Miho Li, Kazue Mizuno, Kazuhisa Ozeki, "
            "Ayako Nishimoto-Kakiuchi, and Kimio Terao"
        ),
        "title": "Development of an AI-based magnetic resonance imaging reading support program (AMP) for deep endometriosis diagnosis",
        "venue": "Scientific Reports",
        "venue_extra": "16, 790 (2025)",
        "link_label": "paper",
        "url": "https://doi.org/10.1038/s41598-025-30277-x",
        "bibtex": """@article{shiokawa2025amp,
  author  = {Shiokawa, Rie and Iwasawa, Junichiro and Tanaka, Yumiko Oishi and Tokuoka, Yuta and Sugawara, Yohei and Hirano, Yuichiro and Takaji, Ryo and Hayakawa, Yayoi and Oda, Keita and Kudo, Yasunori and Li, Miho and Mizuno, Kazue and Ozeki, Kazuhisa and Nishimoto-Kakiuchi, Ayako and Terao, Kimio},
  title   = {Development of an AI-based magnetic resonance imaging reading support program (AMP) for deep endometriosis diagnosis},
  journal = {Scientific Reports},
  volume  = {16},
  pages   = {790},
  year    = {2025},
  doi     = {10.1038/s41598-025-30277-x}
}""",
    },
    {
        "key": "kawakami2025stabilizing",
        "year": "2025",
        "highlight": False,
        "authors": "Wataru Kawakami, Keita Suzuki, and Junichiro Iwasawa",
        "title": "Stabilizing Reasoning in Medical LLMs with Continued Pretraining and Reasoning Preference Optimization",
        "venue": "NeurIPS 2025 Workshop GenAI4Health",
        "venue_extra": "",
        "link_label": "OpenReview",
        "url": "https://openreview.net/forum?id=bGkyFZVyRL",
        "bibtex": """@inproceedings{kawakami2025stabilizing,
  author    = {Kawakami, Wataru and Suzuki, Keita and Iwasawa, Junichiro},
  title     = {Stabilizing Reasoning in Medical LLMs with Continued Pretraining and Reasoning Preference Optimization},
  booktitle = {NeurIPS 2025 Workshop GenAI4Health},
  year      = {2025},
  url       = {https://openreview.net/forum?id=bGkyFZVyRL}
}""",
    },
    {
        "key": "iwase2025medrect",
        "year": "2025",
        "highlight": False,
        "authors": "Naoto Iwase, Hiroki Okuyama, and Junichiro Iwasawa",
        "title": "MedRECT: A Medical Reasoning Benchmark for Error Correction in Clinical Texts",
        "venue": "arXiv preprint arXiv:2511.00421",
        "venue_extra": "(2025)",
        "link_label": "arXiv",
        "url": "https://arxiv.org/abs/2511.00421",
        "bibtex": """@misc{iwase2025medrect,
  author        = {Iwase, Naoto and Okuyama, Hiroki and Iwasawa, Junichiro},
  title         = {MedRECT: A Medical Reasoning Benchmark for Error Correction in Clinical Texts},
  year          = {2025},
  eprint        = {2511.00421},
  archivePrefix = {arXiv},
  url           = {https://arxiv.org/abs/2511.00421}
}""",
    },
    {
        "key": "zhao2025frequency",
        "year": "2025",
        "highlight": False,
        "authors": "Xinkai Zhao, Yuta Tokuoka, Junichiro Iwasawa, and Keita Oda",
        "title": "Frequency-calibrated membership inference attacks on medical image diffusion models",
        "venue": "MICCAI 2025 Workshop on Deep Generative Models",
        "venue_extra": "",
        "link_label": "paper",
        "url": "https://link.springer.com/chapter/10.1007/978-3-032-05472-2_29",
        "bibtex": """@inproceedings{zhao2025frequency,
  author    = {Zhao, Xinkai and Tokuoka, Yuta and Iwasawa, Junichiro and Oda, Keita},
  title     = {Frequency-calibrated membership inference attacks on medical image diffusion models},
  booktitle = {MICCAI 2025 Workshop on Deep Generative Models},
  year      = {2025},
  doi       = {10.1007/978-3-032-05472-2_29}
}""",
    },
    {
        "key": "zhang2025sam2vbtr",
        "year": "2025",
        "highlight": False,
        "authors": "Enzhi Zhang, Junichiro Iwasawa, Keita Oda, and Yuta Tokuoka",
        "title": "SAM2v-BTR: Accelerating SAM 2 Training for 3D Medical Image Segmentation Through Bootstrap and Memory Annealing",
        "venue": "2025 IEEE International Conference on Systems, Man, and Cybernetics (SMC)",
        "venue_extra": "4456–4461 (2025)",
        "link_label": "DOI",
        "url": "https://doi.org/10.1109/SMC58881.2025.11343367",
        "bibtex": """@inproceedings{zhang2025sam2vbtr,
  author    = {Zhang, Enzhi and Iwasawa, Junichiro and Oda, Keita and Tokuoka, Yuta},
  title     = {SAM2v-BTR: Accelerating SAM 2 Training for 3D Medical Image Segmentation Through Bootstrap and Memory Annealing},
  booktitle = {2025 IEEE International Conference on Systems, Man, and Cybernetics (SMC)},
  pages     = {4456--4461},
  year      = {2025},
  doi       = {10.1109/SMC58881.2025.11343367}
}""",
    },
    {
        "key": "iwasawa2025jsai",
        "year": "2025",
        "highlight": False,
        "authors": "Junichiro Iwasawa and Kenta Oono",
        "title": "Advancements and Challenges in Japanese Medical Large Language Models",
        "venue": "Journal of the Japanese Society for Artificial Intelligence",
        "venue_extra": "40(5), 726–734 (2025)",
        "link_label": "paper",
        "url": "https://doi.org/10.11517/jjsai.40.5_726",
        "bibtex": """@article{iwasawa2025jsai,
  author  = {Iwasawa, Junichiro and Oono, Kenta},
  title   = {Advancements and Challenges in Japanese Medical Large Language Models},
  journal = {Journal of the Japanese Society for Artificial Intelligence},
  volume  = {40},
  number  = {5},
  pages   = {726--734},
  year    = {2025},
  doi     = {10.11517/jjsai.40.5_726}
}""",
    },
    {
        "key": "iwasawa2022plos",
        "year": "2022",
        "highlight": True,
        "authors": "Junichiro Iwasawa, Tomoya Maeda, Atsushi Shibai, Hazuki Kotani, Masako Kawada, and Chikara Furusawa",
        "title": "Analysis of the evolution of resistance to multiple antibiotics enables prediction of the Escherichia coli phenotype-based fitness landscape",
        "venue": "PLOS Biology",
        "venue_extra": "20(12): e3001920 (2022)",
        "link_label": "paper",
        "url": "https://doi.org/10.1371/journal.pbio.3001920",
        "bibtex": """@article{iwasawa2022plos,
  author  = {Iwasawa, Junichiro and Maeda, Tomoya and Shibai, Atsushi and Kotani, Hazuki and Kawada, Masako and Furusawa, Chikara},
  title   = {Analysis of the evolution of resistance to multiple antibiotics enables prediction of the {Escherichia coli} phenotype-based fitness landscape},
  journal = {PLOS Biology},
  volume  = {20},
  number  = {12},
  pages   = {e3001920},
  year    = {2022},
  doi     = {10.1371/journal.pbio.3001920}
}""",
    },
    {
        "key": "iwasawa2021prr",
        "year": "2021",
        "highlight": True,
        "authors": "Junichiro Iwasawa, Daiki Nishiguchi, and Masaki Sano",
        "title": "Algebraic correlations and anomalous fluctuations in ordered flocks of Janus particles fueled by an AC electric field",
        "venue": "Physical Review Research",
        "venue_extra": "3, 043104 (2021)",
        "link_label": "paper",
        "url": "https://doi.org/10.1103/PhysRevResearch.3.043104",
        "bibtex": """@article{iwasawa2021prr,
  author  = {Iwasawa, Junichiro and Nishiguchi, Daiki and Sano, Masaki},
  title   = {Algebraic correlations and anomalous fluctuations in ordered flocks of Janus particles fueled by an AC electric field},
  journal = {Physical Review Research},
  volume  = {3},
  pages   = {043104},
  year    = {2021},
  doi     = {10.1103/PhysRevResearch.3.043104}
}""",
    },
    {
        "key": "iwasawa2021brainles",
        "year": "2021",
        "highlight": False,
        "authors": "Junichiro Iwasawa, Yuichiro Hirano, and Yohei Sugawara",
        "title": "Label-Efficient Multi-Task Segmentation using Contrastive Learning",
        "venue": "Brainlesion: Glioma, Multiple Sclerosis, Stroke and Traumatic Brain Injuries",
        "venue_extra": "LNCS 12658, 101 (2021)",
        "link_label": "arXiv",
        "url": "https://arxiv.org/abs/2009.11160",
        "bibtex": """@inproceedings{iwasawa2021brainles,
  author    = {Iwasawa, Junichiro and Hirano, Yuichiro and Sugawara, Yohei},
  title     = {Label-Efficient Multi-Task Segmentation using Contrastive Learning},
  booktitle = {Brainlesion: Glioma, Multiple Sclerosis, Stroke and Traumatic Brain Injuries},
  series    = {LNCS},
  volume    = {12658},
  pages     = {101--112},
  year      = {2021},
  eprint    = {2009.11160},
  archivePrefix = {arXiv}
}""",
    },
    {
        "key": "maeda2020natcomm",
        "year": "2020",
        "highlight": True,
        "authors": (
            "Tomoya Maeda*, Junichiro Iwasawa*, Hazuki Kotani, Natsue Sakata, "
            "Masako Kawada, Takaaki Horinouchi, Aki Sakai, Kumi Tanabe, "
            "and Chikara Furusawa (*co-first authors)"
        ),
        "title": "High-throughput laboratory evolution reveals evolutionary constraints in Escherichia coli",
        "venue": "Nature Communications",
        "venue_extra": "11, 5970 (2020)",
        "link_label": "paper",
        "url": "https://doi.org/10.1038/s41467-020-19713-w",
        "bibtex": """@article{maeda2020natcomm,
  author  = {Maeda, Tomoya and Iwasawa, Junichiro and Kotani, Hazuki and Sakata, Natsue and Kawada, Masako and Horinouchi, Takaaki and Sakai, Aki and Tanabe, Kumi and Furusawa, Chikara},
  title   = {High-throughput laboratory evolution reveals evolutionary constraints in {Escherichia coli}},
  journal = {Nature Communications},
  volume  = {11},
  pages   = {5970},
  year    = {2020},
  doi     = {10.1038/s41467-020-19713-w}
}""",
    },
    {
        "key": "nishiguchi2018njp",
        "year": "2018",
        "highlight": False,
        "authors": "Daiki Nishiguchi, Junichiro Iwasawa, Hong-Ren Jiang, and Masaki Sano",
        "title": "Flagellar dynamics of chains of active Janus particles fueled by an AC electric field",
        "venue": "New Journal of Physics",
        "venue_extra": "20, 015002 (2018)",
        "link_label": "paper",
        "url": "https://doi.org/10.1088/1367-2630/aa9b48",
        "bibtex": """@article{nishiguchi2018njp,
  author  = {Nishiguchi, Daiki and Iwasawa, Junichiro and Jiang, Hong-Ren and Sano, Masaki},
  title   = {Flagellar dynamics of chains of active Janus particles fueled by an AC electric field},
  journal = {New Journal of Physics},
  volume  = {20},
  pages   = {015002},
  year    = {2018},
  doi     = {10.1088/1367-2630/aa9b48}
}""",
    },
    {
        "key": "mano2017pnas",
        "year": "2017",
        "highlight": False,
        "authors": "Tomoyuki Mano, Jean-Baptiste Delfau, Junichiro Iwasawa, and Masaki Sano",
        "title": "Optimal run-and-tumble-based transportation of a Janus particle with active steering",
        "venue": "Proceedings of the National Academy of Sciences",
        "venue_extra": "114(13), E2580–E2589 (2017)",
        "link_label": "paper",
        "url": "https://doi.org/10.1073/pnas.1616013114",
        "bibtex": """@article{mano2017pnas,
  author  = {Mano, Tomoyuki and Delfau, Jean-Baptiste and Iwasawa, Junichiro and Sano, Masaki},
  title   = {Optimal run-and-tumble-based transportation of a Janus particle with active steering},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {114},
  number  = {13},
  pages   = {E2580--E2589},
  year    = {2017},
  doi     = {10.1073/pnas.1616013114}
}""",
    },
]


def _authors_with_self_underlined(authors):
    parts = re.split(r"(Junichiro Iwasawa\*?)", authors)
    return [U(p) if p.startswith("Junichiro Iwasawa") else p for p in parts]


def _title_with_species_italic(title):
    parts = re.split(r"(Escherichia coli)", title)
    return [Em(p) if p == "Escherichia coli" else p for p in parts]


def publication_item(pub):
    bib_id = f"bib-{pub['key']}"
    venue_parts = [Em(pub["venue"])]
    if pub["venue_extra"]:
        sep = ", " if pub["venue_extra"][0].isdigit() and "SMC" in pub["venue"] else " "
        if "Brainlesion" in pub["venue"]:
            sep = ", "
        venue_parts.append(f"{sep}{pub['venue_extra']}")

    return Li(
        Div(pub["year"], cls="pub-year"),
        Div(
            Div(*_title_with_species_italic(pub["title"]), cls="pub-title"),
            Div(*_authors_with_self_underlined(pub["authors"]), cls="pub-authors"),
            Div(
                *venue_parts,
                Span(
                    A(f"[{pub['link_label']}]", href=pub["url"]),
                    Button(
                        "[BibTeX]",
                        type="button",
                        cls="bib-btn",
                        aria_expanded="false",
                        aria_controls=bib_id,
                    ),
                    cls="pub-actions",
                ),
                cls="pub-venue",
            ),
            Pre(
                Button("copy", type="button", cls="copy-btn", aria_label="Copy BibTeX"),
                Code(pub["bibtex"]),
                id=bib_id,
                cls="bib-box",
            ),
        ),
        cls="pub-item highlight" if pub["highlight"] else "pub-item",
    )


def publications_section(standalone=False):
    total = len(PUBLICATIONS)
    selected = sum(1 for p in PUBLICATIONS if p["highlight"])
    heading = H1("Publications", cls="page-title", style="margin:0") if standalone else H2("Publications")

    return Section(
        Div(
            heading,
            Div(
                "Show: ",
                Button(
                    f"all ({total})",
                    type="button",
                    cls="active",
                    data_pub_filter="all",
                    aria_pressed="true",
                ),
                " / ",
                Button(
                    f"selected ({selected})",
                    type="button",
                    data_pub_filter="highlight",
                    aria_pressed="false",
                ),
                cls="filter-links",
            ),
            cls="sec-head",
        ),
        P(
            Span(cls="swatch"),
            "Highlighted papers represent major themes across medical AI, evolutionary biology, and active matter. Full record on ",
            A(
                "Google Scholar",
                href="https://scholar.google.co.jp/citations?user=LampCPIAAAAJ&hl=en",
            ),
            ".",
            cls="legend",
        ),
        Ol(*[publication_item(pub) for pub in PUBLICATIONS], cls="pub-list"),
        id="publications",
    )


def publications_page():
    return page_shell(publications_section(standalone=True), active="publications")
