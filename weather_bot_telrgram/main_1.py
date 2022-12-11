from faker import Faker
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine, Sequence, and_

engine = create_engine("sqlite:///xxx.sqlite3", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    age = Column(Integer)
    address = Column(String)
    id_group = Column(Integer, ForeignKey('groups.id'))

    def __init__(self, full_name: list[str], age: int, address: str, id_group: int):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = f'{full_name[0]} {full_name[1]}'
        self.age = age
        self.address = address
        self.id_group = int(id_group)

    def __repr__(self):
        return f"{self.id} {self.surname} {self.age} {self.id_group}"


class Group(Base):
    __tablename__ = 'groups'
    #
    id = Column(Integer, primary_key=True)
    group_name = Column(String)
    student = relationship('User')

    def __repr__(self):
        return f'{self.id} - {self.group_name}'


association_table = Table('association', Base.metadata,
                          Column('permision_id', Integer, ForeignKey('permisions.id')),
                          Column('group_id', Integer, ForeignKey('groups.id'))
                          )

class PermisionGroup(Base):
    __tablename__ = 'permisions'

    id = Column(Integer, primary_key=True)
    permision = Column(String)
    groups = relationship('Group', secondary=association_table, backref='group_permision')

    def __repr__(self):
        return f'{self.id} / {self.permision} / {self.groups}'


if __name__ == '__main__':

    session = Session()
    Base.metadata.create_all(engine)

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
    for i in range(10000):
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
