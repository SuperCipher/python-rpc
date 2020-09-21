#!/usr/bin/env python
# pip install requests

import getpass
import json
import requests
from requests.auth import HTTPBasicAuth
# python json rpc

# bchd
# URL = "http://127.0.0.1:18556/"

# bchwallet
URL = "http://127.0.0.1:18332/"
# URL = "http://127.0.0.1:18444/"



def instruct_wallet(method, params):
    payload = json.dumps({"jsonrpc":"1.0","id":"0","method": method, "params": params})
    headers = {'content-type': "application/json", 'cache-control': "no-cache"}
    try:
        response = requests.request("POST", URL, data=payload, headers=headers, auth=HTTPBasicAuth(rpc_user, rpc_password))
        print( json.loads(response.text))
    except requests.exceptions.RequestException as e:
        print (e)
    except:
        print(response)
        # print ('No response from Wallet, check Bitcoin is running on this machine')

rpc_user='regtest'
rpc_password='regtest'
# rpc_user='regtest'
# rpc_password='regtest'

# instruct_wallet('getinfo', [])
instruct_wallet('getblockchaininfo', [])
# instruct_wallet('getblockcount', [])

# instruct_wallet('getbalance', [])

# if answer['error'] != None:
#     print (answer['error'])
# else:
#     print( answer['result'])
