from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.get("/hello")
def hello():
    return {"message": "Hello Anushree"}

@app.get("/about")
def about():
    return {
        "name": "Anushree",
        "goal": "AI Engineer"
    }

@app.get("/user/{name}")
def user(name: str):
    return {"user": name}

@app.get("/square/{num}")
def square(num: int):
    return {"square": num * num}