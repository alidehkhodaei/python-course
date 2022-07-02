from tkinter import *
import DatabaseFunction

window = Tk()
window.title="Book Store"

# -------------------Labels----------------------

li = Label(window, text="Title")
li.grid(row=0, column=0)

li2 = Label(window, text="Author")
li2.grid(row=0, column=2)

li3 = Label(window, text="Year")
li3.grid(row=1, column=0)

li4 = Label(window, text="Isbn")
li4.grid(row=1, column=2)

# -------------------Entries---------------------

title_text = StringVar()
entry_1 = Entry(window, textvariable=title_text)
entry_1.grid(row=0, column=1)

author_text = StringVar()
entry_2 = Entry(window, textvariable=author_text)
entry_2.grid(row=0, column=3)

year_text = StringVar()
entry_3 = Entry(window, textvariable=year_text)
entry_3.grid(row=1, column=1)

isbn_text = StringVar()
entry_4 = Entry(window, textvariable=isbn_text)
entry_4.grid(row=1, column=3)

# ----------------------ListBox---------------------

list_box = Listbox(window, width=30, height=6)
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

list_box.configure(yscrollcommand=sb.set)
sb.configure(command=list_box.yview)


def get_selected_row(event):
    global selected_book
    index = list_box.curselection()[0]
    selected_book = list_box.get(index)

    entry_1.delete(0, END)
    entry_1.insert(END, selected_book[1])

    entry_2.delete(0, END)
    entry_2.insert(END, selected_book[2])

    entry_3.delete(0, END)
    entry_3.insert(END, selected_book[3])

    entry_4.delete(0, END)
    entry_4.insert(END, selected_book[4])


list_box.bind("<<ListboxSelect>>", get_selected_row)


# -----------------Functions---------------------

def clear_list(): list_box.delete(0, END)


def fill_list(data):
    for item in data:
        list_box.insert(END, item)


def view_command():
    clear_list()
    data = DatabaseFunction.view()
    fill_list(data)


def search_command():
    clear_list()
    data = DatabaseFunction.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    fill_list(data)


def add_command():
    DatabaseFunction.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()


def update_command():
    DatabaseFunction.update(selected_book[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()


def delete_command():
    DatabaseFunction.delete(selected_book[0])
    view_command()


# -----------------Buttons-----------------------

bt1 = Button(window, text="View All", width=12, command=lambda: view_command())
bt1.grid(row=2, column=3)

bt2 = Button(window, text="Search Entry", width=12, command=lambda: search_command())
bt2.grid(row=3, column=3)

bt3 = Button(window, text="Add Entry", width=12, command=lambda: add_command())
bt3.grid(row=4, column=3)

bt4 = Button(window, text="Update Selected", width=12, command=lambda: update_command())
bt4.grid(row=5, column=3)

bt5 = Button(window, text="Delete Selected", width=12, command=lambda: delete_command())
bt5.grid(row=6, column=3)

bt6 = Button(window, text="Close", width=12, command=lambda: window.destroy())
bt6.grid(row=7, column=3)

# --------------------------------------------------

view_command()

window.mainloop()
