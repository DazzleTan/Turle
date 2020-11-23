'''
绘制正六角形
'''
import turtle as t
def sanjiao():
    for i in range(0,4):
        t.fd(50)
        t.rt(120)
    return
 
for i in range(0,6):
    sanjiao()
    t.lt(180)
t.done()