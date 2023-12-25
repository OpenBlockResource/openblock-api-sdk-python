import sys

import config

sys.path.append("../../")
from openblock_api_sdk_python.client import CompanyWalletClient

client = CompanyWalletClient(
    api_key=config.API_KEY, secret=config.API_SECRET, server=config.SERVER
)

resp = client.get_wallet_info()

if resp.status_code == 200:
    print(resp.json())
else:
    print(resp.text)
