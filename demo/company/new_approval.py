import sys

import config

sys.path.append("../../")
import openblock_api_sdk_python.param.company_param as company_param
from openblock_api_sdk_python.client import CompanyWalletClient

client = CompanyWalletClient(
    api_key=config.API_KEY, secret=config.API_SECRET, server=config.SERVER
)

txinfo = company_param.TxInfoParam()
txinfo.chain = "HECO"
txinfo.fromAddress = "0x5adE66b500B80070F3280198CEBA2Af830D8e0ab"
txinfo.to = "0x7620E9bbb6591b9F53b6b5002B716B8D23ca3950"
txinfo.value = "0.01"
txinfo.gasLimit = "97839"
txinfo.maxPriorityFeePerGas = "2.25"
txinfo.maxFeePerGas = "2.25"

params = company_param.NewApprovalParam()
params.action = "TRANSACTION"
params.txinfo = txinfo
resp = client.new_approval(params)

if resp.status_code == 200:
    print(resp.json())
else:
    print(resp.text)
