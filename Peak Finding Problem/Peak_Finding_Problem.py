#-*- coding: utf-8 -*-
import re
def read_data(file_name):
    data_list=[]
    file=open(file_name,'r')
    while True:
        line_data=file.readline()#按行读取test的数据
        if not line_data:break
        data=re.findall(r'\d+',line_data)#返回a中任何的十进制数,如果没有返回空list
        if not data:
            continue
        else:
            data=map(int,data)#将data转化成int类型
            data_list.append(data)#将data保存在list1
    return data_list
    file.close()
def findpeak(data_list):
    peak=[]
    sum=0
    max=0
    for i in range(1,4):
        for j in range(1,4):
            #print i,j
            if data_list[i][j]>data_list[i][j-1] and data_list[i][j]>data_list[i][j+1] and data_list[i][j]>data_list[i-1][j] and data_list[i][j]>data_list[i+1][j]:
                sum=data_list[i][j]-data_list[i][j-1] + data_list[i][j]-data_list[i][j+1] + data_list[i][j]-data_list[i-1][j] + data_list[i][j]-data_list[i+1][j]
                #print data_list[i][j]
                #peak.append(data_list[i][j])
                if sum>max:
                    max=sum
                    a=i
                    b=j
    #print peak
    return a,b


def main():
    data_list=read_data('02_input.in')
    #print data_list
    x,y=findpeak(data_list)
    print"return index of %d (which is [%d,%d])" %(data_list[x][y],x,y)
if __name__ == '__main__':
    main()