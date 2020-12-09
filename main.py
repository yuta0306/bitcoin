from fetch import *

params = {'pair': 'btc_jpy', 'limit': 100}
res = fetch('https://coincheck.com/api/trades', params=params)
print(res)
data = tinify_response(res, str)

print(data)