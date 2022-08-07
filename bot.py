import discord
from discord.ext.commands import Bot

intents=discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + bot.user.name)
    print("디스코드봇 ID:" + str(bot.user.id))
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')

@bot.event
async def on_message(msg):
    print(f"{msg.channel} ({msg.author}) - {msg.content}")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(round(round(bot.latency, 4)*1000)))


bot.run('MTAwNTgxMDI1NjMxNzc4MDA0OQ.G_0i9W.zcO8us1la-OyvClsWNZI7Bgzq20ZRTPTCij33c')