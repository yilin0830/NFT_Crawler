import requests
import json
import pandas as pd
import time

IPFSHash = "QmSh6tpsw2fEA48y4eyWmcYnBcKgxoZhYSCf4iXJuPoZS8" # TBD
metadata_dict = dict()
tokenIds = [x for x in range(0, 2)]
for tokenId in tokenIds:
    #print("tokenId = ", tokenId)
    url = "https://ipfs.io/ipfs/"+ IPFSHash + "/" + str(tokenId) + ".json"
    response = requests.get(url, allow_redirects=True)
    #print(response.text)

    j = json.loads(response.text)
    # Writing to .json
    with open("./jsons/" + str(tokenId) + ".json", "w") as outfile:
        outfile.write(response.text)
    #print(j)
    name = j['name']
    description = j['description']
    image = j['image']
    attributes = j['attributes']
    #print(properties)
     
    metadata_dict[tokenId] = dict()
    metadata_dict[tokenId]
    for i in range(len(attributes)):
        metadata_dict[tokenId]['tokenId'] = tokenId
        metadata_dict[tokenId]['name'] = name
        metadata_dict[tokenId]['description'] = description
        metadata_dict[tokenId]['image'] = image
        metadata_dict[tokenId][attributes[i]['trait_type']] = attributes[i]['value']
    time.sleep(1) # 太快會被擋

df = pd.DataFrame(metadata_dict)
df = df.T
print(df)
df.to_csv("metadata.csv", index = False)