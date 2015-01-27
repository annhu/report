##create gram data
__author__ = 'Trista'
import re
import codecs
import glob
import os

doc_dic = {}
sen_dic = {}
words_dic = {}
find_words_dic={}
find_words_dic_dup={}
cleanCom = r'/|《|》|，|。|？|：|！|……|◎|——|「|」|,,|、|‧|－|）|（|%|；|,|\.|\(|\)|:|—|※|【|】|？|〈|〉|《|》|┌|┬|┐|〝|〞|‘|’|“|”|『|』|「|」|﹞|﹝|┤|┼|├|└|┴|┘|○|●|↑|↓|！|：|；|、|─|│|§|←|→|。|，|‧|？'
 
def ngram(dic, gram):
    for sentence in dic:
        for start in range(0, len(sentence.decode('utf-8'))):
            if (start+gram) <= len(sentence.decode('utf-8')):
                words = sentence.decode('utf-8')[start:start+gram]
                if words not in words_dic:
                    words_dic[words] = 1
                else:
                    words_dic[words] += 1
    return words_dic
 
def cutsentence(doc_dic, gram):
    sen_dic.clear()
    words_dic.clear()
    for content in doc_dic:
        content = content.strip()
        text = content.encode('utf-8')
        text_clean = re.sub(cleanCom, '|', text)
        newscon = text_clean.split('|')
        for putSentence in newscon:
            if putSentence not in '':
                sen_dic[putSentence] = ''
    words_list = ngram(sen_dic, gram)
    return words_list
def clean(path, gram):
    doc_dic.clear()
    sen_dic.clear()
    words_dic.clear()
    f = codecs.open(path, 'r',encoding='utf-8')
    for line in f.readlines():
        doc_dic[line] = ''
        words_list = cutsentence(doc_dic, gram)
    return words_list
    

blogfile= glob.glob("/home/iii/tainan_dic/blog_data/*.txt")
for blog in blogfile:
    filename= 'tainan_dic//gram_data//gram_data'+os.path.basename(blog)
    f2 = open(filename,'w')
    for gram in range(2,10):
        wordlist = clean(blog,gram)
        for w in wordlist:
            f2.write(w.encode('utf8')+'\n')
    f2.close()
print 'done gram'
