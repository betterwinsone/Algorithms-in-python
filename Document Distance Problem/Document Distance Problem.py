#-*- coding: utf-8 -*-
import string
import math
def computing_word_freq(file_name):
    file=open(file_name,'r')
    doc = file.read()#读取文件的所有内容
    doc = doc.translate(string.maketrans(string.punctuation," "*len(string.punctuation)))#将所有标点符号转换为空格
    doc = doc.translate(string.maketrans(string.uppercase,string.lowercase))#将大写字母转换为小写字母
    words = doc.split()#分词
    dic={}#字典<key.value>:<word：num>
    for word in words:
                if dic.has_key(word):      #如果存在次数加1
                    value = dic[word]
                    dic[word] = value + 1
                elif word!="":                            #否则初值为1
                    dic[word] = 1
    print "File",file_name,":",
    print len(dic),"distinct words"
    file.close()
    return dic

def computing_product_distance(d1,d2):#计算两个文档的distance
    x = 0
    s1 = 0
    s2 = 0
    for word in d1:
        if word in d2:
            x = x + d1[word] * d2[word]
    for word in d1:
        s1=s1+d1[word]*d1[word]
    for word in d2:
        s2=s2+d2[word]*d2[word]
    y = math.sqrt(s1*s2)
    distance =math.acos(float(x) /y)#反余弦
    print "The distance between the documents is: %0.6f"%distance,"(radians)"#输出两个文件的distance


def main():
    file1_name='t2.bobsey.txt'
    file2_name='t1.verne.txt'
    freq1=computing_word_freq(file1_name)
    freq2=computing_word_freq(file2_name)
    computing_product_distance(freq1,freq2)

if __name__ == '__main__':
    main()
