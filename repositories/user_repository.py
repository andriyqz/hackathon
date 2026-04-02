from models import User


class UserRepository:

    def __init__(self, db):
        self.db = db

    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(
            User.id == user_id
        ).first()
    
    def get_by_email(self, email: str):
        return self.db.query(User).filter(
            User.email == email
        ).first()