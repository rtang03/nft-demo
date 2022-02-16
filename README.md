# nft-demo
PoC - NFT creation for teaching


Developer Notes:

brownie run scripts/deploy_and_create.py --network rinkeby
brownie run scripts/simple_collectible/deploy_and_create.py
brownie run scripts/advanced_collectible/deploy_and_create.py
brownie run scripts/advanced_collectible/deploy_and_create.py --network rinkeby
brownie run scripts/advanced_collectible/create_collectible.py --network rinkeby
brownie test -k test_can_create_advanced_collectible
brownie test -k test_can_create_advanced_collectible_integration --network rinkeby

https://testnets.opensea.io/assets/0xf906a835b6d28069f28cd53f9647b1919c8fbf9b/0
https://github.com/juanfranblanco/vscode-solidity#using-a-different-version-of-the-solidity-compiler

final run
brownie run scripts/advanced_collectible/deploy_and_create.py --network rinkeby
brownie run scripts/advanced_collectible/create_collectible.py --network rinkeby
brownie run scripts/advanced_collectible/create_metadata.py --network rinkeby
brownie run scripts/advanced_collectible/set_tokenuri.py --network rinkeby
