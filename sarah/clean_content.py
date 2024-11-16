# clean_content.py
from bs4 import BeautifulSoup
import re

def clean_page_content(content):
    """Cleans the content of a web page by removing unnecessary spaces, script, and style code."""
    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    
    # Remove script and style elements
    for script_or_style in soup(['script', 'style']):
        script_or_style.decompose()  # Remove these elements from the soup
    
    # Extract the cleaned text
    text = soup.get_text()
    
    # Remove extra spaces, newlines, and tabs
    cleaned_text = re.sub(r'\s+', ' ', text)
    
    # Trim leading and trailing spaces
    cleaned_text = cleaned_text.strip()
    
    return cleaned_text

# Example usage
if __name__ == "__main__":
    # Sample HTML content for demonstration
    sample_content = """
    <html>
    <head>
        <title>Sample Page</title>
        <style>body { font-size: 12px; }</style>
    </head>
    <body>
        <h1>Welcome to the Sample Page</h1>
        <p>This is a sample paragraph.</p>
        <script>alert('This is a script');</script>
    </body>
    </html>
    """
    cleaned_content = clean_page_content(sample_content)
    print(cleaned_content)  # Output should be clean and free of script/style content