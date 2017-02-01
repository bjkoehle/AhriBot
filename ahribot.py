import aiohttp
import websockets
import discord
import requests


r = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/beastlymonkey?api_key=RGAPI-dd80b910-d882-4b82-8e11-30a58938652a")
d = r.json()
print(d['beastlymonkey']['id'])
