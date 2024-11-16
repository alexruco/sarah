# get_content_from_page.py

import requests
from bs4 import BeautifulSoup

def get_content_from_page(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract and return the text content of the page
        page_content = soup.get_text()
        return page_content.strip()
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return None

# Example usage
if __name__ == "__main__":
    url = "https://mysitefaster.com"
    content = get_content_from_page(url)
    if content:
        print(content[:500])  # Print the first 500 characters of the content