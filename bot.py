import os
import discord

client = discord.Client()
TOKEN = os.environ['DISCORD_TOKEN']


async def reply(message):
    reply = f'{message.author.mention} 呼んだ？'  # 返信メッセージの作成
    await message.channel.send(reply)  # 返信メッセージを送信


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('/neko'):
        await reply(message)

client.run(TOKEN)
