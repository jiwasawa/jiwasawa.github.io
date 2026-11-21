from fasthtml.common import *

from src.home import home
from src.layout import SITE_HEADERS
from src.publications import publications_page
from src.research import research_page
from src.talks import presentations_page


app, rt = fast_app(
    default_hdrs=False,
    pico=False,
    surreal=False,
    htmx=False,
    htmlkw={"lang": "en"},
    hdrs=SITE_HEADERS,
)


@rt("/")
def get():
    return Title("Junichiro Iwasawa"), home()


@rt("/talks")
def get():
    return Title("Talks - Junichiro Iwasawa"), presentations_page()


@rt("/publications")
def get():
    return Title("Publications - Junichiro Iwasawa"), publications_page()


@rt("/research")
def get():
    return Title("Research - Junichiro Iwasawa"), research_page()


serve()
