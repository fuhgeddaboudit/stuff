import requests
from bs4 import BeautifulSoup

r = requests.get('http://ipchicken.com')
html = r.text
soup = BeautifulSoup(html, 'html.parser')

print(soup.b.get_text().split('\n')[1])
#print(BeautifulSoup(requests.get('http://ipchicken.com').text,'html.parser').b.get_text().split('\n')[1])




