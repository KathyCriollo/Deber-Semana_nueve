# Estrella de n puntas impares.
import turtle
import os
num= int(input("Ingrese un número impar: "))
win=turtle.Screen()
win.bgcolor("MistyRose")
t=turtle.Pen()
t.reset()
t.color(1,0,0)
for x in range (1,num+1):
	v=(180-(90+90)/num)

	t.forward(100)
	t.left(v)
turtle.getscreen()._root.mainloop()