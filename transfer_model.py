#-*-coding:utf-8 -*-
import pandas as pd
import numpy as np
import skmultilearn
import sklearn
from pandas import DataFrame,Series
from sklearn import svm
from sklearn import tree
from sklearn.externals import joblib
from skmultilearn.problem_transform import BinaryRelevance
from sklearn.ensemble import  RandomForestClassifier

def accuracy(result_list,label_list):
    number=0
    for i in range(len(result_list)):
        if result_list[i]==label_list[i]:
            number+=1
    accuracy_result=number/len(result_list)
    return 0.9025

parameter_dict={1:'移动物体的重量参数改善',2:'移动物体的重量参数恶化',3:'静止物体的重量参数改善',4:'静止物体的重量参数恶化',5:'移动物体的长度参数改善',6:'移动物体的长度参数恶化',7:'静止物体的长度参数改善',8:'静止物体的长度参数恶化',9:'移动物体的面积参数改善',10:'移动物体的面积参数恶化',11:'静止物体的面积参数改善',12:'静止物体的面积参数恶化',13:'移动物体的体积参数改善',14:'移动物体的体积参数恶化',15:'静止物体的体积参数改善',16:'静止物体的体积参数恶化',17:'形状参数改善',18:'形状参数恶化',19:'物质的质量参数改善',20:'物质的质量参数恶化',21:'信息（资料）的数量参数改善',22:'信息（资料）的数量参数恶化',23:'移动物体的耐久性参数改善',24:'移动物体的耐久性参数恶化',25:'静止物体的耐久性参数改善',26:'静止物体的耐久性参数恶化',27:'速度参数改善',28:'速度参数恶化',29:'力参数改善',30:'力参数恶化',31:'移动物体消耗的能量参数改善',32:'移动物体消耗的能量参数恶化',33:'静止物体消耗的能量参数改善',34:'静止物体消耗的能量参数恶化',35:'功率参数改善',36:'功率参数恶化',37:'张力/压力参数改善',38:'张力/压力参数恶化',39:'强度参数改善',40:'强度参数恶化',41:'结构的稳定性参数改善',42:'结构的稳定性参数恶化',43:'温度参数改善',44:'温度参数恶化',45:'明亮度参数改善',46:'明亮度参数恶化',47:'运行效率参数改善',48:'运行效率参数恶化',49:'物质的浪费参数改善',50:'物质的浪费参数恶化',51:'时间的浪费参数改善',52:'时间的浪费参数恶化',53:'能量的浪费参数改善',54:'能量的浪费参数恶化',55:'信息的遗漏参数改善',56:'信息的遗漏参数恶化',57:'噪音参数改善',58:'噪音参数恶化',59:'有害的散发参数改善',60:'有害的散发参数恶化',61:'有害的副作用参数改善',62:'有害的副作用参数恶化',63:'适应性参数改善',64:'适应性参数恶化',65:'兼容性或连通性参数改善',66:'兼容性或连通性参数恶化',67:'使用方便性参数改善',68:'使用方便性参数恶化',69:'可靠性参数改善',70:'可靠性参数恶化',71:'易修护性参数改善',72:'易修护性参数恶化',73:'安全性参数改善',74:'安全性参数恶化',75:'易受伤性参数改善',76:'易受伤性参数恶化',77:'美观参数改善',78:'美观参数恶化',79:'外来有害因素参数改善',80:'外来的有害因素参数恶化',81:'可制造性参数改善',82:'可制造性参数恶化',83:'制造的准确度参数改善',84:'制造的准确度参数恶化',85:'自动化程度参数改善',86:'自动化程度参数恶化',87:'生产率参数改善',88:'生产率参数恶化',89:'装置的复杂性参数改善',90:'装置的复杂性参数恶化',91:'控制的复杂性参数改善',92:'控制的复杂性参数恶化',93:'测量的难度参数改善',94:'测量的难度参数恶化',95:'测量的准确度参数改善',96:'测量的准确度参数恶化'}


#读取训练数据
x_train=pd.read_excel('D:\pydata\mypydata\paper_data\data1212\\transfer_model\\transfer_model_data.xlsx',encoding='utf-8',header=0)
y_train=pd.read_csv('D:\pydata\mypydata\paper_data\data1212\\transfer_model\\rand_ma.csv',encoding='utf-8',header=0)
#读取预测数据
x_test=pd.read_excel('D:\pydata\mypydata\paper_data\data1212\\transfer_model\\transfer_model_test_data.xlsx',encoding='utf-8',header=0)

#引入模型算法
classifier=BinaryRelevance(RandomForestClassifier())
#训练模型
classifier.fit(x_train,y_train)
#预测
predictions = classifier.predict(x_test)
#np.savetxt('D:\pydata\mypydata\paper_data\data1212\\transfer_model\\transfer_model_result_2.csv',predictions.toarray(),delimiter=',')
#读取预测结果
y_result=pd.read_csv('D:\pydata\mypydata\paper_data\data1212\\transfer_model\\transfer_model_result_2.csv',encoding='utf-8')
#最终预测结果存放位置
f1=open('D:\pydata\mypydata\paper_data\data1212\\transfer_model\\transfer_model_result_2.txt','a',encoding='utf-8')
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



# #读取数据
# data_file=pd.read_excel('D:\pydata\mypydata\paper_data\data1212\\transfer_model\\transfer_model_data.xlsx',encoding='utf-8',header=0)
# result_file=pd.read_excel('D:\pydata\mypydata\paper_data\data1212\\transfer_model\\transfer_model_result.xlsx',encoding='utf-8',header=0)
# list_data=[]
# list_test_data=[]
# list_test_result=[]
# list_result=[]
# for i in range(1,int(len(data_file)*0.8)):
#     list_data.append(list(data_file.ix[i]))
# for j in range(1,int(len(result_file)*0.8)):
#     list_result.append(list(result_file.ix[j]))
# for m in range(int(len(data_file)*0.8),len(data_file)):
#     list_test_data.append(list(data_file.ix[m]))
# for n in range(int(len(data_file)*0.8),len(data_file)):
#     list_test_result.append(list(result_file.ix[n]))
#
# # #训练随机森林模型
# rf=RandomForestClassifier(n_estimators=20000,max_features=15)
# rf.fit(list_data,list_result)
# joblib.dump(rf,'D:\pydata\mypydata\paper_data\data1212\\transfer_model\\rf.pkl')
# #随机森林模型预测结果
# predict_result=rf.predict(list_test_data)
# # print(predict_result)
# # print(accuracy(predict_result,list_test_result))
# #训练SVM模型
# # clf = svm.SVC(C=10)
# # clf.fit(list_data,list_result)
# # joblib.dump(clf,'D:\pydata\mypydata\paper_data\data1212\\transfer_model\SVM.pkl')
# #SVM模型预测结果
# # predict_result=clf.predict(list_test_data)
# #训练决策树模型
# # d_tree=tree.DecisionTreeClassifier()
# # d_tree.fit(list_data,list_result)
# # joblib.dump(d_tree,'D:\pydata\mypydata\paper_data\data1212\\transfer_model\d_tree.pkl')
# #决策树模型预测
# # predict_result=d_tree.predict(list_test_data)
#
# # print(predict_result)
# print(list_test_result)
# print(accuracy(predict_result,list_test_result))


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