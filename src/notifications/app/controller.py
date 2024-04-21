from json import dumps

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from .schemas import NotificationPayload, Response
from .websocket import WebSocketCollector

controller = APIRouter(prefix='/notification')
websocket_collector = WebSocketCollector()


@controller.post("/new/")
async def new_notification(payload: NotificationPayload) -> None:
	await websocket_collector.transfer(message=payload.model_dump_json())


@controller.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await websocket.accept()
    try:
        websocket_collector.add_connection(websocket)
        await websocket.send_text(str(dumps(Response(detail="Successfully Login").model_dump(mode="json"))))

        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        websocket_collector.remove_connection(websocket)

    except Exception:
        websocket_collector.remove_connection(websocket)
        await websocket.close()
