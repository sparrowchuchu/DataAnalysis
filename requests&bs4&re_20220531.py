#
import requests
from bs4 import BeautifulSoup
import re

resp=requests.get('http://bit.ly/3gkZaJa')
soup=BeautifulSoup(resp.text,'lxml')

titles=soup.find_all(['h1','h2','h3','h4','h5','h6'])
for title in titles:
    print(title.text.strip())
# 利用regex
for title in soup.find_all(re.compile('h[1-6]')):
    print(title.text.strip())

imgs=soup.find_all('img')
for img in imgs:
    if 'src' in img.attrs:
        if img['src'].endswith('.png'):
            print(img['src'])
# 利用regex
for img in soup.find_all('img',{'src':re.compile('\.png$')}):
    print(img['src'])
#
imgs=soup.find_all('img')
for img in imgs:
    if 'src' in img.attrs:
        if 'beginner' in img['src'] and img['src'].endswith('.png'):
            print(img['src'])
# 利用regex
for img in soup.find_all('img',{'src':re.compile('beginner.*\.png$')}):
    print(img['src'])







    