from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: float = Field(gt=0, le=10000)
    quantity: int = Field(ge=0)

item = Item(name="Book", price=10, quantity=10)
print(item)