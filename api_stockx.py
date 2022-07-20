from distutils.command.build_scripts import first_line_re
import sndhdr
from typing import ItemsView
import requests
import jsonpickle,json
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
        Snkr(
        str(output["Products"][item]["name"]),
        str(output["Products"][item]["shoe"]),
        str(output["Products"][item]["media"]["imageUrl"]),
        str(output["Products"][item]["media"]["smallImageUrl"]),
        str(output["Products"][item]["media"]["thumbUrl"]),
        str(output["Products"][item]["retailPrice"]),
        str(output["Products"][item]["year"]),
        str(output["Products"][item]["market"]["lowestAsk"]),
        str(output["Products"][item]["market"]["lowestAskSize"]),
        str(output["Products"][item]["market"]["highestBidSize"]),
        str(output["Products"][item]["market"]["deadstockRangeLow"]),
        str(output["Products"][item]["market"]["deadstockRangeHigh"]),
        str(output["Products"][item]["market"]["averageDeadstockPrice"]),
        str(output["Products"][item]["market"]["lastSale"]),
        str(output["Products"][item]["market"]["lastSaleSize"]),
        str(output["Products"][item]["market"]["salesLast72Hours"]),
        str(output["Products"][item]["urlKey"]),
        ))
    

jsondata = ""

search("Jordan 1 Retro High OG Bleached Coral",snkrs_list)
first_object = True
for snkr in snkrs_list:
    if(first_object):
        first_object = False
        jsondata = jsondata + jsonpickle.encode(snkr, unpicklable=False)
    else:
        jsondata = jsondata + "," + jsonpickle.encode(snkr, unpicklable=False)
print('''{ "snkrs" : [''')
print(jsondata)
print(''']}''')




