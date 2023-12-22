import re


import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from html.parser import HTMLParser
import time


# Replace 'your_url_here' with the actual URL you want to scrape
link_list = []
pdf_list =[]


url = 'https://www.unomaha.edu/college-of-information-science-and-technology/'
while url == 'https://www.unomaha.edu/college-of-information-science-and-technology/':
    try:
        response = requests.get(url, timeout=5)
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        continue

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
        pdf_list.append(href)

print(link_list)

with open("UNO_dataset.txt_master2_1", "w", encoding='utf-8') as f:

    for i in range(len(link_list)):
        new_url = link_list[i]

        responses = requests.get(new_url)
        soup = BeautifulSoup(responses.text, 'html.parser')

        i += 1
        #for data in soup.findAll(["h3","p","li","h6"]):
        for dat2 in soup.find_all('div', attrs={'id':'main-content'}):

            data = dat2.get_text()

            for link in soup.find_All('a', attrs={'href': re.compile(".pdf")}):
                href = link.get("href")


                f.write(f"{data}: {href}")









            #print(f'{data} link: {href}')

