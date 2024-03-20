from covalent import CovalentClient
import json

def getTaikoBalance(key, address):
    c = CovalentClient(key)
    wallet_address=address
    b = c.balance_service.get_token_balances_for_wallet_address("taiko-katla-testnet", wallet_address)
    if not b.error:
        balance_data = b.data
        print("Balance:", balance_data.items[0].balance)
        return balance_data.items[0].balance
        
    else:
        print(b.error_message)

