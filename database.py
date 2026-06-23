from sqlalchemy import create_engine # create engine is a function that creates the connection
from sqlalchemy.orm import sessionmaker #its a function that produces database sesseion on demand 
from sqlalchemy.ext.declarative import declarative_base #

DATABASE_URL = "sqlite:///./grades.db" # this str tells the sqlalchemy where exactly our dtabase lives. "./" this means same folder

# the engine is the actual connection through the database. it uses the URL to know where to connect
engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})

# SessionLocal - blueprint for creating session 
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


# Base is our parent class for all our database model
Base = declarative_base() 

def get_db():
    db = SessionLocal()
    try:
        yield db # yield gives the session to whoever called get_db and PAUSES here
    finally:
        db.close() # closes the connection and returns the connection . cleanup happens.
