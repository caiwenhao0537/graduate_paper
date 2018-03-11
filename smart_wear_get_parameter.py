#-*- coding:utf-8 -*-
import gensim.models as g
import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import re
import nltk.stem
s=nltk.stem.SnowballStemmer('english')
#工程参数字典
parameter_dict={1:'移动物体的重量',2:'静止物体的重量',3:'移动物体的长度',4:'静止物体的长度',5:'移动物体的面积',6:'静止物体的面积',7:'移动物体的体积',8:'静止物体的体积',9:'形状',10:'物质的质量',11:'信息（资料）的数量',12:'移动物体的耐久性',13:'静止物体的耐久性',14:'速度',15:'力',16:'移动物体消耗的能量',17:'静止物体消耗的能量',18:'功率',19:'张力/压力',20:'强度',21:'结构的稳定性',22:'温度',23:'明亮度',24:'运行效率',25:'物质的浪费',26:'时间的浪费',27:'能量的浪费',28:'信息的遗漏',29:'噪音',30:'有害的散发',31:'有害的副作用',32:'适应性',33:'兼容性或连通性',34:'使用方便性',35:'可靠性',36:'易修护性',37:'安全性',38:'易受伤性',39:'美观',40:'外来有害因素',41:'可制造性',42:'制造的准确度',43:'自动化程度',44:'生产率',45:'装置的复杂性',46:'控制的复杂性',47:'测量的难度',48:'测量的准确度'}

#工程参数代表性单词
parameter_dict_list=[[],[],[],[],[],[],[],['space','size','volume','bulk','cubage'],['shape','form','appearance','outline','adumbration','lineament'],[['number','component'],['quantity','component'],['quantity','material']],[],[],[['durability','static'],['work','well','long'],['work','well','still']],[],[],[],['energy',['energy','consume','static']],['rate','power',['volume','power'],['internal','power'],['rate','work']],['pressure','stress','press','extrusion',['compressive','stress'],['extrusion','pressure']],[],['structural','structure','hyperstability','stability',['structural','stability']],[],['brightness','luminance','lighteness','light',['light','intensity']],['operating','operate','efficiency','efficient',['operat','efficiency']],['waste',['material','waste'],['solid','waste'],['liquid','waste']],[['time','waste'],['time','loss']],[['power','waste'],['waste','electricit']],[['retrieval','information'],'location',['determine','cause'],['know','status']],['noise','sound','strepitus'],[],[],['adapt',['wide','condition'],['variety','condition']],['compatibility','compatible','unite','associate','connect'],['comfort','convenient','convenience'],['reliability','dependability','reliable'],['repair','mend','overhaul','revamp'],['safe','safety','security','theft'],['injure','damage','breakdown'],['beautiful','artistic','appearance'],[],[['difficulty','assembly'],'install','build',['complexity','assembly']],[['accuracy','manufacturet']],['automatic','automation','automate'],[['additional','difficulty'],['additional','cost'],['production','cost'],['time','consume'],'expensive','prohibitive'],['complexity','complex','complicated','precision','precise'],[['complexity','control'],['difficulty','control']],['detect','identify','measure','measurement','survey','gauge','meter',['difficulty','detect'],['complexity','measure']],[['measurement','acuuracy'],['accuracy','survey']]]
#获取工程参数正则表达式列表
pattern_txt=open('D:\pythonproject\graduate_paper\pattern_0309.txt','r',encoding='utf-8')
pattern_list=[]
for line in pattern_txt:
    pattern_list.append(str(line.strip()))
#获取工程参数改善或恶化关键词列表
pattern_attribute_txt=open('D:\pydata\mypydata\paper_data\data0227\pattern_improve_worse.txt','r',encoding='utf-8_sig')
pattern_attribute_list=[]
for line in pattern_attribute_txt:
    pattern_attribute_list.append(str(line.strip()))
#抽取一篇专利中符合正则表达式的句子并返回列表
def sentence_extract(patent_txt,patterns):#patent_txt为一篇专利的文本文档，patterns为正则表达式列表
    sentence_list=[]
    patent_sentence=patent_txt.split('.')
    for sentence in patent_sentence:
        for pattern_word in patterns:
            p=re.compile(pattern_word)
            data=p.findall(sentence.strip())
            if len(data)>0:
                for i in data:
                    sentence_list.append(i)
    return sentence_list
#改善或恶化关键词
def dict_improve_worse_get(dic_dir,stem_value):#从文件dic_dir获取表示改善或恶化的关键词词典
    data=open(dic_dir,'r',encoding='utf-8_sig')
    list_dic=[]
    list_dic_word=[]
    if stem_value==0:
        for line in data:
            list_dic.append(line.strip())
        return  list_dic
    else:
        for line in data:
            list_dic.append(line.strip())
            for word in list_dic:
                list_dic_word.append(s.stem(word))
        return list_dic_word
