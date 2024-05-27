import subprocess
import sys
import requests
import urllib.parse
import time
from colorama import Fore, Style

# Install required packages
def install_packages():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "colorama"])
    except subprocess.CalledProcessError:
        print("Failed to install required packages. Please make sure pip is installed.")

# Install required packages if not already installed
def check_dependencies():
    try:
        import requests
        from colorama import Fore, Style
    except ImportError:
        print("Installing required packages...")
        install_packages()

# Function to use default search query
def use_default_query():
    return "(site:forum1.com OR site:forum2.net) (\"malware\" OR \"exploit\" OR \"zero-day\") (\"APT1\" OR \"Group X\") in:title OR in:body"

# Function to use custom search query
def use_custom_query():
    custom_query = input("Enter your custom search query: ")
    return custom_query

# Function to generate auto custom query based on site and keywords
def auto_custom_query():
    site = input("Enter the site you want to monitor (e.g., example.com): ")
    keywords = input("Enter keywords to monitor (separated by comma): ")
    query = f"site:{site} ({keywords}) in:title OR in:body"
    return query

# Function to perform the search
def perform_search(query):
    CSE_ID = "CUSTOM_SEARCH_ID"
    API_KEY = "YOUR_CSE_API_TOKEN"
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CSE_ID}&q={encoded_query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            for item in data['items']:
                print(Fore.BLUE + item['title'] + Style.RESET_ALL, "-", item['link'])
    else:
        print("Error:", response.status_code)

# Main function
def main():
    check_dependencies()
    print(Fore.GREEN + "《《🔎 Google Search》》" + Style.RESET_ALL)
    print(Fore.YELLOW + "[1] Use Default Search Query")
    print("[2] Enter Custom Search Query")
    print(Fore.CYAN + "[3] Generate Auto Custom Query (based on site and keywords)")
    choice = input("Enter your choice: ")
    if choice == '1':
        query = use_default_query()
    elif choice == '2':
        query = use_custom_query()
    elif choice == '3':
        query = auto_custom_query()
    else:
        print("Invalid choice. Exiting...")
        return
    while True:
        perform_search(query)
        time.sleep(60)  # Pause for 60 seconds between searches

if __name__ == "__main__":
    main()
