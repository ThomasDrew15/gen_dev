import requests
import pprint
import json

APIKEY = "sk_live_JuULy2Hj2JHhzouB5CVyUIFt"
url = "https://api.octopus.energy/v1/products/AGILE-18-02-21/electricity-tariffs/E-1R-AGILE-18-02-21-L/standard-unit-rates/"
r = requests.get(url, auth=(APIKEY, ""))
json_string = json.dumps(r.json(), indent=3)

json_dict = json.loads(json_string)

results = json_dict["results"]
end = len(results)

prices = []
times_from = []
times_to = []

for item in results:
    prices.append(item["value_inc_vat"])
    times_from.append(item["valid_from"])
    times_to.append(item["valid_to"])


yesterdays_prices = zip(prices, times_from, times_to)
price_zip = dict(zip(prices, times_from))


pprint.pprint(sorted(price_zip.items(), key=lambda x: x[1]))
# print(list(yesterdays_prices))
