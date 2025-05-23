import requests

def check_eth_balance(address):
    url = f"https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": "YourApiKeyToken"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] == "1":
        balance = int(data["result"]) / 10**18
        print(f"Balance for {address}: {balance:.6f} ETH")
    else:
        print("Error:", data["message"])

if __name__ == "__main__":
    eth_address = input("Enter Ethereum address: ").strip()
    check_eth_balance(eth_address)
