from typing import Union, List

from fastapi import FastAPI
from pydantic.dataclasses import dataclass


@dataclass
class Order:
    # Contains order details
    name: str
    items: List[str]
    

app = FastAPI()
# Set up the connection to mysql


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/place_order")
def read_item(order: Order):
    # return {
    #     "name": order.name,
    #     "items": order.items
    # }
    # Add it to mysql database
    return {"status": "confirmed"}