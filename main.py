import os
token = os.environ['Token.']
import discord
from discord.ext import commands
from keep_alive import keep_alive

regles = "➔ Respecter les Conditions d'Utilisation de Discord (https://discord.com/terms).\n➔ Restez respectueux les un envers les autres.\n➔ Les pseudonymes invisibles ne sont pas autorisés.\n➔ La publicité n'est pas autorisé.\n➔ L'usurpation d'identité est formellement prohibé.\n➔ Les doubles comptes ne sont pas autorisé.\n➔ Tout contournement de ban ou de permissions est bannissable définitivement\n\n:speech_balloon: Les salons textuels\n\n➔ Vous êtes tenus pour seul responsable des messages que vous postez.\n➔ Les thèmes de salons sont à respecter.\n➔ Le chantage est hautement sanctionnable.\n➔ Le spam/flood est interdit dans l'ensemble du serveur.\n➔ Les mentions de rôles sont à éviter.\n➔ La publicité n'est pas autorisée sur ce serveur\n\n:loud_sound: Les salons vocaux\n\n➔ Le changement répétitif de salon vocaux est sanctionnable.\n➔ Les insultes, débits vocal, sont formellement interdit.\n➔ Toute intervention néfaste ou intempestive sera sanctionné.\n➔ Les soundboards, modificateur de voix sont interdit.\n➔ Le contournement ou tentative de sanction est passible de bannissement.\n➔ Une plainte peut être justifiée auprès d'un membre du staff."


intent = discord.Intents.default()
intent.members = True
bot = commands.Bot(intents=intent, command_prefix="%", help_command=None, description=None)

@bot.event
async def on_ready():
    print("i im ready")

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(875291813609607178)
    channel = guild.get_channel(875299474270990367)
    embedwelcome=discord.Embed(title="Nenozia - Bienvenue", description=f"**Bienvenue à {member.mention} sur *{guild.name}* on espère que tu vas t’y plaire !**", color=0x000000)
    embedwelcome.set_footer(text=f"Nous sommes maintenant {guild.member_count}", icon_url=member.avatar_url)
    await channel.send(embed=embedwelcome)
    embedmp=discord.Embed(title="Nenozia - Bienvenue", description=f"Bonjour et merci d'avoir rejoin le serveur discord.\nMerci de bien vouloir lire les régle\nVoici quelque information sur le serveur:", color=0x000000)
    embedmp.add_field(name="Créateur du serveur", value="**maxnat#5139**", inline=True)
    embedmp.add_field(name="Date de création", value="**11/09/2021**")
    embedmp.add_field(name="Nombre de membre", value=f"**{guild.member_count}**")
    await member.send(embed=embedmp)

@bot.command()
async def regle(ctx):
    await ctx.message.delete()
    await ctx.send("**Vous venez de recevoir un message privée du bot avec le réglement.**")
    embedregle=discord.Embed(title="Réglement:", description=regles, color=0x000000)
    await ctx.author.send(embed=embedregle)

@bot.event
async def on_message(message):
    if message.content == "hey" or message.content == "Hey" or message.content == "Bonjour" or message.content == "bonjour" or message.content == "slt" or message.content == "salut" or message.content == "Salut":
                await message.add_reaction("👋")

    await bot.process_commands(message)

@bot.command()
@commands.has_permissions(ban_members=True)
async def prison(ctx, user : discord.User, *reason):
    await ctx.message.delete()
    " ".join(reason)
    await user.send(f"***{user.display_name}* tu à été mis en prison par *{ctx.author.name}* pour la raison: *{reason}***")
    await ctx.guild.ban(user = user, reason = reason)
    await ctx.send(f"***{user.display_name}* à été mis en prison avec succés! ✅**")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user : discord.User, *, reason=None):
    await ctx.message.delete()
    await user.send(f"{user.display_name} tu à été kick par {ctx.author.name} pour la raison: {reason}")
    await ctx.guild.kick(user = user, reason = reason)
    await ctx.send(f"***{user.display_name}* à été kick avec succés! ✅**")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"```python\n{amount} message(s) ont été supprimé avec succés! ✅```")

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f"**Mon ping est de *{round(bot.latency * 1000)}ms***")

