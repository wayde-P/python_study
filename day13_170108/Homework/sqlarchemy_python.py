from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, and_, or_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("mysql+pymysql://zewei:zewei@192.168.50.116:3306/s15_13?charset=utf8", max_overflow=5)
# engine = create_engine("mysql+pymysql://root:dianru@192.168.0.4:3306/zzw_host?charset=utf8", max_overflow=5)
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
# # ret = session.query(users.user_name,users.password).filter_by(user_name='zzw').all()
# ret = session.query(users.uid).filter_by(user_name='zzw').delete()
# #print(ret[0][0:])
# print(ret)
# exit()
# for u,p in ret[0][0:] :
#     print(u,p)
login_status = False


def login():
    global login_status
    # while True:
    c_user_name = input("user: ").strip()
    c_password = input("password: ").strip()
    db_user_pass = session.query(users.user_name, users.password).filter_by(user_name=c_user_name).all()
    print(db_user_pass)
    if c_user_name == db_user_pass[0][0] and \
                    c_password == db_user_pass[0][1]:
        print("login sucsess !")

        login_status = True
    else:
        print("login error ! ")


# def db_add(table,*args,**kwargs):
#     info = table(kwargs)
#     session.add(info)
# 
# def db_delete(table,colunm,value,*args,**kwargs):
#     session.query(table.colunm).filter_by(colunm=value).delete()
# 
# 
# def db_update(table,colunm,value,new_value,*args,**kwargs):
#     session.query(table.colunm).filter_by(colunm=value).update({colunm:new_value})


def user_type_manager():
    function = ['add', 'delete', 'update', 'query']
    for i, o in enumerate(function):
        print(i + 1, o)
    function_choise = int(input("please choise >> ").strip())
    # print(function_choise,type(function_choise))
    if function_choise == 1:
        input_users_type = input("user type:").strip()
        db_users_type = users_type(line_name=input_users_type)
        session.add(db_users_type)
        session.commit()
    elif function_choise == 2:
        input_users_type = input("delete user type:").strip()
        session.query(users_type.line_name).filter_by(line_name=input_users_type).delete()
        session.commit()
    elif function_choise == 3:
        input_users_type = input("update user type:").strip()
        session.query(users_type.line_name).filter_by(line_name=input_users_type).update(
            {'line_name': input_users_type})
        session.commit()
    elif function_choise == 4:
        # print(session.query(users_type.tid,users_type.line_name).all())
        ret = session.query(users_type.tid, users_type.line_name).all()
        for i in ret:
            print(i)


def user_manager():
    function = ['add user', 'delete user', 'update user [user_type or password]', 'query user']
    for i, o in enumerate(function):
        print(i + 1, o)
    function_choise = int(input("please choise >> ").strip())
    # print(function_choise,type(function_choise))
    if function_choise == 1:
        input_user_name = input("user name:").strip()
        input_user_pass = input("user password :").strip()
        input_user_type = input("user type :").strip()
        db_user = users(user_name=input_user_name, password=input_user_pass, user_type=input_user_type)
        session.add(db_user)
        session.commit()
    elif function_choise == 2:
        input_user_name = input("delete user name:").strip()
        session.query(users.user_name).filter_by(user_name=input_user_name).delete()
        session.commit()
    elif function_choise == 3:
        input_user_name = input("user name:").strip()
        input_user_pass = input("user new password :").strip()
        input_user_type = input("user new type :").strip()
        session.query(users.user_name).filter_by(user_name=input_user_name).update({'user_name': input_user_name,
                                                                                    'password': input_user_pass,
                                                                                    'user_type': input_user_type})
        session.commit()
    elif function_choise == 4:
        # print(session.query(users_type.tid,users_type.line_name).all())
        ret = session.query(users.user_name, users_type.line_name).filter(users.user_type == users_type.tid).all()
        for i, o in enumerate(ret):
            print(i + 1, o)


