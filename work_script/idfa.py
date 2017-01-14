# #取出日志里面的固定字段
# import re
#
# with open("log",encoding='utf-8') as log_file:
#     while True:
#         line = log_file.readline()
#         if len(line) == 0:
#             break
#         else:
#             channel = re.search("&channel\=([\w\d\-\_\:]+)?\&",line).group().strip("&")
#             idfa = re.search("&idfa\=([\d\w]+)?&",line).group().strip("&")
#             d = re.search("&d\=[\d\w\-\_\ ]+",line).group().strip("&")
#             mac = re.search("&mac\=([\d\w\:]+)?&",line).group().strip("&")
#             time = re.search("&time\=\d+",line).group().strip("&")
#             print(channel,time,idfa,d,mac)


def test(*aw, **aws):
    print("aw", aw)
    print("aws", aws)


test(1, 333, a=(33, 33))
