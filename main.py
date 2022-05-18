from eth_account import Account
import json
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"))

receiver = "0x683bF3D4232a994A2CA152CAE1320bd0f7Ae1b16"
PRIVATEKEY = "b3787be5404352b7d3c49b10baf407c6069dbf7d700fbebb02ed96b15474ef11"
receiver_address = w3.toChecksumAddress(receiver)
abi = json.load(open("ERC20.json"))
creator_account = w3.eth.account.privateKeyToAccount(PRIVATEKEY)
CONTRACTADDRESS = "0x84cc2a2C1db5cD35F7cE2805656F91a6d45E8eDC"
contract = w3.eth.contract(address=CONTRACTADDRESS, abi=abi)
HOLDERCOUNT = 100000
def make_wallets():
    wallets = []
    holder_index = 0
    while holder_index < HOLDERCOUNT:
        acct = Account.create('KEYSMASH FJAFJKLDSKF7JKFDJ 1530')
        holder_index += 1
        wallets.append(acct.address)
    return wallets
def transfer(reception,amount):
    params = {
                "from": creator_account.address,
                "value": "0x0",
                'gasPrice': w3.eth.gasPrice,
                "gas": 200000,
                "nonce": w3.eth.getTransactionCount(creator_account.address)
            }
    transaction = contract.functions.transfer(reception, amount).buildTransaction(params)
    signed_tx = w3.eth.account.sign_transaction(transaction, private_key=PRIVATEKEY)
    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx = txn_hash.hex()
    print(tx)
    w3.eth.wait_for_transaction_receipt(txn_hash)
    print(f"{reception}: {contract.functions.balanceOf(reception).call()}")
if __name__ == '__main__':
    wallets = make_wallets()
    for wallet in wallets:
        transfer(wallet,1000000000)