#获取单词空间向量
def word_vector_get(word,model):
    #model=g.Doc2Vec.load(model_dir)
    word_vector=model[word].tolist()
    return word_vector

#获取短语空间向量
def vector_merge(vector_list):
    vector_merge_1=np.array([0*200])
    for vector in vector_list:
        vector_merge_1=vector_merge_1+vector
    vector_merged=[x*(1/len(vector_list)) for x in vector_merge_1]
    return vector_merged
#计算两空间向量的余弦相似度
def cos(vector1,vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a,b in zip(vector1,vector2):
        dot_product += a*b
        normA += a**2
        normB += b**2
    if normA == 0.0 or normB==0.0:
        return None
    else:
        return dot_product / ((normA*normB)**0.5)
#加载模型
model=g.Doc2Vec.load('D:\pydata\mypydata\paper_data\data1212\model2\model.bin')

def words_similarity(word,parameter_words_list,value):#计算单词word所属的工程参数
    parameter_num=0
    parameter_num_list=[]
    multi_parameter_list=[]
    parameter_list=[]
    for parameter_words in parameter_words_list:
        parameter_num+=1
        #print('已完成%d个工程参数比对'%parameter_num)
        if len(parameter_words)==0:
            pass
        else:
            for parameter in parameter_words:
                if isinstance(parameter,str):
                    try:
                        similarity=model.similarity(word,parameter)
                        if similarity>=value or word==parameter:
                            parameter_num_list.append(parameter_num)
                            break
                    except:
                        pass
                else:
                    for i in parameter:
                        try:
                            multi_parameter_list.append(word_vector_get(i,model))
                            parameter_vector=vector_merge(multi_parameter_list)
                            word_vector=word_vector_get(word,model)
                            similarity=cos(parameter_vector,word_vector)
                            if similarity>=value:
                                parameter_num_list.append(parameter_num)
                                break
                        except:
                            pass
    for j in set(parameter_num_list):
        parameter_list.append(parameter_dict[j])
    return parameter_list
#抽取句子中含有的参数改善或恶化的单词
def parameter_attribute_extract(sentence,pattern_list):
    parameter_attribute_list=[]
    for pattern_word in pattern_list:
        p=re.compile(pattern_word,re.I)
        for i in p.findall(sentence):
            for j in i:
                if j not in[' ',',','\.']:
                    parameter_attribute_list.append(j)
    return parameter_attribute_list

def patent_parameter_extract(patent_sentence_list,parameter_dict_list):
    patent_parameter_list=[]
    patent_parameter_attribute_list=[]
    for sentence in patent_sentence_list:
        sentence_parameter_list=[]
        sentence_parameter_attribute_list=[]
        sentence_words_list=sentence.split()
        print(sentence_words_list)
        print(len(sentence_words_list))
        for word in sentence_words_list:
            word_parameter=words_similarity(word,parameter_dict_list,0.8)
            if len(word_parameter)>0:
                sentence_parameter_list.append(word_parameter)
        patent_parameter_list.append(sentence_parameter_list)
        sentence_parameter_attribute_list.append(parameter_attribute_extract(sentence,pattern_attribute_list))
        patent_parameter_attribute_list.append(sentence_parameter_attribute_list)
    return patent_parameter_list,patent_parameter_attribute_list




#
# model_smart_wear='D:\pydata\mypydata\paper_data\data1212\model2\model.bin'
# words_similarity('noise',parameter_dict_list,model_smart_wear,0.6)
# output_smart_wear='D:\pydata\mypydata\paper_data\data1212\model2\word_vector.txt'
# word_list_smart_wear=['additional cost','expensive']
# word_vector_get(word_list_smart_wear,model_smart_wear,output_smart_wear)
#读取专利文本
data=pd.read_excel('D:\pydata\mypydata\paper_data\data0227\smart_wear_0302.xlsx')
patent_dict={}
for i in range(1,2):
    patent_list=[]
    patent_list3=[]
    patent_list2=[]
    patent_list.append(data.irow(i)['专利号'])
    sentence_list=sentence_extract(data.irow(i)['专利文本'],pattern_list)
    if len(sentence_list)>0:
        result=patent_parameter_extract(sentence_list,parameter_dict_list)
        patent_list3.append(result[0])
        patent_list3.append(result[1])
    patent_list.append(patent_list3)
    patent_list2.append(patent_list)
    #print(patent_list2)
    patent_dict.update(dict(patent_list2))
    print('已处理%d条专利'%i)
print(patent_dict)
