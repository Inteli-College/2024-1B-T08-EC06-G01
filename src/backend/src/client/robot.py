import asyncio
import os

import websockets
from fastapi import WebSocket
from websockets.exceptions import ConnectionClosedError

ROBOT_WEBSOCKET_URL = os.environ.get('ROBOT_WEBSOCKET_URL') or ""

class Robot:
	def __init__(self):
		self.websocket = None
		self.clients = set()

	async def connect(self):
		"""Connect to the robot WebSocket and start listening for messages."""
		print("Connecting to robot websocket...")
		self.websocket = await websockets.connect(ROBOT_WEBSOCKET_URL)
		asyncio.create_task(self._broadcast_forever())

	async def _broadcast_forever(self):
		"""Listen for messages from the WebSocket and broadcast them to all connected clients."""
		try:
			async for message in self.websocket: # type: ignore
				await self._broadcast(message)
		except ConnectionClosedError:
			print("Connection to robot has been lost, shutting down websocket endpoint")
			await self.close()

	async def add_client(self, client: WebSocket):
		self.clients.add(client)
		print(f"Added client {client}")

	async def remove_client(self, client: WebSocket):
		self.clients.remove(client)
		print(f"Removed client {client}")

	async def send(self, data):
		"""Send a message to the robot."""
		if self.websocket is None:
			raise Exception("Not connected to robot")

		await self.websocket.send(data)

	async def _broadcast(self, message):
		if self.clients:
			await asyncio.gather(*[client.send_text(message) for client in self.clients])

	async def close(self):
		if self.websocket:
			await self.websocket.close()
		self.websocket = None


robot = Robot()