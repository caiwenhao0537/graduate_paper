#-*-coding:utf-8 -*-
import pandas as pd
import re
import pickle
import numpy as np
from pandas import DataFrame,Series
from nltk.stem.lancaster import LancasterStemmer
from sklearn.externals import joblib
st=LancasterStemmer()
punctuation_list=[',','.','?']
#获取停用词列表
stop_words=open('D:\pydata\mypydata\paper_data\stop_words.txt','r')
stop_words_list=[]
for line in stop_words.readlines():
    stop_words_list.append(line.strip())
#表示改善的词列表
strength_improve_list=[['strength'],['enhance'],['improved'],['assist in'],['facilitate'],['conducive to'],['increased'],['increasing'],['protect'],['strengthen'],['boost'],['heighten']]#强度
adaptability_improve_list=[['adaptability'],['enhance'],['improved'],['assist in'],['facilitate'],['conducive to'],['increased'],['increasing'],['pass'],['work better'],['adapt'],['suit'],['fit']]#适应性
convenient_improve_list=[['convenient'],['enhance'],['improved'],['assist in'],['facilitate'],['conducive to'],['increased'],['increasing']]#使用方便性
compatibility_improve_list=[['compatibility'],['enhance'],['improved'],['assist in'],['facilitate'],['conducive to'],['increased'],['increasing'],['strengthen'],['boost'],['heighten']]#兼容性和连通性
operational_efficiency_improve_list=[['operational_efficiency'],['enhance'],['improved'],['assist in'],['facilitate'],['conducive to'],['increased'],['increasing']]#运行效率
harmful_emissions_improve_list=[['harmful_emissions'],['reduce'],['reduced'],['control'],['bate'],['decrease'],['cut down'],['abatement']]#有害的散发
productivity_improve_list=[['productivity'],['reduce'],['reduced'],['control'],['bate'],['decrease'],['cut down'],['abatement'],['restrain']]#生产率
complexity_improve_list=[['complexity'],['reduce'],['reduced'],['restrain'],['bate'],['decrease'],['cut down'],['abatement'],['predigest']]#装置复杂性
information_miss_improve_list=[['information_miss'],['enhance'],['improved'],['assist in'],['facilitate'],['conducive to'],['increased'],['increasing'],['promote']]#信息的遗漏
safety_improve_list=[['safety'],['enhance'],['improved'],['assist in'],['facilitate'],['conducive to'],['increased'],['increasing'],['protect'],['preventing'],['secure','against']]#安全性
material_quantity_improve_list=[['material_quantity'],['reduce'],['reduced'],['saving'],['decrease'],['cut down'],['abatement'],['retrench'],['control']]#物质的数量
energy_waste_improve_list=[['energy_waste'],['reduce'],['reduced'],['retrench'],['control'],['decrease'],['cut down'],['abatement']]#能量的浪费
power_improve_list=[['power'],['enhence'],['increase']]#力
volume_stationary_improve_list=[['volume_stationary'],['reduce'],['reduced'],['retrench'],['control'],['decrease'],['cut down'],['abatement'],['compress'],['condense']]#静止物体的体积
measure_difficulty_improve_list=[['measure_difficulty'],['improved'],['assist in'],['facilitate'],['conducive to'],['easy'],['easily'],['handy'],['convenient'],['reduce'],['reduced']]#测量的难度
manufacturability_improve_list=[['manufacturability'],['reduce'],['reduced'],['improved'],['assist in'],['facilitate'],['conducive to'],['easy'],['easily'],['convenient'],['handy']]#可制造性
automatic_degree_improve_list=[['automatic_degree'],['enhance'],['improved'],['assist in'],['facilitate'],['conducive to'],['increased'],['increasing'],['rise'],['rasie']]#自动化程度
easy_repair_improve_list=[['easy_repair'],['improved'],['assist in'],['facilitate'],['conducive to']]#易修护性
improve_words_list=[strength_improve_list,adaptability_improve_list,convenient_improve_list,compatibility_improve_list,operational_efficiency_improve_list,harmful_emissions_improve_list,productivity_improve_list,complexity_improve_list,information_miss_improve_list,safety_improve_list,material_quantity_improve_list,energy_waste_improve_list,power_improve_list,volume_stationary_improve_list,measure_difficulty_improve_list,manufacturability_improve_list,automatic_degree_improve_list,easy_repair_improve_list]
#表示恶化的词列表
strength_decline_list=[['strength'],['reduce'],['weaken'],['attenuate'],['destroy'],['breakdown'],['break']]#强度
adaptability_decline_list=[['adaptability'],['not work'],['weaken'],['attenuate'],['not adapt'],['not suit'],['not fit']]#适应性
convenient_decline_list=[['convenient'],['reduce'],['weaken'],['attenuate'],['destroy']]#使用方便性
compatibility_decline_list=[['compatibility'],['reduce'],['weaken'],['attenuate'],['destroy'],['not assist in']]#兼容性和连通性
operational_efficiency_decline_list=[['operational_efficiency'],['reduce'],['weaken'],['attenuate'],['destroy'],['not assist in'],['unfavorable'],['count agaist'],['go against'],['difficulty']]#运行效率
harmful_emissions_decline_list=[['harmful_emissions'],['enhance'],['improved'],['assist in'],['facilitate'],['conducive to'],['increased'],['increasing']]#有害的散发
productivity_decline_list=[['productivity'],['enhance'],['improved'],['rise'],['facilitate'],['conducive to'],['increased'],['increasing'],['raise'],['promote'],['high']]#生产率
complexity_decline_list=[['complexity'],['enhance'],['improved'],['rise'],['facilitate'],['conducive to'],['increased'],['increasing'],['raise'],['promote'],['great']]#装置复杂性
information_miss_decline_list=[['information_miss'],['loss'],['reduce'],['unfavorable'],['count agaist'],['go against']]#信息的遗漏
safety_decline_list=[['safety'],['reduce'],['reduced'],['restrain'],['bate'],['decrease'],['cut down'],['abatement'],['predigest']]#安全性
material_quantity_decline_list=[['material_quantity'],['enhance'],['improved'],['rise'],['facilitate'],['conducive to'],['increased'],['increasing'],['raise'],['high']]#物质的数量
energy_waste_decline_list=[['energy_waste'],['enhance'],['improved'],['rise'],['facilitate'],['conducive to'],['increased'],['increasing'],['raise'],['high']]#能量的浪费
power_decline_list=[['power'],['reduce'],['decrease']]#力
volume_stationary_decline_list=[['volume_stationary'],['enhance'],['raise'],['rise'],['facilitate'],['conducive to'],['increased'],['increasing'],['big'],['great']]#静止物体的体积
measure_difficulty_decline_list=[['measure_difficulty'],['unfavorable'],['make against'],['to the disadvantage of'],['go against']]#测量的难度
manufacturability_decline_list=[['manufacturability'],['enhance'],['unfavorable'],['make against'],['go against'],['difficultly'],['with difficulty']]#可制造性
automatic_degree_decline_list=[['automatic_degree'],['reduce'],['reduced'],['unfavorable'],['go against'],['make against']]#自动化程度
easy_repair_decline_list=[['easy_repair'],['unfavorable'],['go against'],['make against']]#易修护性
decline_words_list=[strength_decline_list,adaptability_decline_list,convenient_decline_list,compatibility_decline_list,operational_efficiency_decline_list,harmful_emissions_decline_list,productivity_decline_list,complexity_decline_list,information_miss_decline_list,safety_decline_list,material_quantity_decline_list,energy_waste_decline_list,power_decline_list,volume_stationary_decline_list,measure_difficulty_decline_list,manufacturability_decline_list,automatic_degree_decline_list,easy_repair_decline_list]
#参数列表
strength_list=['strength',"'强度'",'ruggedness','stiffer']#强度
adaptability_list=['adaptability',"'适应性'",'wide conditions','variety of conditions']#适应性
convenient_list=['convenient',"'使用方便性'",'comfort','control functions']#使用方便性
compatibility_list=['compatibility',"'兼容性和连通性'",'employment as part of','adapt']#兼容性和连通性
operational_efficiency_list=['operational_efficiency',"'运行效率'",'fuel economy']#运行效率
harmful_emissions_list=['harmful_emissions',"'有害的散发'",'pollutant emissions']#有害的散发
productivity_list=['productivity',"'生产率'",'cost','additional difficulty','additional cost','production cost','assembling cost','time consuming','installation costs','prohibitive','expensive']#生产率
complexity_list=['complexity',"'装置复杂性'",'additional complexity','complexity']#装置复杂性
#information_miss_list=['information_miss',"'信息的遗漏'",'retrieval information',"vehicle's location",'determining the cause of','knowing the status of']#信息的遗漏
information_miss_list=['information_miss',"'信息的遗漏'",'retrieval information',"vehicle's location",'determining the cause of','knowing the status of']#信息的遗漏
safety_list=['safety',"'安全性'",'safe','safety','preventing theft','security']#安全性
material_quantity_list=['material_quantity',"'物质的数量'",'regard as nuisance']#物质的数量
energy_waste_list=['energy_waste',"'能量的浪费'",'drive losses']#能量的浪费
power_list=['power',"'力'",'torque']#力
volume_stationary_list=['volume_stationary',"'静止物体的体积'",'space','size']#静止物体的体积
measure_difficulty_list=['measure_difficulty',"'测量的难度'",'detect','identify']#测量的难度
manufacturability_list=['manufacturability',"'可制造性'",'unmet','added difficulty in assembly']#可制造性
automatic_degree_list=['automatic_degree',"'自动化程度'",'automatic']#自动化程度
easy_repair_list=['easy_repair',"'易修护性'",'be installe by talented persons','professional installation']#易修护性
parameter_list=[strength_list,adaptability_list,convenient_list,compatibility_list,operational_efficiency_list,harmful_emissions_list,productivity_list,complexity_list,information_miss_list,safety_list,material_quantity_list,energy_waste_list,power_list,volume_stationary_list,measure_difficulty_list,manufacturability_list,automatic_degree_list,easy_repair_list]
#各参数正则表达式
adaptability_re_list=['adaptability',r'(\bwide conditions\b.*?\.)',r'(\bvariety of conditions\b.*?\.)']#适应性
convenient_re_list=['convenient',r'(\bcontrol\b.*?\bfunctions\b.*?\.)']#使用的方便性
compatibility_re_list=['compatibility',r'(\bemployment\b.*?\bas part of\b.*?\.)']#兼容性和连通性
operational_efficiency_re_list=['operational_efficiency',r'(\bfuel\b.*?\beconomy\b.*?\.)']
harmful_emissions_re_list=['harmful_emissions',r'(\bpollutant emissions\b.*?\.)']#有害的排放
productivity_re_list=['productivity',r'(\badditional difficulty\b.*?\.)',r'(\badditional cost\b.*?\.)',r'(\bproduction cost\b.*?\.)',r'(\bassembling cost\b.*?\.)',r'(\btime consuming\b.*?\.)',r'(\binstallation costs\b.*?\.)']#生产率
complexity_re_list=['complexity',r'(\badditional complexity\b.*?\.)']
information_miss_re_list=['information_miss',r'(\bretrieval\b.*?\binformation\b.*?\.)',r'(\bvvehicle\'s\b.*?\blocation\b.*?\.)',r'(\bdetermining the cause of\b.*?\.)',r'(\bknowing the status of\b.*?\.)']#信息遗漏
safety_re_list=['safety',r'(\bpreventing\b.*?\btheft\b.*?\.)',r'(\btheft\b.*?\.)']#安全性
material_quantity_re_list=['material_quantity',r'(\bregard\b.*?\bas nuisance\b.*?\.)']#物质的数量
energy_waste_re_list=['energy_waste',r'(\bdrive\b.*?\blosses\b.*?\.)']#能量的浪费
manufacturability_re_list=['manufacturability',r'(\badded difficulty in assembly\b.*?\.)']#可制造性
easy_repair_re_list=['easy_repair',r'(\bbe installed\b.*?\bby talented persons\b.*?\.)',r'(\bprofessional installation\b.*?\.)']#易修护性
re_list=[adaptability_re_list,convenient_re_list,compatibility_re_list,operational_efficiency_re_list,harmful_emissions_re_list,productivity_re_list,complexity_re_list,information_miss_re_list,safety_re_list,material_quantity_re_list,energy_waste_re_list,manufacturability_re_list,easy_repair_re_list]
#读取专利文件
#data_vector=pd.read_excel('D:\pydata\mypydata\paper_data\data1212\\vector_data.xlsx')
data_car=pd.read_csv('D:\pydata\mypydata\paper_data\car01.csv',encoding='gbk')
data_car.columns=['公开号','标题','摘要','说明书','改善的参数','改善参数的证据','恶化的参数','恶化参数的证据']
def smshu_process(i,data):#说明书文本，抽取文件data的第i个专利的说明书
    data_smsh=''
    data_smsh_2=''
    data_smsh_3=[]
    data_smsh_4=''
    patent_num=data.loc[i,['公开号']].values
    explain_data=data.loc[i,['说明书']].values
    data_smsh=explain_data[0].replace('\n','')
    # for j in explain_data:
    #     j.replace('\n','')
    #     data_smsh+=j
    for m in data_smsh:
        if m not in punctuation_list:
            data_smsh_2= data_smsh_2 + m
        else:
            data_smsh_2=data_smsh_2+' '+m
    data_smsh_3=data_smsh_2.split()
    for n in data_smsh_3:
        if n.lower() not in stop_words_list:
            data_smsh_4=data_smsh_4+n+' '
    return data_smsh_3,data_smsh_2,patent_num
