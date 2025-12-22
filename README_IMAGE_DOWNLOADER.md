# Image Downloader for Alt-Text Data

This script downloads images from the URLs specified in `alt-text-data.csv`.

## Usage

```bash
python3 download_images.py
```

## What it does

1. Reads `alt-text-data.csv` which contains:
   - `base_url`: URL for the base image
   - `context_url`: URL for the context image
   - `image_id`: Unique identifier for the image pair

2. Downloads images from both URLs for each row

3. Saves images in the `alt-text-data/` directory with filenames:
   - `{image_id}_base.{extension}` - for base images
   - `{image_id}_context.{extension}` - for context images

4. File extensions are automatically detected from:
   - URL path (if present)
   - Content-Type header from the server
   - Defaults to `.jpg` if unable to determine

## Features

- **Error handling**: Gracefully handles network errors, missing URLs, and HTTP errors
- **Progress reporting**: Shows progress for each image download
- **Summary statistics**: Reports total downloads, successes, and failures
- **Automatic directory creation**: Creates the output directory if it doesn't exist

## Requirements

- Python 3.x (uses standard library only, no external dependencies)
- Internet access to reach the image URLs

## Output

Downloaded images are stored in: `alt-text-data/`

This directory is excluded from git via `.gitignore`.

## Notes

The script processes all 2057+ entries in the CSV file. Depending on network conditions, this may take some time to complete.
