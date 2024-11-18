from urllib.request import urlopen
from urllib.parse import urlparse
from list_counter import ListCounter # Import the class
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    
    # Validate URL
    try:
        result = urlparse(url)
        if not all([result.scheme, result.netloc]):
            raise ValueError("Invalid URL")
    except ValueError:
        print("Please provide a valid URL")
        sys.exit(1)

    try:
        # Fetch the webpage content
        with urlopen(url) as response:
            html_content = response.read().decode('utf-8')

        # Parse the HTML and count list items
        parser = ListCounter()
        parser.feed(html_content)

        print(f"The largest unordered list contains {parser.max_list_count} items")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()