import websockets
import os

ROBOT_WEBSOCKET_URL = os.environ.get('ROBOT_WEBSOCKET_URL') or ""

class Robot:
	def __init__(self):
		self.websocket = None

	async def connect(self):
		self.websocket = await websockets.connect(ROBOT_WEBSOCKET_URL)

	async def send(self, data):
		if self.websocket is None:
			raise Exception("Not connected to robot")

		await self.websocket.send(data)

	async def receive(self):
		if self.websocket is None:
			raise Exception("Not connected to robot")

		return await self.websocket.recv()

	async def close(self):
		if self.websocket is None:
			raise Exception("Not connected to robot")

		await self.websocket.close()


robot = Robot()