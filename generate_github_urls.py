#!/usr/bin/env python3
"""
Script to generate GitHub raw URLs for images in a specified folder.
Usage: python generate_github_urls.py <folder_name>
"""

import os
import sys
import json
from pathlib import Path

# GitHub repository configuration
GITHUB_USERNAME = "shresthjain-bs"
REPO_NAME = "public"
BRANCH = "main"
BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH}"

# Supported image extensions
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.webp', '.tiff', '.ico'}

def get_image_files(folder_path):
    """Get all image files from the specified folder."""
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return []
    
    image_files = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            if ext.lower() in IMAGE_EXTENSIONS:
                image_files.append(file)
    
    return sorted(image_files)

def generate_github_urls(folder_name, image_files):
    """Generate GitHub raw URLs for the image files."""
    urls = []
    for image_file in image_files:
        url = f"{BASE_URL}/{folder_name}/{image_file}"
        urls.append(url)
    
    return urls

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_github_urls.py <folder_name>")
        print("Example: python generate_github_urls.py ally_high_latency_debug_req_1")
        sys.exit(1)
    
    folder_name = sys.argv[1]
    
    # Get the current working directory (should be the repo root)
    current_dir = os.getcwd()
    folder_path = os.path.join(current_dir, folder_name)
    
    print(f"Scanning folder: {folder_name}")
    print(f"Full path: {folder_path}")
    print("-" * 50)
    
    # Get all image files
    image_files = get_image_files(folder_path)
    
    if not image_files:
        print(f"No image files found in '{folder_name}'")
        return
    
    # Generate URLs
    urls = generate_github_urls(folder_name, image_files)
    
    print(f"Found {len(image_files)} image(s):")
    print()
    
    # Output URLs in different formats
    
    # 1. Simple list
    print("=== URL List ===")
    for url in urls:
        print(url)
    
    print()
    
    # 2. JSON array format
    print("=== JSON Array ===")
    print(json.dumps(urls, indent=2))
    
    print()
    
    # 3. Quoted strings (as requested)
    print("=== Quoted Strings ===")
    for url in urls:
        print(f'"{url}",')
    
    # Save to file
    output_file = f"{folder_name}_urls.txt"
    with open(output_file, 'w') as f:
        f.write("URL List:\n")
        f.write("-" * 20 + "\n")
        for url in urls:
            f.write(url + "\n")
        
        f.write("\nJSON Array:\n")
        f.write("-" * 20 + "\n")
        f.write(json.dumps(urls, indent=2))
        
        f.write("\n\nQuoted Strings:\n")
        f.write("-" * 20 + "\n")
        for url in urls:
            f.write(f'"{url}",\n')
    
    print(f"\nURLs saved to: {output_file}")

if __name__ == "__main__":
    main()
