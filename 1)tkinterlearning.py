from tkinter import *   # sonraki kullanımlarda tkinter belirtmemize gerek kalmaz.
#import tkinter

window = Tk()
window.title("Python Tkinter")
window.geometry("600x400+200+200")   #window size
#window.minsize(300,200)
#window.maxsize(800,600)
window.resizable(TRUE,FALSE)

my_label = Label(text="this is a label")  # text in window
my_label.pack()  # label'ın gorunmesi icin yazilan bir method


window.mainloop()


























