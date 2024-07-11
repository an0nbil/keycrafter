import requests
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from wordfreq import word_frequency
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        keywords = re.findall(r'\b\w+\b', text)
        return set(keywords)
    except requests.RequestException as e:
        console.print(f"[bold red]Error scraping {url}: {e}[/bold red]")
        return set()

def filter_keywords(keywords):
    stop_words = set(stopwords.words('english'))
    filtered_keywords = [word.lower() for word in keywords if word.lower() not in stop_words and word.isalpha()]
    filtered_keywords = set(filtered_keywords)
    return sorted(filtered_keywords, key=lambda word: word_frequency(word, 'en'), reverse=True)

def generate_wordlist(keywords):
    common_patterns = ['admin', 'login', 'user', 'test', 'dev', 'api', 'config', 'backup', 'old']
    wordlist = set()
    
    for keyword in keywords:
        for pattern in common_patterns:
            wordlist.add(f"{pattern}{keyword}")
            wordlist.add(f"{keyword}{pattern}")
        wordlist.add(keyword)
    
    return wordlist

def save_wordlist(wordlist, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for word in sorted(wordlist):
            f.write(f"{word}\n")
    console.print(f"[bold green]Wordlist saved to {filename}[/bold green]")


# Main function
def main():
    console.print(r"""
[bold red]
  _  __           _____            __ _            
 | |/ /          / ____|          / _| |           
 | ' / ___ _   _| |     _ __ __ _| |_| |_ ___ _ __ 
 |  < / _ \ | | | |    | '__/ _` |  _| __/ _ \ '__|
 | . \  __/ |_| | |____| | | (_| | | | ||  __/ |   
 |_|\_\___|\__, |\_____|_|  \__,_|_|  \__\___|_|   
            __/ |  by an0nbil                                
           |___/                                   
[/bold red]""")
    console.print("[bold blue]KeyCrafter Wordlist Generator[/bold blue]")
    console.print("[bold]Welcome to KeyCrafter by an0nbil![/bold]")
    console.print("[bold yellow]Educational Use Only: Misuse not endorsed or supported by developer.[/bold yellow]")

    target_url = Prompt.ask("[bold cyan]Enter the target URL[/bold cyan]")
    output_file = Prompt.ask("[bold cyan]Enter the output wordlist filename[/bold cyan]")
    
    console.print("[bold yellow]Scraping website for keywords...[/bold yellow]")
    keywords = scrape_website(target_url)
    console.print(f"[bold yellow]Found {len(keywords)} keywords.[/bold yellow]")
    
    console.print("[bold yellow]Filtering and enhancing keywords...[/bold yellow]")
    filtered_keywords = filter_keywords(keywords)
    console.print(f"[bold yellow]Filtered to {len(filtered_keywords)} relevant keywords.[/bold yellow]")
    
    console.print("[bold yellow]Generating wordlist...[/bold yellow]")
    wordlist = generate_wordlist(filtered_keywords)
    console.print(f"[bold yellow]Generated wordlist with {len(wordlist)} entries.[/bold yellow]")
    
    save_wordlist(wordlist, output_file)

if __name__ == "__main__":
    import nltk
    nltk.download('stopwords')
    main()
