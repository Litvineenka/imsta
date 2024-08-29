import os
import base64
import requests
from colorama import Fore, Style, init

# Initialize colorama for color display
init(autoreset=True)

# Find your API Key here --> https://platform.openai.com/settings/profile?tab=api-keys

# OpenAI API key (NOTE: Be sure not to expose API keys in production source code)
# To add your API Key to your environment, type :
# export API_KEY="your_api_key" (Linux/MacOS - .bashrc, .bash_profile, or .zshrc)
# or
# setx API_KEY "your_api_key" (Windows)

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set the API_KEY environment variable.")


# Function to display titles in the terminal
def print_title(title):
    print(f"\n{Fore.CYAN + Style.BRIGHT}{'='*len(title)}")
    print(f"{title}")
    print(f"{'='*len(title)}{Style.RESET_ALL}\n")

# Function for renaming files in a folder
def rename_files_sequentially(directory, prefix='img_', extension_filter=None):
    print_title("Renaming files")
    files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    
    if extension_filter:
        files = [f for f in files if f.lower().endswith(extension_filter.lower())]

    for i, filename in enumerate(files, start=1):
        old_path = os.path.join(directory, filename)
        _, ext = os.path.splitext(filename)
        new_filename = f"{prefix}{i:02d}{ext}"
        new_path = os.path.join(directory, new_filename)
        
        os.rename(old_path, new_path)
        print(f"{Fore.GREEN}Renamed: {Fore.YELLOW}{filename}{Fore.RESET} -> {Fore.YELLOW}{new_filename}")

# Function to encode an image in base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to send a request to the OpenAI API for each image
def analyze_images_in_directory(directory, prefix='img_', extension_filter='.jpg'):
    print_title("Analyze images and send queries to OpenAI")
    
    files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    
    if extension_filter:
        files = [f for f in files if f.lower().endswith(extension_filter.lower())]
    
    for i, filename in enumerate(files, start=1):
        image_path = os.path.join(directory, filename)
        base64_image = encode_image(image_path)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a highly experienced community manager with 20 years of expertise in social networks, specializing in crafting engaging Instagram content."
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Please analyze the attached image {filename} and craft a compelling Instagram caption along with relevant hashtags to maximize engagement."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        
        print(f"\n{Fore.GREEN}Response for {filename}:")
        print(response.json())

directory = 'images'  # Folder containing images

# Renaming files in the “images” folder
rename_files_sequentially(directory, prefix='img_', extension_filter='.jpg')

# Analyze images and send requests to the OpenAI API
analyze_images_in_directory(directory, prefix='img_', extension_filter='.jpg')
