# btcsignature
btcsignature is a command line tool for signing bitcoin transaction data offline easily and securely.

Install btcsignature and all dependencies in one line:

$ pip install btcsignature

The tool currently has one functionality only: to sign a single bitcoin transaction hex with a single private key.

to run the signing script simply execute command:

$ sign-offline

*to ensure security the script will exit before signing if it notices an internet connection so you must be offline

The script will prompt the user for a private key and then the transaction hex data to sign.
If the private key matches the address for all transaction inputs the script will succeed, the terminal will reset, and your signed transaction hex will be output and ready for broadcast. 

Multisig and other functionalities are soon to come in future versions.

Security is obviously the main concern in signing transactions. This does not claim to be the highest security option (see hardware wallets and other




