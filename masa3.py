import discord
import asyncio
import re
import random
import talking
client = discord.Client()
def colors():
    list_colors = [{'color':"16777215"},{'color':"16711680"},{'color':"0"},{'color':"255"},{'color':"8388736"},{'color':"65535"},{'color':"8421504"},{'color':"8421504"},{'color':"10040319"}]
    random_color = random.choice(list_colors)
    random_color['color']
    return random_color
def escape_mass_mentions(text):
    words = {
        "@everyone": "@\u200beveryone",
        "@here": "@\u200bhere"
    }
    for k, v in words.items():
        text = text.replace(k, v)
    return text

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence( game=discord.Game( name= '.mhelp'))
@client.event
async def on_message(message):
    random_color = colors()
 #   if message.content.startswith('=ok'):
     #   await client.send_message(message.channel,'ok')
    if message.content.startswith('.mhelp'):
        await client.send_message(message.channel,"""```
..........................................
|Commands       |    Usage               |
+=-=-=-=-=-=--=-+-=-=-=-=-=-=-=-=-=-=-=-=+
|.muser         | info about msgauthor.  |
|.muser <tag>   | info about tagged user.|
|.msay <text>   | repeats your words.    |
''''''''''''''''''''''''''''''''''''''''''
 Masamune <text> to talk ;D        
 More to come soon ;D```""")
    elif message.content.startswith('.muser'):
        try:
            if message.channel.id !='274387797140570112':
                coloursman = int(random_color['color'])
                if message.content == '.muser':
                    discord.Member = None
                    author = message.author
                    if not discord.Member :
                        discord.Member = message.author
                    roles = [x.name for x in discord.Member.roles if x.name != "@everyone"]
                    if not roles: roles = ["None"]
                    data = "\n"
                    data += "Name: {}\n".format(escape_mass_mentions(str(discord.Member)))
                    data += "Nickname: {0}\n".format(discord.Member.display_name)
                    data += "ID: {}\n".format(discord.Member.id)
                    passed = (message.timestamp - discord.Member.created_at).days
                    data += "Created: {} days ago.\n".format(passed)
                    passed = (message.timestamp - discord.Member.joined_at).days
                    data += "Joined: {} days ago\n".format(passed)
                    data += "Server: {}\n".format(discord.Member.server)
                    data += "Status: {}\n".format(discord.Member.status)
                    data += "Playing: {}\n".format(discord.Member.game)
                    data += "Bot Account: {}\n".format(discord.Member.bot)
                    data += "Roles: {}\t".format(", ".join(roles))
                    data += "**({0})**\n".format(len(roles))
                    data += "Top Role: {}\n\n".format(discord.Member.top_role)
                
                    user_em = discord.Embed(
                    description=data)
                    user_em.set_author(
                    name="Your Info 😄 :")
                    user_em.set_image(url = discord.Member.avatar_url)
                    user_em.color=coloursman
                
                    await client.send_message(message.channel,embed = user_em)          
           
           
           
                else:
                    check_tagger = re.findall('.muser\s(.*)',message.content)
        
                    hilol_ = ' '.join(check_tagger)
                    no1is = re.sub(r'[^\w]', ' ', hilol_)
                    thisiscool = no1is.replace(' ','')
                
                    member_id = message.author.server.get_member(user_id = thisiscool)
                    
                    discord.Member = member_id 
                    roles = [x.name for x in discord.Member.roles if x.name != "@everyone"]
                    if not roles: roles = ["None"]
                    data = "\n"
                    data += "Name: {}\n".format(escape_mass_mentions(str(discord.Member)))
                    data += "ID: {}\n".format(discord.Member.id)
                    passed = (message.timestamp - discord.Member.created_at).days
                    data += "Created: {} days ago\n".format(passed)
                    passed = (message.timestamp - discord.Member.joined_at).days
                    data += "Joined: {} days ago\n".format(passed)
                    data += "Server: {}\n".format(discord.Member.server)
                    data += "Status: {}\n".format(discord.Member.status)
                    data += "Playing: {}\n".format(discord.Member.game)
                    data += "Bot Account: {}\n".format(discord.Member.bot)
                    data += "Roles: {}\t".format(", ".join(roles))
                    data += "**({0})**\n".format(len(roles))
                    data += "Top Role: {}\n\n".format(discord.Member.top_role)
                    user_em = discord.Embed(
                    description=data)
                    user_em.set_author(
                    name="User Info 😄 :")
                    user_em.set_image(url = discord.Member.avatar_url)
                    user_em.color=coloursman
                
                    await client.send_message(message.channel,embed = user_em)
  
        except Exception as e: print (str(e))
    
    
    elif message.content.startswith('Masamune'):  
        if message.content == 'Masamune':return
        else:
            text = re.findall('Masamune\s(.*)',message.content)
            refined = ' '.join(text)
            near_done = refined
            lower_them = near_done.lower()
            stuff = lower_them
            new = talking.talk(stuff)
            await client.send_typing(message.channel)
            await client.send_message(message.channel,new)
                  
    elif message.content.startswith('h!say'):
        if message.content == '.msay':return
        else:
            text = re.findall('.msay\s(.*)',message.content)
            refined = ' '.join(text)
            await client.send_message(message.channel, '{0}'.format(refined))
                            

print('Starting....')
client.run('MzMzNjAxMzE1OTY1ODk0NjU2.DFDCrw.RPxweTa0q8ANnfU-lEIAcvpCfDk')
