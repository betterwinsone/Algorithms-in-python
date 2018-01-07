#_*_coding:utf-8_*_
from __future__ import print_function
def find_path(path, word):
        if len(pre_word[word])==0:
            path.append(word); curr_path=path[:]
            curr_path.reverse(); result.append(curr_path)
            path.pop()
            return
        path.append(word)
        for i in pre_word[word]:
            find_path(path, i)
        path.pop()
def find_Ladders(start, end, dict):
    distance=1
    word_long=len(start)
    for i in dict:
        pre_word[i]=[]
    level_word=[set(),set()]; cur=0; pre=1
    level_word[cur].add(start)
    while True:
        cur, pre=pre, cur
        for i in level_word[pre]: dict.remove(i)
        level_word[cur].clear()
        for word in level_word[pre]:
            for i in range(word_long):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i]!=j:
                        next_word=word[:i]+j+word[i+1:]
                        if next_word in dict:
                            pre_word[next_word].append(word)
                            level_word[cur].add(next_word)
        distance=distance+1
        if len(level_word[cur])==0: return result
        if end in level_word[cur]: break
    return distance



def
    ():
    file_txt=[]
    file=open('08_input.in','r')
    while True:
        a=file.readline()
        a=a.strip('\n')
        file_txt.append(a)
        if not a:break
    file.close()
    return file_txt

if __name__ == "__main__":
    result=[] #找出的最短路径
    pre_word={}#前驱单词表,字典类型，pre_word={cog:[log, dog]}表示cog的前驱是：log和dog。
    all_word=read_dictionary()#读取字典的单词
    #print (all_word)
    distance=find_Ladders("aaa", "jab", set(all_word))#寻找最短路径
    k=0
    #print (len(result[0]))
    find_path([], 'jab')#使用DFS来重建一条最短路径
    for i in result[0]:
        print(i,end=' ')
        if k==len(result[0])-1:
            print ('')
            break
        else:
            print("->",end=' ')
        k=k+1
    print (distance)
