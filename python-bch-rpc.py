#!/usr/bin/env python

import getpass
import json
import requests

URL = "http://127.0.0.1:18556/"

def instruct_wallet(method, params):
    payload = json.dumps({"method": method, "params": params})
    headers = {'content-type': "application/json", 'cache-control': "no-cache"}
    try:
        response = requests.request("POST", URL, data=payload, headers=headers, auth=(rpc_user, rpc_password))
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print e
    except:
        print 'No response from Wallet, check Bitcoin is running on this machine'

rpc_user='foo'
rpc_password='bar'

answer = instruct_wallet('notifyblocks', [])
if answer['error'] != None:
    print answer['error']
else:
    print answer['result']
