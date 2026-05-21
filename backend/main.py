from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.get("/hello/{name}")
def greet(name: str):
    return {"Message": f"Hello {name}"}

@app.get("/user/{id}")
def get_user_id(id: int):
    return {"user_id is": id}

@app.get("/search")
def search_name(name: str):
    return {"searched_name": name}

@app.get("/movie")
def movie_name(name: str):
    return {"Movie name is": name}