#-*-encoding:utf8-*-
import re
def rehash(table_size,insert_data):
    table=[None]*int(table_size)
    data=re.split(' ',insert_data)
    #print table,data[0]
    for i in range(len(data)):
        index=int(data[i])%int(table_size)
        table[index]=data[i]
    #print table
    content = ''
    for i in table:
        if i==None:
            i='None'
        content = content + i+' '
    print content
def main():
    file = open('07_input.in', 'r')
    first_line=[]
    second_line=[]
    ss=[]
    c = 0
    for line in file:
        line = line.strip()
        ss.append(line)
        c=c+1
        if (c%2 !=0):
            first_line.append(line)
        else :
            second_line.append(line)
        if not line:
            break
    file.close()
    for i in range(c/2):
        rehash(first_line[i],second_line[i])
if __name__ == '__main__':
    main()