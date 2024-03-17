import requests


def getContracts(address, APIKEY):
    api= f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={address}&apikey={APIKEY}"
    data= requests.get(api)
    if(data.status_code==200):
        responsedata= data.json()
        response= responsedata["result"]
        print(len(response))
        return len(response)
    else:
        print(f"Error is {data.status_code}")



