from fasthtml.common import *
from monsterui.all import *
import markdown
from bs4 import BeautifulSoup

from src.sidebar import sidebar, navbar


def markdown_to_fasthtml(md_content):
    "Convert markdown content to FastHTML components"
    # Convert markdown to HTML
    html_content = markdown.markdown(
        md_content, 
        extensions=[
            'markdown.extensions.fenced_code',
            'markdown.extensions.codehilite',
            'markdown.extensions.tables',
            'markdown.extensions.toc',
            'markdown.extensions.nl2br'
        ]
    )
    
    # Use NotStr to render the HTML directly
    return NotStr(html_content)


def blog_post_from_markdown(md_file, title, date, author="Junichiro Iwasawa", tags=None):
    "Create a blog post from a markdown file"
    tags = tags or []
    
    # Read the markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert to FastHTML
    content = markdown_to_fasthtml(md_content)
    
    # Return the blog post layout with the converted content
    return Container(
        # Header
        Div(
            H1(title, cls="text-4xl font-bold mb-8 mt-8"),
            P(author, cls=TextT.muted + " mb-1"),
            P(date, cls=TextT.muted + " mb-6"),
            Div(*[Label(tag, cls="mr-2 mb-2") for tag in tags], cls="mb-8 flex flex-wrap"),
            cls="text-center"
        ),
        
        # Main content with right sidebar layout
        Grid(
            # Main content column (2/3 width)
            Div(content, cls="col-span-8 blog-content text-base"),
            
            # Sidebar on the right (1/3 width)
            Div(
                Div(
                    H3("目次", cls="text-xl font-semibold mb-4"),
                    # Table of contents will be generated from the markdown
                    Div(id="toc", cls="toc"),
                    cls="p-4 bg-gray-50 rounded-lg mb-6"
                ),
                Card(
                    Div(
                        H3("カテゴリ", cls="text-xl font-semibold mb-4"),
                        Ul(
                            Li(A("すべて", href="/blog", cls=AT.primary)),
                            *[Li(A(tag, href=f"/blog/category/{tag.lower()}", cls=AT.primary)) for tag in tags],
                            cls="list-none space-y-2"
                        ),
                        cls="p-4"
                    )
                ),
                cls="col-span-4"
            ),
            
            cols=12,
            cls="gap-8"
        ),
        
        cls=ContainerT.lg
    )


def blog_listing():
    def blog_post_entry(title, date, summary, link, image_url=None, tags=None):
        tags = tags or []
        
        return Div(
            Div(
                P(date, cls=TextT.muted + " mb-1"),
                #P("Junichiro Iwasawa", cls=TextT.muted + " mb-3"),
                cls="mb-2"
            ),
            Grid(
                Div(
                    H3(A(title, href=link), cls="text-xl font-semibold mb-3"),
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
        )
    
    return Div(
        navbar(),
        Container(
            # Header
            Div(
                H1("Blog", cls="text-4xl font-bold mb-8 mt-8"),
                cls="text-left"
            ),
            
            Grid(
                Div(
                    blog_post_entry(
                        "コードで理解するTransformer：AttentionとGPTモデル入門",
                        "Apr 10, 2025",
                        "ChatGPTやGPT-4などの大規模言語モデルを支える中核技術であるTransformerのAttentionメカニズムについて解説します。",
                        "/blog/transformer-attention",
                        None,
                        ["Machine Learning", "Transformer", "Python"]
                    ),
                    cls="col-span-8"
                ),
                
                Div(
                    Card(
                        Div(
                            H3("カテゴリ", cls="text-xl font-semibold mb-4"),
                            Ul(
                                Li(A("すべて", href="/blog", cls=AT.primary), " (1)"),
                                Li(A("Machine Learning", href="/blog/category/machine-learning", cls=AT.primary), " (1)"),
                                Li(A("Transformer", href="/blog/category/transformer", cls=AT.primary), " (1)"),
                                Li(A("Python", href="/blog/category/python", cls=AT.primary), " (1)"),
                                cls="list-none space-y-2"
                            ),
                            cls="p-4"
                        )
                    ),
                    cls="col-span-4"
                ),
                cols=12,
                cls="gap-8"
            ),
            cls=ContainerT.lg
        ),
    )

