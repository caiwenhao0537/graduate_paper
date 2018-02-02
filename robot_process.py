#-*- coding:utf-8 -*-
import re
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import pymysql
import nltk
from nltk.tokenize import word_tokenize
text_robot=open('D:\pydata\mypydata\paper_data\data_robot\patent_data2.txt','a',encoding='utf-8')
pattern1=r'(\b.*?\bSUMMARY)'
pattern2=r'(\b.*?\bBRIEF DESCRIPTION)'
stop_words_list=[]
stop_words_text=open('D:\pydata\mypydata\paper_data\stop_words.txt','r')
for line in stop_words_text.readlines():
    stop_words_list.append(line.strip())
def stop_words(stop_word_list,patent_text):
    patent_data_process=''
    patent_text_list=[]
    sens=nltk.sent_tokenize(patent_text,language='english')
    for sent in sens:
        for words in word_tokenize(sent):
            patent_text_list.append(words)
    for word in patent_text_list:
        if word.lower() not in stop_words_list:
            patent_data_process=patent_data_process+word+' '
    return patent_data_process

def extract(data_extract):
    for j in range(0, len(data_extract)):
        print("正在处理第%d条专利"%(j+4776))
        str_data1 = str(data_extract[j])
        str_data2 = str_data1.replace("\n", "").strip()
        result = re.findall(pattern1, str_data2)
        if len(result)==0:
            result=re.findall(pattern2,str_data2)
        if len(result)==0:
            result=list(str_data2)
        result_process=stop_words(stop_words_list,result[0])
        data_extract[j] = result_process
        text_robot.write(result_process)
        text_robot.write('\n')

def integrate(i):
    sql_1 = "select * from patent_data_robot2 limit 4776,9382"
    cur.execute(sql_1)
    data = cur.fetchall()
    data_pandas = DataFrame(list(data))
    #print(data_pandas)
    data_pandas.columns = ['公开号', '标题', 'IPC_德温特', '施引专利', '摘要', '说明书', 'IPC_现版', '德温特手工代码', '德温特分类码', '集成数据']
    data_pandas['集成数据'] = data_pandas['标题'] + data_pandas['摘要'] + data_pandas['说明书']
        #print(type(data_pandas['集成数据']))
        #print(data_pandas['集成数据'])
    extract(data_pandas['集成数据'])
    #data_pandas['集成数据'].drop([0],inplace=True)
        #print(data_pandas['集成数据'])
    #data_pandas['集成数据'].to_csv('D:\pydata\mypydata\paper_data\data_robot\patent_data1.txt', encoding='utf-8',index=False)
    #print("已处理%d条"%i)
    # else:
    #     sql_1 = "select * from patent_data_robot2 limit %d,%d" % (i, 9383)
    #     cur.execute(sql_1)
    #     data = cur.fetchall()
    #     data_pandas = DataFrame(list(data))
    #     data_pandas.columns = ['公开号', '标题', 'IPC_德温特', '施引专利', '摘要', '说明书', 'IPC_现版', '德温特手工代码', '德温特分类码', '集成数据']
    #     data_pandas['集成数据'] = str(data_pandas['标题']) + str(data_pandas['摘要']) + str(data_pandas['说明书'])
    #     data_pandas['集成数据'].to_csv('D:\pydata\mypydata\paper_data\data_robot\patent_data1.csv', 'a', encoding='utf-8')
    #     print("已处理完毕！")

conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='patent_data',port=3306,charset='utf8')
cur=conn.cursor()#获取一个游标
integrate(0)

    # for col_name in data:
    #     str1=''
    #     for p_num in col_name[0:1]:
    #         patent_num=str(p_num)
    #     for d in col_name[1:4]:
    #         str1=str1+' '+str(d)
    #     print(str1)
    #     #print(patent_num)
    #     #print(d[5:5])
    # sql_2="insert into patent_data_robot('集成数据') VALUES (%s) WHERE 公开号=%s"%(str1,patent_num)
    # cur.execute(sql_2)
    # conn.commit()
cur.close()#关闭游标
conn.close()#释放数据库资源
# except Exception:
#     conn.rollback()
#     print("查询失败")


