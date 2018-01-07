#-*-encoding:utf8-*-
class RollingHash:
        def __init__(self, string, size):
                self.str  = string#字符串
                self.hash_value = 0#hash值，这里是四个字符ASCII的值
                for i in xrange(0, size):
                        self.hash_value += ord(self.str[i])#将substr长度开头的字串转换成ASCII码加起来的值
                self.str_init = 0
                self.str_end  = size

        def update_hash_value(self):
                if self.str_end <= len(self.str) -1:
                        self.hash_value -= ord(self.str[self.str_init])#减去前一个字母的ASCII的值
                        self.hash_value += ord(self.str[self.str_end])#加上后一个字母的ASCII的值
                        self.str_init += 1#判断之后将位置往后移
                        self.str_end  += 1

        def return_hash_value(self):
                return self.hash_value

        def text(self):
                return self.str[self.str_init:self.str_end]
def rabin_karp(substring, string):
        s = RollingHash(string, len(substring))#获取hash值
        sub = RollingHash(substring, len(substring))
        sub.update_hash_value()#先算出子字符串的hash值
        for i in range(len(string)-len(substring)+1):
            if s.return_hash_value() == sub.return_hash_value():
                if s.text() == substring:
                    print "Pattern found at index " + str(i)
            s.update_hash_value()
def main():
    file = open('06_input.in', 'r')
    s=[]
    sub=[]
    ss=[]
    c = 0
    for line in file:
        line = line.strip()
        ss.append(line)
        c=c+1
        if (c%2 !=0):
            s.append(line)
        else :
            sub.append(line)
        if not line:
            break
    for i in range(c/2):
       rabin_karp(sub[i], s[i])
    file.close()
if __name__ == '__main__':
    main()