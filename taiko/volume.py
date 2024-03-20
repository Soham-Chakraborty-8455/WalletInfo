from covalent import CovalentClient
import asyncio

async def getTaikoVolume(Key, address):
    c = CovalentClient(Key)
    total_transaction_value = 0

    try:
        wallet_address = address
        async for res in c.transaction_service.get_all_transactions_for_address("taiko-katla-testnet", wallet_address):
            print(res)
            total_transaction_value= total_transaction_value+ res.value
        print("Total Transaction Value: ", total_transaction_value)
        return total_transaction_value
    except Exception as e:
        print(e)

# asyncio.run(main())
