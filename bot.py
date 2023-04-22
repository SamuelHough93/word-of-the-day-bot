import discord
import responses
from discord.ext import tasks

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = '[INSERT DISCORD BOT TOKEN HERE]'
    intents = discord.Intents.all()
    intents.message_content = True
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        wotd.start()

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' in ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @tasks.loop(hours=24)
    async def wotd():
        channel = client.get_channel([INSERT CHANNEL ID HERE])
        message = responses.handle_response('!word')
        await channel.send(message)

    client.run(TOKEN)