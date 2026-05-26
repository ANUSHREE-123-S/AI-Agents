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

@app.put("/update-notes/{index}")
def update_notes(index:int, note:Note):
    if index>=len(notes):
        return{"message":"note not found"}
    notes[index]= note.dict()
    return{
        "message":"notes is updated",
        "notes":notes
    }

@app.delete("/delete-notes/{index}")
def delete_notes(index:int):
    if index>=len(notes):
        return {"errorr":"note is not found"}
    deleted_note=notes.pop(index)
    return{"message":"note book is deleted",
           "deleted_note":deleted_note,
           "notes":notes
            }
