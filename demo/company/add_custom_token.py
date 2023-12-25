import sys

import config

sys.path.append("../../")
import openblock_api_sdk_python.param.company_param as company_param
from openblock_api_sdk_python.client import CompanyWalletClient

client = CompanyWalletClient(
    api_key=config.API_KEY, secret=config.API_SECRET, server=config.SERVER
)

token_data = company_param.TokenDataParam()
token_data.address = "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619"
token_data.symbol = "WETH"
token_data.decimals = 18

params = company_param.AddCustomTokenParam()
params.chain_name = ""
params.token_data = token_data

resp = client.add_custom_token(params)

if resp.status_code == 200:
    print(resp.json())
else:
    print(resp.text)
