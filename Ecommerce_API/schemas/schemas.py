from pydantic import BaseModel,Field
from typing import Optional

class CreateProduct(BaseModel):
    id:int
    name:str= Field(...)
    description:Optional[str] = None
    price:float = Field(gt=0)
    stock:int= Field(ge=0)
    category:str = Field(example="electronics, clothing")

    def __repr__(self):
        return f"< name= {self.name} , price= {self.price}>"

class UpdateProduct(BaseModel):
    id:int
    name:Optional[str]= Field(...)
    description:Optional[str] = None
    price:Optional[float] = Field(gt=0)
    stock:Optional[int]= Field(ge=0)
    category:Optional[str] = Field(example="electronics, clothing")

