#!/bin/bash

# Script to generate GitHub raw URLs for images in a specified folder
# Usage: ./generate_urls.sh <folder_name>

# GitHub repository configuration
GITHUB_USERNAME="shresthjain-bs"
REPO_NAME="public"
BRANCH="main"
BASE_URL="https://raw.githubusercontent.com/${GITHUB_USERNAME}/${REPO_NAME}/${BRANCH}"

# Check if folder name is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <folder_name>"
    echo "Example: $0 ally_high_latency_debug_req_1"
    exit 1
fi

FOLDER_NAME="$1"

# Check if folder exists
if [ ! -d "$FOLDER_NAME" ]; then
    echo "Error: Folder '$FOLDER_NAME' does not exist."
    exit 1
fi

echo "Generating URLs for images in folder: $FOLDER_NAME"
echo "================================================"

# Find all image files and generate URLs
find "$FOLDER_NAME" -maxdepth 1 -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.gif" -o -iname "*.bmp" -o -iname "*.svg" -o -iname "*.webp" -o -iname "*.tiff" -o -iname "*.ico" \) | sort | while read -r file; do
    filename=$(basename "$file")
    url="${BASE_URL}/${FOLDER_NAME}/${filename}"
    echo "\"$url\","
done

echo
echo "URLs generated successfully!"
