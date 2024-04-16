from tkinter import *

window = Tk()
window.title("Label Learning")
window.geometry("600x400")

my_label = Label(text="this is a label",fg = "#E7E241",bg="black",font="Arial 30 bold underline")
my_label.grid(row=0,column=0)

def click_button():
    my_label.config(text="button clicked",fg="blue")
    #print("button clicked")

my_button = Button(text="Ok", command=click_button,fg="white",bg="black")
my_button.grid(row=0,column=1)

my_label2 = Label(text="this is a label2",fg = "#E7E241",bg="black",font="Arial 30 bold underline")
my_label2.grid(row=1,column=1)


window.mainloop()
