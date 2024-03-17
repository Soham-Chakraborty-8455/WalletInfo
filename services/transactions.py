import requests
import json

def getTransactions(address, APIKEY):
    url = "https://docs-demo.bera-artio.quiknode.pro/"
    payload = json.dumps({
    "method": "eth_getTransactionCount",
    "params": [
        address,
        "latest"
    ],
    "id": 1,
    "jsonrpc": "2.0"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code==200):
        data= response.json()
        print(int(data["result"], 16))
        return int(data["result"], 16)
    else:
        return f"Error: {response.status_code}"



