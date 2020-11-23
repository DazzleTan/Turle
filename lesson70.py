'''
绘制5个相同的菱形
'''
import turtle as t
def lingxing1():
    for i in range(0,2):
        t.fd(50)
        t.rt(120)
        t.fd(50)
        t.rt(60)
    return
 
def lingxing2():
    for i in range(0,2):
        t.fd(50)
        t.lt(60)
        t.fd(50)
        t.lt(120)
    return
        
lingxing1()
t.fd(100)
lingxing1()
t.lt(60)
t.fd(50)
t.rt(60)
lingxing2()
t.bk(100)
lingxing2()
t.fd(50)
t.lt(60)
t.bk(50)
t.done()