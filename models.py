from sqlalchemy import Column, Integer, String, Float # how we define a coulm in our table
from database import Base # we import Base from databse.py. Bse is the parent class

class Student(Base): # this creates a python class called student. we create this by inheriting from the base
    __tablename__ ="students" # this sets the actuall name of the table inside the database


    id = Column(Integer, primary_key=True, index=True) #id is a column in the table  and is an interger
    name = Column(String, nullable=False) # nullable false means this field is required
    course = Column(String, nullable=False)
    grade = Column(float, default=0.0) # is a column and the data type is float, default to 0.0
    email = Column(String, unique=True)

    


