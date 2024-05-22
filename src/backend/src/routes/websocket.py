import asyncio
import json

import pydantic
from client.robot import robot
from fastapi import APIRouter, WebSocket
from schemas.websocket import ControlPacket

router = APIRouter(
	prefix="/websocket",
	tags=["websocket"],
)

@router.websocket("/control")
async def control_robot(websocket: WebSocket):
	await websocket.accept()

	while True:
		raw = await websocket.receive_text()

		try: data = json.loads(raw)
		except json.JSONDecodeError:
			await websocket.send_json({ "type": "SPacketError", "message": "Invalid JSON" })
			continue

		try: packet = ControlPacket(**data)
		except pydantic.ValidationError as e:
			await websocket.send_json({ "type": "SPacketError", "message": str(e).replace('\n', '') })
			continue

		await robot.send(json.dumps({ 'control': packet.data.state }))

# @router.websocket("/video")
# async def video_feed(websocket: WebSocket):
# 	await websocket.accept()

# 	while True:
# 		await websocket.send_text("Hello, world!")
# 		await asyncio.sleep(1)