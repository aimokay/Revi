import discord
from discord.ext import commands

from discord_slash import cog_ext
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

import json
import random


class Rang(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        else:
            with open("data_rank.json", "r") as js_file:
                lvl = json.load(js_file)
            
            lvl[f"{message.author.id}"] = [{
                "rank": 0,
                "score": 0,
            }]
            with open("data_rank.json", "w") as js_file:
                json.dump(lvl, js_file, indent=2)


def setup(bot):
    bot.add_cog(Rang(bot))