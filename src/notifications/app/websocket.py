from starlette.websockets import WebSocket


class WebSocketCollector:
    def __init__(self):
        self.websocket_connections: set[WebSocket] = set()

    def add_connection(self, websocket: WebSocket):
        self.websocket_connections.add(websocket)

    def remove_connection(self, websocket: WebSocket):
        self.websocket_connections.remove(websocket)

    async def transfer(self, message):
        for connection in self.websocket_connections:
            await connection.send_text(str(message))
