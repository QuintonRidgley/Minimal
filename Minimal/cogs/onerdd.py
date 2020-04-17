import discord
from discord.ext import commands

class oNerdd(commands.Cog):

    def _int_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog : oNerdd, loaded')

    twitch = 'https://www.twitch.tv/oNerdd'
    youtube = 'https://www.youtube.com/channel/UCIUoUynJlHjfH1cn35sfO2w'
    twitter = 'https://twitter.com/QuintonRidgley'

    @commands.command(name='oNerdd')
    #@commands.has_permissions(embed_links=True)
    async def oNerdd(self, ctx, *, arg1, arg2, twitch, youtube, twitter):
        if arg1 is 'twitch':
            await ctx.send(twitch)
        if arg1 is 'youtube':
            await ctx.send(youtube)
        if arg1 is 'twitter':
            await ctx.send(twitter)
        else:
            await ctx.send("This argument is not a function option, please select another more suitable option.")

def setup(client):
    client.add_cog(oNerdd(client))
