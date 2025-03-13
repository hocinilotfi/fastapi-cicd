from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World from continus deployment - test de deployment'}

@app.get('/login')
async def method_name():
    return {'message': 'Login page modified'}

@app.get('/signup')
async def method_name():
    return {'message': 'Signup page'}