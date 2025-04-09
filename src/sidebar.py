from fasthtml.common import *
from monsterui.all import *


def sidebar():
    return Div(
        Div(
            Img(src="static/profile_img.jpg", cls="rounded-full w-full h-auto mb-4"),
            H4("Junichiro Iwasawa", cls="text-1xl font-semibold"),
            #H5("岩澤 諄一郎", cls="text-1xl font-semibold"),
            P("Researcher at Preferred Networks Inc.", cls=TextPresets.muted_sm),
            P("iwasawa [at] preferred.jp", cls=TextPresets.muted_sm),
            Div(cls="mt-6"),
            # Social media links with icons
            Div(
                A(
                    DivLAligned(
                        UkIcon("twitter", cls="mr-2"), 
                        Span("Twitter")
                    ), 
                    href="https://twitter.com/jiwasawa", 
                    cls="flex items-center mb-2 text-primary hover:underline"
                ),
                A(
                    DivLAligned(
                        UkIcon("linkedin", cls="mr-2"), 
                        Span("LinkedIn")
                    ), 
                    href="https://www.linkedin.com/in/junichiro-iwasawa-875b37130/", 
                    cls="flex items-center mb-2 text-primary hover:underline"
                ),
                A(
                    DivLAligned(
                        UkIcon("graduation-cap", cls="mr-2"), 
                        Span("Google Scholar")
                    ), 
                    href="https://scholar.google.co.jp/citations?user=LampCPIAAAAJ&hl=en", 
                    cls="flex items-center mb-2 text-primary hover:underline"
                ),
                A(
                    DivLAligned(
                        UkIcon("github", cls="mr-2"), 
                        Span("GitHub")
                    ), 
                    href="https://github.com/jiwasawa", 
                    cls="flex items-center mb-2 text-primary hover:underline"
                ),
                A(
                    DivLAligned(
                        UkIcon("book-open", cls="mr-2"), 
                        Span("researchmap")
                    ), 
                    href="https://researchmap.jp/jiwasawa?lang=en", 
                    cls="flex items-center mb-2 text-primary hover:underline"
                ),
                cls="mt-4 text-left"  # Align links to the left for better readability
            ),
            cls="text-center p-4"
        ),
        cls="sticky top-8 col-span-2"
    )

def navbar():
    return NavBar(
        *map(lambda x: A(x[0], href=x[1], cls="mx-3"), 
             [("About", "/"), ("Publications", "/publications"), 
              ("Research", "/research"), ("Talks", "/talks"), ("Blog", "/blog")]),
        brand=H3("Junichiro Iwasawa", cls="text-2xl font-semibold"),
        cls="px-4 py-2 container",  # Add a background color and shadow
        #cls="justify-between container mx-1 px-4 py-2 bg-white rounded-lg"  # Add a background color and shadow
        #cls="flex items-center w-full container mx-2 px-4 py-2 mr-12"
    )
