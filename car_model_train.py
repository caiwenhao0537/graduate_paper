#-*-coding:utf-8 -*-
import pandas as pd
import numpy as np
#from Scikit_learn import scikit-multilearn
from pandas import DataFrame,Series
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn import tree
from sklearn.externals import joblib
from skmultilearn.problem_transform import BinaryRelevance
def accuracy(result_list,label_list):
    number=0
    for i in range(len(result_list)):
        if result_list[i]==label_list[i]:
            number+=1
    accuracy_result=number/len(result_list)
    return accuracy_result
#读取数据
data_file=pd.read_excel('D:\pydata\mypydata\paper_data\data1212\car\car_model_data2.xlsx',encoding='utf-8',header=0)
result_file=pd.read_excel('D:\pydata\mypydata\paper_data\data1212\car\car_model_data_result2.xlsx',encoding='utf-8',header=0)
test_file=pd.read_excel('D:\pydata\mypydata\paper_data\data1212\car\\test_data.xlsx',encoding='utf-8',header=0)
# print(type(data_file))
# print(result_file)
data_file2=data_file.as_matrix(columns=None)
result_file2=result_file.as_matrix(columns=['温度改善','温度恶化','复杂性改善','复杂性恶化','稳定性改善','稳定性恶化'])
# print(data_file_2)
# print(result_file2)
list_data=[]
list_test_data=[]
list_test_result=[]
list_result=[]
# for i in range(0,int(len(data_file)*0.8)):
#     list_data.append(list(data_file.ix[i]))
# for j in range(0,int(len(result_file)*0.8)):
#     list_result.append(list(result_file.ix[j]))
# for m in range(int(len(data_file)*0.8),len(data_file)):
#     list_test_data.append(list(data_file.ix[m]))
# for n in range(int(len(data_file)*0.8),len(data_file)):
#     list_test_result.append(list(result_file.ix[n]))
# #训练随机森林模型
rf=BinaryRelevance(RandomForestClassifier(n_estimators=200,max_features=15))
# rf=RandomForestClassifier(n_estimators=20000,max_features=15)
#rf.fit(list_data,list_result)
rf.fit(data_file2,result_file2)
joblib.dump(rf,'D:\pydata\mypydata\paper_data\data1212\car\\rf.pkl')
#随机森林模型预测结果
predict_result=rf.predict(test_file)
print(predict_result)
#jingdu=accuracy_score(list_test_result,predict_result)
#print(jingdu)
# print(predict_result)
# print(accuracy(predict_result,list_test_result))
#训练SVM模型
# clf = svm.SVC(C=10)
# clf.fit(list_data,list_result)
# joblib.dump(clf,'D:\pydata\mypydata\paper_data\data1212\car\SVM.pkl')
#SVM模型预测结果
#predict_result=clf.predict(list_test_data)
#训练决策树模型
# d_tree=tree.DecisionTreeClassifier()
# d_tree.fit(list_data,list_result)
# joblib.dump(d_tree,'D:\pydata\mypydata\paper_data\data1212\car\d_tree.pkl')
#决策树模型预测
#predict_result=d_tree.predict(list_test_data)

#print(predict_result)
# print(list_test_result)
# print(accuracy(predict_result,list_test_result))


#print(type(data_file))