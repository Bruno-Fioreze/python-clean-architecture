from faker import Faker
from .user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()


def test_insert_user_repository():
    name = faker.name()
    password = faker.word() 

    user_repository.insert_user_repository(name, password)
    assert user_repository.get_user_repository(name) is not None