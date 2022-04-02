import discord
from discord.ext import commands

from discord_slash import cog_ext
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option


class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    """Ping command"""

    @cog_ext.cog_slash(
    name="ping",
    description="Замеры затержки бота по протоколу WebSocket в мс",
    guild_ids=[745244523587698698]
    )
    async def _ping(self, ctx:SlashCommand):
        embed=discord.Embed(
            title="Понг!",
            color=0x8e18dc,
            description='Задержка: {0}'.format(self.bot.latency)
        )
        embed.set_footer(text="ТыГыДыК | by DuyFI")
        await ctx.send(embed=embed)
    
    """BC Command"""

    @cog_ext.cog_slash(
    name="say",
    description="Пишем сообщения в чат от моего имени!",
    guild_ids=[745244523587698698],
    #options
    options = [
        create_option(
        name="сообщение",
        required = True,
        description = "Ваши каракули",
        option_type=3
        )
    ]
    )
    async def _say(self, ctx:SlashContext, сообщение):
        ch = self.bot.get_channel(957231841956478997)
        
        await ch.send(f"{сообщение}")
          
    


def setup(bot):
    bot.add_cog(Other(bot))