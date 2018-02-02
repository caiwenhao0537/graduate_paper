#python example to infer document vectors from trained doc2vec model
import gensim.models as g
import codecs

#parameters
#model="D:\pydata\mypydata\paper_data\model.bin"
model= "D:\pythonproject\graduate_paper\doc2vec-master\\toy_data\model.bin"
test_docs="D:\pythonproject\graduate_paper\doc2vec-master\\toy_data\\test_docs.txt"
output_file="D:\pythonproject\graduate_paper\doc2vec-master\\test_vectors.txt"

#inference hyper-parameters
start_alpha=0.01
infer_epoch=1000

#load model
m = g.Doc2Vec.load(model)
test_docs = [x.strip().split() for x in codecs.open(test_docs, "r", "utf-8").readlines()]
# simi_num=m.n_similarity(['plane'],['aircraft'])
# print(simi_num)
#infer test vectors
output = open(output_file, "w")
for d in test_docs:
    output.write( " ".join([str(x) for x in m.infer_vector(d, alpha=start_alpha, steps=infer_epoch)]) + "\n" )
output.flush()
output.close()
