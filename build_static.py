from fasthtml.common import *
from monsterui.all import *
import os, shutil, requests
from pathlib import Path
import subprocess
import time
import signal
import sys


def fix_github_pages_links(html_content, repo_name, current_path):
    """
    Rewrite all internal links to include the repository name for GitHub Pages.
    Also fixes relative paths for assets like images and PDFs.
    
    Args:
        html_content: The HTML content to fix
        repo_name: The GitHub repository name
        current_path: The current path being processed (e.g., "/", "/publications")
    """
    # Fix href and src attributes that start with "/" (absolute paths)
    html_content = html_content.replace('href="/', f'href="/{repo_name}/')
    html_content = html_content.replace('src="/', f'src="/{repo_name}/')
    html_content = html_content.replace('data-src="/', f'data-src="/{repo_name}/')
    
    # Fix relative paths for assets based on current path depth
    if current_path != "/":
        # Count the directory depth
        depth = current_path.count("/") - 1  # -1 because the leading "/" counts as one
        path_prefix = "../" * depth
        
        # Replace relative asset references with path-adjusted ones
        # Be careful to only replace attributes that don't already have a protocol or leading /
        html_content = html_content.replace('src="profile_img.jpg"', f'src="{path_prefix}profile_img.jpg"')
        html_content = html_content.replace('href="junichiro_iwasawa_cv.pdf"', f'href="{path_prefix}junichiro_iwasawa_cv.pdf"')
        
        # Add more replacements for other assets as needed
    
    return html_content


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

# Copy profile image if it exists
if Path("static/profile_img.jpg").exists():
    shutil.copy("data/profile_img.jpg", output_dir / "static" / "profile_img.jpg")
if Path("static/junichiro_iwasawa_cv.pdf").exists():
    shutil.copy("data/junichiro_iwasawa_cv.pdf", output_dir / "static" / "junichiro_iwasawa_cv.pdf")

# Create a simple robots.txt
with open(output_dir / "robots.txt", "w") as f:
    f.write("User-agent: *\nAllow: /\n")

# Create a simple .nojekyll file to disable Jekyll processing
with open(output_dir / ".nojekyll", "w") as f:
    f.write("")

# Define routes to capture
routes = [
    ("/", "index.html"),
    ("/publications", "publications.html"),
    ("/research", "research.html"),
    ("/talks", "talks.html"),
    ("/blog", "blog/index.html")
]

# Start the FastHTML server in a subprocess
server_process = subprocess.Popen(
    ["python", "main.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Wait for the server to start
print("Starting server...")
time.sleep(5)  # Give the server time to start

try:
    # Fetch each page and save it
    for route, output_path in routes:
        print(f"Fetching {route}...")
        
        # Make a request to the local server
        response = requests.get(f"http://localhost:5001{route}")
        
        if response.status_code == 200:
            # Create directory if needed
            file_path = output_dir / output_path
            file_path.parent.mkdir(exist_ok=True, parents=True)

            fixed_html = fix_github_pages_links(response.text, "personal-webpage", route)
            
            # Save the HTML content
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(fixed_html)
            
            print(f"Saved {output_path}")
        else:
            print(f"Error fetching {route}: {response.status_code}")
    
    print("Static site generation complete!")

finally:
    # Always terminate the server process
    print("Shutting down server...")
    server_process.terminate()
    server_process.wait(timeout=5)

print(f"Static site generated in {output_dir}")
