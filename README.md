# GitHub URL Generator Scripts

This repository contains two scripts to generate GitHub raw URLs for images in your folders.

## Scripts

### 1. Python Script (`generate_github_urls.py`)

A comprehensive Python script that provides multiple output formats.

**Usage:**
```bash
python3 generate_github_urls.py <folder_name>
```

**Example:**
```bash
python3 generate_github_urls.py ally_high_latency_debug_req_1
```

**Features:**
- Supports multiple image formats: .png, .jpg, .jpeg, .gif, .bmp, .svg, .webp, .tiff, .ico
- Provides three output formats:
  - Simple URL list
  - JSON array
  - Quoted strings (with trailing commas)
- Saves output to a text file
- Sorts images alphabetically

### 2. Bash Script (`generate_urls.sh`)

A simple bash script for quick URL generation.

**Usage:**
```bash
./generate_urls.sh <folder_name>
```

**Example:**
```bash
./generate_urls.sh ally_high_latency_debug_req_1
```

**Features:**
- Fast execution
- Outputs quoted URLs with trailing commas (ready for array usage)
- Supports common image formats

## Configuration

Both scripts are configured for this repository:
- **GitHub Username:** shresthjain-bs
- **Repository:** public
- **Branch:** main

If you need to use these scripts for a different repository, update the configuration variables at the top of each script.

## Output Format

The URLs generated follow this pattern:
```
https://raw.githubusercontent.com/shresthjain-bs/public/main/folder_name/image_name.ext
```

Example output:
```
"https://raw.githubusercontent.com/shresthjain-bs/public/main/ally_high_latency_debug_req_1/4aeb9131-be55-4229-b127-b7d637c3b24a.png",
```

## Requirements

- **Python script:** Python 3.x
- **Bash script:** Standard Unix/Linux/macOS shell environment

Both scripts work from the repository root directory and expect folder names as relative paths.
