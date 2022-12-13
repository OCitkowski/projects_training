from faker import Faker
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine, Sequence, and_
from models import *
from create_database import Base


base = declarative_base()
b = Base(declarative_base(), "sqlite:///xxx.sqlite3")
b.create_base()
engine = b.engine
# engine = create_engine("sqlite:///xxx.sqlite3", echo=True)
# Base = declarative_base
# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':

    fake = Faker()
    # *************************************************
    groups = []
    for number_group in range(10):
        ed_group = Group(group_name=f'group_name_{number_group}')
        session.add(ed_group)
        groups.append(ed_group)
    session.commit()
    # *************************************************
    permision_names = ['Full', 'Admin', 'User', 'Guest']

    for key, it in enumerate(permision_names):
        group = fake.random.choice(groups)
        print(group)
        permision = PermisionGroup(permision=it)
        print(fake.random.choice(groups))
        permision.groups.append(fake.random.choice(groups))
        session.add(permision)
    # *************************************************
    for gr in session.query(Group):
        groups.append(gr)

    # *************************************************
    for i in range(100):
        print(i)
        full_name = fake.name()
        'y y'.split()
        group = fake.random.choice(groups)
        print(group.id)
        ed_user = User(full_name=full_name.split(' '),
                       age=fake.random.randint(16, 105),
                       address=fake.address(),
                       id_group=group.id)
        session.add(ed_user)
    # *************************************************
    session.commit()
    session.close()
    # *************************************************
    for it in session.query(User):
        print(it)
    for it2 in session.query(User).filter(and_(User.id >= 3,
                                               User.surname.like('R%'))):
        print(it2)

    for it, op in session.query(PermisionGroup.permision, Group.group_name).filter(and_(
            association_table.c.permision_id == PermisionGroup.id,
            association_table.c.group_id == Group.id,
            Group.id > 1
    )):
        print(f'******* {it} {op}')
