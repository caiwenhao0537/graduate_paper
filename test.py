#-*-coding:utf-8 -*-
import pandas as pd
import numpy as np
import fileinput
data=open('D:\pydata\mypydata\paper_data\data0227\smart_wear_0307.txt','r',encoding='utf-8')
data2=open('D:\pydata\mypydata\paper_data\data0227\smart_wear_0307_2.txt','a',encoding='utf-8')
j=0
for line in data:
    j=j+1
    i=0
    for word in line:
        i=i+1
        if word==' ':
            line=line[:i-1]+'&'+line[i:]
            data2.write(line)
            #data2.write('\n')
            break
    print('已处理%d行'%j)
data.close()
data2.close()
