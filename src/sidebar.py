from fasthtml.common import *
from monsterui.all import *


def sidebar():
    return Div(
        Div(
            Img(
                src="static/profile_img.jpg",
                #cls="rounded-full w-full h-auto mb-4",
                cls="rounded-full w-full max-w-[150px] h-auto mb-4 mx-auto"
            ),
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
                    cls="flex items-center mb-2 text-primary hover:underline w-full"
                ),
                A(
                    DivLAligned(
                        UkIcon("linkedin", cls="mr-2"), 
                        Span("LinkedIn")
                    ), 
                    href="https://www.linkedin.com/in/junichiro-iwasawa-875b37130/", 
                    cls="flex items-center mb-2 text-primary hover:underline w-full"
                ),
                A(
                    DivLAligned(
                        UkIcon("graduation-cap", cls="mr-2"), 
                        Span("Google Scholar")
                    ), 
                    href="https://scholar.google.co.jp/citations?user=LampCPIAAAAJ&hl=en", 
                    cls="flex items-center mb-2 text-primary hover:underline w-full"
                ),
                A(
                    DivLAligned(
                        UkIcon("github", cls="mr-2"), 
                        Span("GitHub")
                    ), 
                    href="https://github.com/jiwasawa", 
                    cls="flex items-center mb-2 text-primary hover:underline w-full"
                ),
                A(
                    DivLAligned(
                        UkIcon("book-open", cls="mr-2"), 
                        Span("researchmap")
                    ), 
                    href="https://researchmap.jp/jiwasawa?lang=en", 
                    cls="flex items-center mb-2 text-primary hover:underline w-full"
                ),
                A(
                    DivLAligned(
                        UkIcon("notebook-pen", cls="mr-2"), 
                        Span("Blog")
                    ), 
                    href="https://jiwasawa.github.io/blog/", 
                    cls="flex items-center mb-2 text-primary hover:underline w-full"
                ),
                #cls="mt-4 text-left"  # Align links to the left for better readability
                #cls="mt-4 text-left flex flex-wrap justify-center sm:justify-start",
                cls="mt-4 text-left flex flex-col"
            ),
            cls="text-center p-4"
        ),
        #cls="sticky top-8 col-span-2"
        cls="col-span-12 md:col-span-3 lg:col-span-2 md:sticky md:top-8"
    )

def navbar():
    return NavBar(
        *map(lambda x: A(x[0], href=x[1], cls="mx-3"), 
             [("About", "/"), ("Publications", "/publications"), 
              ("Research", "/research"), ("Talks", "/talks"), 
              ("Blog", "/blog"), ("ブログ", "/blog_jp")]),
        brand=H3("Junichiro Iwasawa", cls="text-2xl font-semibold"),
        cls="px-4 py-2 container mb-4",  # Added margin-bottom for spacing
        #sticky=True,  # Make navbar sticky to prevent content overlap
    )
