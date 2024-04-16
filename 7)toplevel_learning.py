from tkinter import *

root = Tk()
root.title("Tkinter Learning")
root.geometry("400x300")

label1 = Label(root,text="This is root window")
label1.pack()

def add_window():
    top = Toplevel()
    top.geometry("200x100")
    top.title("Toplevel")
    label2 = Label(top,text="This is toplevel window")
    label2.pack()
    exit_button = Button(top, text="exit", command=exit)
    exit_button.pack()

add_button = Button(root,text="add window",command=add_window)
add_button.pack()

root.mainloop()