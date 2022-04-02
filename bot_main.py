from keep_alive import keep_alive
import os

import discord
from discord.ext import commands

from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
"""Here need enter python file names to connect cogs"""
cogs = [
    "other",
    "inf",
]

bot = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents.all())
sl = SlashCommand(bot, sync_commands=True)


"""Commands"""

@bot.event
async def on_ready():
    print("Bingo! I ready!!")

@sl.slash(
  name="help",
  description="Помощь по командам бота",
  guild_ids=[745244523587698698]
)
async def _help(ctx:SlashCommand):
  embed=discord.Embed(
    title="Команды",
    color=0x8e18dc,
    description="**/ping** - Замер задержки бота\n**/say** - Сообщение от моего имени\n **/inf** - Информация об учаснике"
  )
  embed.set_footer(text="ТыГыДыК | by DuyFI")
  await ctx.send(embed=embed)

"""Cog loader"""

if __name__ == "__main__":
    for extensoin in cogs:
        cog = f"cogs.{extensoin}"
        try:
            bot.load_extension(cog)
        except Exception as err:
            print(err)

keep_alive()
bot.run("ENTER TOKEN HERE!") #Pleace do not publish bot token!
