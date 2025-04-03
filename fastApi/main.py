from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
# items = []
items = [
        {
            "name": "Hai",
            "description": 'DESC11',
            "id": 1,
        },
        {
            "name": "Hello",
            "description": "DESC122",
            "id": 2,
        },
        {
            "name": "Hello",
            "description": "DESC",
            "id": 3
        }
    ]
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    id: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}   

@app.post("/items")
async def create_item(item: Item):
    items.append(item)
    return {"message": "Item added successfully", "items": items}


# @app.post("/items")
# async def create_item(item: Item):
#     if not item.name:
#         raise HTTPException(status_code=400, detail="Item name cannot be empty")
    
#     items.append(item.name)
#     return {"message": "Item added successfully", "items": items}

# @app.get("/items")
# async def read_items(limit: int = 1):
#     # return items[:limit]
#     return {"message": "Hello World"}  
@app.get("/items")
async def read_items(limit: int = 1):
    return items[:limit] 

@app.get("/items/{item_id}")
async def get_data(item_id: int):
    if item_id > len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id - 1]

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item): 
    for index, exst_item in enumerate(items):
        if exst_item["id"] == item_id:
            items[index] = item.dict()
            return {"message": "Item updated successfully", "items": items}
        
    raise HTTPException(status_code=404, detail="Item not found")  


@app.patch("/items/{item_id}")
async def update_item_data(item_id: int, item: Item):
    for index, exst_item in enumerate(items):
        if exst_item["id"] == item_id:
            update_item = exst_item.copy()  # Create a copy to avoid modifying the original item
            if item.name:
                update_item["name"] = item.name  # Update name if provided
            if item.description is not None:  # Check if description is provided (could be None)
                update_item["description"] = item.description  # Update description if provided
            items[index] = update_item  # Replace the old item with the updated one
            return {"message": "Item updated successfully", "items": items}
    
    # If the item with the given id is not found, raise a 404 error
    raise HTTPException(status_code=404, detail="Item not found")
