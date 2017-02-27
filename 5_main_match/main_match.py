#读取syntaxnet语义依存树，根据句子来
def load_syntaxnet_parsh(textroot):
    sentence={}
    sentences=[]
    with codecs.open(textroot,"rb","utf-8") as f:
        for word in f.readlines():
            word=word.split()
            if len(word)<=0:
                continue
            if int(word[0])==1:
                sentences.append(sentence)
                sentence={}
            sentence[int(word[0])]=word[1:]


    return sentences
#从语义依存分析结果中，分析主干
def extract_main(sentence_parsh):
    main={}
    #寻找root
    rootid=-1
    for item in sentence_parsh:
        if sentence_parsh[item][6]=="ROOT":
            rootid=str(item)
            main['ROOT']=sentence_parsh[item][0]
            break

    for item in sentence_parsh:
        if sentence_parsh[item][5]==str(rootid):
            if sentence_parsh[item][6]=="nsubj":
                main['nsubj']=sentence_parsh[item][0]
            elif sentence_parsh[item][6]=="dobj":
                main['dobj']=sentence_parsh[item][0]
    if len(main)==3:
        print  "main:",json.dumps(main, encoding="UTF-8", ensure_ascii=False)
par=load_syntaxnet_parsh("data/out.txt")
for p in par:
    extract_main(p)
