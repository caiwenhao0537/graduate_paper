import nltk
from nltk.corpus import wordnet
def Word_synonyms_and_antonyms(word):
    synonyms=[]
    antonyms=[]
    list_good=wordnet.synsets(word)
    for syn in list_good:
        for l in syn.lemmas():
            #print('l.name()',l.name())
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return (set(synonyms),set(antonyms))
def Word_synonyms(word):
    list_synonyms_and_antonyms=Word_synonyms_and_antonyms(word)
    return list_synonyms_and_antonyms[0]
def Word_antonyms(word):
    list_synonyms_and_antonyms=Word_synonyms_and_antonyms(word)
    return list_synonyms_and_antonyms[1]
word='good'
result=Word_antonyms(word)
print(result)