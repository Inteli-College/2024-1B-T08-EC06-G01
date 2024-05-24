import asyncio
import datetime
import base64
import json

import cv2
import websockets


class WebSocketServer:
    def __init__(self, host='localhost', port=8765):
        self.host = host
        self.port = port
        self.clients = set()
        self.loop = None
        self.thread = None
        # self.capture = cv2.VideoCapture(0)
        self.capture = None

    async def register_client(self, websocket):
        self.clients.add(websocket)
        try:
            async for msg in websocket:
                pass  # Ignore incoming messages
        finally:
            self.clients.remove(websocket)

    async def _broadcast(self, message):
        if self.clients:
            await asyncio.gather(*[client.send(message) for client in self.clients])

    def broadcast(self, message):
        """Synchronous wrapper for the asynchronous _broadcast function."""
        if self.loop:
            asyncio.run_coroutine_threadsafe(self._broadcast(message), self.loop)

    async def websocket_handler(self, websocket, path):
        await self.register_client(websocket)

    def start_server(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        server_coro = websockets.serve(self.websocket_handler, self.host, self.port)
        self.loop.run_until_complete(server_coro)

        self.loop.create_task(self.broadcast_image_forever())

        print(f"WebSocket server started on ws://{self.host}:{self.port}")
        self.loop.run_forever()

    # def run_in_thread(self):
    #     self.thread = threading.Thread(target=self.start_server)
    #     self.thread.start()

    async def broadcast_image(self):
        if not self.capture:
            self.capture = cv2.VideoCapture(0)

        ret, frame = self.capture.read()
        timestamp = datetime.datetime.now().timestamp() * 1000
        if ret:
            _, buffer = cv2.imencode('.jpg', frame)

            self.broadcast(json.dumps({
                "bytes": base64.b64encode(buffer).decode('utf-8'),
                "timestamp": timestamp
            }))

    async def broadcast_image_forever(self):
        while not self.loop:
            await asyncio.sleep(0.1)

        while True:
            if len(self.clients) == 0:
                if self.capture:
                    self.capture.release()
                    self.capture = None

                await asyncio.sleep(0.1)
                continue

            self.loop.create_task(self.broadcast_image())
            await asyncio.sleep(0.02) # 50Hz

if __name__ == "__main__":
    websocket_server = WebSocketServer(host='0.0.0.0')
    websocket_server.start_server()

