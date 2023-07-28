#Application-ID : 1134525900986261515
#Public-Key : 0c4738293c02edd3bf723c48a34c8842355bad712dc8d5946b9c115f8d0863d1

import openai
# This example requires the 'message_content' intent.
import os
import discord

TOKEN = os.environ['SECRET_KEY']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('TOKEN')

