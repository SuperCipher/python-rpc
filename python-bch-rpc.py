#!/usr/bin/env python

import getpass
import json
import requests
# python json rpc

URL = "http://127.0.0.1:18556/"

def instruct_wallet(method, params):
    payload = json.dumps({"jsonrpc":"1.0","id":"0","method": method, "params": params})
    headers = {'content-type': "application/json", 'cache-control': "no-cache"}
    try:
        response = requests.request("POST", URL, data=payload, headers=headers, auth=(rpc_user, rpc_password))
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print (e)
    except:
        print ('No response from Wallet, check Bitcoin is running on this machine')

rpc_user='pat'
rpc_password='biggestfan'

answer = instruct_wallet('getinfo', [])
if answer['error'] != None:
    print (answer['error'])
else:
    print( answer['result'])
