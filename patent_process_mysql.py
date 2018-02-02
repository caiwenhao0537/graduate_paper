#-*- coding:utf-8 -*-
import pymysql
import re
import pandas as pd
import numpy
from pandas import Series,DataFrame
import nltk
from nltk.tokenize import word_tokenize
#获取停用词表
stop_words=open('D:\pydata\mypydata\paper_data\stop_words.txt','r')
stop_words_list=[]
for line in stop_words.readlines():
    stop_words_list.append(line.strip())
#文本保存
file_data=open('D:\pydata\mypydata\paper_data\data_1127\smart_wear.txt','a',encoding='utf-8')
#去停用词函数
def data_process_stop_words(stop_words,patent_text):
    patent_data_process=''
    patent_text_list=word_tokenize(patent_text)
    for word in patent_text_list:
        if word.lower() not in stop_words:
            patent_data_process=patent_data_process+word+' '
    return patent_data_process
def data_extract(data):
    pattern1 = r'(\b.*?\bSUMMARY)'
    pattern2 = r'(\b.*?\bBRIEF DESCRIPTION)'
    patent_data_text1=data['patent_text'].replace("\n","").strip()
    patent_data_text2=re.findall(pattern1,patent_data_text1)
    if len(patent_data_text2)==0:
        patent_data_text2=re.findall(pattern2,patent_data_text1)
    if len (patent_data_text2)==0:
        patent_data_text2=list(patent_data_text1)
    patent_data_text3=data_process_stop_words(stop_words_list,patent_data_text2[0])
    patent_data_text4=str(patent_data_text3)
    return patent_data_text4
#创建数据库参数
config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db': 'patent_data',
    'charset': 'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor
}
#连接数据库
db=pymysql.connect(**config)
#创建游标
cursor=db.cursor()
#执行SQL,并返回结果
def insert_data(i,i_2):
    number_tag=0
    result_extract=[]
    sql_select_text='select patent_text  from patent_data_car limit %d,%d'%(i,i_2)
    cursor.execute(sql_select_text)
    result_text=cursor.fetchall()
    for patent_text_dict in result_text:
        number_tag+=1
        dict_text=data_extract(patent_text_dict)
        #result_extract.append(dict_text)
        file_data.write(dict_text)
        file_data.write('\n')
        print('已处理%d条专利'%number_tag)
    #return result_extract
insert_data(43521,5000)
# sql_select_text = 'select patent_text  from patent_data_swear limit %d,%d' % (1, 4)
# cursor.execute(sql_select_text)
# result_text = cursor.fetchall()

#name_text = data_extract(result_text)
#print(name_text)
#result_text_process=data_process(stop_words_list,result_text)
# sql_insert_text='insert into patent_data_swear(patent_text_processed) VALUE '
#try_text=insert_data('patent_data_swear',0,5)
# i=0
# i_2=0
# while i+10<6678:
#     i_2=i+10
#     i=i_2
#     try_text=insert_data(i,i_2)
#     print(try_text)
#     sql_insert_text = 'insert into patent_data_swear(patent_text_processed) VALUES(%s) where index BETWEEN i AND i_2'
#     cursor.executemany(sql_insert_text, try_text)
#     db.commit()
#     print('已处理%d条专利'%i_2)
# else:
#     i_2=6678
#     try_text = insert_data(i, i_2)
#     sql_insert_text='insert into patent_data_swear(patent_text_processed) VALUES(%s) where index BETWEEN i AND i_2'
#     cursor.executemany(sql_insert_text, try_text)
#     db.commit()
#     print('已处理%d条专利'%i_2)
# #print(sql_insert_text)
# #cursor.executemany(sql_insert_text,try_text)
cursor.close()
db.close()
