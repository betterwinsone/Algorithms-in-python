#-*-encoding:utf8-*-
import re
#将重叠的数组进行排序，前提是在进行merge之前所有的数组要先按照从小到大的顺序排序
def merge(data):
    result=[]
    for i in range(1,len(data)):
        if data[i-1][1]>=data[i][0]:
            data[i][0]=data[i-1][0]
            data[i][1]=data[i][1]
        else:
            result.append(data[i-1])
        #处理最后一个数组
        if i is (len(data)-1) and data[i-1][1]>=data[i][0]:
            data[i][0]=data[i-1][0]
            data[i][1]=data[i][1]
            result.append(data[i])
        if i is (len(data)-1) and data[i-1][1]<data[i][0]:
            result.append(data[i])
    #结果输出，先将list强制装换成str,在用切片操作
    output=str(result)[1:len(str(result))-1]
    print output
def main():
    file=open('04_input.in','r')
    while True:
        data=[]#sample input
        result=[]
        a=file.readline()
        #print a
        if not a:
            break
        data_list=re.findall(r'\d+',a)#只读取数值，返回list
        #print data_list
        data_list=map(int,data_list)#将list的值转换为int的数值
        #print data_list

        for i in range(0,len(data_list),2):#i=0,i<len(data),i+=2
            data.append([data_list[i],data_list[i+1]])
        #print data
        #print len(data)
        merge(data)
    file.close()


if __name__ == '__main__':
    main()