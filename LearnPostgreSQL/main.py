from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, and_
from models import *
import psycopg2  # https://pypi.org/project/psycopg2/

engine = create_engine("postgresql+psycopg2://fox:111@localhost/db", isolation_level="SERIALIZABLE", )
Base = declarative_base
Base.metadata.create_all(engine)

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

    # ****************** select ************************
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
