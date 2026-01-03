from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/users/me")
async def read_current_user(request: Request):

    # Accessing the app instance via the request object
    app = request.app

    return {
        "app_name": app.state.name,
        "initialized": app.state.initialized,
    }