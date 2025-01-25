#Tkinter è una libreria utile per creare "GUI", ossia finestre interattive, nel caso sottostante la libreria "tkinter" è richiamabile anche come "tk" per semplificare

import tkinter as tk

#Per creare una finestra si utilizza la funzione .Tk() e viene assegnata ad una variabile

window = tk.Tk()

#La funzione <Nome Finestra>.title da un nome alla finestra creata

window.title("Test Window")

#Nonostante la finestra è stata creata, una volta aperta si chiude automaticamente, poiché è pur sempre un programma che si apre e si chiude una volta terminato.
#Per risolvere questo problema si utilizza la funzione <Nome Finestra>.mainloop(), la quale fa sì che il programma entri in un ciclo while infinito per rimanere la finestra aperta.

window.mainloop()
