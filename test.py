#-*-coding:utf-8 -*-
import pandas as pd
import numpy as np
import re

def sentence_extract(patent_txt,patterns):#patent_txt为一篇专利的文本文档，patterns为正则表达式列表
    sentence_list=[]
    patent_sentence=patent_txt.split('.')
    for sentence in patent_sentence:
        for pattern_word in patterns:
            p=re.compile(pattern_word)
            data=p.findall(sentence.strip())
            if len(data)>0:
                for i in data:
                    sentence_list.append(i)
    return sentence_list
pattern_txt=open('D:\pythonproject\graduate_paper\pattern_0309.txt','r',encoding='utf-8')
pattern_list=[]
for line in pattern_txt:
    pattern_list.append(str(line.strip()))
data=pd.read_excel('D:\pydata\mypydata\paper_data\data0227\smart_wear_0302.xlsx')
patent_dict={}
for i in range(1,9):
    patent_list=[]
    patent_list2=[]
    patent_list.append(data.irow(i)['专利号'])
    print(sentence_extract(data.irow(i)['专利文本'],pattern_list))
    patent_list.append(sentence_extract(data.irow(i)['专利文本'],pattern_list))
    patent_list2.append(patent_list)
    #print(patent_list2)
    patent_dict.update(dict(patent_list2))
print(patent_dict)

