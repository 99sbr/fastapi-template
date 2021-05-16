import uvicorn
import subprocess 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from application.initializer import IncludeAPIRouter
from application.main.config import settings


def get_application():
    _app = FastAPI(title=settings.API_NAME,
                   description=settings.API_DESCRIPTION,
                   version=settings.API_VERSION)
    _app.include_router(IncludeAPIRouter())
    _app.add_middleware(
        CORSMiddleware,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return _app

try:
    process = subprocess.Popen(["streamlit", "run", 'streamlit_app.py'])
except Exception as e:
    pass

app = get_application()


@app.on_event("shutdown")
async def app_shutdown():
    # on app shutdown do something probably close some connections or trigger some event
    print("On App Shutdown i will be called.")


#uvicorn.run("manage:app", host=settings.HOST, port=settings.PORT, log_level=settings.LOG_LEVEL, use_colors=True,reload=True)
