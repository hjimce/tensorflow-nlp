#coding=utf-8

import  numpy as np
import  codecs
import  os
import  re
import  json

#读取文本，根据句号、行段落进行分割
def load_data(textroot):
    sentences=[]
    with open(textroot,"rb") as f:
        for sentence in f.readlines():
            sentence=sentence.split()
            for s in sentence:
                s=re.split(u'：|”|“|，|。',s.decode('utf-8'))
                for s1 in s:
                    sentences.append(s1)
    return sentences
def load_traindata(textroot):
    sentences=[]
    with open(textroot,"rb") as f:
        for sentence in f.readlines():
            sentence=sentence.split()
            sentence=''.join(sentence)
            s=re.split(u'，|。',sentence.decode('utf-8'))
            for s1 in s:
                if len(s1)>10 and len(s1)<30:
                    print s1
                    sentences.append(s1)
    return sentences






def write_data(listsentences,textroot):
    print listsentences[0]
    with codecs.open(textroot,"wb","utf-8") as ftemp:
        for s in listsentences:
            if len(s)<20 and len(s)>15:
                ftemp.write(s + "\n")




par=load_traindata("../data/sougou.utf8")
write_data(par,"data.utf8")
#create_train_data("image","text","corpus/sougou.utf8")
#preprocess_data('text','text2id')]





