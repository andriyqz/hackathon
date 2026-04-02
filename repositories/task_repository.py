from models import Task


class TaskRepository:

    def __init__(self, db):
        self.db = db
    
    def create(self, task: Task):
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task
    
    def get_by_id(self, task_id: int):
        return self.db.query(Task).filter(
            Task.id == task_id
        ).first()
    
    def get_by_request(self, request_id: int):
        return self.db.query(Task).filter(
            Task.request.id == request_id
        )
    
    def update(self, task: Task):
        self.db.commit()
        self.db.refresh(task)
        return task