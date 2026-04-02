from models import User
from repositories.user_repository import UserRepository

class UserService:

    def __init__(self, db):
        self.db = db
        self.__user_rep = UserRepository(db=db)

    def get_user(self, user_id: int):
        return self.__user_rep.get_by_id(user_id)
    