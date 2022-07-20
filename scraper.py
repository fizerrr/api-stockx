from turtle import clear
import requests
from bs4 import BeautifulSoup
import re
import os.path,time



headers = {
        'accept': 'application/json',
        'accept-encoding': 'utf-8',
        'accept-language': 'en-GB,en;q=0.9',
        'app-platform': 'Iron',
        'referer': 'https://stockx.com/en-gb',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
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
        source = BeautifulSoup(requests.get("https://stockx.com/sneakers?page=" + convert_page_to_text, headers=headers).content,"lxml")
        snkrs = source.find_all("div", {"class": "css-1ibvugw-GridProductTileContainer"})
        for snkr in snkrs:
            for link in snkr.find_all('a', attrs={'href': re.compile("^/")}):
                snkrs_links.append( link.get('href') )

    f = open(filepath_links, "a")

    for snkr in snkrs_links:
        f.write(base_stocx_link + snkr + "\n")

    f.close()


#print(snkrs_links)

source2 =  BeautifulSoup(requests.get("https://stockx.com/air-jordan-1-retro-high-og-stage-haze", headers=headers).content,"lxml")
print(source2.text)








