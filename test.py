#-*-coding:utf-8 -*-
import pandas as pd
import numpy as np
import re

text='Hello,Are you ok? In my opinion,you areb very good!hi,arbyd boy.you must reduce your money.'
pattern_attribute_txt=open('D:\pydata\mypydata\paper_data\data0227\pattern_improve_worse.txt','r',encoding='utf-8_sig')
pattern_attribute_list=[]
for line in pattern_attribute_txt:
    pattern_attribute_list.append(str(line.strip()))


def parameter_attribute_extract(sentence,pattern_list):
    parameter_attribute_list=[]
    for pattern_word in pattern_list:
        p=re.compile(pattern_word,re.I)
        for i in p.findall(sentence):
            for j in i:
                if j not in[' ',',','\.']:
                    parameter_attribute_list.append(j)
    return parameter_attribute_list
print(parameter_attribute_extract(text,pattern_list))

