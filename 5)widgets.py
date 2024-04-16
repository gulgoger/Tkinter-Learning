from tkinter import *

window = Tk()
window.title("Python Tkinter Widgets")
window.geometry("600x400+200+200")

#checkbutton
def checkbutton_selected():
    print(check_state.get())

check_state = IntVar() # tıklanıp tıklanmadıgını gosterır 0-1 olarak
my_checkbutton = Checkbutton(text="check",variable=check_state,command=checkbutton_selected)
my_checkbutton.pack()

#radiobutton
def radioselected():
    print(radio_check_state.get())

radio_check_state = IntVar()
my_radiobutton = Radiobutton(text="Option 1",value=100,variable=radio_check_state,command=radioselected)
my_radiobutton2 = Radiobutton(text="Option 2",value=200,variable=radio_check_state,command=radioselected)
my_radiobutton.pack()
my_radiobutton2.pack()

window.mainloop()
