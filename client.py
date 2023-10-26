import asyncio
import websockets

async def hello():
    uri = "ws://127.0.0.1:8886"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, WebSocket!")
        response = await websocket.recv()
        print(response)

asyncio.get_event_loop().run_until_complete(hello())
