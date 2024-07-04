from fastapi import FastAPI
from fastapi import FastAPI, Body, Request
from fastapi.responses import JSONResponse

appV1 = FastAPI(openapi_prefix='/v1')


@appV1.get('/health-check')
def healthCheck():
    return {
        'is_success': True
    }

@appV1.post('/save')
def saveData(locale: str = 'en', request: dict = Body(...)):
    if not (request.get('id') and request.get('user_response')):
        raise ErrorDecorator(name="Invalid request", status=Constants.StatusCodes.BAD_REQUEST)
    print(request.get('user_response'))
    return {"result": request.get('user_response')}

@appV1.get('/getQuestions')
def getQuestions(locale: str = 'en'):
    try:
         return {
        'is_success': True
    }
    except IndexError as error:
        raise ErrorDecorator(name=f"No data found for locale - {locale}", status=Constants.StatusCodes.BAD_REQUEST)
