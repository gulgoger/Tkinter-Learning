from tkinter import *

root = Tk()
root.title("Tkinter Learning")
root.geometry("400x200+250+250")


menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

def copy_button():
    print("copied")

def open_button():
    open_window = Toplevel()

file_menu.add_command(label="Open",command=open_button)
#file_menu.add_command(label="Save")

save_menu = Menu(file_menu,tearoff=0)
file_menu.add_cascade(label="Save", menu=save_menu)
save_menu.add_command(label=".py")
save_menu.add_command(label=".exe")

file_menu.add_command(label="Exit",command=exit)

edit_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu = edit_menu)

edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy",command=copy_button)

root.mainloop()