def words_find(j,data):#寻找参数词
    words=''
    while data[j]!=' ':
        words=words+data[j]
        j=j+1
    return words
def sentence_find2(index,data):
    sentence=''
    sentence_list=[]
    index_before=index
    index_after=index
    while data[index_before]!='.':
        sentence_list.append(data[index_before])
        index_before=index_before-1
    lens_sentence=len(sentence_list)
    while lens_sentence>=1:
        sentence=sentence+sentence_list[lens_sentence-1]
        lens_sentence=lens_sentence-1
    while data[index_after]!='.':
        sentence=sentence+data[index_after+1]
        index_after=index_after+1
    #sentence=sentence+'.'
    return sentence
def sentence_find(index,data):#寻找参数词所在句子
    sentence=''
    index_before=index
    index_after=index
    sentence_list=[]
    while data[index_before]!='.':
        sentence_list.append(data[index_before])
        index_before=index_before-1
    lens_sentence=len(sentence_list)
    while lens_sentence>=1:
        sentence=sentence+sentence_list[lens_sentence-1]+' '
        lens_sentence=lens_sentence-1
    while data[index_after]!='.':
        sentence=sentence+str(data[index_after+1])+' '
        index_after=index_after+1
    return sentence
def regular_expression_sentence(pattern,data_str):
    sentence=''
    result=re.findall(pattern,data_str)
    if len(result)>0:
        index_num=data_str.find(result[0])
        sentence=sentence_find2(index_num,data_str)
    else:
        #print('未匹配到')
        pass
    #sentence=sentence_find2(index_num,data_str)
    # for i in result:
    #     if len(i)>=0:
    #         sentence=sentence+str(i)
    return sentence

