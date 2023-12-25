import sys

import config

sys.path.append("../../")
import openblock_api_sdk_python.param.company_param as company_param
from openblock_api_sdk_python.client import CompanyWalletClient

client = CompanyWalletClient(
    api_key=config.API_KEY,
    secret=config.API_SECRET,
    server=config.SERVER,
)

params = company_param.GetBalanceParam()
params.chain_name = "Polygon"
params.page = 0
params.limit = 20
resp = client.get_balance(params)

if resp.status_code == 200:
    print(resp.json())
else:
    print(resp.text)
