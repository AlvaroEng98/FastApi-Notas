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