import discord
import discord_slash
import json
import os

TOKEN = os.getenv('DISCORD_TOKEN')

wangy_file = open('wangy.json',)
wangy_string = json.load(wangy_file)

client = discord.Client(intents=discord.Intents(), command_prefix="/")
slash = discord_slash.SlashCommand(client, sync_commands=True)

options = options=[
    discord_slash.utils.manage_commands.create_option(
        name="message", description="What do you want to say?" , option_type=3, required=True
    )
]

@slash.slash(name="wangy",
            description="Default wangy",
            options=options)
async def wangy(ctx, message: str):
    wangy_text = wangy_string['wangy_1'].replace('$name', '**' + message.upper() + '**')
    await ctx.send(content=f"{wangy_text}")

@slash.slash(name="wangy2",
            description="wangy tipe 2",
            options=options)
async def wangy2(ctx, message: str):
    wangy_text = wangy_string['wangy_2'].replace('$name', '**' + message.upper() + '**')
    await ctx.send(content=f"{wangy_text}")

@slash.slash(name="wangy3",
            description="wangy tipe 3",
            options=options)
async def wangy3(ctx, message: str):
    wangy_text = wangy_string['wangy_3'].replace('$name', '**' + message.upper() + '**')
    await ctx.send(content=f"{wangy_text}")

# Start the Bot
client.run(TOKEN)
