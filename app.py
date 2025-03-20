from task_model import Task
from fastapi import FastAPI
from task_service import *

app = FastAPI()

task_list: list[Task] = [
    Task(description= "Clean house"),
    Task(description= "Wash Room"),
    Task(description= "Test3")
]


@app.get("/")
def root():
    return "Hello World"

@app.get("/tasks/all")
def get_all():
    return get_all_tasks()

@app.get("/get-task/{task_id}")
def get(task_id: int): 
    return get_task
     

@app.post("/task")
def create(task: Task):
    return create_task(task)


@app.put("/update/{task_id}")
def update_task(task_id: int, updated: Task):
    for task in task_list:
        if task.id == task_id:
            task.description = updated.description
            task.isComplete = updated.isComplete
            return "Updated task"
        
        return "Task not found"


@app.delete("/task/delete/{task_id}")
def delete_task(task_id: int ):
    for index, task in enumerate(task_list):
        if task.id == task_id:
            task_list.pop(index)
            return 



@app.post("/")
def post_tasks():
    return None