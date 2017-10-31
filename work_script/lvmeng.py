import requests
import random
import time
import socket
import http.client
from bs4 import BeautifulSoup

def get_content(url , data = None):
    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/4.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.get(url,headers = header,timeout = timeout)
            rep.encoding = 'utf-8'
            break
        except socket.timeout as e:
            print( '3:', e)
            time.sleep(random.choice(range(8,15)))

        except socket.error as e:
            print( '4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print( '5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print( '6:', e)
            time.sleep(random.choice(range(5, 15)))

    return rep.text

url ='http://www.nsfocus.net/index.php?os=Linux&type_id=3&keyword=&act=sec_bug&submit=+'
html = get_content(url)

# print(html)
bs=BeautifulSoup(html,"html.parser")


tiaoshu_div=bs.body.find('div',{"class":"page"})

# print(tiaoshu_div)
pages=[]
for string in tiaoshu_div.stripped_strings:
    pages.append(repr(string))
    # print(pages)

count_num=pages[-1].split(" ")[1]
print(count_num)
# with open
