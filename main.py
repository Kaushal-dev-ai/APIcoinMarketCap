import requests
import json

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=c4404bfc-6ffe-4b81-a03f-f162a694c1f3")


api = json.loads(api_request.content)

#print(api["data"][0]["symbol"])
#print(api["data"][0]["quote"]["USD"]["price"])

#portfolio dictionary


coins = ["BTC", "ETH"]
# creating a portfolio of my with what coin name , no of coin i bought
# and price

coins = [
  {
    "symbol":"BTC",
    "amount_owned":2,
    "price_per_coin":3200
  },
  {
    "symbol":"ETH",
    "amount_owned":100,
    "price_per_coin":2.05
  }
]

total_pl = 0
# create a list & understanting loop

for i in range(0, 5):
    for coin in coins:
      if api["data"][i]["symbol"] == coin["symbol"]:
        #calculating profit and loss
        total_paid = coin["amount_owned"] * coin["price_per_coin"]
        current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
        pl_percoin  = api["data"][i]["quote"]["USD"]["price"] -  coin["price_per_coin"]
        total_pl_coin = pl_percoin * coin ["amount_owned"]
        
        total_pl = total_pl + total_pl_coin
        #print(api["data"][0]["quote"]["USD"]["price"])

        print(api["data"][i]["name"]+" - " + api["data"][i]["symbol"])
        print("price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
        print("number of coin:", coin["amount_owned"])
        print("Total Amount paid", "${0:.2f}".format(total_paid))
        print("Current Value:", "${0:.2f}".format(current_value))
        print("P/L Per Coin:", "${0:.2f}".format(pl_percoin))
        print("Total P/L with Coin", "${0:.2f}".format(total_pl_coin))
        print("----------------------")
        
print("Total P/L for Portfolio", "${0:.2f}".format(total_pl))
        



