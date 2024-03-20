from covalent import CovalentClient
import asyncio

async def getTaikoTransaction(Key, address):
    c = CovalentClient(Key)
    try:
        cnt=0
        wallet_address= address
        async for res in c.transaction_service.get_all_transactions_for_address("taiko-katla-testnet", wallet_address):
            print(res)
            cnt= cnt+1
        print(cnt)
        return cnt
    except Exception as e:
        print(e)
# asyncio.run(main())
