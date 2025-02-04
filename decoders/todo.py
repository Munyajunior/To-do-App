
def decode_todo(doc) -> dict:
    return {
        '_id': doc._id,
        'title': doc.todo,
        'timestamp': doc.timestamp
    }
    
    
def decode_all_todo(docs) -> list:
    return[
        decode_todo(doc) for doc in docs
    ]