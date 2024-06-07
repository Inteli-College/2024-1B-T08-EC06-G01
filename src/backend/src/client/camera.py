import asyncio
import json
import os
import base64
import cv2
import numpy as np

import websockets
from fastapi import WebSocket
from websockets.exceptions import ConnectionClosedError
# from ultralytics import YOLO

CAMERA_WEBSOCKET_URL = os.environ.get('CAMERA_WEBSOCKET_URL') or ""

class Camera:
    def __init__(self):
        self.websocket = None
        self.clients = set()

        # self.yolo_model = YOLO("best.pt")

    async def connect(self):
        """Connect to the camera WebSocket and start listening for messages."""
        print("Connecting to camera websocket with URL: ", CAMERA_WEBSOCKET_URL)
        self.websocket = await websockets.connect(CAMERA_WEBSOCKET_URL)
        asyncio.create_task(self._broadcast_forever())

    
    async def _broadcast_forever(self):
        """Listen for messages from the WebSocket of the camera and broadcast them to all connected clients."""
        try:
            async for message in self.websocket: # type: ignore
                # print(f"Received message from robot: {message}")
                await self.process_message(message)
        except ConnectionClosedError:
            print("Connection to camera has been lost, attempting to reconnect...")
            await self._broadcast(json.dumps({ "type": "SPacketError", "data": {
                "message": "Conexão com a câmera foi perdida"
            }}))
            await self.reconnect()

    async def process_message(self, message):
        """Process the message received from the camera, run YOLO model and broadcast results."""
        data = json.loads(message)
        if "bytes" in data:
            img_data = base64.b64decode(data["bytes"])
            np_arr = np.frombuffer(img_data, np.uint8)
            img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            # results = self.yolo_model.predict(img)  # Rodar o modelo YOLO

            # results = results[0]

            object_to_detect = "cell phone"

            # for box in results.boxes:
            #     class_id = results.names[box.cls[0].item()]
            #     # cords = box.xyxy[0].tolist()
            #     # cords = [round(x) for x in cords]
            #     # conf = round(box.conf[0].item(), 2)
            #     # print("Object type:", class_id)
            #     # print("Coordinates:", cords)
            #     # print("Probability:", conf)
            #     # print("---")

                # if class_id == object_to_detect:
                #     # await self._broadcast(json.dumps({ "type": "SPacketInfo", "data": {
                #     #     "message": "Pessoa detectada"
                #     # }}))
                    
                #     print(f"{object_to_detect} detectada")

            # Randomizar se detectou ou não
            detected = np.random.choice([True, False], p=[0.1, 0.9])
            if detected:
                # print("Sujeira detectada")

                await self._broadcast(json.dumps({ "type": "SPacketInfo", "data": {
                    "message": "Sujeira detectada"
                }}))
            # else:
                # print("Nenhuma sujeira detectada")

                # await self._broadcast(json.dumps({ "type": "SPacketInfo", "data": {
                #     "message": "Nenhuma sujeira detectada"
                # }}))


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
        # print(f"Broadcasting message to {len(self.clients)} clients: {message}")
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