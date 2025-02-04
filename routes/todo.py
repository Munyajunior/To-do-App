from fastapi import APIRouter
from model.pydantic_model import Todo
import all_routes
import operations.to_do as db 


todo_route = APIRouter()


# create a new todo
@todo_route.post(all_routes.todo_create)
def new_todo(doc: Todo):
    doc = dict(doc)
    todo: str = doc['todo']
    res = db.create_todo(todo)
    
# get all
@todo_route.get(all_routes.todo_all)
def all_todos():
    res = db.get_all()
    return res

#get one
@todo_route.get(all_routes.todo_one)
def todo_one(_id:int):
    res = db.get_one(_id)
    return res

# update one todo
@todo_route.patch(all_routes.todo_update)
def todo_update(_id:int, doc : Todo):
    doc = dict(doc)
    title: str = doc['todo']
    res = db.update_todo(_id,title)
    return res

# delete todo
@todo_route.delete(all_routes.todo_delete)
def todo_delete(_id:int):
    res = db.delete_todo(_id)
    return res
