from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from sockets.websocket_router import websocket_endpoint
from routers.users import router as users


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code here
    app.state.initialized = True
    app.state.name = "My FastAPI App"
    print("Starting up...")
    yield
    # Shutdown code here
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)
app.include_router(users)
app.add_websocket_route("/ws", websocket_endpoint)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)