@bot.command()
async def suggestion(ctx, *txt):
    guild = bot.get_guild(875291813609607178)
    channel = guild.get_channel(885975469151899668)
    if ctx.channel == channel:
        await ctx.message.delete()
        embed=discord.Embed(title="**Suggestion**", description=f"{' '.join(txt)}", color=0xDFEC0D)
        embed.set_footer(text=f"suggestion de {ctx.author}")
        message =  await ctx.send(embed=embed)  
        await message.add_reaction("✅")
        await message.add_reaction("❌")
    else:
        await ctx.message.delete()        
        await ctx.send("**Veuiller faire votre suggestion dans le bon salon.**")

@bot.command()
async def welcome(ctx, user : discord.User):
        await ctx.message.delete()
        await ctx.send(f"**Bienvenue {user.display_name} sur le serveur {ctx.guild.name} de la par de {ctx.author.display_name}.**")


@bot.command()
async def help(ctx):
        embedhelp=discord.Embed(title="Nenozia - Help", description=f"**En cas de probleme merci de faire la commandes `{bot.command_prefix}report`**\n\n**Modération:**\n`{bot.command_prefix}clear, {bot.command_prefix}kick, {bot.command_prefix}prison, {bot.command_prefix}avert.`\n\n**Utile:**\n`{bot.command_prefix}report, {bot.command_prefix}welcome, {bot.command_prefix}suggestion, {bot.command_prefix}sondage, {bot.command_prefix}regle.`", color=0xDFEC0D)
        embedhelp.set_footer(text=f"éxécuté par {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embedhelp)     
@bot.command()
async def report(ctx, *report):
        guild = bot.get_guild(875291813609607178)
        reportcmdchannel = guild.get_channel(886544528314609685)
        reportstaff = guild.get_channel(886544823643942942)
        await ctx.message.delete()
        if ctx.channel == reportcmdchannel:
                await ctx.send("**Report éfféctué avec succés! ✅**") 
                embedreport=discord.Embed(title="Nenozia - Report", description=f"{' '.join(report)}", color=0xDFEC0D)
                embedreport.set_footer(text=f"report de {ctx.author}", icon_url=ctx.author.avatar_url)
                await reportstaff.send(embed=embedreport)
        else:
                await ctx.send(f"**Veuiller éxécuté la commandes dans le bon salon (<#{reportcmdchannel.id}>).**")

@bot.command()
@commands.has_permissions(administrator=True)
async def sondage(ctx, *message):
        await ctx.message.delete()
        message = " ".join(message)
        embedsuggest=discord.Embed(title="Nenozia - Sondage", description=f"**{message}**\n**Pour répondre cocher la réaction ✅ (oui) ou la réaction ❌ (non).**", color=0xDFEC0D)
        embedsuggest.set_footer(text=f"Sondage fait par {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        text = await ctx.send(embed=embedsuggest)
        await text.add_reaction("✅")
        await text.add_reaction("❌")

    
@bot.command()
@commands.has_permissions(kick_members=True)
async def avert(ctx, user : discord.User, *, reason="Aucune raison n'a été spécifiée."):
        guild = bot.get_guild(875291813609607178)
        channel = guild.get_channel(886569730687774780)
        embedwarn = discord.Embed(title="<!> Un utilisateur a reçu un avertissement", description="Un modérateur/administrateur a averti un membre", color=0xDFEC0D)

        embedwarn.set_author(name=ctx.author.name, url=ctx.author.avatar_url)
        embedwarn.add_field(name="Membre averie:", value=f"{user.mention}", inline=True)
        embedwarn.add_field(name="Modérateur:", value=ctx.author.mention)
        embedwarn.add_field(name="Raison:", value=reason)
        await ctx.send(embed=embedwarn)
        await ctx.message.delete()
        embedlogs = discord.Embed(title="<!> Un utilisateur a reçu un avertissement", description="Un modérateur/administrateur a averti un membre", color=0xDFEC0D)

        embedlogs.set_author(name=ctx.author.name, url=ctx.author.avatar_url)
        embedlogs.add_field(name="Membre averie:", value=f"{user.mention}", inline=True)
        embedlogs.add_field(name="Modérateur:", value=ctx.author.mention)
        embedlogs.add_field(name="Raison:", value=reason)
        await channel.send(embed=embedlogs)
          
          
keep_alive()
bot.run(token)