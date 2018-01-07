#-*-encoding:utf8-*-
import re
def main():
    file=open('05_input.in','r')
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
        data_list.sort()
        #print data_list
        count=0
        for i in range(len(data_list)-1):
            if data_list[i+1] is  data_list[i]+1 or data_list[i+1] is  data_list[i] :
                if data_list[i+1] is  data_list[i]:
                    continue
                else:
                    count=count+1
        print count+1
    file.close()


if __name__ == '__main__':
    main()