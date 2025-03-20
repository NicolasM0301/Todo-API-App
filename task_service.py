from task_model import Task
from fastapi import FastAPI


app = FastAPI()

task_list: list[Task] = [
    Task(description= "Clean house"),
    Task(description= "Wash Room"),
    Task(description= "Test3")
]


def root():
    return "Hello World"


def get_all_tasks():
    return task_list


def get_task(task_id: int): 
    for task in task_list:
        if task.id == task_id:
            return task

    return "Task not Found"
     

@app.post("/task")
def create_task(task: Task):
    task_list.append(task)
    return "Task Added"


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