import asyncio
import websockets
import time

async def echo(websocket, path):
    async for message in websocket:
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        str = f"[{time_str}] Received: {message}"
        print(str)
        await websocket.send(f"Received: {message}")

host = "0.0.0.0"
port = 8886

start_server = websockets.serve(echo, host, port)
print(f"Server started at {host}:{port}")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()