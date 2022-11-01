

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker


#erzeugen db
# # Do not touch!
# # Database Connection stuff!
# Erzeugen einer neuen Datenbank Engine
database = create_engine("sqlite:///todo.db")
# Basisklasse für Klassen
Base = declarative_base()

# Öffne Verbindung zur Datenbank
Session = sessionmaker(bind=database)
# Offene Verbindung zur Datenbank
session = Session()

#--------------------------------------------------------------------
#klasse erstellen und datenbank initialize
class Task(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)
    to_do = Column(String)

def initialize_database():
    """
    Initializes the database and creates all tables.
    See more here: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    """
    Base.metadata.create_all(database)
#--------------------------------------------------------------------
 


#create taskmenu
def taskmenu():

    menu = """
    Menu:
    - Add task (A)
    - Delete task (D)
    - Mark task done (X)
    - Show all tasks (S)
    - Close (exit)
    """
    print(menu)

#get user menu input and run it
def input_menu():
    userinput = input("Choose A,D,X,S,exit : ")

    if userinput == "A":
        add_new_task()
    elif userinput == "D":
        delete_task()
    elif userinput == "X":
        mark_task_done()
    elif userinput == "S":
        print(database_show_all_tasks())
    elif userinput == "exit":
        exit()



#-------------------------------------------FUNCTIONS------------------------------
#function for add new task to db
def add_new_task():
    print("Add a new task")
    to_do = input("task: ")
    new_todo = Task(to_do = to_do)
    database_add_task(new_todo)

#function to delete task from db
def delete_task():
    print(database_show_all_tasks())
    print("check above which task u want to delete? enter the ID : ")
    deletetask_id = input("ID : ")
    delete = database_get_one_task(deletetask_id)
    database_delete_task(delete)

#function to mark task as done
def mark_task_done():
    print(database_show_all_tasks())
    task_id = int(input("check above which task u want to mark as done? enter the ID : "))
    task = database_get_one_task(task_id)
    task_fields = {}
#-----------------------------------------DATABASE COMMANDS --------------------------------------------------------
#database command to add new task
def database_add_task(task: Task):
    session.add(task)
    session.commit()

#database command to delete task
def database_delete_task(task: Task):
    session.delete(task)
    session.commit()
    
#show all tasks from db
def database_show_all_tasks():
    
    return session.query(Task).all()

#database command to mark task done
def database_get_one_task(task_id: int):
    
    return session.query(Task).get(task_id)

#--------------------------------------------------------MAIN------------------------------------------------
if __name__ == "__main__":
    initialize_database()

    while True:
        taskmenu()
        input_menu()