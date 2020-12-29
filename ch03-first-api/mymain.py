import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/api/calculate')
def calculate(x: int, y: int, z: int = 10):
    value = (x+y)*z
    return {
        'value': value,
        'value2': 6,
    }

uvicorn.run(api)