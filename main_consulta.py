from fastapi import FastAPI 


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"},{"item_name": "Foo2"},{"item_name": "Foo3"},{"item_name": "Foo4"},{"item_name": "Foo5"},]

@app.get('/')
async def home():
    return {"message":"hello-word"}

@app.get('/items/') 
async def read_items(skip: int = 0, limit: int = 10) -> list: #de esta manera se esta definiendo que tipo de dato deberia ser y cual es su valor por defeto
    return fake_items_db[skip: limit]

#parametros de consulta opcionales
#aqui se define un parametro de ruta y uno de consulta
@app.get('/item_optional/{item_id}')
async def read_items_opc(item_id: str, opcional: str | None = None):
    if opcional:
        return {"item_id": item_id, "opcional": opcional}
    return {"item_id": item_id}


#conversion de tipo de parametro de consulta
@app.get("/items_boolean/{item_id}")
async def read_item_bool(item_id: str, opcional: str | None = None, short: bool = False):
    item = {"item_id":item_id}
    if opcional:
        item.update({"opcional":opcional})
    if not short:
        item.update(
            {"desc":"this is amazing"}
        )
    return item

#multiples  parametros de ruta y consulta
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id":item_id, "ower_id": user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"desc":"This is amazing"}
        )
    return item
    
#parametros de consulta requeridos
@app.get("/items_required/{item_id}")
async def read_user_item_required(item_id: str, needy: str):
    item = {"item_id":item_id, "needy": needy}
    return item

#parametros opcionales y obligatorios
@app.get("/parametros_dos/{item_id}")
async def read_opc_req(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id":item_id, "needy":needy, "skip": skip, "limit": limit}
    return item

