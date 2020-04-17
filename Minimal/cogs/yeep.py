import discord
from discord.ext import commands

class Yeep(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog : yeep, loaded')

    @commands.command()
    #@commands.has_permissions(embed_links=True)
    async def yeep(self, ctx):
        urls = 'https://www.twitch.tv/Yonnian'
        await ctx.send(urls)

def setup(client):
    client.add_cog(Yeep(client))
