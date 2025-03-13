from task_model import Task
from fastapi import FastAPI

app = FastAPI()

tasks = [
    Task(description= "Clean house"),
    Task(description= "Clean Room"),
    Task(description= "Test3")
]


@app.get("/")
def root():
    return "Hello World"

@app.get("/get-tasks")
def get_all_tasks():
    return tasks

@app.get("/get-task/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
     

# @app.put("/")
# def update_task():
#     return "Hello World"

# @app.post("/")
# def create_task():
#     return "Hello World"

# @app.delete("/")
# def delete_task():
#     return "Hello World"

@app.post("/")
def post_tasks():
    return None