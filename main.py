from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from database import get_db, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Grade Tracker", 
              description=" Track student grades with FastAPI",
              version="1.0.0")

# CREATE
@app.post("/students/", response_model = schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)
 
# READ ALL
@app.get("/students/", response_model = List[schemas.StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)
 
# READ ONE
@app.get("/students/{student_id}", response_model = schemas.StudentResponse)
def get_student(student_id: int, db:Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(404, "Student not found")
    return student

# UPDATE
@app.put("/student/{student_id}", response_model = schemas.StudentResponse)
def update_student(student_id: int, data: schemas.StudentUpdate,
                   db: Session = Depends(get_db)):
    updated_student = crud.update_student(db, student_id, data)
    if not updated_student:
        raise HTTPException(404, "Student already recorded")
    return updated_student

# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student= crud.delete_student(db, student_id)
    if not student:
        raise HTTPException(404, "Student not found")
    return {"message": "Student deleted successfully"}
