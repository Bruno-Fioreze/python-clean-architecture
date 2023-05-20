from src.infra.confg import DBConnectionHandler
from src.infra.entities import Users

class UserRepository:
    """
    UserRepository class
    """
    @classmethod
    def insert(cls, name: str, password: str):
        with DBConnectionHandler() as db_connection:
            try:
                user = Users(name=name, password=password)
                db_connection.session.add(user)
                db_connection.session.commit()
                return user
            except Exception as e:
                db_connection.session.rollback()
            finally:
                db_connection.session.close()
