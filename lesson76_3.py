'''
方法三
'''
import turtle as t
def banyuan(r, d):
    for i in range(0, 180):
        t.fd(0.0174*r)
        if(d==1):
            t.rt(1)
        else:
            t.lt(1)
    return
 
banyuan(50, 1)
t.rt(180)
banyuan(100, 0)
banyuan(50, 0)
t.done()