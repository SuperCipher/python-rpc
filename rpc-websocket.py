#!/usr/bin/env python
# pip install websockets
import asyncio
import websockets
import json

from base64 import b64encode

def basic_auth_header(username, password):
    assert ':' not in username
    user_pass = f'{username}:{password}'
    basic_credentials = b64encode(user_pass.encode()).decode()
    return ('Authorization', f'Basic {basic_credentials}')

async def run():
    async with websockets.connect(
        'ws://127.0.0.1:18332/ws',
        extra_headers=[basic_auth_header('pat', 'biggestfan')],
    ) as websocket:

        await websocket.send('{"jsonrpc":"1.0","id":"0","method":"getinfo","params":[]}')
        greeting = await websocket.recv()
        print(f"{greeting}")

asyncio.get_event_loop().run_until_complete(run())
