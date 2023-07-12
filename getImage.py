import requests
import csv
import pandas as pd

df = pd.read_csv("metadata.csv")
print(df)
for tokenID in range(len(df)):
    token_url = df['image'][tokenID]
    if token_url[:7] == 'ipfs://':
        url = 'https://ipfs.io/ipfs/' + token_url[7:]
        # print(url)
    else:
        url = token_url
    r = requests.get(url, allow_redirects=True)
    imageFileName = df['name'][tokenID]
    open("./images/" + str(tokenID) + ".png", 'wb').write(r.content)