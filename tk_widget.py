#Gli elementi grafici, anche interagibili, che compaiono nella finestra prendono il nome di "widget".

#Il codice sottostante crea una finestra senza alcun elemento grafico al suo interno

import tkinter as tk

window_widget = tk.Tk()
window_widget.title("Window With Widgets")

#La funzione tk.Label crea del testo che compare in una specifica finestra e utilizza con il comando: <Nome Variabile> = tk.Label(<Nome Variabile Della Finestra>, text = "Testo">)
#La funzione <Nome Variabile Widget>.pack() posiziona automaticamente i widgets di testo creati in colonna e stamparlo a schermo nella finestra

text_one = tk.Label(window_widget, text = "This is a test")
text_two = tk.Label(window_widget, text = "And This is a second test")
text_one.pack()
text_two.pack()

#La funzione tk.Button è un widget assegnato a una variabile che crea un pulsante. Una volta cliccato manualmente, legge un blocco di codice specifico.
#Si utilizza con il comando: <Nome Variabile> = tk.Button(<Nome Variabile Della Finestra>, text = "Testo Sul Pulsante", command = <Codice Letto Se Si Preme Sul Pulsante>)
#ATTENZIONE! La funzione eseguita dopo il "command", se non inserita nella finestra generata, viene eseguita di base nel terminale

def print_message():
    text_button = tk.Label(window_widget, text = "You clicked the button!")
    text_button.pack()


def print_second_message():
    second_text_button = tk.Label(window_widget, text = "You clicked another button!")
    second_text_button.pack()


def print_third_message():
    print("You clicked another button again!")


def show_buttons():
    button = tk.Button(window_widget, text = "Click Here First", command = print_message)
    button.pack()

    button_two = tk.Button(window_widget, text = "Click Here After", command = print_second_message)
    button_two.pack()

    button_three = tk.Button(window_widget, text = "Click Here And Print In The Terminal", command = print_third_message)
    button_three.pack()


show_buttons()
window_widget.mainloop()