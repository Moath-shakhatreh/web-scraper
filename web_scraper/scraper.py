import requests
from  bs4 import BeautifulSoup
import json

URL = 'https://www.reddit.com/'
page = requests.get(URL)
print(page.content)

soup = BeautifulSoup(page.content,'html.parser')