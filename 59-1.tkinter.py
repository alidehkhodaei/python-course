from tkinter import *

root = Tk()  # Create a instance of Tk (window)
root.title("Ali")  # Set title
root.geometry("400x300")  # Set size for window
root.resizable(width=False, height=False)  # Fix width and height

my_name = StringVar()
full_name = "Hello there"

label = Label(root, text="This is a label.")  # Create a label
label.place(x=0, y=0)  # Set position label

label_2 = Label(root, textvariable=my_name)
label_2.place(x=0, y=20)

label_3 = Label(root, text=full_name)
label_3.place(x=0, y=40)

def print_my_name():
    print("Hello")


def print_my_name_2():
    my_name.set("Ali")


def print_my_name_3():
    full_name = "Reza" # This variable don't changed when click button / we should use to StringVar().

# Or

def print_my_name_4(new_full_name): # Pass by value
    new_full_name = "Reza"


btn = Button(root, text="Click me!", command=lambda: print_my_name())  # Create a button
btn.place(x=0, y=70)

btn2 = Button(root, text="Click me!", command=lambda: print_my_name_2())
btn2.place(x=0, y=110)

btn3 = Button(root, text="click me!", command=lambda: print_my_name_3())
btn3.place(x=0, y=150)

btn4 = Button(root, text="click me!", command=lambda: print_my_name_4(full_name))
btn4.place(x=0, y=190)

root.mainloop()  # Show window
