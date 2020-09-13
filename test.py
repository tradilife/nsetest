
import requests
import pandas as pd
import json
from nsepython import *


print(fnolist())
print(nse_optionchain_scrapper('NIFTY'))
oi_data, ltp, crontime = oi_chain_builder("NIFTY")
print(oi_data)
print(ltp)
print(crontime)
