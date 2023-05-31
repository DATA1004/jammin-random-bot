import discord
from discord.ext import commands
import random
import requests

bot = commands.Bot(command_prefix='!')

@bot.command()
async def 랜덤(ctx):
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}

    # 버전
    version = requests.get('https://ddragon.leagueoflegends.com/api/versions.json', headers=headers).json()[0]

    # 챔피언
    champion_res = requests.get('https://ddragon.leagueoflegends.com/cdn/' + version + '/data/ko_KR/champion.json', headers=headers).json()['data']

    champions = []
    for champion in champion_res:
        champion_name = champion_res[champion]['name']
        if champion_name not in ['아우렐리온 솔', '피들스틱스']:
            champions.append(champion_name)

    random.shuffle(champions)

    team1 = champions[:10]
    team2 = champions[10:20]

    response = "1팀: "
    response += ", ".join(team1) + "\n"
    response += "2팀: "
    response += ", ".join(team2)

    await ctx.send(response)

@bot.event
async def on_ready():
    print(f'봇 이름: {bot.user.name}')
    print(f'봇 아이디: {bot.user.id}')
    print('봇이 준비되었습니다.')

# 봇 실행하기
TOKEN = os.environ.get('TOKEN')