from models import Task, Request
from models.enums import TaskStatus, RequestStatus
from repositories.request_repository import RequestRepository
from repositories.task_repository import TaskRepository


class TaskService:
    
    def __init__(self, db):
        self.db = db
        self.__request_repo = RequestRepository(db=db)
        self.__task_repo = TaskRepository(db=db)

    def assign_driver(self, request_id: int, driver_id: int):
        request = self.__request_repo.get_by_id(request_id)

        if not request_id:
            raise Exception("Request not found")
        
        task = Task(
            request_id=request_id,
            driver_id=driver_id,
            status=TaskStatus.ASSIGNED
        )

        request.status = RequestStatus.IN_PROGRESS

        self.__task_repo.create(task=task)

        return task
    
    def complete_task(self, task_id: int):
        task = self.__task_repo.get_by_id(task_id)

        task.status = TaskStatus.DONE

        all_tasks_done = all(
            t.status == Task.DONE
            for t in task.request.tasks
        )

        if all_tasks_done:
            task.request.status = RequestStatus.DONE
        
        self.__task_repo.update(task)