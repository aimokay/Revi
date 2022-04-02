import discord
from discord.ext import commands

from discord_slash import cog_ext
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option


class Inf(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @cog_ext.cog_slash(
        name = "inf",
        description="Информация об учасниках сервера",
        guild_ids=[745244523587698698],
        options=[
            create_option(
                name="учасник",
                description="Выберите учасника из списка",
                required = True,
                option_type=6,
            )
        ]
    )
    async def _inf(self, ctx:SlashContext, учасник:discord.Member):
        embed=discord.Embed(title=f"Информация про {учасник.display_name}, color=0x8e18dc")
        embed.set_thumbnail(url=f"{учасник.avatar_url}")
        embed.add_field(name="Ник", value=f"{учасник.display_name}", inline=True)
        embed.add_field(name="id", value=f"{учасник.id}", inline=True)
        embed.add_field(name="На сервере с", value=f"`{учасник.joined_at}`", inline=False)
        
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Inf(bot))