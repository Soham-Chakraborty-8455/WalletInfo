import requests


def getTransactions(address, APIKEY):
    api= f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey={APIKEY}"
    data= requests.get(api)
    if(data.status_code==200):
        responsedata= data.json()
        response= responsedata["result"]
        cnt=0
        for i in response:
            if i["isError"]=="0":
                cnt= cnt+1
        print(cnt)
        return cnt
    else:
        print(f"Error is {data.status_code}")



