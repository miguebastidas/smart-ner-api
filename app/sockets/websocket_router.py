from fastapi import WebSocket

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("WebSocket connection established.")
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")
        if data.lower() == "close":
            break
    await websocket.close()