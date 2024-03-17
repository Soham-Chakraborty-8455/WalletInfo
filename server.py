from flask import Flask, request, jsonify
import os
from services.balance import getBalance
from services.contracts import getContracts
from services.transactions import getTransactions
from services.volume import getVolume

app = Flask(__name__)

APIKEY= os.getenv("APIKEY")


@app.route('/api/wallet-info/<address>', methods=["GET"])
def hello(address):
    if request.method == 'GET':
        balancez= getBalance(address, APIKEY)
        tranactionz= getTransactions(address, APIKEY)
        contractz= getContracts(address, APIKEY)
        volumez= getVolume(address, APIKEY)
        return jsonify({
            "Balance (in wei)": balancez,
            "Transactions": tranactionz,
            "Contracts": contractz,
            "Volume (in wei)": volumez
        })