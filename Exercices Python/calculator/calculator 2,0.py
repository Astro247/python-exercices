#This project is unfinished

from tkinter import *


def print_characters(show_operation, character, operation):
    show_operation.insert(END,character)
    get_operation(operation,character)


def delete_all(show_operation, operation):
    show_operation.delete(0,END)
    operation.clear()


def get_operation(operation, character):
    operation.append(character)


def get_separated_numbers(operation, numbers_list):
    operation_string = ""

    for number in operation:
        operation_string.join(number)
        if number=="+-x÷=":
            continue
    numbers_list.append(operation_string)
    operation_string = ""
                

def main():

    calculator_gui = Tk()
    calculator_gui.title("Astro's Calculator 2.0")

    calculator_gui.geometry("357x260")
    calculator_gui.config(bg="gray")
    calculator_icon = PhotoImage(file = "calculator_image.png")
    calculator_gui.iconphoto(True,calculator_icon)

    show_operation = Entry(state=NORMAL)
    show_operation.config(font=("Fixedsys", 20, "bold"))
    show_operation.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    operation = []
    numbers_list = []


    button_7 = Button(calculator_gui, text="7", command=lambda: print_characters(show_operation,"7", operation))
    button_7.config(font=("Fixedsys", 20, "bold"))
    button_8 = Button(calculator_gui, text="8", command=lambda: print_characters(show_operation,"8", operation))
    button_8.config(font=("Fixedsys", 20, "bold"))
    button_9 = Button(calculator_gui, text="9", command=lambda: print_characters(show_operation,"9", operation))
    button_9.config(font=("Fixedsys", 20, "bold"))
    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_4 = Button(calculator_gui, text="4", command=lambda: print_characters(show_operation,"4", operation))
    button_4.config(font=("Fixedsys", 20, "bold"))
    button_5 = Button(calculator_gui, text="5", command=lambda: print_characters(show_operation,"5", operation))
    button_5.config(font=("Fixedsys", 20, "bold"))
    button_6 = Button(calculator_gui, text="6", command=lambda: print_characters(show_operation,"6", operation))
    button_6.config(font=("Fixedsys", 20, "bold"))
    button_6.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_4.grid(row=2, column=2)

    button_1 = Button(calculator_gui, text="1", command=lambda: print_characters(show_operation,"1", operation))
    button_1.config(font=("Fixedsys", 20, "bold"))
    button_2 = Button(calculator_gui, text="2", command=lambda: print_characters(show_operation,"2", operation))
    button_2.config(font=("Fixedsys", 20, "bold"))
    button_3 = Button(calculator_gui, text="3", command=lambda: print_characters(show_operation,"3", operation))
    button_3.config(font=("Fixedsys", 20, "bold"))
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_0 = Button(calculator_gui, text="0", command=lambda: print_characters(show_operation,"0", operation))
    button_0.config(font=("Fixedsys", 20, "bold"))
    button_cancel = Button(calculator_gui, text="C", command=lambda: delete_all(show_operation, operation))
    button_cancel.config(font=("Fixedsys", 20, "bold"))
    button_equal = Button(calculator_gui, text="=", command=lambda: print_characters(show_operation, "=", operation))
    button_equal.config(font=("Fixedsys", 20, "bold"))
    button_0.grid(row=4, column=0)
    button_cancel.grid(row=4, column=1)
    button_equal.grid(row=4, column=2)

    button_divided = Button(calculator_gui, text="÷", command=lambda: print_characters(show_operation,"÷", operation))
    button_divided.config(font=("Fixedsys", 20, "bold"))
    button_times = Button(calculator_gui, text="x", command=lambda: print_characters(show_operation,"x", operation))
    button_times.config(font=("Fixedsys", 20, "bold"))
    button_minus = Button(calculator_gui, text="-", command=lambda: print_characters(show_operation,"-", operation))
    button_minus.config(font=("Fixedsys", 20, "bold"))
    button_plus = Button(calculator_gui, text="+", command=lambda: print_characters(show_operation,"+", operation))
    button_plus.config(font=("Fixedsys", 20, "bold"))
    button_divided.grid(row=1, column=3)
    button_times.grid(row=2, column=3)
    button_minus.grid(row=3, column=3)
    button_plus.grid(row=4, column=3)

    get_separated_numbers(operation, numbers_list)
    button_test = Button(calculator_gui, text="test", command=lambda: print(operation))
    button_test.grid(row=5, column=0)
    button_test2 = Button(calculator_gui, text="test2", command=lambda: print(numbers_list))
    button_test2.grid(row=5, column=1)

    calculator_gui.mainloop()

main()
