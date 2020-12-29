import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/api/calculate')
def calculate():
    value = 2+2
    return {
        'value': value,
        'value2': 6,
    }

uvicorn.run(api)