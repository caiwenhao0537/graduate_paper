#-*-coding: utf-8 -*-
import re
import pymysql
from sqlalchemy import *
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
patent_data=pd.read_excel('D:\pydata\mypydata\paper_data\data_1127\WO_15_17_car.xlsx',encoding='utf-8')
#patent_data_df=DataFrame(patent_data,columns=['专利号','标题','德温特标题','IPC','德温特摘要','德温特摘要-用途','权利要求项','独立权利要求项','说明书'])
#patent_data_df=DataFrame(patent_data)
patent_data.columns=['patent_num','标题','德温特标题','IPC','德温特摘要','德温特摘要-用途','权利要求项','独立权利要求项','说明书']

# patent_data_df['集成数据']=patent_data_df['德温特标题']+'.'+patent_data_df['德温特摘要']+'.'+patent_data_df['权利要求项']+'.'+patent_data_df['说明书']+'.'
# #print(patent_data_df.ix[1,['集成数据']])
# patent_data_df.drop([0],inplace=True)
# patent_data_df.to_excel('D:\\pydata\\mypydata\\ti_data_try_1.xlsx')

# patent_data=pd.read_csv('D:\pydata\mypydata\paper_data\plane_1117.csv',encoding='gbk')
# #patent_data_df=DataFrame(patent_data,columns=['专利号','标题','德温特标题','IPC','德温特摘要','德温特摘要-用途','权利要求项','独立权利要求项','说明书'])
# patent_data_df=DataFrame(patent_data)
# patent_data_df.columns=['序号','专利号','标题','德温特标题','IPC','德温特摘要','德温特摘要-用途','权利要求项','独立权利要求项','说明书']
#
patent_data['patent_text']=patent_data['德温特摘要'] + patent_data['说明书']+'.'
patent_data.drop([0],inplace=True)
#print(patent_data_df.ix[1,['集成数据']].values)
# #print(patent_data_df['专利号'])
# for i in range(1,len(patent_data_df)):
#     patent_data_df.ix[i,['集成数据']]=patent_data_df.ix[i,['集成数据']].values[0].replace("\n","").strip()
#db=pymysql.connect('localhost','root','123456','patent_data')
engine=create_engine("mysql+pymysql://root:123456@localhost/patent_data?charset=utf8")
#print(patent_data_df.ix[1,['集成数据']].values[0])
#patent_data_df[['专利号','集成数据']].to_csv('D:\pydata\mypydata\paper_data\data_1127\smart_wear.csv')
patent_data[['patent_num','patent_text']].to_sql(name='patent_data_car',con=engine,if_exists='append',index=True,chunksize=None)
#print(type(patent_data[['专利号','集成数据']]))


# patent_data1=pd.read_csv('D:\pydata\mypydata\paper_data\plane_1117_processed.csv',encoding='gbk')
# #patent_data_df=DataFrame(patent_data,columns=['专利号','标题','德温特标题','IPC','德温特摘要','德温特摘要-用途','权利要求项','独立权利要求项','说明书'])
# patent_data_df1=DataFrame(patent_data1)
#
# patent_data2=pd.read_csv('D:\pydata\mypydata\paper_data\plane_9410_processed.csv',encoding='gbk')
# #patent_data_df=DataFrame(patent_data,columns=['专利号','标题','德温特标题','IPC','德温特摘要','德温特摘要-用途','权利要求项','独立权利要求项','说明书'])
# patent_data_df2=DataFrame(patent_data2)
#
# patent_data3=pd.read_csv('D:\pydata\mypydata\paper_data\plane_83_processed.csv',encoding='gbk')
# #patent_data_df=DataFrame(patent_data,columns=['专利号','标题','德温特标题','IPC','德温特摘要','德温特摘要-用途','权利要求项','独立权利要求项','说明书'])
# patent_data_df3=DataFrame(patent_data3)


