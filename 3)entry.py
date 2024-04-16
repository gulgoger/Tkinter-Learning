from tkinter import *

window = Tk()
window.title("Tkinter Learning")
window.geometry("600x400+200+200")

def click_clear_button():
    data_entry.delete(0,END)

def click_send_button():
    print("button clicked")
    data_input = data_entry.get()
    print(data_input)
    click_clear_button()

def click_send_button2():
    data_input_text = text_input.get(1.0,END)
    print(data_input_text)

data_entry = Entry(width=40)
data_entry.focus()
data_entry.pack()

clear_button = Button(text="clear",width=30,bg="black",fg="white",command=click_clear_button)
clear_button.pack()

send_button = Button(text="Send",width=30,bg="black",fg="white",command=click_send_button)
send_button.pack()

text_input = Text(width=30,height=5,bg="light blue",fg="black")
text_input.pack(padx=10,pady=10)

send_button2 = Button(text="Send",width=30,bg="black",fg="white",command=click_send_button2)
send_button2.pack()



window.mainloop()