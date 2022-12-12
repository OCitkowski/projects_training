from sqlalchemy import create_engine


class Base():
    def __init__(self, declarative_base, name_base: str):
        self.declarative_base = declarative_base
        self.name_base = name_base  # "sqlite:///xxx.sqlite3"
        self.engine = create_engine(self.declarative_base, echo=True)

    def create_base(self):
        base = self.declarative_base
        base.metadata.create_all(self.engine)
        return base
