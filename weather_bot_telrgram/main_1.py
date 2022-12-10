from sqlalchemy.orm import declarative_base, sessionmaker
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import Sequence
from faker import Faker

engine = create_engine("sqlite:///xxx.sqlite3", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f"{self.name} {self.fullname} {self.nickname}"


if __name__ == '__main__':

    session = Session()
    Base.metadata.create_all(engine)

    fake = Faker()

    'ku'.split(" ")
    for i in range(555):
        print(i)
        fa = fake.name()
        name = fa.split(" ")[0]
        nickname = fa.split(" ")[1]

        ed_user = User(name=name, fullname=fa, nickname=nickname)
        session.add(ed_user)

    session.commit()
    session.close()
