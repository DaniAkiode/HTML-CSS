import requests
from bs4 import BeautifulSoup

url = "https://www.worldfootball.net/teams/real-madrid/10/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

player_names = []

player_links = soup.find_all('a', {'title': True})

for link in player_links:
    title = link.get('title')
    if title and title.startswith('Category:'):
        continue
    player_names.append(title)


with open('RealMadridPlayers.txt', 'w', encoding='utf-8') as file:
    for name in player_names:
        file.write(name + '\n')

