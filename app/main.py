from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World from continus deployment - test de deployment'}

@app.get('/login')
async def login():
    return {'message': 'Login'}