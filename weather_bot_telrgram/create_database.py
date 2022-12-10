from faker import Faker

from models.database import create_db, Session
# from models.lesson import Lesson
from models.student import Student
# from models.group import Group


def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session: Session):
    # lessons_names = ['Математика', 'Физкультура']
    #
    # group1 = Group(group_name='МДА7')
    # group2 = Group(group_name='МДА9')
    # session.add(group1)
    # session.add(group2)
    #
    # for key, it in enumerate(lessons_names):
    #     lesson = Lesson(lesson_title=it)
    #     lesson.groups.append(group1)
    #     if key % 2 == 0:
    #         lesson.groups.append(group2)
    #     session.add(lesson)

    faker = Faker('ru_RU')
    # group_list = [group1, group2]
    # session.commit()

    for _ in range(10):
        full_name = faker.name().split(' ')
        age = faker.random.randint(16, 25)
        address = faker.address()
        # group = faker.random.choice(group_list)
        # student = Student(full_name, age, address, group.id)
        student = Student(full_name, age, address)
        session.add(student)
        print(student)
        session.commit()

    session.close()
