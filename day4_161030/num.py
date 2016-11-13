count = 0
with open("info",'r',encoding='utf-8') as r_file,open("user_new",'w+',encoding='utf-8') as w_file:
    for i in r_file:
        count +=1
        w_file.write("%s,%s"%(count,i))