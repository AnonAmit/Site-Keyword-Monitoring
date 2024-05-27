# Google Custom Search Monitoring Script

This script allows you to perform automated searches using Google's Custom Search API to monitor specific keywords across specified sites. It offers three modes of operation: using a default search query, entering a custom search query, or generating an automatic custom query based on user input for site and keywords.

## Features

- **Default Search Query**: Use a predefined query to search for malware, exploit, and zero-day discussions on specific forums.
- **Custom Search Query**: Manually input a search query.
- **Auto Custom Query**: Automatically generate a search query based on a user-specified site and keywords.
- **Continuous Monitoring**: Perform searches at regular intervals (every 60 seconds).

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

The script automatically installs the required packages (`requests` and `colorama`) if they are not already installed. To manually install the dependencies, run:
```sh
pip install requests colorama
```

## Usage

1. Clone Repo
   ```sh
   git clone https://github.com/AnonAmit/
   cd Site-Keyword-Monitoring
``
2. Run the script using:
   ```sh
   python cse.py
   ```
3. Follow the prompts to select the type of search query you want to use:
   - Press `1` to use the default search query.
   - Press `2` to enter a custom search query.
   - Press `3` to generate an auto custom query based on site and keywords.

## Getting Google Custom Search API Credentials

To use the script, you need to set up a Google Custom Search Engine (CSE) and obtain an API key. Follow these steps:

1. **Create a Custom Search Engine**:
   - Go to the [Custom Search Engine](https://cse.google.com/cse/) page.
   - Click on "Add" to create a new search engine.
   - Enter the sites you want to search (e.g., `forum1.com`, `forum2.net`).
   - Click "Create".

2. **Get the CSE ID**:
   - After creating your search engine, go to the control panel.
   - Note the `Search engine ID` displayed at the top of the page. This is your `CSE_ID`.

3. **Enable the Custom Search API**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing project.
   - Go to the [APIs & Services Dashboard](https://console.cloud.google.com/apis/dashboard).
   - Click on "Enable APIs and Services".
   - Search for "Custom Search API" and enable it.

4. **Get the API Key**:
   - In the [Google Cloud Console](https://console.cloud.google.com/), go to "APIs & Services" > "Credentials".
   - Click "Create credentials" and select "API key".
   - Copy the generated API key. This is your `API_KEY`.

5. **Update the Script with Your Credentials**:
   - Replace the placeholders in the script with your own CSE ID and API Key:
     ```python
     CSE_ID = "your_custom_search_engine_id"
     API_KEY = "your_api_key"
     ```

## Script Breakdown

- **Dependencies Check and Installation**: Ensures `requests` and `colorama` are installed.
- **Query Functions**: 
  - `use_default_query()`: Returns a predefined query string.
  - `use_custom_query()`: Prompts user for a custom query.
  - `auto_custom_query()`: Prompts user for site and keywords, then generates a query.
- **Search Execution**: Encodes the query and makes a request to the Google Custom Search API.
- **Main Function**: Handles user interaction, executes the search, and repeats the search every 60 seconds.

## Example Queries

- **Default Query**: 
  ```plaintext
  (site:forum1.com OR site:forum2.net) ("malware" OR "exploit" OR "zero-day") ("APT1" OR "Group X") in:title OR in:body
  ```
- **Auto Custom Query**: 
  ```plaintext
  site:example.com (keyword1,keyword2) in:title OR in:body
  ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to contribute to this project by submitting issues or pull requests on the [GitHub repository](#). For any questions or support, contact [Anon.Amit](mailto:anon.amit.contact@gmail.com).

---

**Note**: This script is for educational purposes. Be mindful of Google's usage policies and terms of service when using the Custom Search API.
