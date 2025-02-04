import sys
sys.path.append('./')
from connection import db_session
from model.sql_model import Todo
import decoders.todo as decode


# create a todo
def create_todo(todo: str) -> dict:
    try:
        req = Todo(todo)
        db_session.add(req)
        db_session.commit()
        return {
            'status': 'created',
            'message': 'New todo Added'
        }
    except Exception as e:
        return {
            'status': 'error',
            'message':str(e)
        }


# get all to-do
def get_all():
    try:
        res = db_session.query(Todo).all()
        docs = decode.decode_all_todo(res)
        return {
            'status': 'success',
            'data': docs
        }
    except Exception as e:
        return {
            'status': 'error',
            'message':str(e)
        }
        
# get one todo
def get_one(_id:int):
    try:
        criteria = {'_id':_id}
        res = db_session.query(Todo).filter_by(**criteria).one_or_none()
        if res is not None:
            record = decode.decode_todo(res)
            return {
            'status': 'success',
            'data': record
        }
        else:
            return {'status': 'error',
                    'message': f'Record with id {_id} do not Exist!!!'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message':str(e)
        }

# update to-do
def update_todo(_id:int, title: str):
    try:
        criteria = {'_id':_id}
        res = db_session.query(Todo).filter_by(**criteria).one_or_none()
        if res is not None:
            res.todo = title
            db_session.commit()
            return {
            'status': 'success',
            'data': 'Record Updated Successfully'
        }
        else:
            return {'status': 'error',
                    'message': f'Record with id {_id} do not Exist!!!'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message':str(e)
        }


#delete to-do

def delete_todo(_id:int):
    try:
        criteria = {'_id':_id}
        res = db_session.query(Todo).filter_by(**criteria).one_or_none()
        if res is not None:
            db_session.delete(res)
            db_session.commit()
            return {
            'status': 'success',
            'data': 'Record deleted Successfully'
        }
        else:
            return {'status': 'error',
                    'message': f'Record with id {_id} do not Exist!!!'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message':str(e)
        }


# res = create_todo("Create a blog")
# print(res)

# res = get_all()
# print(res)

# res = get_one(3)
# print(res)

# res = update_todo(1, 'Creating a website')
# print(res)

# res = delete_todo(1)
# print(res)