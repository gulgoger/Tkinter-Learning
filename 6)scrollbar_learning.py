from tkinter import *

window = Tk()
window.title("Tkinter Learning")
#window.geometry("400x300+200+200")

# scrollbar y side
# my_scrollbar = Scrollbar()
# my_scrollbar.pack(side=RIGHT,fill=Y)

# my_text = Text(bg="black",fg="white",yscrollcommand=my_scrollbar.set)
# my_text.pack()
# my_scrollbar.config(command=my_text.yview)

# scrollbar x side
my_scrollbar = Scrollbar()
my_scrollbar.pack(side=RIGHT,fill=Y)

# my_text = Text(bg="black",fg="white",wrap=NONE, xscrollcommand=my_scrollbar.set)
# my_text.pack()

mylist = Listbox(yscrollcommand=my_scrollbar.set,width=30, height=20)

for line in range(1,100):
    mylist.insert(END, "Item" + str(line))

mylist.pack(side=LEFT, fill=BOTH)

my_scrollbar.config(command=mylist.yview)



window.mainloop()