from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infra.config import Base

class Users(Base):
    """ User Entity  """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    pet = relationship("Pets")

    def __repr__(self):
        return f'<User {self.name}>'

