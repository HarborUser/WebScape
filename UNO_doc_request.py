import re

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from html.parser import HTMLParser

# Replace 'your_url_here' with the actual URL you want to scrape
url = 'https://www.unomaha.edu/college-of-information-science-and-technology/'
link_list = []
response = requests.get(url, timeout=5)
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a', attrs={'href':re.compile(("https://www.unomaha.edu/college-of-information-science-and-technology/"))}):

    href = link.get('href')
    text = link.text
    link_list.append(href)
    #for link2 in soup.select("a[href$='.pdf']"):
        #link_list.append(link2)

    for link2 in soup.findAll('a',attrs={'href': re.compile(".pdf")}):
        href = link2.get('href')
        link_list.append(href)

print(link_list)

with open("UNO_data2.txt", "w", encoding='utf-8') as f:

    for i in range(len(link_list)):
        new_url = link_list[i]
        print(new_url)
        responses = requests.get(new_url)
        soup = BeautifulSoup(responses.text, 'html.parser')

        i += 1
        for data in soup.findAll('p'):
            href = data.get('href')
            data = data.text
            print(data)

            f.write(f'{data}')
            #print(f'{data} link: {href}')

