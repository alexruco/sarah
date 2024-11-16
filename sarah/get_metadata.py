# page_metadata.py
import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    """Fetches the title of a web page."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        return title.strip()
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return None

def get_page_description(url):
    """Fetches the meta description of a web page."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        soup = BeautifulSoup(response.content, 'html.parser')
        description_tag = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', attrs={'property': 'og:description'})
        description = description_tag['content'] if description_tag and 'content' in description_tag.attrs else "No description found"
        return description.strip()
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return None

# Example usage
if __name__ == "__main__":
    url = "https://mysitefaster.com"
    title = get_page_title(url)
    description = get_page_description(url)
    
    print(f"Title: {title}")
    print(f"Description: {description}")