def hosts_manager():
    function = ['add host', 'delete host', 'update host', 'query host']
    for i, o in enumerate(function):
        print(i + 1, o)
    function_choise = int(input("please choise >> ").strip())
    # print(function_choise,type(function_choise))
    if function_choise == 1:
        input_hosts_ip = input("host ip:").strip()
        input_hosts_service = input("host service:").strip()
        db_hosts = hosts(ip=input_hosts_ip)
        session.add(db_hosts)
        session.commit()
    elif function_choise == 2:
        input_hosts_ip = input("delete host type:").strip()
        session.query(hosts.line_name).filter_by(line_name=input_hosts_ip).delete()
        session.commit()
    elif function_choise == 3:
        input_hosts_ip = input("host ip:").strip()
        input_hosts_service = input("update host to service:").strip()
        session.query(hosts.ip).filter_by(ip=input_hosts_ip).update({'ip': input_hosts_ip,
                                                                     'to_service': input_hosts_service})
        session.commit()
    elif function_choise == 4:
        # print(session.query(hosts_ip.tid,hosts_ip.line_name).all())
        ret = session.query(hosts.ip, hosts.to_service).all()
        for i in ret:
            print(i)


def service_line_manager():
    function = ['add line', 'delete line', 'update line_name', 'query all line']
    for i, o in enumerate(function):
        print(i + 1, o)
    function_choise = int(input("please choise >> ").strip())
    if function_choise == 1:
        input_line_name = input("line name:").strip()
        db_service_line = service_line(line_name=input_line_name)
        session.add(db_service_line)
        session.commit()
    elif function_choise == 2:
        input_line_name = input("delete line name:").strip()
        session.query(service_line.line_name).filter_by(line_name=input_line_name).delete()
        session.commit()
    elif function_choise == 3:
        input_line_name = input("update line name:").strip()
        input_new_line_name = input("update new line name:").strip()
        session.query(service_line.line_name).filter_by(line_name=input_line_name).update(
            {'line_name': input_new_line_name})
        session.commit()
    elif function_choise == 4:
        # print(session.query(service_line.tid,service_line.line_name).all())
        ret = session.query(service_line.sid, service_line.line_name).all()
        for i in ret:
            print(i)


def user_host_map_manager():
    function = ['add host to user', 'delete host for user ', 'query user host']
    for i, o in enumerate(function):
        print(i + 1, o)
    function_choise = int(input("please choise >> ").strip())
    # print(function_choise,type(function_choise))
    if function_choise == 1:
        input_hosts_ip = input("host ip:").strip()
        input_hosts_service = input("host service:").strip()
        db_hosts = hosts(ip=input_hosts_ip)
        session.add(db_hosts)
        session.commit()
    elif function_choise == 2:
        input_hosts_ip = input("delete host type:").strip()
        session.query(hosts.line_name).filter_by(line_name=input_hosts_ip).delete()
        session.commit()
    elif function_choise == 3:
        input_hosts_ip = input("host ip:").strip()
        input_hosts_service = input("update host to service:").strip()
        session.query(hosts.ip).filter_by(ip=input_hosts_ip).update({'ip': input_hosts_ip,
                                                                     'to_service': input_hosts_service})
        session.commit()
    elif function_choise == 4:
        # print(session.query(hosts_ip.tid,hosts_ip.line_name).all())
        ret = session.query(hosts.ip, hosts.to_service).all()
        for i in ret:
            print(i)


# # user_type_manager()
# while True:
#     service_line_manager()
# exit()

dic = {1: user_manager,
       2: hosts_manager,
       3: service_line_manager,
       4: user_type_manager,
       5: user_host_map_manager}

while True:
    if login_status:
        function_list = ['用户管理', '主机管理', '业务线管理', '用户类型管理', '用户分配主机']
        for i, o in enumerate(function_list):
            print(i + 1, o)
        choise = int(input("选择功能: ").strip())
        if choise in dic.keys():
            dic[choise]()
        else:
            print("错误,请重新选择!")
    else:
        print("欢迎来到管理系统.")
        login()
        # todo
