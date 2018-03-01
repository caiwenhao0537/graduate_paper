#-*- coding:utf-8 -*-
def repeat_remove(input_file,output_file):
    txt_list=open(input_file).readlines()
    txt_repeat_remove=set(txt_list)
    output=open(output_file,'w')
    for word in txt_repeat_remove:
        output.write(word)
        #output.write('\n')
    output.close()

input_dir='D:\pydata\mypydata\paper_data\data0227\\vector.txt'
output_dir='D:\pydata\mypydata\paper_data\data0227\\vector_processed.txt'
repeat_remove(input_dir,output_dir)
