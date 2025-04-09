from fasthtml.common import *
from monsterui.all import *
import os, shutil
from pathlib import Path

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

# Set up theme and headers
theme_headers = Theme.blue.headers()

# Generate HTML for each page
pages = [
    ("index.html", "Home", home()),
    ("publications/index.html", "Publications", publications_page()),
    ("research/index.html", "Research", research_page()),
    ("talks/index.html", "Presentations", presentations_page()),
    ("blog/index.html", "Blog", blog_page())
]

for path, title, content in pages:
    file_path = output_dir / path
    file_path.parent.mkdir(exist_ok=True, parents=True)
    
    # Create a complete HTML document with proper structure
    full_page = "<!DOCTYPE html>\n" + str(
        Html(
            Head(
                Meta(charset="utf-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1"),
                Title(f"{title} - Junichiro Iwasawa"),
                *theme_headers
            ),
            Body(content)
        )
    )
    
    # Write to file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(full_page)

print(f"Static site generated in {output_dir}")
