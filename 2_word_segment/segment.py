
import jieba
import  codecs

def fenci(filename,outname) :
    out=codecs.open(outname,'wb',"utf-8")
    with codecs.open(filename,'rb',"utf-8") as f:
        for l in f.readlines():
            seg_list = jieba.cut(l,cut_all=False)
            out.writelines(" ".join(seg_list))
            #print

    out.close()



fenci("../1_data_prepare/data.utf8",'segment.utf8')