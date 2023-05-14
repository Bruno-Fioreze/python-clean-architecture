import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infra.config import Base



class AnimalTypes(enum.Enum):
    """ Defining Animals Types """

    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"

class Pets(Base):
    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    def __repr__(self):
        return f"<Pet(id={self.id}, name={self.name}, species={self.species}, age={self.age})>"
