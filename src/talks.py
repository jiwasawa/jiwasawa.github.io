from fasthtml.common import *
from monsterui.all import *

from src.sidebar import sidebar, navbar

def presentations_content():
    return Div(
        Section(
            H2("Talks and presentations", cls="text-3xl font-semibold mb-4"),
            #P("Selected academic presentations and talks.", cls="mb-6 text-lg"),
            Div(
                Ul(
                    Li(A("Invited Talks", href="#invited-talks", cls=AT.primary)),
                    Li(A("International Conferences (Oral)", href="#international-talks", cls=AT.primary)),
                    Li(A("International Conferences (Posters)", href="#international-posters", cls=AT.primary)),
                    Li(A("Japanese Conferences", href="#japanese-conferences", cls=AT.primary)),
                    Li(A("Outreach", href="#outreach", cls=AT.primary)),
                    cls="list-disc pl-5 space-y-1"
                ),
                cls="mb-8 p-4 rounded-md text-base"
            ),
            cls="mb-8"
        ),
        
        Section(
            H3("Invited Talks", cls="text-2xl font-semibold mb-4", id="invited-talks"),
            Div(*[
                presentation_item(
                    "Finetuning Foundation Models for the Development and Application of Healthcare-Specific Models",
                    "基盤モデルの finetuning による医療特化モデルの構築と応用",
                    "Science Tokyo設立記念 社会的課題解決型データサイエンス・AI研究推進体シンポジウム ～AI とデータサイエンスが拓く新時代の医療～",
                    "March 24, 2025",
                    "Tokyo, Japan",
                    "https://www.isct.ac.jp/ja/news/g0s5tlw8z8vg"
                    
                ),
                presentation_item(
                    "Finetuning or RAG? Towards Building a Medical Domain-Specialized LLM",
                    "Finetuning or RAG? 医療ドメイン特化 LLM 構築に向けて",
                    "55th meeting of IBISML",
                    "December 20, 2024",
                    "Hokkaido, Japan",
                    "https://ibisml.org/ibisml055"
                    
                ),
                presentation_item(
                    "Latest Developments in Finetuning LLMs for Healthcare",
                    "医療向けLLM-finetuningの最前線",
                    "Clinical AI Symposium",
                    "November 24, 2024",
                    "Online",
                    "https://www.tohoku.ac.jp/japanese/2024/10/event20241009-01-hosp.html"
                ),
                presentation_item(
                    "High-throughput laboratory evolution with machine learning reveals constraints for drug resistance evolution",
                    None,
                    "RIKEN iTHEMS biology seminar",
                    "February 18, 2021",
                    "Online",
                    "https://ithems.riken.jp/en/news/biology-seminar-mr-junichiro-iwasawa-february-18-2021"
                ),
                presentation_item(
                    "High-throughput laboratory evolution with machine learning reveals constraints for drug resistance evolution",
                    None,
                    "RIKEN iTHEMS biology seminar",
                    "February 18, 2021",
                    "Online",
                    "https://ithems.riken.jp/en/news/biology-seminar-mr-junichiro-iwasawa-february-18-2021"
                ), 
                presentation_item(
                    "Analyses of evolutionary constraints using microbial laboratory evolution and machine learning",
                    "大腸菌進化実験と機械学習を用いた進化的拘束の解析",
                    "統計物理と統計科学のセミナー",
                    "February 16, 2021",
                    "Online",
                    "https://sites.google.com/view/ismstatphys/"
                ), 
                presentation_item(
                    "Investigation of evolutionary constraints through large scale laboratory evolution and data analysis",
                    None,
                    "Kaneko lab. seminar",
                    "July 14, 2020",
                    "Online",
                    "http://chaos.c.u-tokyo.ac.jp/index.html",
                ),]),
            cls="mb-12"
        ),
        
        Section(
            H3("International Conferences (Oral)", cls="text-2xl font-semibold mb-4", id="international-talks"),
            Div(*[presentation_item(
                "Label-Efficient Multi-Task Segmentation using Contrastive Learning",
                None,
                "MICCAI BrainLes 2020 workshop",
                "October 4, 2020",
                "Online",
                "http://www.brainlesion-workshop.org/",
            ), presentation_item(
                "Combining interpretable machine learning with high dimensional multi-omics data from laboratory evolution",
                None,
                "The 20th International Conference on Systems Biology",
                "November 1-5, 2019",
                "Okinawa, Japan",
                "https://www2.aeplan.co.jp/icsb2019/index.html"
            )]),
            cls="mb-12"
        ),
        
        Section(
            H3("International Conferences (Posters)", cls="text-2xl font-semibold mb-4", id="international-posters"),
            Div(*[presentation_item(
                "Deciphering evolutionary constraints through high-dimensional data of E. coli laboratory evolution",
                None,
                "Phylogeny and inference: from models to data and back",
                "February 1 - 6, 2021",
                "Online",
                "https://indico.math.cnrs.fr/category/389/"
            ), presentation_item(
                "Interplay of polarity and motion in swarming Janus particles",
                None,
                "International Conference on Advances in Physics of Emergent orders in Fluctuations 2018",
                "November 12 - 15, 2018",
                "Tokyo, Japan",
                "https://apef2018.org/program"
            ), presentation_item(
                "Collective properties of artificial self-propelling particles fueled by an AC electric field",
                None,
                "Physical Approaches to Understanding Microbial Life",
                "August 28 - September 6, 2018",
                "Gif-sur-Yvette, France",
                "https://microbes.sciencesconf.org/",
            ), presentation_item(
                "Collective Motion of Asymmetric Self-Propelling Particles under an AC Electric Field (Poster Award)",
                None,
                "International Symposium on Fluctuation and Structure out of Equibrium 2017",
                "November 20-23, 2017",
                "Miyagi, Japan",
                "http://sfs-dynamics.jp/sfs2017/"
            ), presentation_item(
                "Properties of Directed Collective Motion of Asymmetric Self-Propelling Particles",
                None,
                "Synergy of Fluctuation and Structure Symposium, Current and Future Perspectives in Active Matter",
                "October 28-29, 2016",
                "The University of Tokyo, Tokyo, Japan",
                "http://sfs-dynamics.jp/eng/kenkyukai/20161028/index.html"
            )]),
            cls="mb-12"
        ),
        
        Section(
            H3("Japanese Conferences (Oral)", cls="text-2xl font-semibold mb-4", id="japanese-conferences"),
            Div(*[presentation_item(
                "Inferring E. coli fitness landscapes through drug resistance time series",
                "大腸菌進化実験の薬剤耐性時系列を用いた適応度地形の推定",
                "The Physical Society of Japan 2021 Annual Meeting",
                "March 14, 2021",
                "Online",
                "https://jps2021s.gakkai-web.net/data/html/program11.html"
            ), presentation_item(
                "Long-range order in Janus particles fueled by an AC electric field: Algebraic correlations and anomalous fluctuations",
                None,
                "Active Matter Workshop 2021",
                "January 23, 2021",
                "Online",
                "https://sites.google.com/view/activematter2021"
            ), presentation_item(
                "交流電場下での非対称自己駆動粒子集団の統計的性質",
                None,
                "The Physical Society of Japan 2018 Annual Meeting",
                "March 22-25 2018",
                "Tokyo University of Science, Chiba, Japan",
                "http://www.rs.tus.ac.jp/jps2018tus/index.html"
            ), presentation_item(
                "Directed Collective Motion of Asymmetric Colloidal Particles under an AC electric field",
                None,
                "Active Matter Workshop 2018",
                "January 19 20, 2018",
                "Kyoto University, Kyoto, Japan",
                "http://www.fukui.kyoto-u.ac.jp/users/tarama/workshop/activematter2018.html"
            ), presentation_item(
                "Statistical Properties of Collective Motion of Asymmetric Self-Propelling Particles",
                None,
                "Active Matter Workshop 2017",
                "January 20,21, 2017",
                "Kyushu University, Fukuoka, Japan",
                "http://www.fukui.kyoto-u.ac.jp/users/tarama/workshop/activematter2017.html"
            )]),
            cls="mb-12"
        ),
        
        # Outreach
        Section(
            H3("Outreach", cls="text-2xl font-semibold mb-4", id="outreach"),
            H4("Public Talks in Japanese", cls="text-xl font-semibold mb-4"),
            Div(*[presentation_item(
                "「進化」は予測可能？",
                None,
                "『10分で伝えます！東大研究最前線』第70回東京大学駒場祭",
                "November 22-24, 2019",
                "",
                "https://ut-10min.github.io/kf70/talks.html"
            ), presentation_item(
                "迷子の最適戦略",
                None,
                "『10分で伝えます！東大研究最前線』第92回東京大学五月祭",
                "May 18, 19, 2019",
                "",
                "https://ut-10min.github.io/mf92/"
            ), presentation_item(
                "指紋とトポロジー",
                None,
                "『10分で伝えます！東大研究最前線』第69回東京大学駒場祭",
                "November 23-25, 2018",
                "",
                "https://ut-10min.github.io/kf69/talks.html",
            ), presentation_item(
                "大腸菌はサイコロを振るか 〜ギャンブル理論を通して見る生物学〜",
                None,
                "CLASP",
                "August 25, 2018",
                "",
                "https://www.facebook.com/events/tokyo-womens-plaza-forum/%E7%AC%AC4%E5%9B%9E-%E5%A4%A7%E8%85%B8%E8%8F%8C%E3%81%AF%E3%82%B5%E3%82%A4%E3%82%B3%E3%83%AD%E3%82%92%E6%8C%AF%E3%82%8B%E3%81%8B-%E3%82%AE%E3%83%A3%E3%83%B3%E3%83%96%E3%83%AB%E7%90%86%E8%AB%96%E3%82%92%E9%80%9A%E3%81%97%E3%81%A6%E8%A6%8B%E3%82%8B%E7%94%9F%E7%89%A9%E5%AD%A6/244813266120454/"
            ), presentation_item(
                "大腸菌はサイコロを振るか？",
                None,
                "『10分で伝えます！東大研究最前線』第91回東京大学五月祭",
                "May 19, 20, 2018",
                "",
                "https://ut-10min.github.io/mf91/talks.html"
            ), presentation_item(
                "15歳からの相対性理論 ～光速の世界を体験しよう～",
                None,
                "千代田区立麹町中学校",
                "September 12, 2015",
                "",
                "http://www.kojimachijh-dosokai.jp/dosokai_koushi4.html",
            ), presentation_item(
                "理科とは何か～アインシュタインから最先端の物理学まで～",
                None,
                "千代田区立麹町中学校",
                "November 2, 2013",
                "",
                "http://www.kojimachijh-dosokai.jp/dosokai_koushi3.html"
            )]),
            cls="mb-12"
        ),
        cls="col-span-7"
    )

def presentation_item(title, title_jp, venue, date, location="", venue_link=""):
    location_text = f", {location}" if location else ""
    return Card(
        Div(
            H4(title, cls=TextT.bold),
            H5(title_jp, cls=TextT.bold) if title_jp else None,
            DivLAligned(
                UkIcon("calendar", cls="mr-2"),
                P(f"{date}{location_text}", cls=TextPresets.muted_sm)
            ),
            P(A(venue, href=venue_link, cls=AT.primary) if venue_link else venue, cls=TextT.italic),
            cls="space-y-2"
        ),
        cls="mb-4 p-4 hover:bg-secondary"
    )


def presentations_page():
    content = Container(
        Grid(
            sidebar(),
            presentations_content(),
            cols=12,
            cls="gap-8 mt-8"
        ),
        cls=ContainerT.xl
    )
    
    return Div(navbar(), content)
