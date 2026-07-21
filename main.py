from fasthtml.common import *
from monsterui.all import *

from src.talks import presentations_page
from src.home import home
from src.publications import publications_page
from src.research import research_page


# Cross-page polish shared by every route: keyboard focus rings and smooth
# color transitions on interactive elements.
custom_styles = Style("""
    :focus-visible { outline: 2px solid #3b82f6; outline-offset: 2px; border-radius: 6px; }
    a, button { transition: color .2s ease, background-color .2s ease, border-color .2s ease; }
""")

# Persist the light/dark choice the way FrankenUI's own init script reads it,
# so the selection survives reloads and navigation.
theme_script = Script("""
function __toggleMode(){
  const html = document.documentElement;
  const isDark = html.classList.toggle('dark');
  let s = {};
  try { s = JSON.parse(localStorage.getItem('__FRANKEN__')) || {}; } catch (e) {}
  s.mode = isDark ? 'dark' : 'light';
  localStorage.setItem('__FRANKEN__', JSON.stringify(s));
}
""")

# mode="auto": honor a saved preference, otherwise follow the OS setting.
app, rt = fast_app(hdrs=(*Theme.blue.headers(mode="auto"), custom_styles, theme_script))

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


serve()
