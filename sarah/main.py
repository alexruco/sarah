import time
from env_loader import load_env  # Import the env_loader module first
from get_content import get_content_from_page
from clean_content import clean_page_content 
from get_metadata import get_page_title, get_page_description

load_env()
from kate import get_response  # Import AI response function

def describe_page(url, prompt="What company owns this website and what do they do?", length=500):
    start_time = time.time()  # Track the start time

    # Step 1: Retrieve page content
    raw_page_content = get_content_from_page(url)
    print(f"Time taken for getting page content: {time.time() - start_time:.2f} seconds")

    # Step 2: Clean page content
    page_content = clean_page_content(raw_page_content)
    print(f"Time taken after cleaning content: {time.time() - start_time:.2f} seconds")

    # Step 3: Retrieve metadata
    page_title = get_page_title(url)
    page_description = get_page_description(url)
    print(f"Time taken after retrieving metadata: {time.time() - start_time:.2f} seconds")

    # Step 4: Build the prompt and call the AI model
    final_prompt = f"""{prompt}: 
    Page title: {page_title}
    Page description: {page_description}
    Page content: {page_content} 
    Limit your response to {length} words."""
    response = get_response(final_prompt, 'phi3')
    #response = get_response(final_prompt, 'llama3')
    #response = get_response(final_prompt, 'gemma2')#timeout
    #response = get_response(final_prompt, 'gemma2:2b')
    #response = get_response(final_prompt, 'qwen2.5:latest')
    #response = get_response(final_prompt, 'mistral-nemo:latest')#timeout
    #response = get_response(final_prompt, 'smollm2:135m')  # Replace with any desired model
    print(f"Time taken for generating response: {time.time() - start_time:.2f} seconds")

    return response

if __name__ == "__main__":
    url = "https://mysitefaster.com"
    content = describe_page(url)
    if content:
        print(content[:50000])  # Print the first 500 characters of the content   
        
