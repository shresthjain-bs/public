#!/usr/bin/env python3
"""
Script to download images from URLs specified in alt-text-data.csv.
Downloads both base_url and context_url images and saves them with appropriate naming.
"""

import os
import sys
import csv
import urllib.request
import urllib.error
from pathlib import Path
from urllib.parse import urlparse

# Configuration
CSV_FILE = "alt-text-data.csv"
OUTPUT_DIR = "alt-text-data"

def get_file_extension(url, content_type=None):
    """
    Determine file extension from URL or content-type header.
    """
    # Try to get extension from URL first
    parsed_url = urlparse(url)
    path = parsed_url.path
    if '.' in path:
        ext = os.path.splitext(path)[1]
        if ext:
            return ext
    
    # Try to determine from content-type
    if content_type:
        content_type = content_type.lower()
        mime_to_ext = {
            'image/jpeg': '.jpg',
            'image/jpg': '.jpg',
            'image/png': '.png',
            'image/gif': '.gif',
            'image/webp': '.webp',
            'image/svg+xml': '.svg',
            'image/bmp': '.bmp',
            'image/tiff': '.tiff',
            'image/x-icon': '.ico',
        }
        for mime, extension in mime_to_ext.items():
            if mime in content_type:
                return extension
    
    # Default to .jpg if unable to determine
    return '.jpg'

def download_image(url, output_path):
    """
    Download an image from URL and save to output_path.
    Returns True if successful, False otherwise.
    """
    try:
        # Create a request with a user agent to avoid potential blocks
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        
        with urllib.request.urlopen(req, timeout=30) as response:
            # Get content type to determine extension if needed
            content_type = response.headers.get('Content-Type', '')
            
            # Read the image data
            image_data = response.read()
            
            # If output_path doesn't have extension, add one
            if not os.path.splitext(output_path)[1]:
                ext = get_file_extension(url, content_type)
                output_path = output_path + ext
            
            # Write the image to file
            with open(output_path, 'wb') as f:
                f.write(image_data)
            
            return True, output_path
    
    except urllib.error.HTTPError as e:
        print(f"  HTTP Error {e.code}: {url}")
        return False, None
    except urllib.error.URLError as e:
        print(f"  URL Error: {e.reason} - {url}")
        return False, None
    except Exception as e:
        print(f"  Error downloading {url}: {str(e)}")
        return False, None

def main():
    # Check if CSV file exists
    if not os.path.exists(CSV_FILE):
        print(f"Error: CSV file '{CSV_FILE}' not found.")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")
    print("-" * 60)
    
    # Read CSV and download images
    total_rows = 0
    successful_base = 0
    successful_context = 0
    failed_downloads = 0
    
    with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row_num, row in enumerate(reader, start=1):
            total_rows += 1
            base_url = row.get('base_url', '').strip()
            context_url = row.get('context_url', '').strip()
            image_id = row.get('image_id', '').strip()
            
            if not image_id:
                print(f"Row {row_num}: Missing image_id, skipping...")
                continue
            
            print(f"[{row_num}/{total_rows}] Processing: {image_id}")
            
            # Download base image
            if base_url:
                base_output = os.path.join(OUTPUT_DIR, f"{image_id}_base")
                success, final_path = download_image(base_url, base_output)
                if success:
                    successful_base += 1
                    print(f"  ✓ Base image saved: {os.path.basename(final_path)}")
                else:
                    failed_downloads += 1
            else:
                print(f"  ⚠ No base_url provided")
            
            # Download context image
            if context_url:
                context_output = os.path.join(OUTPUT_DIR, f"{image_id}_context")
                success, final_path = download_image(context_url, context_output)
                if success:
                    successful_context += 1
                    print(f"  ✓ Context image saved: {os.path.basename(final_path)}")
                else:
                    failed_downloads += 1
            else:
                print(f"  ⚠ No context_url provided")
            
            print()  # Empty line for readability
    
    # Print summary
    print("-" * 60)
    print("Download Summary:")
    print(f"  Total rows processed: {total_rows}")
    print(f"  Base images downloaded: {successful_base}")
    print(f"  Context images downloaded: {successful_context}")
    print(f"  Total successful: {successful_base + successful_context}")
    print(f"  Failed downloads: {failed_downloads}")
    print(f"\nImages saved to: {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
