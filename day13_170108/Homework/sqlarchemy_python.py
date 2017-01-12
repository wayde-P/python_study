from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("mysql+pymysql://root:dianru@192.168.0.4:3306/zzw_host?charset=utf8", max_overflow=5)
Session = sessionmaker(bind=engine)
session = Session()

# select user,password
ret = session.query('users.user_name').all()
print(ret)
# for i in ret:
#     print(i)
