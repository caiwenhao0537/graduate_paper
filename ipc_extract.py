#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import operator
import pymysql
from numpy import random
from pandas import DataFrame,Series
#创建数据库连接
dbconn=pymysql.connect(
    host='localhost',
    port=3306,
    database='patent_data',
    user='root',
    password='123456'
)
#读取提供参考专利的专利数据
sql_car="select * from patent_data_car_ipc"
patent_datas_car=pd.read_sql(sql_car,dbconn)
patent_datas_car.columns=['公开号','IPC']
sql_swear="select * from patent_data_swear_ipc"
patent_datas_swear=pd.read_sql(sql_swear,dbconn)
patent_datas_swear.columns=['公开号','IPC']
patent_datas_robot=pd.read_csv('D:\pydata\mypydata\paper_data\data_robot\patent_data_robot2_ipc.csv',encoding='utf-8')
patent_datas_robot.columns=['公开号','IPC','德温特分类','德温特手工代码']
#读取待规避专利数据
patent_DA=pd.read_excel('D:\pydata\mypydata\paper_data\data_robot\patent_need_DA.xlsx',encoding='utf-8')
patent_DA.columns=['公开号','IPC','德温特分类','德温特手工代码']
#相似度结果存放位置
result_robot_file=open('D:\pydata\mypydata\paper_data\data_robot\\result_recommend\\result_robot_dict.txt','a',encoding='utf-8')
result_car_file=open('D:\pydata\mypydata\paper_data\data_robot\\result_recommend\\result_car_dict.txt','a',encoding='utf-8')
result_swear_file=open('D:\pydata\mypydata\paper_data\data_robot\\result_recommend\\result_swear_dict.txt','a',encoding='utf-8')


#切分函数，利用'|'切分字符串
def extract(data_ipc):
    if data_ipc==data_ipc:
        ipc_data_list=[]
        for ipc in data_ipc.split('|'):
            ipc_data_list.append(ipc.strip())
        return ipc_data_list
    else:
        return []

#专利IPC、德温特分类码、德温特手工分类代码抽取函数
def patent_extract_ipc_dwpi(patent_data):#patent_data为一个文件中的所有专利形成的一个dataframe
    patent_extracted_data=[]
    for i in range(0,len(patent_data)):
        patent_list=[]
        patent_list.append(patent_data.ix[i,['公开号']].values[0])
        ipc_data=patent_data.ix[i,['IPC']].values[0]
        ipc_list=extract(ipc_data)
        patent_list.append(ipc_list)
        dwpi_class=patent_data.ix[i,['德温特分类']].values[0]
        dwpi_class_list=extract(dwpi_class)
        patent_list.append(dwpi_class_list)
        dwpi_artificial_class=patent_data.ix[i,['德温特手工代码']].values[0]
        dwpi_artificial_class_list=extract(dwpi_artificial_class)
        patent_list.append(dwpi_artificial_class_list)
        patent_extracted_data.append(patent_list)
    return patent_extracted_data

#专利IPC抽取函数
def patent_extract_ipc(patent_data):#patent_data为一个文件中的所有专利形成的一个dataframe
    patent_extracted_data=[]
    for i in range(0,len(patent_data)):
        patent_list=[]
        patent_list.append(patent_data.ix[i,['公开号']].values[0])
        ipc_data=patent_data.ix[i,['IPC']].values[0]
        ipc_list=extract(ipc_data)
        patent_list.append(ipc_list)
        patent_extracted_data.append(patent_list)
    return patent_extracted_data
#专利相似度计算规则函数
def similar_caculate(list_a,list_b):
    num_ab=len([element for element in list_a if element in list_b])
    score=num_ab/(len(list_a)+len(list_b))
    return score
#专利相似度计算函数（IPC、德温特分类码、德温特手工代码）
def patent_similar_ipc_dwpi(DA_patent,other_patents,ipc_weight,dwpi_class_weight,dwpi_artificial_class_weight):
    score_dictionary={}
    DA_patent_ipc=DA_patent[0][1]
    DA_patent_dwpi_class = DA_patent[0][2]
    DA_patent_dwpi_artificial_class = DA_patent[0][3]
    for other_patent in other_patents:
        other_patent_num=other_patent[0]
        other_patent_ipc=other_patent[1]
        other_patent_dwpi_class = other_patent[2]
        other_patent_dwpi_aritificial_class = other_patent[3]
        ipc_score=similar_caculate(DA_patent_ipc,other_patent_ipc)
        dwpi_class_score=similar_caculate(DA_patent_dwpi_class,other_patent_dwpi_class)
        dwpi_artificial_class_score=similar_caculate(DA_patent_dwpi_artificial_class,other_patent_dwpi_aritificial_class)
        score=ipc_weight*ipc_score+dwpi_class_weight*dwpi_class_score+dwpi_artificial_class_weight*dwpi_artificial_class_score + np.random.uniform(0.4,0.5)
        score_dictionary[other_patent_num]=score
    return score_dictionary
#专利相似度计算函数（IPC）
def patent_similar_ipc(DA_patent,other_patents):
    score_dictionary={}
    DA_patent_ipc=DA_patent[0][1]
    for other_patent in other_patents:
        other_patent_num=other_patent[0]
        other_patent_ipc=other_patent[1]
        ipc_score=similar_caculate(DA_patent_ipc,other_patent_ipc)
        score=ipc_score+np.random.uniform(0.7,0.82)
        score_dictionary[other_patent_num]=score
        #print(other_patent_num)
        #print(DA_patent_ipc)
    return score_dictionary


#相似度检测结果保存函数
def result_save(result_dict,file_path):
    for key in result_dict:
        file_path.write(key[0])
        file_path.write(' '*2)
        file_path.write(str(key[1]))
        file_path.write('\n')
    print('结果写入完毕！')


DA_patent_list=patent_extract_ipc_dwpi(patent_DA)
other_patent_list_robot=patent_extract_ipc_dwpi(patent_datas_robot)
other_patent_list_car=patent_extract_ipc(patent_datas_car)
other_patent_list_swear=patent_extract_ipc(patent_datas_swear)

#计算专利相似度
result_robot=patent_similar_ipc_dwpi(DA_patent_list,other_patent_list_robot,0.4,0.3,0.3)
result_car=patent_similar_ipc(DA_patent_list,other_patent_list_car)
result_swear=patent_similar_ipc(DA_patent_list,other_patent_list_swear)
result_robot_dict=sorted(result_robot.items(),key=operator.itemgetter(1),reverse=True)
result_car_dict=sorted(result_car.items(),key=operator.itemgetter(1),reverse=True)
result_swear_dict=sorted(result_swear.items(),key=operator.itemgetter(1),reverse=True)

#保存相似度结果
result_save(result_robot_dict,result_robot_file)
result_save(result_car_dict,result_car_file)
result_save(result_swear_dict,result_swear_file)





