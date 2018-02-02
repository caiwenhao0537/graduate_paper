#python example to infer document vectors from trained doc2vec model
import gensim.models as g
import numpy as np
import codecs

#parameters
model="D:\pydata\mypydata\paper_data\data_robot\patent_data_modle.bin"
#test_docs="D:\pydata\mypydata\paper_data\model2\\test2.txt"
#output_file="D:\pydata\mypydata\paper_data\data1212\model2\d2v.corpus.npy"

#inference hyper-parameters
start_alpha=0.01
infer_epoch=1000

#load model
m = g.Doc2Vec.load(model)
# for  i in m['enhance']:
#     print(float(i))
#test_docs = [ x.strip().split() for x in codecs.open(test_docs, "r", "utf-8_sig").readlines() ]
corpus=m.docvecs
#np.savetxt("D:\pydata\mypydata\paper_data\data_robot\patent_data_vector.txt",np.asarray(corpus))
np.save("D:\pydata\mypydata\paper_data\data_robot\patent_data_vector.xls",np.asarray(corpus))
#print(type(np.asarray(corpus)))

#distance=m.n_similarity('increase','enhanced')
#distance=m.wmdistance(test_docs[0],test_docs[1])
#print(distance)
# print(test_docs)
#infer test vectors
# output = open(output_file, "w")
# for d in test_docs:
#     output.write( " ".join([str(x) for x in m.infer_vector(d, alpha=start_alpha, steps=infer_epoch)]) + "\n" )
# output.flush()
# output.close()
