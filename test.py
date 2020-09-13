"""import os
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, os.path.join(sys.path[0], '..'))
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'oi_data')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)"""
import requests
import pandas as pd
import json
from nsepython import *
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
}
response = requests.get('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O',headers=headers).content

"""xmr = json.loads(response)
df = pd.json_normalize(xmr,'data')
print(df)"""
#df.head(10)

#print (xmr['symbol']['lastPrice'])

#rowlist=[]
#for x in xmr['data']:
    #symbol = x['symbol']
    #price =x['lastPrice']
    #rowlist.append(symbol)
    #rowlist.append(price)
    #print(symbol,price)
#print(rowlist)
#df =pd.DataFrame(rowlist)
#print(df)

print(fnolist())
print(nse_optionchain_scrapper('NIFTY'))
oi_data, ltp, crontime = oi_chain_builder("NIFTY")
print(oi_data)
print(ltp)
print(crontime)
