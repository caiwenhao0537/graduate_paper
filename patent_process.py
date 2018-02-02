#-*- coding;utf-8 -*-
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
data=pd.read_csv('D:\pydata\mypydata\paper_data\car.csv',encoding='gbk')
dictory_data=open('D:\pydata\mypydata\paper_data\keywords_dictory.txt')
dictory=dictory_data.readlines()
patent_data=DataFrame(data)
patent_data['分句后数据']=''
patent_data['重要句子']=''
test_data='Electronic component esp. modularly stacked multichip module with impedance control includes mounting substrate with external connectors in form of primary and secondary conductors e.g. coaxial conductors with preset impedance per unit length.The electronic component includes a substrate with circuit traces, and active circuitry installed on the substrate and connected to the circuit traces. Multiple connectors are connected to the circuit traces, each consisting of a primary and a secondary conductors. The impedance between the primary and secondary conductors per unit length is a predetermined value pref. in a coaxial pin.The connectors are connectable into a stacked module, where the component may be interconnected with additional components are configured to mate with the component to form an interconnected stack of components. The group of components may in turn be connected through a bottom component to external circuitry e.g. a ground plane. Connections between components is such that connectors on overlying substrates are vertically aligned, including connectors on the component. USE/ADVANTAGEE.g. video display signal controller with bit map output. Matched impedance system for second level multichip module.'
def sentence_split(str_sentence):
    list_ret=[]
    for s_str in str_sentence.split('.'):
        if '?' in s_str:
            s=s_str.split('?')
            for i in s:
                if ';' in i:
                    for j in i.split(';'):
                        list_ret.append(j)
                else:
                    list_ret.append(i)
        elif ';' in s_str:
            m=s_str.split(';')
            for i in m:
                if '?' in i:
                    for j in i.split('?'):
                        list_ret.append(j)
                else:
                    list_ret.append(i)
        else:
            list_ret.append(s_str)
    return list_ret
for i in range(0,25903):
    sentence_data=patent_data.ix[i:i,['集成数据']]
    sentence_data_2=''
    for j in sentence_data.values:
        for m in j:
            sentence_data_2 += str(m)
    sentence_data_2.strip()
    sentence_data_split=sentence_split(sentence_data_2)
    #sentence_data_split = sentence_split(test_data)

    for strs in sentence_data_split:
        if len(strs)<1:
            sentence_data_split.remove(strs)
        else:
            pass
    #print(sentence_data_split)
    processed_data=''
    strong_sentences=''
    for m in sentence_data_split:
        number=0
        processed_data+=m
        processed_data+='\n'
        for keys in dictory:
            if keys.strip() in m:
                number+=1
        if number>=1:
            strong_sentences+=m
            strong_sentences+='\n'
    #print(processed_data)
    patent_data.ix[i:i,['分句后数据']]=processed_data
    patent_data.ix[i:i, ['重要句子']] = strong_sentences
    #patent_data.iloc[i:i,[11]]=processed_data
    print("已处理%d条"%(i+1))
patent_data.to_csv('D:\pydata\mypydata\paper_data\car_processed.csv')
print('处理完毕')
# a='do you love me ? yes! i love you.oh! i know. i love you too.'
# b='Method for monitoring and controlling robotic systems, involves communicating instructions to robotic device to operate in accordance with one or more adjustments.The method (800) involves providing (802) an end effector tool mounted to a moveable component of a robotic device. An image data indicative of work surface is received (808) from first sensor. The first movement information indicating unintended movement is determined (810) based on image data. '
# result=sentence_split(b)
# print(result)