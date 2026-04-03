from models import User
from core.security import hash_password, verify_password
from repositories.user_repository import UserRepository

class UserService:

    def __init__(self, db):
        self.db = db
        self.__user_rep = UserRepository(db=db)

    def get_user(self, user_id: int):
        return self.__user_rep.get_by_id(user_id)

    def register_user(self, data):
        existing_user = self.__user_rep.get_by_email(email=data.email)
        if existing_user:
            raise ValueError("User with this email already exists")

        user = User(
            email=data.email,
            password_hash=hash_password(data.password),
            role=data.role,
        )

        return self.__user_rep.create(user=user)

    def authenticate_user(self, email: str, password: str):
        user = self.__user_rep.get_by_email(email=email)
        if not user:
            return None

        if not verify_password(password=password, hashed=user.password_hash):
            return None

        return user
