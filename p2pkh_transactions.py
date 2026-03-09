from bitcoinrpc.authproxy import AuthServiceProxy

RPC_USER = "cs_216_assignment2_rpc"
RPC_PASSWORD = "cs_216"
RPC_PORT = 18443

rpc = AuthServiceProxy(f"http://{RPC_USER}:{RPC_PASSWORD}@127.0.0.1:{RPC_PORT}")

wallet_name = "testwallet"

wallets = rpc.listwallets()

if wallet_name not in wallets:
    try:
        rpc.loadwallet(wallet_name)
    except:
        rpc.createwallet(wallet_name)

rpc = AuthServiceProxy(f"http://{RPC_USER}:{RPC_PASSWORD}@127.0.0.1:{RPC_PORT}/wallet/{wallet_name}")

print("Wallet loaded")

A = rpc.getnewaddress("", "legacy")
B = rpc.getnewaddress("", "legacy")
C = rpc.getnewaddress("", "legacy")

print("Address A:", A)
print("Address B:", B)
print("Address C:", C)

txid_fund = rpc.sendtoaddress(A, 10)

print("Funding TX:", txid_fund)

mine_addr = rpc.getnewaddress()
rpc.generatetoaddress(1, mine_addr)

utxos = rpc.listunspent()

utxoA = None
for u in utxos:
    if u["address"] == A:
        utxoA = u
        break

txidA = utxoA["txid"]
voutA = utxoA["vout"]
amountA = utxoA["amount"]

print("UTXO A:", txidA)

fee = 0.001
amount_to_B = round(float(amountA) - fee, 8)

inputs = [{"txid": txidA, "vout": voutA}]
outputs = {B: amount_to_B}

raw_tx = rpc.createrawtransaction(inputs, outputs)

print("Raw TX A->B:", raw_tx)

signed_tx1 = rpc.signrawtransactionwithwallet(raw_tx)

print("Signed TX 1:", signed_tx1)

decoded = rpc.decoderawtransaction(signed_tx1['hex'])

print("Decoded Transaction:")
print(decoded)

script_pubkey = decoded["vout"][0]["scriptPubKey"]

print("Locking Script (ScriptPubKey):")
print(script_pubkey)

txid_AB = rpc.sendrawtransaction(signed_tx1["hex"])

print("TXID A->B:", txid_AB)

rpc.generatetoaddress(1, mine_addr)

utxos = rpc.listunspent()

utxoB = None
for u in utxos:
    if u["address"] == B:
        utxoB = u
        break

txidB = utxoB["txid"]
voutB = utxoB["vout"]
amountB = utxoB["amount"]

amount_to_C = round(float(amountB) - fee, 8)

inputs2 = [{"txid": txidB, "vout": voutB}]
outputs2 = {C: amount_to_C}

raw_tx2 = rpc.createrawtransaction(inputs2, outputs2)

print("Raw TX B->C:", raw_tx2)

signed_tx2 = rpc.signrawtransactionwithwallet(raw_tx2)

print("Signed TX 2:", signed_tx2)

decoded2 = rpc.decoderawtransaction(signed_tx2["hex"])

print("Decoded B->C:")
print(decoded2)

scriptSig = decoded2["vin"][0]["scriptSig"]

print("ScriptSig (Unlocking Script):")
print(scriptSig)

txid_BC = rpc.sendrawtransaction(signed_tx2["hex"])

print("TXID B->C:", txid_BC)