from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, and_, or_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

Base = declarative_base()
# engine = create_engine("mysql+pymysql://zewei:zewei@192.168.50.116:3306/s15_13?charset=utf8", max_overflow=5)
engine = create_engine("mysql+pymysql://root:dianru@192.168.0.4:3306/zzw_host?charset=utf8", max_overflow=5)
Session = sessionmaker(bind=engine)
session = Session()


class service_line(Base):
    __tablename__ = 'service_line'
    sid = Column(Integer, primary_key=True, autoincrement=True)
    line_name = Column(String(10), nullable=False)


class users_type(Base):
    __tablename__ = 'users_type'
    tid = Column(Integer, primary_key=True, autoincrement=True)
    line_name = Column(String(10), nullable=False)


class users(Base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(10), nullable=False)
    password = Column(String(20), nullable=False)
    user_type = Column(Integer, ForeignKey('users_type.tid'), nullable=False)


class hosts(Base):
    __tablename__ = 'hosts'
    hid = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(20), nullable=False)
    to_service = Column(Integer, ForeignKey('service_line.sid'), nullable=ForeignKey)


class user_host_map(Base):
    __tablename__ = 'user_host_map'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.uid'), nullable=False)
    host_id = Column(Integer, ForeignKey('hosts.hid'), nullable=False)
    user = relationship('users', backref='users_relation')
    host = relationship('hosts', backref='hosts_relation')

    __table_args__ = (
        UniqueConstraint('user_id', 'host_id', name='uiq_user_host'),
    )

# Base.metadata.create_all(engine)

# select user,password
# ret = session.query(users).filter(user_name=zzw)
# print(ret)
# for i in ret:
#     print(i)
