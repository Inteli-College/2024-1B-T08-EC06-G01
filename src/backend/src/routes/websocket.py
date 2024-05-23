import json

import pydantic
from client.robot import robot
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from schemas.websocket import ControlPacket
from websockets.exceptions import ConnectionClosedError

router = APIRouter(
	prefix="/websocket",
	tags=["websocket"],
)

@router.websocket("/control")
async def control_robot(websocket: WebSocket):
	await websocket.accept()

	if not robot.websocket:
		await websocket.send_json({ "type": "SPacketError", "message": "Connection to robot has been lost" })
		await websocket.close()
		return

	await robot.add_client(websocket)

	try:
		while True:
			raw = await websocket.receive_text()

			if not robot.websocket:
				await websocket.send_json({ "type": "SPacketError", "message": "Connection to robot has been lost" })
				await websocket.close()
				return

			try: data = json.loads(raw)
			except json.JSONDecodeError:
				await websocket.send_json({ "type": "SPacketError", "message": "Invalid JSON" })
				continue

			try: packet = ControlPacket(**data)
			except pydantic.ValidationError as e:
				await websocket.send_json({ "type": "SPacketError", "message": str(e).replace('\n', '') })
				continue

			await robot.send(json.dumps({ 'control': packet.data.state }))

	except WebSocketDisconnect:
		await robot.remove_client(websocket)
		await websocket.close()
	except ConnectionClosedError:
		print("Connection to robot has been lost, shutting down websocket endpoint")
		await robot.close()
		await websocket.send_json({ "type": "SPacketError", "message": "Connection to robot has been lost" })
		await websocket.close()
		return
