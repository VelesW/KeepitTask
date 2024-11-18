from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import URLError, HTTPError
from list_counter import ListCounter # Import the class
import sys
import ssl

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    
    # Validate URL
    try:
        result = urlparse(url)
        if not all([result.scheme, result.netloc]) or not result.scheme in ['http', 'https']:
            raise ValueError("Invalid URL: Must be http or https")
    except ValueError as e:
        print(f"Please provide a valid URL: {e}")
        sys.exit(1)

    try:
        # Create SSL context for secure connections
        ssl_context = ssl.create_default_context()

        # Fetch the webpage content
        with urlopen(url, timeout=10, context=ssl_context) as response:
            # Verify Content type
            content_type = response.getheader('Content-Type', '').lower()

            if 'text/html' not in content_type:
                raise ValueError(f"Content type is invalid: {content_type}")
            
            # Verify content length
            content_length = response.getheader('Content-Length', '')
            if content_length and int(content_length) > 10 * 1024 * 1024: # 10 MB
                raise ValueError("Content length is too large: Limit is 10 MB")

            html_content = response.read().decode('utf-8', errors='replace')

        # Parse the HTML and count list items
        parser = ListCounter()
        parser.feed(html_content)

        print(f"The largest unordered list contains {parser.max_list_count} items")

    except HTTPError as e:
        print(f"HTTP error occurred: {e.code} - {e.reason}")
        sys.exit(1)
    except URLError as e:
        print(f"URL error occurred: {e.reason}")
        sys.exit(1)
    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Value error: {e}")
        sys.exit(1)
    except TimeoutError:
        print(f"Connection timed out")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()