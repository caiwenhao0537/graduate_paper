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

list_result=['静止物体的体积恶化','形状恶化']
list_result2=['移动物体的重量改善','静止物体的重量改善','移动物体的长度改善','静止物体的长度改善','移动物体的面积改善']
def parameter_attribute_change(parameter_result_list):
    attribute_list=[]
    result_list=[]
    for parameter_attribute in parameter_result_list:
        attribute_list.append(parameter_attribute[len(parameter_attribute)-2:])
    if len(list(set(attribute_list)))==1:
        for parameter_attribute in parameter_result_list[:len(parameter_result_list) - 1]:
            result_list.append(parameter_attribute)
        if list(set(attribute_list))[0]=='恶化':
            result1=parameter_result_list[-1]
            result2=str(result1[:len(result1)-2]) + '改善'
            result_list.append(result2)
        if list(set(attribute_list))[0]=='改善':
            result1=parameter_result_list[-1]
            result2=str(result1[:len(result1)-2]) + '恶化'
            result_list.append(result2)
    return result_list

print(parameter_attribute_change(list_result2))



parameter_attribute_change(list_result2)








