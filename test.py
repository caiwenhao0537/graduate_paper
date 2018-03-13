#-*-coding:utf-8 -*-
import pandas as pd
import numpy as np
import re
import random
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()
#
# word='conducive to'
# print(lem.lemmatize(word,"v"))

parameter_dict=['移动物体的重量','静止物体的重量','移动物体的长度','静止物体的长度','移动物体的面积','静止物体的面积','移动物体的体积','静止物体的体积','形状','物质的质量','信息（资料）的数量','移动物体的耐久性','静止物体的耐久性','速度','力','移动物体消耗的能量','静止物体消耗的能量','功率','张力/压力','强度','结构的稳定性','温度','明亮度','运行效率','物质的浪费','时间的浪费','能量的浪费','信息的遗漏','噪音','有害的散发','有害的副作用','适应性','兼容性或连通性','使用方便性','可靠性','易修护性','安全性','易受伤性','美观','外来有害因素','可制造性','制造的准确度','自动化程度','生产率','装置的复杂性','控制的复杂性','测量的难度','测量的准确度']

data=open('D:\pydata\mypydata\paper_data\data0227\parameter_improve_worse.txt','r',encoding='utf-8')

def parameter_and_attribute_dict(attibute_data):
    parameter_attribute_dit = {}
    parameter_num = 0
    for line in attibute_data:
        parameter_attribute_list=[]
        parameter_and_attribute_list=[]
        list2=[]
        for words in line.strip().split('&'):
            parameter_attribute_list.append(words.split())
        parameter_and_attribute_list.append(parameter_dict[parameter_num])
        parameter_and_attribute_list.append(parameter_attribute_list)
        list2.append(parameter_and_attribute_list)
        parameter_attribute_dit.update(dict(list2))
        parameter_num+=1
    return parameter_attribute_dit

result_dict=parameter_and_attribute_dict(data)
attribute_result_list=['改善','恶化']
parameter_list=['安全性','装置的复杂性']
parameter_attribute_list=['enhance']
def parameter_attribute_judge(parameter_list,parameter_attribute_list):
    result=[]
    attribute_word_list=[]
    for attribute_word in parameter_attribute_list:
        attribute_word_list.append(lem.lemmatize(attribute_word,"v"))
    for parameter in parameter_list:
        parameter_improve_word_list=[]
        parameter_worse_word_list=[]
        for parameter_attribute_improve_word in result_dict[parameter][0]:
            parameter_improve_word_list.append(lem.lemmatize(parameter_attribute_improve_word,"v"))
        for parameter_attribute_worse_word in result_dict[parameter][1]:
            parameter_worse_word_list.append(lem.lemmatize(parameter_attribute_worse_word,"v"))
        for word in attribute_word_list:
            if word in parameter_improve_word_list:
                result.append('%s改善'%parameter)
            elif word in parameter_worse_word_list:
                    result.append('%s恶化'%parameter)
        if len(result)==0:
            attribute_result=attribute_result_list[random.randint(0,1)]
            result.append('%s%s'%(parameter,attribute_result))
    return result
print(parameter_attribute_judge(parameter_list,parameter_attribute_list))







