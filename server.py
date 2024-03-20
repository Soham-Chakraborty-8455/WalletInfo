from flask import Flask, request, jsonify
import os
import asyncio
from berachain.balance import getBalance
from berachain.contracts import getContracts
from berachain.transactions import getTransactions
from berachain.volume import getVolume
from taiko.balance import getTaikoBalance
from taiko.transactions import getTaikoTransaction
from taiko.volume import getTaikoVolume
from mode.balance import getModeBalance
from mode.transactions import getModeTransaction
from mode.volume import getModeVolume

app = Flask(__name__)

APIKEY= os.getenv("APIKEY")
KEY= os.getenv("KEY")

@app.route('/api/wallet-info/<address>', methods=["GET"])
def hello(address):
    if request.method == 'GET':
        balanceBera= getBalance(address, APIKEY)
        tranactionBera= getTransactions(address, APIKEY)
        contractBera= getContracts(address, APIKEY)
        volumeBera= getVolume(address, APIKEY)
        balanceTaiko= getTaikoBalance(KEY, address)
        tranactionTaiko= asyncio.run(getTaikoTransaction(KEY, address))
        volumeTaiko= asyncio.run(getTaikoVolume(KEY, address))
        balanceMode= getModeBalance(KEY, address)
        tranactionMode= asyncio.run(getModeTransaction(KEY, address))
        volumeMode= asyncio.run(getModeVolume(KEY, address))
        return jsonify({
            "address": address,
            "Berachain":{
            "Balance (in wei)": balanceBera,
            "Transactions": tranactionBera,
            "Contracts": contractBera,
            "Volume (in wei)": volumeBera
            },
            "Taiko":{
                "Balance(in wei)": balanceTaiko,
                "Transactions": tranactionTaiko,
                "Volume (in wei)": volumeTaiko
            },
            "Mode":{
                "Balance(in wei)": balanceMode,
                "Transactions": tranactionMode,
                "Volume (in wei)": volumeMode
            }
        })
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')