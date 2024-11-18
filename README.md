# HTML List Counter

A Python tool that analyzes HTML content and finds the largest unordered list (`<ul>`) on a webpage. This tool can process both local HTML files and web URLs.

## Features

- Counts items in unordered lists (`<ul>`)
- Handles nested lists correctly (only counts top-level items)
- Includes comprehensive error handling for URL requests
- Built-in security features (SSL verification, content-type checking, size limits)

## Requirements

- Python Installed

## Installation

Clone this repository: 

```bash
git clone https://github.com/VelesW/KeepitTask.git
cd KeepitTask
```


## Usage

### Command Line Interface

Run the script with a URL as an argument:

```bash
python script.py <URL>
```

Example:
```bash
python script.py https://example.com
```



## Project Structure

- `script.py` - Main script for URL processing and HTML fetching
- `list_counter.py` - HTML parser implementation for counting list items
- `test_list_counter.py` - Unit tests for the list counter functionality
- `test.html` - Sample HTML file for testing purposes

## How It Works

1. The script validates the provided URL
2. Fetches the HTML content with proper error handling
3. Parses the HTML using a custom HTMLParser implementation
4. Tracks and counts list items while handling nested structures
5. Returns the count of items in the largest unordered list

## Testing

Run the unit tests using:

```bash
    python -m unittest test_list_counter.py
```

## The test suite includes cases for:
- Empty HTML content
- Single lists
- Nested lists
- Multiple lists
- Parser reset functionality

## Error Handling

The script handles various error cases:
- Invalid URLs
- HTTP errors
- SSL/TLS errors
- Network timeouts
- Invalid content types
- Oversized content (>10MB)
