import sndhdr
from typing import ItemsView
import requests,json
from snkr import Snkr

snkrs_list = []

def search(query,list = []):
    url = f'https://stockx.com/api/browse?_search={query}'

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

    html = requests.get(url=url, headers=headers)
    output = json.loads(html.text)

    
    items = int(len(output['Products']))
    for item in range(0,items):
        list.append( 
        Snkr(output["Products"][item]["name"],
        output["Products"][item]["shoe"],
        output["Products"][item]["media"]["imageUrl"],
        output["Products"][item]["media"]["smallImageUrl"],
        output["Products"][item]["media"]["thumbUrl"],
        output["Products"][item]["retailPrice"],
        output["Products"][item]["year"],
        output["Products"][item]["market"]["lowestAsk"],
        output["Products"][item]["market"]["lowestAskSize"],
        output["Products"][item]["market"]["highestBidSize"],
        output["Products"][item]["market"]["deadstockRangeLow"],
        output["Products"][item]["market"]["deadstockRangeHigh"],
        output["Products"][item]["market"]["averageDeadstockPrice"],
        output["Products"][item]["market"]["lastSale"],
        output["Products"][item]["market"]["lastSaleSize"],
        output["Products"][item]["market"]["salesLast72Hours"],
        ))
    



search("nike city market",snkrs_list)

for snkrs in snkrs_list:
    print(snkrs.name,snkrs.shoe,snkrs.imageUrl ,snkrs.smallImageUrl ,snkrs.thumbUrl ,snkrs.retailPrice ,snkrs.year ,snkrs.lowestAsk ,
    snkrs.lowestAskSize ,snkrs.highestBidSize ,snkrs.deadstockRangeLow ,snkrs.deadstockRangeHigh ,snkrs.averageDeadstockPrice ,snkrs.lastSale ,
    snkrs.lastSaleSize,snkrs.salesLast72Hours)
    print("\n")
