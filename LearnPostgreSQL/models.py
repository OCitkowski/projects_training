from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table

declarative_base = declarative_base()

association_table = Table('association', declarative_base.metadata,
                          Column('permision_id', Integer, ForeignKey('permisions.id')),
                          Column('group_id', Integer, ForeignKey('groups.id'))
                          )


class Group(declarative_base):
    __tablename__ = 'groups'
    #
    id = Column(Integer, primary_key=True)
    group_name = Column(String)
    student = relationship('User')

    def __repr__(self):
        return f'{self.id} - {self.group_name}'


class PermisionGroup(declarative_base):
    __tablename__ = 'permisions'

    id = Column(Integer, primary_key=True)
    permision = Column(String)
    groups = relationship('Group', secondary=association_table, backref='group_permision')

    def __repr__(self):
        return f'{self.id} / {self.permision} / {self.groups}'


class User(declarative_base):
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
