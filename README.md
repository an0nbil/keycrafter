# KeyCrafter Wordlist Generator

KeyCrafter is a Python script designed for generating customized wordlists for penetration testing and security assessment purposes. It scrapes a target website for keywords, filters them based on relevance, and combines them with common patterns to create comprehensive wordlists.

## Features

- **Web Scraping**: Extracts keywords from a specified target URL using BeautifulSoup.
- **Keyword Filtering**: Removes stopwords and non-alphabetic characters to enhance relevance.
- **Pattern Generation**: Combines keywords with common patterns like 'admin', 'login', etc., for varied testing scenarios.
- **File Output**: Saves the generated wordlist to a specified file.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/an0nbil/keycrafter.git
   cd keycrafter
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
3. **Run the script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where you cloned the repository.
   - Execute the following command to run KeyCrafter:
     ```bash
     python keycrafter.py
     ```
   - Follow the on-screen instructions to enter the target URL and specify the output filename for the generated wordlist.

## Usage
 - When prompted, enter the target URL you want to scrape for keywords.
 - Specify the filename where you want to save the generated wordlist.
 - Follow the on-screen instructions to complete the process.

## Example
Here's a brief example of how to use KeyCrafter:
  ```bash
python keycrafter.py
 ```
  ```bash
[+] Welcome to KeyCrafter by an0nbil!
[+] Educational Use Only: Misuse not endorsed or supported by developer.

Enter the target URL: https://example.com
Enter the output wordlist filename: example_wordlist.txt

[+] Scraping website for keywords...
[+] Found 100 keywords.
[+] Filtering and enhancing keywords...
[+] Filtered to 80 relevant keywords.
[+] Generating wordlist...
[+] Generated wordlist with 200 entries.
[+] Wordlist saved to example_wordlist.txt
 ```
## Contributing
Contributions are welcome! If you have any suggestions, improvements, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
