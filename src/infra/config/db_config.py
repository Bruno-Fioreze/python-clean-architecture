from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """SQLAlchemy"""

    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """Return connection engine"""
        return create_engine(self.__connection_string)

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        self.session = sessionmaker(bind=engine)()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
