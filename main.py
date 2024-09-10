from fastapi import FastAPI, Body
import uvicorn
from pydantic import EmailStr, BaseModel

app = FastAPI()

class CreateUser(BaseModel):
    email: EmailStr

@app.get("/")
def hello_index():
    return {
        "message": "Hello index"
    }

@app.get("/hello")
def hello(name: str = "World"):
    name = name.strip().title()
    return {
        "message": f"Hello {name}"
    }

@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "User created",
        "email": user.email
    }

@app.post("/calc/add")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }

@app.get("/items/")
def items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@app.get("/items/latest/")
def latest():
    return {
        "item": {
            "item_id": 1,
            "item_name": "Item1"
        }
    }


@app.get("/items/{item_id}/")
def item_id(item: int):
    return {"item_id": item}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
