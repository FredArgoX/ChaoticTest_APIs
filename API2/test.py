"""
# FUNCTIONAL 1ST ------------------------

from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items{item_id}")
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item
"""

"""
# FUNCTIONAL 2ND ------------------------

from fastapi import FastAPI, HTTPException

app = FastAPI()

app.state.items = []

@app.get("/")
def root():
    return {"Hello": "World"}

# POST
# WSL command:
# curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
@app.post("/items")
def create_item(item: str):
    app.state.items.append(item)
    return app.state.items

# GET
# WSL command:
# curl -X GET http://127.0.0.1:8000/items/0
# Browser link:
# http://127.0.0.1:8000/items/0
@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    try:
        return app.state.items[item_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

# GET
# WSL command (generic):
# curl -X GET http://127.0.0.1:8000/items
# WSL command (custom):
# curl -X GET 'http://127.0.0.1:8000/items?limit=3'
@app.get("/items")
def list_items(limit: int=10):
    return app.state.items[0:limit]
"""

# FUNCTIONAL 3RD ------------------------

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

app.state.items = []

@app.get("/")
def root():
    return {"Hello": "World"}

# POST
# WSL command:
# curl -X POST -H "Content-Type: application/json" -d '{"text":"apple"}' 'http://127.0.0.1:8000/items'
@app.post("/items")
def create_item(item: Item):
    app.state.items.append(item)
    return app.state.items

# GET
# WSL command:
# curl -X GET http://127.0.0.1:8000/items/0
# Browser link:
# http://127.0.0.1:8000/items/0
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    try:
        return app.state.items[item_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

# GET
# WSL command (generic):
# curl -X GET http://127.0.0.1:8000/items
# WSL command (custom):
# curl -X GET 'http://127.0.0.1:8000/items?limit=3'
@app.get("/items", response_model=list[Item])
def list_items(limit: int=10):
    return app.state.items[0:limit]

# http://127.0.0.1:8000/docs#
# http://127.0.0.1:8000/redoc
# http://127.0.0.1:8000/openapi.json