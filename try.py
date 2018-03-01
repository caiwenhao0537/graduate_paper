import re
import random
import numpy as np
import pandas as pd
from pandas import DataFrame,Series
a=np.random.randint(0,1,size=[1463,96])
list_cs=list(range(0,96))

for i in range(1,len(a)):
    b=np.random.randint(2,5)
    selected_list = random.sample(list_cs, b)
    for j in selected_list:
        a[i][j]=1
#print(a[1][1])
np.savetxt('D:\pydata\mypydata\paper_data\data1212\\transfer_model\\rand_ma.csv',a,delimiter=',')
# str1="it mostly is you that make the things bad. it is Jim who saved me. it like me .So I think you should apologize to Bob"
# pattern="^it.*is.*that.*\."
# str2=re.findall(pattern,str1)
# print(str2)

# train_corpus = "D:\pythonproject\graduate_paper\doc2vec-master\\toy_data/train_docs.txt"
# f=open(train_corpus,encoding='utf-8')
# line=f.readlines()
# for j in line:
#     print(j)

import pandas as pd
from pandas import DataFrame,Series

# f=open('D:\pydata\mypydata\paper_data\plane.txt','a')
# data=pd.read_csv('D:\pydata\mypydata\paper_data\car.csv',encoding='gbk')
# for m in range(0,len(data)):
#     data_get=data.ix[m:m,['集成数据']]
#     for i in data_get.values:
#         for j in i:
#             f.write(j+'\n')
#     print('已处理%d条'%m)
# f.close()

# data=pd.read_csv('D:\pydata\mypydata\paper_data\car1024.csv',encoding='gbk')
# pattern="(.*?)BRIEF DESCRIPTION OF THE DRAWINGS.*"
# for m in range(1,2):
#     data_get=data.ix[m:m,['集成数据']]
#
#     for i in data_get.values:
#         for j in i:
#             print(j)
#             result=''
#             #result=re.findall(pattern,j,re.S)[0]
#             #print(result)
#             #data.ix[m:m,['集成数据']]=result
#     print('已处理%d条' % m)
# pattern="(.*?)(USE/ADVANTAGE|ADVANTAGE|USE)(.*)"
# stop_word=[]
# f=open('D:\pydata\mypydata\paper_data\stop_words.txt','r')
# for m in f.readlines():
#     stop_word.append(m.strip('\n').strip(' '))
# f1=open('D:\pydata\mypydata\paper_data\plane_processed_2.txt','r')
# for i in f1.readlines():
#     print(i)
#print(f1.readline())
# f2=open('D:\pydata\mypydata\paper_data\plane_processed.txt','r',encoding='utf-8_sig')
# number=0
#
# for j in f2.readlines():
#     number+=1
#     result=''
#     result3=''
#     test=j.strip().split()
#     for i in test:
#         if i.lower() not in stop_word:
#             result=result+i+' '
#     result2=re.findall(pattern,result,re.S)
#     #print(result2[0][0])
#     if len(result2)>0:
#         result3=result2[0][0]+result2[0][2]
#         f1.write(result3+'\n')
#     else:
#         f1.write(result+'\n')
#     print("已处理%d条"%number)
# print("处理完毕！")


#data.to_csv('D:\pydata\mypydata\paper_data\car1024_1.csv')






