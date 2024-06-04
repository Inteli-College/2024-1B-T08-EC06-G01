import asyncio
import json
import os

import websockets
from fastapi import WebSocket
from websockets.exceptions import ConnectionClosedError

CAMERA_WEBSOCKET_URL = os.environ.get('CAMERA_WEBSOCKET_URL') or ""

class Camera:
    def __init__(self):
        self.websocket = None
        self.clients = set()

    async def connect(self):
        """Connect to the camera WebSocket and start listening for messages."""
        print("Connecting to camera websocket...")
        self.websocket = await websockets.connect(CAMERA_WEBSOCKET_URL)
        asyncio.create_task(self._broadcast_forever())

    
    async def _broadcast_forever(self):
        """Listen for messages from the WebSocket of the camera and broadcast them to all connected clients."""
        try:
            async for message in self.websocket: # type: ignore
                await self._broadcast(message)
        except ConnectionClosedError:
            print("Connection to camera has been lost, attempting to reconnect...")
            await self._broadcast(json.dumps({ "type": "SPacketError", "data": {
                "message": "Conexão com a câmera foi perdida"
            }}))
            await self.reconnect()

    async def add_client(self, client: WebSocket):
        self.clients.add(client)
        print(f"Added client {client}")
    
    async def remove_client(self, client: WebSocket):
        self.clients.remove(client)
        print(f"Removed client {client}")
    
    async def send(self, data):
        """Send a message to the camera."""
        if self.websocket is None:
            raise Exception("Not connected to camera")

        await self.websocket.send(data)
    
    async def _broadcast(self, message):
        if self.clients:
            await asyncio.gather(*[client.send_text(message) for client in self.clients])
    
    async def _reconnect(self):
        if self.websocket:
            try: await self.close()
            except: pass

        try: await self.connect()
        except Exception as e:
            print(f"Failed to reconnect to camera: {e}, retrying in 5 seconds...")
            await asyncio.sleep(5)
            return await self.reconnect()

        await self._broadcast(json.dumps({ "type": "SPacketInfo", "data": {
            "message": "Conexão com a câmera estabelecida"
        }}))
        print("Connected to camera")

    async def reconnect(self):
        """Close the current connection and reconnect to the camera WebSocket."""
        # use _reconnect in a non-blocking way
        asyncio.create_task(self._reconnect())

    async def close(self):
        if self.websocket:
            await self.websocket.close()
        self.websocket = None

camera = Camera()