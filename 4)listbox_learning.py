from tkinter import *

window = Tk()
window.title("Python Tkinter Widgets")
window.geometry("600x400+200+200")

def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()

item_list = ["Option 1","Option 2","Option 3","Option 4","Option 5","Option 6",]

for i in range(len(item_list)):
    my_listbox.insert(i, item_list[i])

my_listbox.bind("<<ListboxSelect>>",listbox_selected)
my_listbox.pack()



window.mainloop()