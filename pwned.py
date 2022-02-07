import requests
from bs4 import BeautifulSoup

page = requests.get("https://haveibeenpwned.com/")
soup = BeautifulSoup(page.content, "html.parser")
print(soup.find('p'))