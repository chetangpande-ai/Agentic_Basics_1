from pydantic import BaseModel


class Address(BaseModel):
    street:str
    city:str
    zip_code:str

class Customer(BaseModel):
    customer_id:int
    name:str
    address:Address  ## nested model


customer=Customer(customer_id=1,name="chetan",
                  address={"street":"s school","city":"pune","zipcode":"123456"})