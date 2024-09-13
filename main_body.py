from fastapi import FastAPI 
from pydantic import BaseModel

#GET BODY

#definir una clase(objeto)
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.post("/items/")
async def create_item(item: Item) :
    return item

#accediendo a los valores dentro de la funcion
@app.post("/items_dos/")
async def create_item_dos(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_whith_tax = item.price + item.tax
        item_dict.update({"price_whit_tax":price_whith_tax})
    return item_dict