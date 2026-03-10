# CS 216 – Assignment 2

This repository contains the implementation and analysis for **Assignment 2 of the CS 216 course**.
The assignment focuses on understanding Bitcoin transactions, specifically **P2PKH (legacy)** and **P2SH-P2WPKH (SegWit)** transactions, along with their structure and validation process.

---

## Team Kryptonite

| Name | Roll Number |
|:--- |:--- |
| **Aarush Bindod** | 240051001 |
| **Abhiroop Gohar** | 240051002 |
| **Kartikey Raghav** | 240021008 |
| **Tanishq Dhari** | 240001072 |

---

## Repository Structure

```
.
├── part1
│   ├── p2pkh_debugger_video.mp4
│   ├── p2pkh_transactions_output.txt
│   └── p2pkh_transactions.py
│
├── part2
│   ├── p2sh_segwit_debugger_video.mp4
│   ├── p2sh_segwit_transactions_output.txt
│   └── p2sh_segwit_transactions.py
│
├── part_3_comparison.txt
├── setup_outputs.txt
└── .gitignore
```

---

## Part 1 – P2PKH Transactions

Located in the **`part1`** folder.

This section demonstrates the creation and analysis of **legacy P2PKH transactions**.

Files included:

* **`p2pkh_transactions.py`**
  Python script used to generate and process P2PKH transactions.

* **`p2pkh_transactions_output.txt`**
  Contains:

  * The formatted output produced by the script
  * A detailed explanation of how the transaction was constructed
  * Step-by-step dissection of the transaction structure
  * An explanation of the locking and unlocking scripts

* **`p2pkh_debugger_video.mp4`**
  Screen recording demonstrating the script execution and script verification on an online platform.

---

## Part 2 – P2SH-P2WPKH (SegWit) Transactions

Located in the **`part2`** folder.

This section demonstrates the creation and analysis of **SegWit-based transactions (P2SH-P2WPKH)**.

Files included:

* **`p2sh_segwit_transactions.py`**
  Python script used to generate SegWit transactions.

* **`p2sh_segwit_transactions_output.txt`**
  Contains:

  * The formatted output produced by the script
  * A detailed breakdown of the transaction structure
  * Explanation of SegWit witness data
  * Analysis of how unlocking and locking scripts are validated

* **`p2sh_segwit_debugger_video.mp4`**
  Screen recording showing the verification of the script execution.

---

## Part 3 – Comparison

The file **`part_3_comparison.txt`** contains the comparison between:

* Legacy **P2PKH transactions**
* **P2SH-P2WPKH SegWit transactions**

This section explains:

* Differences in transaction structure
* Differences in script execution
* Transaction size comparison
* Benefits of SegWit transactions

---

## Setup Instructions

`Assumption: The bitcoind and bitcoin-cli commands are configured and run in the terminal(or command prompt)`

Run the following commands to give a 50BTC balance to an address in a wallet which we name as **testwallet**.
* ```bitcoind -regtest -daemon``` - To start the bitcoin core
* ```bitcoin-cli -regtest createwallet "testwallet"``` - To create a wallet named testwallet and load it
* ```address=$(bitcoin-cli -regtest getnewaddress)``` - Generate a new address linked to the loaded wallet and store it in the `address` variable
* ```bitcoin-cli -regtest generatetoaddress 101 "$address"``` - Mine a block to the address generated earlier with 101 confirmations

*Note: Make sure that file `bitcoin.conf` has the configuration as given in the assignment. The rpcusername is **cs_216_assignment2_rpc**
and the rpcpassword is **cs_216**.*

*We use only the **python-bitcoinrpc** library. The same has been stated in `requirements.txt`*

---


## Setup Outputs

The file **`setup_outputs.txt`** contains outputs related to the setup and configuration used for running the scripts.

---

## Note on Script Verification (btcdeb)

The assignment originally required the use of **btcdeb (Bitcoin Script Debugger)** to test the scripts.

However, due to issues running `btcdeb` locally, the scripts were instead tested using an **online Bitcoin Script debugger**.

The **link to the online tool is included inside the respective output files**, and **screen recordings of the script execution have been provided** in the `.mp4` files for verification.

---

## Summary

* **Part 1** implements and analyzes **P2PKH transactions**
* **Part 2** implements and analyzes **P2SH-P2WPKH SegWit transactions**
* **Part 3** compares the two transaction types
* Output files include **both raw script outputs and detailed explanations** of the transaction structure and validation process.
