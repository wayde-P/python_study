menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
master = menu
last_layer = []

while True:
    for i in master:
        print(i)
    choice = input("请输入你的选择:").strip()
    if len(choice) == 0:
        continue
    if choice == 'b':
        master = last_layer[-1]
        last_layer.pop()
        continue
    if choice in master:
        last_layer.append(master)
        master = master[choice]
    else:
        print("error")
