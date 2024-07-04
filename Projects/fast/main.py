import uvicorn
from fastapi import FastAPI, Request
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM

from config.config import Config
from src.modules.v1.routes import appV1
from src.utils.errors.error_decorator import ErrorDecorator

app = FastAPI()

if Config.NODE_ENV != 'local':
    apm = make_apm_client({
        'SERVICE_NAME': '',
        'SERVER_URL': Config.APM_SERVER_URL,
        'LOG_LEVEL': 'info',
        'ENVIRONMENT': Config.NODE_ENV,
        'CAPTURE_HEADERS': True,
        'CAPTURE_BODY': 'all',
        'FRAMEWORK_NAME': 'fastapi'
    })
    app.add_middleware(ElasticAPM, client=apm)

@app.on_event("startup")
def startupEvents():
    app.config = Config()

@app.get('/health-check')
def healthCheck():
    return {
        'is_success': True
    }

@appV1.exception_handler(ErrorDecorator)
async def exception_handler(request: Request, exc: ErrorDecorator):
    return JSONResponse(
        status_code=exc.status,
        content={"error": {"message": f"{exc.name}"}, "is_success": False},
    )

app.mount('/v1', appV1)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
