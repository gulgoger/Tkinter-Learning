from tkinter import *

window = Tk()
window.title("Tkinter Learning")
window.geometry("400x300+200+200")

#scale
def print_selection(value):
    print(value)

my_scale = Scale(from_=100, to=200, command=print_selection,label="volume")
my_scale.pack()

my_scale2 = Scale(from_=1, to=100, command=print_selection,label="bas")
my_scale2.pack()

#spinbox
def spinbox_selected():
    print(my_spinbox.get())

my_spinbox = Spinbox(from_=0,to=100,values=(0,10,20,30,40,50,60,70,80,90,100),command=spinbox_selected)
my_spinbox.pack()


window.mainloop()