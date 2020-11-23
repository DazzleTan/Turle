'''
每个正方形长度依次增加10
'''
import turtle as t
s = 40
for i in range(0,7):
    for j in range(0,4):
        t.fd(s)
        t.lt(90)
    s=s+10
t.done()