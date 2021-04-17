import re
import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
from datetime import datetime


TOKEN = 'NjcxNjc3OTUxMDc0MzY5NTQw.XjS6vg.XqCZS0o5EqzjmQrs_SjbwUFeUPk'
bot = commands.Bot(command_prefix='%')

html_Tablica_tarkovhelp = requests.get('https://escapefromtarkov.fandom.com/ru/wiki/%D0%91%D0%BE%D0%B5%D0%BF%D1%80%D0%B8%D0%BF%D0%B0%D1%81%D1%8B')
soup = BeautifulSoup(html_Tablica_tarkovhelp.text, "html.parser")





@bot.command(pass_context=True)
async def п(ctx, arg):
    dobav=0
    c=0
    cou=0
    bilo=[]
    author = ctx.author
    patr = ""
    patr = patr+arg
    vers = []
    vers.append(patr)

    red=""+patr.upper()
    red2=""+patr.lower()
    red3=""+patr.title()
    vers.append(red)
    vers.append(red2)
    vers.append(red3)


    flag = 0
    for i in vers :
        b=len(set(soup.findAll('a',text=re.compile(i))))

        print(set(soup.findAll('a', text=re.compile(i))))


        if len(set(soup.findAll(text=re.compile(i))))>0 and c<=b and flag ==0:
            tableAll = soup.findAll(text=re.compile(i))


            for j in tableAll:
                c = c + 1
                try:
                    table = j.find_parent('tr')

                    output = table.find("img")
                    icon = output.get("src")
                    output = table.findChild("td")
                    name = output.text
                    output = table.findAll("td")
                    dmg = str(output[1])
                    dmg = dmg[4:len(dmg) - 5]


                    pen = str(output[2])
                    pen = pen[4:len(pen) - 5]
                    armordmg = str(output[3])
                    armordmg = armordmg[4:len(armordmg) - 5]
                    accu = str(output[4])
                    accu = accu[25:len(accu) - 12]
                    recoil = str(output[5])
                    recoil = recoil[25:len(recoil) - 12]
                    fragm = str(output[6])
                    fragm = fragm[4:len(fragm) - 5]
                    bounce = str(output[7])
                    bounce = bounce[4:len(bounce) - 5]
                    speed = str(output[8])
                    seller = str(output[9].text)




                    speed = speed[4:len(speed) - 5]
                    if name not in bilo:

                        bilo.append(name)
                    else: continue

                    if "шт" in table.extract():
                        continue

                    embed= discord.Embed(
                        #title = name,
                        #description= f"Урон: {dmg}, Пробитие: {pen}, Урон броне: {armordmg}%, Скорость: {speed}",
                        colour= discord.Colour.from_rgb(0,0,0)
                    )
                    embed.add_field(name=name, value=f"Урон: **{dmg}**,     Пробитие: **{pen}** \n Урон броне: **{armordmg}%** ,  Скорость: **{speed}**\n ", inline=False)
                    embed.set_thumbnail(url=icon)
                    if seller:
                        embed.set_footer(text=f"Продает {seller}")
                    else:
                        embed.set_footer(text=f"Нельзя купить у торговцев")
                    await ctx.send(embed=embed)


                    flag=1

                    print(c)
                    if c == len(set(soup.findAll(text=re.compile(i)))):
                        break
                except:

                    continue

        if flag==1:
            break

      


@bot.command(pass_context=True)
async def play(ctx, video_url):
    author = ctx.author
    channel = author.voice.channel

    await ctx.send("will be played soon... " + video_url)



@bot.command(pass_context=True)
async def status(ctx, user: discord.Member):
    date: datetime
    date = user.joined_at
    if date.month == 1:
        month = "Jan"
    elif date.month == 2:
        month = "Feb"
    elif date.month == 3:
        month = "Mar"
    elif date.month == 4:
        month = "Apr"
    elif date.month == 5:
        month = "May"
    elif date.month == 6:
        month = "June"
    elif date.month == 7:
        month = "Jule"
    elif date.month == 8:
        month = "Aug"
    elif date.month == 9:
        month = "Sep"
    elif date.month == 10:
        month = "Oct"
    elif date.month == 11:
        month = "Nov"
    else:
        month = "Dec"

    fulldate = str(user.name+' joined ' + str(date.day) + "'th of " + month + " " + str(date.year))
    await ctx.send(fulldate)
print("im ready")
bot.run(TOKEN)
