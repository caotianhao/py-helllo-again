from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
async def root():
    return {'msg': 'Hello World'}


@app.get('/user')
async def user():
    return {'msg': 'This is my user'}


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8080)