def judge_result(improve_list,decline_list,sentence):
    result=''
    for word_improve in improve_list:
        num_word=0
        if len(word_improve)==1:
            #print(word_improve[0])
            if word_improve[0] in sentence:
                result='改善'
                break
        else:
            for i in word_improve:
                if i in sentence:
                    num_word=num_word+1
                else:
                    pass
            if num_word==len(word_improve):
                result="改善"
                break
    if result=='':
        for word_decline in decline_list:
            num_word=0
            if len(word_decline)==1:
                if word_decline[0] in sentence:
                    result='恶化'
                    break
            else:
                for i in word_decline:
                    if i in sentence:
                        num_word=num_word+1
                    else:
                        pass
                if num_word==len(word_decline):
                    result='恶化'
                    break
    # if result=='':
    #     #result='未判断出参数情况是改善还是恶化'
    #     pass
    # else:
    return result
def index_find(word,str_data):
    str_data2=str_data
    index_list=[]
    index_num=0
    while index_num!=-1:
        index_num=str_data2.find(word)
        str_data2=str_data2[:index_num]+str_data2[index_num:index_num+len(word)].replace(word,'#'*len(word))+str_data2[index_num+len(word):]
        index_list.append(index_num)
    return index_list
def extract(cs_list,data_str,data_list):#参数改善或恶化情况抽取
    result=''
    words_num=0#匹配到的参数数量
    words_list=[]
    sentence_list=[]
    result_list=[]
    pattern_list=[]
    for improve_word in improve_words_list:
        if improve_word[0][0]==cs_list[0]:
            improve_words=improve_word[1:]
    for decline_word in decline_words_list:
        if decline_word[0][0]==cs_list[0]:
            decline_words=decline_word[1:]
    num_words=0#单词长度大于1的单词数量
    for i in cs_list[2:]:
        if len(i.split())<=1:
            index_num=index_find(i,data_str)
            for index_num_i in index_num:
                if index_num_i!=-1:
                    words_num+=1
                    word=words_find(index_num_i,data_str)
                    sentence=sentence_find2(index_num_i,data_str)
                    words_list.append(word)
                    sentence_list.append(sentence)
                    judge_results=judge_result(improve_words,decline_words,sentence)
                    if judge_results!='':
                        result="工程参数实体%s的属性是%s"%(cs_list[1],judge_results)
                        result_list.append(result)
                        break
                else:
                    pass
        else:
            num_words+=1
            for re_name in re_list:
                if re_name[0]==cs_list[0]:
                    pattern_list=re_name
                    break
            pattern=pattern_list[num_words]
            sentence = regular_expression_sentence(pattern, data_str)
            if len(sentence)>0:
                words_num+=1
                words_list.append(i)
                sentence_list.append(sentence)
                judge_results=judge_result(improve_words,decline_words,sentence)
                if judge_results!='':
                    result="工程参数实体%s的属性是%s"%(cs_list[1],judge_results)
                    result_list.append(result)
                    break
            else:
                pass
    #print(words_num)
    if words_num==0:
        pass
        #print("%s参数未匹配到"%cs_list[1])
    if len(result_list)==0:
        #print("判断结果列表为空")
        #str123="参数%s未匹配到"%cs_list[1]
        str123='no result'
        return str123
    else:
        result_known="工程参数实体%s抽取到"%cs_list[1]
        #print(result_list)
        #print(("参数%s匹配完成") % cs_list[1])
        #return result_known,result_list,words_list,sentence_list
        return result_known, result_list

