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

# Generate HTML for each page
pages = [
    ("index.html", home()),
    ("publications/index.html", publications_page()),
    ("research/index.html", research_page()),
    ("talks/index.html", presentations_page()),
    ("blog/index.html", blog_page())
]

for path, content in pages:
    file_path = output_dir / path
    file_path.parent.mkdir(exist_ok=True, parents=True)
    
    # Convert FT objects to HTML string with proper doctype
    html_content = Div(
        Title(f"{path.split('/')[0].title() if path != 'index.html' else 'About'} - Junichiro Iwasawa"),
        content
    )
    html = "<!DOCTYPE html>\n" + str(html_content)
    
    # Write to file
    with open(file_path, "w") as f:
        f.write(html)

print(f"Static site generated in {output_dir}")
