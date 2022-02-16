from brownie import AdvancedCollectible
from scripts.helpful_scripts import fund_with_link, get_account
from web3 import Web3


def main():
    account = get_account()
    advancedCollectible = AdvancedCollectible[-1]
    fund_with_link(advancedCollectible.address, amount=Web3.toWei(0.1, "ether"))
    creation_transaction = advancedCollectible.createCollectible({"from": account})
    creation_transaction.wait(1)
    print("Collectible created!")
