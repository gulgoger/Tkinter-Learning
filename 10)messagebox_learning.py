from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tkinter Learning")
root.geometry("400x200+250+250")

def click_message_button():

    # Information message box
    #messagebox.showinfo("showinfo", "Information")

    # Warning message box
    #messagebox.showwarning("showwarning","Warning")
    #messagebox.showerror("showerror","Error")

    # Question message box
    #messagebox.askquestion("askquestion","Are you sure?")
    #messagebox.askokcancel("askokcancel","Want to continue?")
    #messagebox.askyesno("askyesno","Find the value?")
    #messagebox.askretrycancel("askretrycancel","Try again?")
    messagebox.askyesnocancel("askyesnocancel","Are you sure?")

message_button = Button(text="Message",command=click_message_button)
message_button.pack()

root.mainloop()