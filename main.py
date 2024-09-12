from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/item/{item_id}")
async def item(item_id):
    return {"item_id": item_id}

#definiendo que tipo de datos espera
@app.get("/items/{item_id}")
async def item_inst(item_id: int):
    return {"item_id": item_id}

'''
variables de rutas 
urls fijas 
urls dinamicas 
'''

#fijas
@app.get('/users/me')
async def read_user_me():
    return {"user_id":"me"}

#dinamica
@app.get('/users/{user_id}')
async def read_user_me(user_id: str):
    return {"user_id": user_id}
