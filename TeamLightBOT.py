import discord #importer la librairie discord.py
from discord.ext import commands #importer des commandes spécifiques de la librairie
import os

bot = commands.Bot(description='Description', command_prefix='a!')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game (name="Team Light | a!help"))

@bot.command()
async def credits(ctx):
    embed=discord.Embed(
        title="-Crédits-",
        color=discord.Colour.purple()
        )

    embed.set_author(name="TeamLightBOT", icon_url="https://cdn.discordapp.com/attachments/332845778290868224/548943401173909537/1logo_TL_detourer.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/332845778290868224/548942388614135809/1logo_TeamLight2.jpg")
    embed.add_field(name="```Créateurs```", value="R3DLock", inline=True)
    embed.add_field(name="```Codeurs```", value="R3DLock", inline=True)
    embed.add_field(name="```Appartenance```", value="TeamLight", inline=True)
    embed.add_field(name="```Remerciements```", value="AP3RETURE Devlopment Team et つきしま | Tsukishima | 月島", inline=True)
    embed.set_footer(text="TeamLightBOT v1.0")



    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def help(ctx):
    embed=discord.Embed(
        title='-Liste des commandes-',
        colour=discord.Colour.purple()
        )

    embed.set_footer(text='TeamLightBOT v1.0')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/332845778290868224/548942388614135809/1logo_TeamLight2.jpg')
    embed.set_author(name='TeamLightBOT', icon_url='https://cdn.discordapp.com/attachments/332845778290868224/548943401173909537/1logo_TL_detourer.png')
    embed.add_field(name='```\Commandes simple/```', value='*a!cs*')
    embed.add_field(name='```\Commandes Utilitaires/```', value='*a!cu*')
    embed.add_field(name='```\Coming Soon/```', value='[...]')
    embed.add_field(name='```\Coming Soon/```', value='[...]')
    
    

    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
@commands.has_permissions(administrator=True, manage_messages=True)
async def say(ctx, *, texte):
    dire = discord.Embed(
        title = texte,
        colour = discord.Colour.purple()
    )
    await ctx.send(embed=dire)
    await ctx.message.delete()

@say.error
async def say_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        embed=discord.Embed(
            title="Vous n'avez pas les permissions d'utiliser cette commande !",
            color=discord.Colour.purple()
            )

        embed.set_author(name="TeamLightBOT", icon_url="https://cdn.discordapp.com/attachments/332845778290868224/548943401173909537/1logo_TL_detourer.png")
        embed.set_footer(text="TeamLightBOT v1.0")

        
            
        await ctx.send(embed=embed)

@bot.command()
async def cs(ctx):
    embed=discord.Embed(
        title="-Commandes simples-",
        color=discord.Colour.purple()
        )

    embed.set_footer(text='TeamLightBOT v1.0')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/332845778290868224/548942388614135809/1logo_TeamLight2.jpg')
    embed.set_author(name='TeamLightBOT', icon_url='https://cdn.discordapp.com/attachments/332845778290868224/548943401173909537/1logo_TL_detourer.png')
    embed.add_field(name='```Crédits```', value='a!credits')
    embed.add_field(name='```Aides```', value='a!help')
    embed.add_field(name='```Say```', value='a!say [Texte]')
    embed.add_field(name='```\Coming Soon/```', value='[...]')



    await ctx.send(embed=embed)
    await ctx.message.delete()

def tsuki(tsuki_id: int):
    def tsuki_check(ctx: commands.Context):
        return ctx.guild.id == tsuki_id
    return commands.check(tsuki_check)

def owner():
    def user(ctx: commands.Context):
        return ctx.author.id == 323080283261763585
    return commands.check(user)

@tsuki(540891671055958034)
@bot.command(name="fiche")
async def _fiche(ctx: commands.Context,* , texted: str):
    channel_id = ctx.bot.get_channel(548887763018317837)
    await channel_id.send(f'de : {ctx.message.author.id}/{ctx.message.author.name} par {ctx.message.author.mention}\n\n{texted}')
    await ctx.message.delete()
    return await ctx.send("Votre fiche a bien été envoyée")

@owner()
@bot.command(name= 'guild', hidden = True)
async def _guild(ctx: commands.Context):
    return await ctx.send(ctx.guild.id)

@commands.has_permissions(administrator=True)
@bot.command(name="confirmation")
async def _confirmation(ctx: commands.Context, Member: discord.Member, as_lisk: str, *, reason=None):
    Roled = discord.utils.get(ctx.guild.roles, id=548905234982764544)
    if as_lisk == "oui":
        await Member.add_roles(Roled)
        await ctx.send("La fiche à bien été accepté !")
        await Member.send("Félicitation, votre fiche à été accepté")
    else:
        if reason != None:
            await Member.send(f"Votre fiche n'as pas été accepter, la raison et la suivante : \n{reason}")
        else:
            await ctx.send("La fiche à bien été refusé !")
            return Member.send("Votre fiche n'as pas été accepter, pour en connaitre la raison contacté un administrateur.")

@bot.command()
async def cu(ctx):
    embed=discord.Embed(
        title="-Commandes utilitaires-",
        color=discord.Colour.purple()
        )

    embed.set_footer(text='TeamLightBOT v1.0')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/332845778290868224/548942388614135809/1logo_TeamLight2.jpg')
    embed.set_author(name='TeamLightBOT', icon_url='https://cdn.discordapp.com/attachments/332845778290868224/548943401173909537/1logo_TL_detourer.png')
    embed.add_field(name='```Fiches RP (seulement sur le SCP RP By TeamLight)```', value='*a!fiche [Votre fiche RP]*')
    embed.add_field(name='```\Coming Soon/```', value='[...]')
    embed.add_field(name='```\Coming Soon/```', value='[...]')
    embed.add_field(name='```\Coming Soon/```', value='[...]')



    await ctx.send(embed=embed)
    await ctx.message.delete()


bot.run(bot.run(os.environ('TOKEN'))) #Lancer le bot. Remplacez token par votre token et laissez les apostrophes
