from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI app instance
app = FastAPI()

# Define a Pydantic model for data validation
class Item(BaseModel):
    name: str
    price: float
    description: str | None = None  # Optional field
    tax: float | None = None

# Define a GET endpoint
@app.get("/")
def read_root():
    return {"message": "Test FastAPI!"}

# Define a GET endpoint with a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}

# Define a POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {
        "name": item.name,
        "price_with_tax": item.price + (item.tax or 0),
        "description": item.description
    }