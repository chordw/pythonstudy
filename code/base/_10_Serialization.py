import pickle

# 序列化
f = open('C:\serialization.txt', 'wb')
d = ['a', 1, 2, 36]
ds = pickle.dump(d, f)
f.close()

# 反序列化
ff = open('C:\serialization.txt', 'rb')
da = pickle.load(ff)
for x in da:
    print(x)
print(da)
ff.close()

# JSON
# dict 对应 {}
# list 对应 []
# True/False 对应 true/false
# None对应 null

import json

jd = [5, 6, 56, 23, 78]
fj = open('C:\json.txt','w')
jo = json.dump(jd, fj)
print(jo)
fj.close()
