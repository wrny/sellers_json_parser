import json
import requests
import pandas as pd

url_dict = {"https://cdn.indexexchange.com/sellers.json": 'IndexExchange',
           "https://cdn-source.spotxchange.com/media/cdn/cdn/iab/sellers.json": 'SpotX',
           "https://cdn.pubmatic.com/sellers/data/sellers.json": "Pubmatic",
           "https://smartadserver.com/sellers.json": "SmartAdServer"}

columns = ['seller_id', 'is_confidential', 'directness', 'name', 'domain', 'comment', 'ext', 'seller_type']

ordered_columns = ['comment', 'directness', 'domain', 'ext', 'is_confidential', 'name', 'seller_id', 'seller_type']

def order_dictionary(dictionary):
    """Sorts dictionary alphabetically"""
    sorted_keys = sorted(list(dictionary.keys()))
    sorted_values = [dictionary[key] for key in sorted_keys]
    new_dict = dict(zip(sorted_keys, sorted_values))
    return new_dict

def make_upper(string):
    return string.upper()

df_container = []

for url in url_dict.keys():
    print(f"Fetching {url_dict[url]}...")
    r = requests.get(url)
    j = json.loads(r.text)
    sellers = j['sellers']

    for seller in sellers:
        for c in columns:
            if c not in seller.keys():
                seller[c] = ""

        seller = order_dictionary(seller)

        # print(seller)
        seller_values = list(seller.values())
        exchange_name = url_dict[url]
        data = [tuple([exchange_name] + seller_values)]
        # print(data)
        df = pd.DataFrame(data)
        df_container.append(df)

df_concat = pd.concat(df_container, axis=0)
df_concat.columns = ['exchange']+ordered_columns
df_concat.index = range(len(df_concat))
df_concat = df_concat[['exchange', 'seller_id', 'name', 'domain', 'seller_type', 'comment', 'directness', 'is_confidential', 'ext']]

df_concat['seller_type'] = df_concat['seller_type'].apply(lambda x: make_upper(x))

df_concat.to_csv('sellers_json.csv', index=False)