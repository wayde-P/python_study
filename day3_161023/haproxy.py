import json
read = input('请输入要添加的记录:')
config_file = "haproxy.txt"  # 配置文件
try:
    con_dic = json.loads(read)  # 转换为字典
    print(con_dic)
    tmp_backend = con_dic['backend']
    print(tmp_backend)
    tmp_record_dic = con_dic['record']
    print("tmp_record_dic:::",tmp_record_dic)
    val_format = ' ' * 8
    backend = 'backend {0}'.format(tmp_backend)
    record = '{0}server {1} weight {2} maxconn {3}'.format(val_format, tmp_record_dic['server'],
                                                           tmp_record_dic['weight'], tmp_record_dic['maxconn'])
    print("recode ::: ",record)

except Exception as ex:
    print(ex)
    exit('输入错误,请输入如下格式{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}')
