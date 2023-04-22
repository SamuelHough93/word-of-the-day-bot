from bs4 import BeautifulSoup
import requests

def scrape():
    page_to_scrape = requests.get("https://www.merriam-webster.com/word-of-the-day")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    word = soup.find_all('h2')
    definition = soup.find_all('p')
    part_of_speech = soup.find_all(class_='main-attr')
    pronunciation = soup.find_all(class_='word-syllables')

    return_object = word[0].text, part_of_speech[0].text, pronunciation[0].text,  definition[0].text
    return return_object
