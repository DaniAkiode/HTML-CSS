import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Real_Madrid_CF_players"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')

for link in links:
    print(link.get('href'))


#https://chat.openai.com/share/6ec9149a-b6e1-4dd8-943a-de60ff070611