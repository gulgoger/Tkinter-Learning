from tkinter import *
from tkinter import messagebox

window= Tk()
window.title("Calculator")
window.geometry("270x250+300+100")
window.resizable(FALSE,FALSE)

store = ""

def calculate(key):
    global store
    if key in "0123456789":
        screen.insert(END,key)
        store = store + key

    if key in "+-*/":
        screen.insert(END,key)
        store = store + key
    
    if key == "=":
        screen.delete(0,END)
        result = eval(store,{"__builtins__":None},{})
        store = str(result)
        screen.insert(END,store)
    
    if key == "C":
        screen.delete(0,END)
        store = ""

screen = Entry(width=40, justify=RIGHT)
screen.grid(row=0,column=0,columnspan=3,ipady=4)

list = ["1","2","3","4","5","6","7","8","9","0","+","-","*","/","=","C"]

row = 1
column = 0

for i in list:
    command = lambda x=i: calculate(x)
    Button(text=i,font="verdana 8 bold",bg="light blue",fg="purple",width=10,height=2,relief=GROOVE,command=command).grid(row=row,column=column)
    column +=1
    if column >2:
        column = 0
        row += 1





window.mainloop()