from src.infra.confg import DBConnectionHandler
from src.infra.entities import Users


class FakerRepo:
    @classmethod
    def insert_user(cls, name: str, password: str):
        with DBConnectionHandler() as conn:
            try:
                user = Users(name="teste", password="1234")
                conn.session.add(user)
                conn.session.commit()
            except Exception as e:
                conn.connection.rollback()
                raise
                print(e)
            finally:
                conn.connection.close()
