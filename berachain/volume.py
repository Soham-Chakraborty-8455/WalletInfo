import requests


def getVolume(address, APIKEY):
    api= f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey={APIKEY}"
    data= requests.get(api)
    if(data.status_code==200):
        responsedata= data.json()
        response= responsedata["result"]
        vol=0
        for i in response:
            vol+= int(i["value"])
        print(vol)
        return vol
    else:
        print(f"Error is {data.status_code}")



