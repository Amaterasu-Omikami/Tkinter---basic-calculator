from tkinter import *

window = Tk()
window.title("Calculator")
window.minsize(width=200, height=200)

# LABELS
first_number_label = Label(text="first number:")
first_number_label.grid(row=1, column=0)

second_number_label = Label(text="second number:")
second_number_label.grid(row=2, column=0)

operations_symbol = Label(text="Operations:")
operations_symbol.grid(row=3, column=0)

# ENTRIES
first_number_entry = Entry(width=35)
first_number_entry.grid(row=1, column=1, columnspan=2)
first_number = first_number_entry.get()
first_number_entry.focus()

second_number_entry = Entry(width=35)
second_number_entry.grid(row=2, column=1, columnspan=2)
second_number = second_number_entry.get()


# SAVING THE NUMBER INPUTS FUNCTIONS
def save_first_number():
    global first_number
    first_number = None
    first_number = first_number_entry.get()


def save_second_number():
    global second_number
    second_number = None
    second_number = second_number_entry.get()


# CALCULATOR FUNCTIONS
def add():
    text_box.delete("1.0", END)
    sum = int(first_number) + int(second_number)
    text_box.insert(END, sum)


def sub():
    text_box.delete("1.0", END)
    sum = int(first_number) - int(second_number)
    text_box.insert(END, sum)


def multipy():
    text_box.delete("1.0", END)
    sum = int(first_number) * int(second_number)
    text_box.insert(END, sum)


def divide():
    text_box.delete("1.0", END)
    sum = int(first_number) / int(second_number)
    text_box.insert(END, sum)

# BUTTONS
add_button = Button(text="+", width=5, command=add)
add_button.grid(row=3, column=2)

subtract_button = Button(text="-", width=5, command=sub)
subtract_button.grid(row=3, column=3)

multiply_button = Button(text="*", width=5, command=multipy)
multiply_button.grid(row=3, column=4)

divide_button = Button(text="/", width=5, command=divide)
divide_button.grid(row=3, column=5)

first_number_button = Button(text="Save", command=save_first_number)
first_number_button.grid(row=1, column=3)
second_number_button = Button(text="Save", command=save_second_number)
second_number_button.grid(row=2, column=3)

# WRITING THE ANSWER IN THE TEXT BOX
text_box = Text(height=5, width=20)
text_box.grid(row=5, column=1)
text_box.insert(END, "The answer")



window.mainloop()
