import random
import scraper

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello there!'

    if p_message == '!help':
        # placeholder"
        return ''

    if p_message == '!word':
        word = scraper.scrape()
        return word[0].capitalize() + '\n' + word[1] + ' | ' + word[2] + '\n\n' + word[3]