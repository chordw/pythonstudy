import chardet

ch = chardet.detect('hello,world'.encode('utf-8'))
print(ch)

a= '再见了，心爱的'.encode('gbk')
print(chardet.detect(a))