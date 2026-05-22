from pydantic import BaseModel
from fastapi import FastAPI
app=FastAPI()
notes=[]

class Note(BaseModel):
    title:str
    content:str

@app.post("/add-note")
def add_note(note:Note):
    notes.append({
        "title":note.title,
        "content":note.content
    })
    return{
        "message":"Note added",
        "notes":notes
    }
@app.get("/get-notes")
def get_notes():
    return {"notes":notes}