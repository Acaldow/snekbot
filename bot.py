import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix = '!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    SW_quotes = ['Do or do not. There is no try.',
    'You must unlearn what you have learned.',
    'Named must be your fear before banish it you can.',
    'Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.',
    'That is why you fail.',
    'The greatest teacher, failure is.',
    'Pass on what you have learned.',
    'The Force will be with you. Always.',
    'A long time ago in a galaxy far, far away.',
    'If you strike me down I shall become more powerful than you can possibly imagine.',
    "It's a trap!",
    'No. I am your father.',
    'Now, young Skywalker, you will die.'
    ]

    if 'star wars' in message.content:
        response = random.choice(SW_quotes)
        await message.channel.send(response)
    elif 'raise-exception' in message.content:
        raise discord.DiscordException

    await bot.process_commands(message) # if you override the default on_message you have to use this to be able to use commands as well


@bot.command(name = 'funfact', help= 'Gives out a random fun fact')
async def fun_facts(ctx):
    fun_facts_quotes = ["North Korea and Cuba are the only places you can't buy Coca Cola",
    "The entire world's population could fit inside Los Angeles.",
    'More people visit France than any other country (yikes)',
    "The world's quietest room is located at Microsoft's headquarters in Washington state.",
    "There are only 3 countries in the world that don't use the metric system.",
    "Only 2 countries use purple in their national flags."
    ]

    response = random.choice(fun_facts_quotes)
    await ctx.send(response)


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name = 'create-channel')
@commands.has_role('Admin')
async def create_channel(ctx, channel_name = 'real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name = channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

print("hello")

bot.run(TOKEN)

print('Hello World')
print('Salut ça va')
print('This is the dev branch')


print('hello')
print('techteam')