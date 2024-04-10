import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Real_Madrid_CF_players"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

player_names = []

# Find the table containing player information
player_table = soup.find('table', class_='wikitable')

# Iterate over each row in the table
for row in player_table.find_all('tr')[1:]:  # Skip the header row
    # Extract the name from the first column
    name_cell = row.find('td')
    if name_cell:
        name = name_cell.get_text(strip=True)
        player_names.append(name)

# Print the collected player names
for name in player_names:
    print(name)