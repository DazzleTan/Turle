'''
使用嵌套循环绘制4个方块
'''
import turtle as t
for i in range(0,4):
	for j in range(0,3):
		t.fd(50)
		t.rt(90)
	t.lt(180)
t.done()