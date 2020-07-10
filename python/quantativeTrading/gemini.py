###### GEMINI 行情接口 ##########
## https://api.gemini.com/v1/pubticker/:symbol

import json
import requests

gemini_tocker = 'https://api.gemini.com/v1/pubticker/{}'

symbol = 'btcusd'
btc_data = requests.get(gemini_tocker.format(symbol)).json()
print(json.dumps(btc_data, indent = 4))



