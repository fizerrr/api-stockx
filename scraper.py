from turtle import clear
import requests
from bs4 import BeautifulSoup
import re
import os.path,time



headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0',
    'Accept-Language': 'en-US,en;q=0.5'
}



snkrs_links = []

base_stocx_link = "https://stockx.com"

filepath_links = "links.txt"


if os.path.exists(filepath_links):
    print('The file  exists')
    with open(filepath_links) as file:
        snkrs_links = file.readlines()   
else:
    print('The file is creating')
    for page in range(1,26):
        convert_page_to_text = str(page)
        source = BeautifulSoup(requests.get("https://stockx.com/sneakers?page=" + convert_page_to_text, headers=headers, cookies=cookies).content,"lxml")
        snkrs = source.find_all("div", {"class": "css-1ibvugw-GridProductTileContainer"})
        for snkr in snkrs:
            for link in snkr.find_all('a', attrs={'href': re.compile("^/")}):
                snkrs_links.append( link.get('href') )

    f = open(filepath_links, "a")

    for snkr in snkrs_links:
        f.write(base_stocx_link + snkr + "\n")

    f.close()


#print(snkrs_links)








