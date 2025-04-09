from fasthtml.common import *
from monsterui.all import *
import os, shutil, requests
from pathlib import Path
import subprocess
import time
import signal
import sys

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
if Path("profile_img.jpg").exists():
    shutil.copy("profile_img.jpg", output_dir / "profile_img.jpg")

# Create a simple robots.txt
with open(output_dir / "robots.txt", "w") as f:
    f.write("User-agent: *\nAllow: /\n")

# Create a simple .nojekyll file to disable Jekyll processing
with open(output_dir / ".nojekyll", "w") as f:
    f.write("")

# Define routes to capture
routes = [
    ("/", "index.html"),
    ("/publications", "publications/index.html"),
    ("/research", "research/index.html"),
    ("/talks", "talks/index.html"),
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
            
            # Save the HTML content
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            
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
