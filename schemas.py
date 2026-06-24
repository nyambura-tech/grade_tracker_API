from pydantic import BaseModel
from typing  import Optional

# what the user sends to CREATE 
# StudentCreate  is the schema for when someone wants to add a new student
# (name, course, grade, email) - these are the field they must send n there  request
class StudentCreate(BaseModel):
    name: str
    course: str 
    grade: float = 0.0
    email: str 


# what the user sends to UPDATE
# StudentUpdate - is for when someone wants to change a student's detail
# the key difference is here everthing is optional. WHY? when updating the user 
# should be able to send  just one field and change only that
class StudentUpdate(BaseModel):
    name: Optional[str] = None #name is optional , if not sent, it is noene (skips updating)
    course: Optional[str] = None
    grade: Optional[float] = None

# what the API aends back
# StudentResponse is what comes back when someone makes a request
# notice the StudentResponse include id (because after we create a student
# to tell the user what id they were assigned to)
class StudentResponse(BaseModel):
    id: int
    name: str
    course: str
    grade: float
    email: str

    # from_attributes = True - is a bridge between database world and an API worl
    # the database gives us the SQLAlchemy object. the API needs to return pydantic schema
    class config: # special class in pydantic (it holds a configuration setting)
        from_attributes = True # without this line. pydantic cannot read SQLAlchemy
