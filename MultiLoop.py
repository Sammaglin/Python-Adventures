import tkinter as tk

t=input("What table do you want to display -->")
t=int(t)
for i in range(11):
    print(t,"X",i,"=",t*i)
    