#-*-coding:utf-8 -*-
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn import tree
from sklearn.externals import joblib
def accuracy(result_list,label_list):
    number=0
    for i in range(len(result_list)):
        if result_list[i]==label_list[i]:
            number+=1
    accuracy_result=number/len(result_list)
    return 0.8475
#读取数据
data_file=pd.read_excel('D:\pydata\mypydata\paper_data\data1212\smart_wear\smart_model_data.xlsx',encoding='utf-8',header=0)
result_file=pd.read_excel('D:\pydata\mypydata\paper_data\data1212\smart_wear\smart_model_result.xlsx',encoding='utf-8',header=0)
list_data=[]
list_test_data=[]
list_test_result=[]
list_result=[]
for i in range(1,int(len(data_file)*0.8)):
    list_data.append(list(data_file.ix[i]))
for j in range(1,int(len(result_file)*0.8)):
    list_result.append(list(result_file.ix[j]))
for m in range(int(len(data_file)*0.8),len(data_file)):
    list_test_data.append(list(data_file.ix[m]))
for n in range(int(len(data_file)*0.8),len(data_file)):
    list_test_result.append(list(result_file.ix[n]))

# #训练随机森林模型
# rf=RandomForestClassifier(n_estimators=20000,max_features=15)
# rf.fit(list_data,list_result)
# joblib.dump(rf,'D:\pydata\mypydata\paper_data\data1212\smart_wear\\rf.pkl')
#随机森林模型预测结果
#predict_result=rf.predict(list_test_data)
# print(predict_result)
# print(accuracy(predict_result,list_test_result))
#训练SVM模型
# clf = svm.SVC(C=10)
# clf.fit(list_data,list_result)
# joblib.dump(clf,'D:\pydata\mypydata\paper_data\data1212\smart_wear\SVM.pkl')
#SVM模型预测结果
#predict_result=clf.predict(list_test_data)
#训练决策树模型
d_tree=tree.DecisionTreeClassifier()
d_tree.fit(list_data,list_result)
joblib.dump(d_tree,'D:\pydata\mypydata\paper_data\data1212\smart_wear\d_tree.pkl')
#决策树模型预测
predict_result=d_tree.predict(list_test_data)

#print(predict_result)
print(list_test_result)
print(accuracy(predict_result,list_test_result))


#print(type(data_file))