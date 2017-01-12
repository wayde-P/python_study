# MySQL
# pymysql
# pip3 install sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

Base = declarative_base()


# 创建单表
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    extra = Column(String(16))


# 一对多
# 篮球、足球、乒乓球、玻璃球
class Hobby(Base):
    __tablename__ = 'hobby'
    nid = Column(Integer, primary_key=True)
    caption = Column(String(50), default='red', unique=True)


class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    hobby_id = Column(Integer, ForeignKey("hobby.nid"))
    # 专门用户简化查询或者增加的操作
    hobby = relationship("Hobby", backref='persons')


# 多对多
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True, nullable=False)
    # g2s
    g2s = relationship("Server", secondary="servertogroup", backref='s2g')


class Server(Base):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    # s2g


class ServerToGroup(Base):
    __tablename__ = 'servertogroup'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))

    # server = relationship("Server", backref='s2g')
    # group = relationship("Group", backref='g2s')

    __table_args__ = (
        UniqueConstraint('server_id', 'group_id', name='uix_server_group'),
    )


# session.query(Person).join(Hobby).all()


def init_db():
    engine = create_engine("mysql+pymysql://root:123456@192.168.12.233:3306/s15day13?charset=utf8", max_overflow=5)
    Base.metadata.create_all(engine)


def drop_db():
    engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/t1", max_overflow=5)
    Base.metadata.drop_all(engine)


# init_db()
# drop_db
######################## 一对多和多对多操作

engine = create_engine("mysql+pymysql://root:123456@192.168.12.233:3306/s15day13?charset=utf8", max_overflow=5)

Session = sessionmaker(bind=engine)
session = Session()
############## 增加操作 ################
# session.add_all([
#     Group(name='车商城'),
#     Group(name='咨询'),
#     Group(name='广告'),
# ])
# session.commit()

# session.add_all([
#     Server(hostname='c1'),
#     Server(hostname='c2'),
#     Server(hostname='c3'),
# ])
# session.commit()

# session.add_all([
#     ServerToGroup(server_id=1,group_id=3),
#     ServerToGroup(server_id=5,group_id=3),
#     ServerToGroup(server_id=5,group_id=1),
#     # ServerToGroup(server_id=1,group_id=2),
#     # ServerToGroup(server_id=2,group_id=1),
#     # ServerToGroup(server_id=3,group_id=1),
# ])
# session.commit()

# v = session.query(Person,Hobby.caption).join(Hobby).all()
# for row in v:
#     print(row,type(row))


# v = session.query(ServerToGroup,Server.hostname,Group.name).join(Server).join(Group).filter(Server.id==1).all()
# for row in v:
#     print(row)

##### 创建关系
# obj = session.query(Person).filter(Person.nid==1).first()
# print(obj.nid,obj.name,obj.hobby_id,obj.hobby.caption)

# obj = session.query(Hobby).filter(Hobby.nid == 1).first()
# print(obj.nid,obj.caption,obj.persons)
# for row in obj.persons:
#     print(row.name)

# session.add(Person(nid=11,name='liufeng2',hobby=session.query(Hobby).filter(Hobby.nid==3).first()))
# session.commit()

# relationship
# 跨表查询
# 增加相关联的数据

# v = session.query(ServerToGroup).all()
# for row in v:
#     print(row.server.hostname, row.group.name)


# obj = session.query(Group).filter(Group.id==1).first()
# print(obj.id,obj.name,obj.g2s) # [第三张表]
# for row in obj.g2s:
#     print(row.server_id,row.group_id,row.server.hostname)

# obj = session.query(Group).filter(Group.id==1).first()
# print(obj.id,obj.name,obj.g2s)
# for row in obj.g2s:
#     print(row.hostname)



#
# engine = create_engine("mysql+pymysql://root:123456@192.168.12.233:3306/s15day13?charset=utf8", max_overflow=5)
#
# Session = sessionmaker(bind=engine)
# session = Session()

# 添加一条信息
# obj1 = Users(id=1,name='root',extra='...')
# session.add(obj1)
# 添加多条
# session.add_all([
#     Users(id=2,name='root2',extra='...'),
#     Users(id=3,name='root3',extra='...'),
# ])
# session.commit()

# 删除
# session.query(Users).filter(Users.id == 1).delete()
# session.commit()

# 改
# session.query(Users).filter(Users.id==2,Users.name=="root2").update({Users.name:"root1"})
# session.commit()

# session.query(Users).filter(Users.id==2,Users.name=="root1").update({"name":"root111"})
# session.commit()
# ****
# session.query(Users).filter(Users.id==2,Users.name=="root1").update({"name":Users.name + 1},synchronize_session="evaluate")
# session.commit()

# 获取全部数据
# v = session.query(Users).all()
# for row in v:
#     print(row.id,row.name,row.extra)

# 获取第一条数据
# v = session.query(Users).first()
# print(v)

# session.query(Users).filter(Users.id==2)
# session.query(Users).filter(Users.id==2,Users.name=="root1")
# session.query(Users).filter(Users.id==2)
#
# v = session.query(Users).filter_by(id=2).all()
# print(v)
# 获取指定映射
# v = session.query(Users.id,Users.name)
# print(v)

# session.query(Users).filter(Users.id==2, Users.name=="root1")
# from sqlalchemy import and_,or_
# session.query(Users).filter(and_(Users.id==2, Users.name=="root1"))
#
# session.query(Users).filter(or_(Users.id < 2, Users.name == 'eric'),Users.extra=='...').all()

# session.add_all([
#     Users(id=4,name='root2',extra='...'),
#     Users(id=5,name='root3',extra='...'),
#     Users(id=6,name='root2',extra='...'),
# ])
# session.commit()

# from sqlalchemy.sql import func
#
# ret = session.query(
#     func.max(Users.id),
#     func.sum(Users.id),
#     func.min(Users.id)).group_by(Users.name).all()
#
# for item in ret:
#     print(item[0],item[1],item[2])# __getitem__


# session.query(Users, Favor)

# session.query(Person).join(Favor, and_(Person.id == Favor.nid)).all()
# session.query(Person).join(Favor).all()


# session.add_all([
#     Hobby(nid=1,caption='篮球'),
#     Hobby(nid=2,caption='足球'),
#     Hobby(nid=3,caption='棒球')
# ])
# session.commit()



# session.add_all([
#     Person(nid=1,name='alex1',hobby_id=1),
#     Person(nid=2,name='alex2',hobby_id=2),
#     Person(nid=3,name='alex3',hobby_id=1),
# ])
# session.commit()

# v = session.query(Person).join(Hobby,isouter=True)
# print(v)
