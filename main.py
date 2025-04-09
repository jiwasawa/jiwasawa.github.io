from fasthtml.common import *
from monsterui.all import *

from src.talks import presentations_page
from src.home import home
from src.publications import publications_page
from src.research import research_page
from src.blog import blog_page


app, rt = fast_app(hdrs=(Theme.blue.headers(mode="light")))

@rt("/")
def get():
    return Title("About - Junichiro Iwasawa"), home()


@rt("/talks")
def get():
    return Title("Talks - Junichiro Iwasawa"), presentations_page()


@rt("/publications")
def get():
    return Title("Publications - Junichiro Iwasawa"), publications_page()


@rt("/research")
def get():
    return Title("Research - Junichiro Iwasawa"), research_page()


@rt("/blog")
def get():
    return Title("Blog - Junichiro Iwasawa"), blog_page()


serve()
