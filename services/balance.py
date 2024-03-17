import requests


def getBalance(address, APIKEY):
    api= f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={APIKEY}"
    data= requests.get(api)
    if(data.status_code==200):
        responsedata= data.json()
        response= responsedata["result"]
        print(response)
        return int(response)
    else:
        print(f"Error is {data.status_code}")



