from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

Base = declarative_base()


class user(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    extra = Column(String(16))


def init_db():
    engine = create_engine("mysql+pymysql://root:root@192.168.123.134:5001/s15?charset=utf8", max_overflow=5)
    Base.metadata.create_all(engine)


def drop_db():
    engine = create_engine("mysql+pymysql://root:123@127.0.0.1:5001/t1", max_overflow=5)
    Base.metadata.drop_all(engine)


# init_db()
engine = create_engine("mysql+pymysql://root:root@192.168.123.134:5001/s15?charset=utf8", max_overflow=5)
Session = sessionmaker(bind=engine)
session = Session()

obj1 = user(id=1, name='root', extra='123')
session.add(obj1)
session.add_all(
    user(id=2, name='root2', extra='1232'),

    user(id=3, name='root3', extra='1233'),

    user(id=4, name='root4', extra='1234'),
)
