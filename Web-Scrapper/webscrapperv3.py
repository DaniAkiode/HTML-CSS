import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Real_Madrid_CF_players"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

player_names = []

# Find all <a> tags with title attributes (these usually contain player names)
player_links = soup.find_all('a', {'title': True})

# Keywords to filter out non-footballer titles
football_keywords = ['footballer', 'soccer player', 'forward', 'midfielder', 'defender', 'goalkeeper']

# Iterate over the links and extract player names
for link in player_links:
    # Some links have 'title' attribute but not all represent player names
    # We can filter out those by checking the format of the 'title' attribute
    title = link.get('title')
    if title and any(keyword in title.lower() for keyword in football_keywords):
        player_names.append(title)

# Print the collected player names
for name in player_names:
    print(name)