'''
绘制扇子
'''
import turtle as t
def sanjiao():
    for i in range(0,3):
        t.fd(100)
        t.lt(120)
    return
 
t.lt(20)
for i in range(0,9):
    sanjiao()
    t.lt(10)
t.done()