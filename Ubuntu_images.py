import requests
import os
from urllib.parse import urlparse
from typing import List

def download_image(url: str, directory: str = "Fetched_Images"):
    
    try:
        
        os.makedirs(directory, exist_ok=True)
        
        
        headers = {
            'User-Agent': 'Ubuntu-Image-Fetcher/1.0 (Python requests)'
        }
        response = requests.get(url, timeout=15, headers=headers)
        
        # 2. Check for HTTP errors (Respect)
        response.raise_for_status()  # Raises HTTPError for 4xx/5xx status codes
        
        # 3. Extract filename from URL or generate one (Practicality)
        parsed_url = urlparse(url)
        # Use the last segment of the path as the filename
        filename = os.path.basename(parsed_url.path)
        
        # Add basic content-type check to ensure it's an image before saving
        content_type = response.headers.get('Content-Type', '').lower()
        
        if not filename or not any(ext in filename.lower() for ext in ['.jpg', '.jpeg', '.png', '.gif']):
            # If no good filename is found in URL, generate one based on content type
            if 'jpeg' in content_type or 'jpg' in content_type:
                filename = "downloaded_image.jpg"
            elif 'png' in content_type:
                filename = "downloaded_image.png"
            elif 'gif' in content_type:
                filename = "downloaded_image.gif"
            else:
                filename = "downloaded_image_unknown"
        
        # Define the full path for saving
        filepath = os.path.join(directory, filename)
        
        # 4. Save the image in binary mode ('wb')
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"  ✓ Successfully fetched: {filename}")
        print(f"  ✓ Image saved to {filepath}")
        return True # Return success
        
    # 5. Handle errors gracefully (Respect)
    except requests.exceptions.HTTPError as e:
        print(f" HTTP Error for {url}: {e.response.status_code} - {e.response.reason}")
    except requests.exceptions.ConnectionError:
        print(f"Connection Error for {url}: Could not reach the server.")
    except requests.exceptions.Timeout:
        print(f"Timeout Error for {url}: Request took too long to complete.")
    except requests.exceptions.RequestException as e:
        # Catch all other requests-related errors (e.g., DNS failure, invalid URL)
        print(f"General Request Error for {url}: {e}")
    except IOError as e:
        print(f"File System Error: Could not write file to disk. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    return False # Return failure

def main():
    """Main function to run the Ubuntu Image Fetcher."""
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web (I am because we are)\n")
    
    # Get URL from user
    url = input("Please enter the image URL: ").strip()
    
    print("\n--- Starting Download ---\n")
    download_image(url)
    
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
