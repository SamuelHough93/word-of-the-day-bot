import random
import scraper

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello there!'

    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message == '!help':
        # "`This is a help message that you can modify`"
        return 'Fuck off :)'

    if p_message == '!word':
        word = scraper.scrape()
        return word[0].capitalize() + '\n\n' + word[1]
