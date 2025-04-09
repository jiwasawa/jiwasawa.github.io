from fasthtml.common import *
from monsterui.all import *

from src.sidebar import sidebar, navbar


def blog_content():
    return Container(
        # Header
        Div(
            H1("Junichiro Iwasawa's Blog", cls="text-4xl font-bold mb-8 mt-8"),
            cls="text-center"
        ),
        
        # Main content with right sidebar layout
        Grid(
            # Main content column (2/3 width)
            Div(
                # Coming Soon Message
                Card(
                    Div(
                        DivCentered(
                            UkIcon("file-edit", height=64, width=64, cls="text-primary mb-4"),
                            H3("Blog Posts Coming Soon!", cls="text-2xl font-semibold mb-2"),
                            P("I'm working on some interesting articles to share. Check back soon for updates on my research, projects, and thoughts on AI, machine learning, and biophysics.", 
                              cls="text-center max-w-2xl mb-4"),
                            Div(
                                P("Topics I plan to write about:", cls="font-semibold mb-2"),
                                Ul(
                                    Li("Advances in Large Language Models for healthcare"),
                                    Li("Evolutionary constraints and antibiotic resistance"),
                                    Li("Self-supervised learning in medical imaging"),
                                    Li("Statistical physics approaches to biological systems"),
                                    cls="list-disc pl-5 space-y-1"
                                ),
                                cls="text-left"
                            ),
                            cls="py-8 px-4"
                        ),
                        cls="p-4"
                    ),
                    cls="mb-12"
                ),
                
                # Sample entries (commented out until you have actual entries)
                Div(
                    blog_entry(
                        "The Medical AI Revolution: Specialized LLMs in Healthcare",
                        "October 15, 2024",
                        "Junichiro Iwasawa",
                        "An exploration of how specialized medical language models are transforming healthcare diagnostics and decision-making, with insights from our recent projects at Preferred Networks.",
                        ["Medical AI", "LLMs", "Healthcare"],
                        "/blog/medical-llms",
                        "/static/blog/medical_llm.jpg"
                    ),
                    blog_entry(
                        "Evolutionary Dynamics and Antibiotic Resistance",
                        "September 28, 2024",
                        "Junichiro Iwasawa",
                        "Discussing recent breakthroughs in understanding evolutionary constraints in bacteria and how this knowledge can help combat antibiotic resistance.",
                        ["Evolution", "Biophysics", "Antibiotic Resistance"],
                        "/blog/evolutionary-dynamics",
                        "/static/blog/evolution.jpg"
                    ),
                    cls="hidden" # Hide these sample entries until you're ready to show them
                ),
                cls="col-span-8"
            ),
            
            # Categories sidebar on the right (1/3 width)
            Div(
                Card(
                    Div(
                        H3("Categories", cls="text-xl font-semibold mb-4"),
                        Ul(
                            Li(A("All", href="/blog", cls=AT.primary), " (0)"),
                            Li(A("Medical AI", href="/blog/category/medical-ai", cls=AT.primary), " (0)"),
                            Li(A("LLMs", href="/blog/category/llms", cls=AT.primary), " (0)"),
                            Li(A("Biophysics", href="/blog/category/biophysics", cls=AT.primary), " (0)"),
                            Li(A("Machine Learning", href="/blog/category/machine-learning", cls=AT.primary), " (0)"),
                            Li(A("Research", href="/blog/category/research", cls=AT.primary), " (0)"),
                            cls="list-none space-y-2"
                        ),
                        cls="p-4"
                    )
                ),
                cls="col-span-4 hidden"
            ),
            
            cols=12,
            cls="gap-8"
        ),
        
        cls=ContainerT.lg
    )


def blog_entry(title, date, author, summary, tags=None, link="#", image_url=None):
    tags = tags or []
    
    return Div(
        Div(
            Div(
                P(date, cls=TextT.muted + " mb-1"),
                P(author, cls=TextT.muted + " mb-3"),
                cls="mb-2"
            ),
            Grid(
                Div(
                    H3(title, cls="text-xl font-semibold mb-3"),
                    P(summary, cls="mb-3"),
                    Div(*[A(tag, href=f"/blog/tag/{tag.lower()}", cls="mr-2 text-sm bg-gray-100 px-2 py-1 rounded") 
                          for tag in tags], cls="flex flex-wrap mb-3"),
                    A("Read more →", href=link, cls=AT.primary),
                    cls="space-y-1"
                ),
                Div(
                    Img(src=image_url, cls="rounded-md object-cover w-full h-40"),
                ) if image_url else None,
                cols=image_url and 2 or 1,
                cls="gap-6"
            ),
            cls="mb-8 pb-8 border-b border-gray-200"
        ),
        cls="mb-4"
    )


def blog_entry_old(title, date, summary, link="#", image_url=None):
    return Card(
        Div(
            Div(
                P(date, cls=TextPresets.muted_sm),
                H3(title, cls="text-xl font-semibold mb-2"),
                P(summary, cls="mb-2"),
                A("Read more →", href=link, cls=AT.primary),
                cls="space-y-1"
            ) if not image_url else Grid(
                Div(
                    P(date, cls=TextPresets.muted_sm),
                    H3(title, cls="text-xl font-semibold mb-2"),
                    P(summary, cls="mb-2"),
                    A("Read more →", href=link, cls=AT.primary),
                    cls="space-y-1"
                ),
                Div(
                    Img(src=image_url, cls="rounded-md object-cover w-full h-full"),
                    cls="h-40"
                ),
                cols=2,
                cls="gap-4"
            ),
            cls="p-4"
        ),
        cls="mb-6 hover:shadow-md transition-shadow"
    )


def blog_page_old():
    content = Container(
        Grid(
            sidebar(),
            blog_content(),
            cols=12,
            cls="gap-8 mt-8"
        ),
        cls=ContainerT.xl
    )
    
    return Div(navbar(), content)


def blog_page():
    #navbar = create_navbar()
    
    return Div(
        navbar(), 
        blog_content(),
        cls="bg-gray-50 min-h-screen"
    )
