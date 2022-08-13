import time
import requests
import json
import csv

time_stamp = int(time.time())
print(f"Now timestamp: {time_stamp}")

request_link = f"https://web-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical?convert=USD&slug=bitcoin&time_end={time_stamp}&time_start=1367107200"
print("Request link: " + request_link)
r = requests.get(url = request_link)

content = json.loads(r.content)

quoteList = content['data']['quotes']

start = False
with open('BTC.csv','w' ,encoding='utf8',newline='') as f:
    csv_write = csv.writer(f)
    csv_head = ["Date", "Open", "High", "Low", "Close", "Price", "Volume", "Market Cap"]
    csv_write.writerow(csv_head)

    for quote in quoteList:
        quote_date = quote["time_open"][:10]
        quote_open = "{:.2f}".format(quote["quote"]["USD"]["open"])
        quote_high = "{:.2f}".format(quote["quote"]["USD"]["high"])
        quote_low = "{:.2f}".format(quote["quote"]["USD"]["low"])
        quote_price = "{:.2f}".format(quote["quote"]["USD"]["close"])
        quote_volume = "{:.2f}".format(quote["quote"]["USD"]["volume"])
        quote_market_cap = "{:.2f}".format(quote["quote"]["USD"]["market_cap"])

        if quote_date == "2017-07-01":
            start = True
        if start == True:
            csv_write.writerow([quote_date, quote_open, quote_high, quote_low, quote_price, quote_volume, quote_market_cap])
        if quote_date == "2022-06-30":
            start = False

print("Done")