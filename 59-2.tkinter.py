from tkinter import *

root = Tk()
root.title("Ali")
root.geometry("400x300")
root.resizable(width=False, height=False)

label=Label(root,text="Please enter your name:")
label.place(x=0,y=0)

input=Entry(root)
input.place(x=0,y=20)

def get_name():
    print(input.get())

btn=Button(root,text="Get name",command=lambda :get_name()) # Or command=get_name
btn.place(x=0,y=50)

root.mainloop()
