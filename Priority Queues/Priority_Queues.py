# -*-encoding: utf8-*-
import re
def swap(data,i,j):
    temp = data[i]
    data[i]=data[j]
    data[j]=temp
#令root的左右子树皆符合heap，如果不符合将此树调整为max heap
def heapify(data,root,len):
    leftchild = root*2+1;
    rightchild = root*2+2;
    maxnode = -1;

    if(leftchild <len and (data[leftchild]>data[root])):
        maxnode = leftchild;
    else:
        maxnode = root
    if(rightchild < len and (data[rightchild])>data[maxnode]):
        maxnode = rightchild

    if(maxnode!=root):
        swap(data,root,maxnode)
        heapify(data,maxnode,len)

def heapsort(data):
    #将数列转换成max heap
    l=int(len(data)/2)-1
    for i in range(l+1):
        heapify(data,l,len(data))
        l=l-1

    #排序
    '''k=len(data)-1
    for i in range(k):
        swap(data,0,k)
        heapify(data,0,k)
        k=k-1
        '''

def main():
    heap = []
    file=open('03_input.in','r')
    while True:
        a=file.readline()
        if not a:
            break
        data=[]
        data=re. findall(r"\d+\d*",a)
        data=map(int,data)
    #print data
    #data=[14,16,10,8,3,7,9,4,2,1]
    file.close()
    heapsort(data)
    print data
    file.close()
if __name__ == '__main__':
    main()