#-*- coding:utf-8 -*-
import gensim.models as g
import numpy as np
#工程参数字典
parameter_dict={1:'移动物体的重量',2:'静止物体的重量',3:'移动物体的长度',4:'静止物体的长度',5:'移动物体的面积',6:'静止物体的面积',7:'移动物体的体积',8:'静止物体的体积',9:'形状',10:'物质的质量',11:'信息（资料）的数量',12:'移动物体的耐久性',13:'静止物体的耐久性',14:'速度',15:'力',16:'移动物体消耗的能量',17:'静止物体消耗的能量',18:'功率',19:'张力/压力',20:'强度',21:'结构的稳定性',22:'温度',23:'明亮度',24:'运行效率',25:'物质的浪费',26:'时间的浪费',27:'能量的浪费',28:'信息的遗漏',29:'噪音',30:'有害的散发',31:'有害的副作用',32:'适应性',33:'兼容性或连通性',34:'使用方便性',35:'可靠性',36:'易修护性',37:'安全性',38:'易受伤性',39:'美观',40:'外来有害因素',41:'可制造性',42:'制造的准确度',43:'自动化程度',44:'生产率',45:'装置的复杂性',46:'控制的复杂性',47:'测量的难度',48:'测量的准确度'}

#工程参数代表性单词
parameter_dict_list=[[],[],[],[],[],[],[],['space','size','volume','bulk','cubage'],['shape','form','appearance','outline','adumbration','lineament'],[['number','component'],['quantity','component'],['quantity','material']],[],[],[['durability','static'],['work','well','long'],['work','well','still']],[],[],[],['energy',['energy','consume','static']],['rate','power',['volume','power'],['internal','power'],['rate','work']],['pressure','stress','press','extrusion',['compressive','stress'],['extrusion','pressure']],[],['structural','structure','hyperstability','stability',['structural','stability']],[],['brightness','luminance','lighteness','light',['light','intensity']],['operating','operate','efficiency','efficient',['operat','efficiency']],['waste',['material','waste'],['solid','waste'],['liquid','waste']],[['time','waste'],['time','loss']],[['power','waste'],['waste','electricit']],[['retrieval','information'],'location',['determine','cause'],['know','status']],['noise','sound','strepitus'],[],[],['adapt',['wide','condition'],['variety','condition']],['compatibility','compatible','unite','associate','connect'],['comfort','convenient','convenience'],['reliability','dependability','reliable'],['repair','mend','overhaul','revamp'],['safe','safety','security','theft'],['injure','damage','breakdown'],['beautiful','artistic','appearance'],[],[['difficulty','assembly'],'install','build',['complexity','assembly']],[['accuracy','manufacturet']],['automatic','automation','automate'],[['additional','difficulty'],['additional','cost'],['production','cost'],['time','consume'],'expensive','prohibitive'],['complexity','complex','complicated','precision','precise'],[['complexity','control'],['difficulty','control']],['detect','identify','measure','measurement','survey','gauge','meter',['difficulty','detect'],['complexity','measure']],[['measurement','acuuracy'],['accuracy','survey']]]

def word_vector_get(word,model):
    #model=g.Doc2Vec.load(model_dir)
    word_vector=model[word].tolist()
    return word_vector

def vector_merge(vector_list):
    vector_merge_1=np.array([0*200])
    for vector in vector_list:
        vector_merge_1=vector_merge_1+vector
    vector_merged=[x*(1/len(vector_list)) for x in vector_merge_1]
    return vector_merged

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

def words_similarity(word,parameter_words_list,model_dir,value):#计算单词word所属的工程参数
    model=g.Doc2Vec.load(model_dir)
    parameter_num=0
    parameter_num_list=[]
    multi_parameter_list=[]
    parameter_list=[]
    for parameter_words in parameter_words_list:
        parameter_num+=1
        print('已完成%d个工程参数比对'%parameter_num)
        if len(parameter_words)==0:
            pass
        for parameter in parameter_words:
            if isinstance(parameter,str):
                try:
                    similarity=model.similarity(word,parameter)
                    print(word==parameter)
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
    print(parameter_list)
    return parameter_num_list


#
model_smart_wear='D:\pydata\mypydata\paper_data\data1212\model2\model.bin'
words_similarity('noise',parameter_dict_list,model_smart_wear,0.6)
# output_smart_wear='D:\pydata\mypydata\paper_data\data1212\model2\word_vector.txt'
# word_list_smart_wear=['additional cost','expensive']
# word_vector_get(word_list_smart_wear,model_smart_wear,output_smart_wear)