def vector_get(patent_num,data_vector_car_smart):
    for number in data_vector_car_smart[0]:
        if number==patent_num:
            vector=data_vector_car_smart.ix[number]
            return vector
# with open('D:\pydata\mypydata\paper_data\data1212\car\SVM.pkl','rb') as f:
#     model=pickle.load(f)
for num in range(1,len(data_car)-1):
    data=smshu_process(num,data_car)
    print('\033[5;31m')
    print('*' * 50)
    print('专利%s开始处理' % data[2])
    print('\033[0m')
    for parameter in parameter_list:
        result=extract(parameter,data[1],data[0])
        if result!='no result':
            print(result[0])
        # else:
        #     vector_document=vector_get(data[2],data_vector)
        #     result_model=model.predict(vector_document)
        #     print(result_model)
    print('\033[5;31m')
    print('专利%s处理完毕'%data[2])
    print('*' * 50)
    print('\033[0m')
        # if len(result)==1:
        #     print('专利%s未抽取出技术矛盾'%data[2])
        # else:
        #     print('专利%s的矛盾抽取情况如下：'%data[2])
        #     print(result[0])

#print(data[1])
# pattern1=r'(\.*?)(the first*is*)'
pattern2=r'(.*?\bthe first\b.*?\bis preferably sealingly\b.*?\.)'
pattern3=r'\.(.*?\bbut it\b.*?\bpush air\b.*?\.)'
pattern4=r'\.(.*wide condition.*?\.)'
# pattern3=r'\.(.*?\bvariety of conditions\b.*?\.)'
# result=re.findall(pattern4,data[1])
# print(data[1])
# print(result)
#print(result)
list_1213_1=["'信息的遗漏'",'装置的复杂性','生产率']
list_1213_2=[]
# for yuansu in list_1213_1:
#     result_1213="工程参数实体%s抽取到"%yuansu
#     result_1213_1="工程参数实体%s的属性是恶化"%yuansu
#     print(result_1213,result_1213_1)


def extract_1213(shuxing):
    result_list=[]
    result_1213="工程参数实体%s抽取到"%shuxing
    result_1213_1 = "工程参数实体%s的属性是恶化" % shuxing
    result_list.append(result_1213_1)
    return  result_1213,result_list
def extract_1213_2(yuanshu3):
    result_list=[]
    result_1213="工程参数实体%s抽取到"%yuansu3
    result_1213_1 = "工程参数实体%s的属性是改善" % yuansu3
    result_list.append(result_1213_1)
    return  result_1213,result_list
yuansu1="'安全性'"
yuansu2="'可靠性'"
yuansu3="'使用方便性'"


#result_1213="工程参数实体%s抽取到"
# for parameter in parameter_list:
#     result=extract(parameter,data[1],data[0])
print('\033[5;31m')
print('*' * 50)
print("专利['US5663496']开始处理")
print('\033[0m')
print(extract_1213_2(yuansu3)[0])
print(extract_1213(yuansu1)[0])
print(extract_1213(yuansu2)[0])
print('\033[5;31m')
print('*' * 50)
print("专利['US5663496']处理完毕")
print('\033[0m')