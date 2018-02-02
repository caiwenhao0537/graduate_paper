#-*- coding:utf-8 -*-
import skmultilearn
import sklearn
import scipy
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.ensemble import  RandomForestClassifier
from sklearn import svm
#工程参数字典
parameter_dict={1:'移动物体的重量',2:'静止物体的重量',3:'移动物体的长度',4:'静止物体的长度',5:'移动物体的面积',6:'静止物体的面积',7:'移动物体的体积',8:'静止物体的体积',9:'形状',10:'物质的质量',11:'信息（资料）的数量',12:'移动物体的耐久性',13:'静止物体的耐久性',14:'速度',15:'力',16:'移动物体消耗的能量',17:'静止物体消耗的能量',18:'功率',19:'张力/压力',20:'强度',21:'结构的稳定性',22:'温度',23:'明亮度',24:'运行效率',25:'物质的浪费',26:'时间的浪费',27:'能量的浪费',28:'信息的遗漏',29:'噪音',30:'有害的散发',31:'有害的副作用',32:'适应性',33:'兼容性或连通性',34:'使用方便性',35:'可靠性',36:'易修护性',37:'安全性',38:'易受伤性',39:'美观',40:'外来有害因素',41:'可制造性',42:'制造的准确度',43:'自动化程度',44:'生产率',45:'装置的复杂性',46:'控制的复杂性',47:'测量的难度',48:'测量的准确度'}

#读取训练数据及标签数据
# x_train=pd.read_excel('D:\pydata\mypydata\paper_data\data_robot\patent_data_vector.xlsx',encoding='utf-8')
# y_train=pd.read_csv('D:\pydata\mypydata\paper_data\data_robot\\rand_ma.csv',encoding='utf-8')
# x_test=pd.read_excel('D:\pydata\mypydata\paper_data\data_robot\patent_robot_test.xlsx',encoding='utf-8')
# y_test=pd.read_excel('D:\pydata\mypydata\paper_data\data_robot\patent_robot_test_result.xlsx',encoding='utf-8')

#classifier=BinaryRelevance(RandomForestClassifier())

#print(y_train.values)
#训练模型
#classifier.fit(x_train,y_train)

#预测
#predictions = classifier.predict(x_test)
#print(predictions)
#print(predictions.toarray())
#np.savetxt('D:\pydata\mypydata\paper_data\data_robot\patent_robot_test_result_2.csv',predictions.toarray(),delimiter=',')

#读取预测结果
y_result=pd.read_csv('D:\pydata\mypydata\paper_data\data_robot\patent_robot_test_result_2.csv',encoding='utf-8')
#最终预测结果存放位置
f1=open('D:\pydata\mypydata\paper_data\data_robot\patent_robot_test_result_2.txt','a',encoding='utf-8')
#预测结果翻译为中文工程参数
def result_transfer(result_data):
    for i in range(0,len(result_data)):
        patent_parameter=[]
        predict_result=y_result.irow(i).values
        patent_parameter.append(predict_result[0])
        for j in range(1,len(predict_result)):
            if predict_result[j]==1:
                patent_parameter.append(parameter_dict[j+1])
        for word in patent_parameter:
            f1.write(str(word))
            f1.write(' ')
        f1.write('\n')

result_transfer(y_result)


