from bs4 import BeautifulSoup
import requests

def scrape():
    page_to_scrape = requests.get("https://www.merriam-webster.com/word-of-the-day")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    word = soup.find_all('h1')
    definition = soup.findAll('p')
    return_object = word[0].text, definition[0].text
    return return_object
