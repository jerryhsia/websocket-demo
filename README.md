# websocket-demo

## start container

```
docker run -d --name="websocket-demo" -p 8886:8886 jerry9916/websocket-demo:latest python3 server.py
```

## test

```python3
import asyncio
import websockets

async def hello():
    uri = "ws://127.0.0.1:8886"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, WebSocket!")
        response = await websocket.recv()
        print(response)

asyncio.get_event_loop().run_until_complete(hello())
```