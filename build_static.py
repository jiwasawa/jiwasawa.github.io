from fasthtml.common import *
from monsterui.all import *
import os, shutil
from pathlib import Path

# Import your app and route handler from main.py
from main import app, rt

# Import your page components
from src.home import home
from src.publications import publications_page
from src.research import research_page
from src.talks import presentations_page
from src.blog import blog_page

# Create output directory
output_dir = Path("_site")
if output_dir.exists():
    shutil.rmtree(output_dir)
output_dir.mkdir()

# Create static directory if needed
static_dir = output_dir / "static"
static_dir.mkdir(exist_ok=True)

# Copy static assets if you have any
if Path("static").exists():
    shutil.copytree("static", static_dir, dirs_exist_ok=True)

# Helper function to render HTML properly
def render_page(title, content):
    from fasthtml.common import render_to_string
    page = Title(title), content
    return "<!DOCTYPE html>\n" + render_to_string(page)

# Generate HTML for each page
pages = [
    ("index.html", "About - Junichiro Iwasawa", home()),
    ("publications/index.html", "Publications - Junichiro Iwasawa", publications_page()),
    ("research/index.html", "Research - Junichiro Iwasawa", research_page()),
    ("talks/index.html", "Talks - Junichiro Iwasawa", presentations_page()),
    ("blog/index.html", "Blog - Junichiro Iwasawa", blog_page())
]

for path, title, content in pages:
    file_path = output_dir / path
    file_path.parent.mkdir(exist_ok=True, parents=True)
    
    # Render HTML properly
    html = render_page(title, content)
    
    # Write to file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

print(f"Static site generated in {output_dir}")
