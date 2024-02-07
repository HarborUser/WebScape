import re
from unowebsite import *
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from html.parser import HTMLParser
import time

# Replace 'your_url_here' with the actual URL you want to scrape
link_list = []


extended_url = []


with open("UNO_link_new_dataset4.txt", "w", encoding='utf-8') as f:

    for i in range(len(modified_list)):#link_list
        
        new_url = modified_list[i]

        responses = requests.get(new_url)
        soup = BeautifulSoup(responses.text, 'html.parser')

        i += 1
        #"a", "h3", "href", "span"

        topmost_id = soup.find('div', id='template-a')
    
        if topmost_id:

            for tag in topmost_id.find_all(["p","li","h2","a"]):
                text = tag.get_text(strip=True)
            
                f.write(f"{text}\n")
        # for data in soup.findAll(["h3","p","a","li"]):
        #     #for x in soup.find("div", attrs="col").findChildren("p"):
        #     href = data.get('href')
        #     extended_url.append(href)
            
        #     data1 = data.text
        #     f.write(f"{new_url}")
           
        #     f.write(f' {data1} \n')
        #     #print(f'{data} link: {href}')


