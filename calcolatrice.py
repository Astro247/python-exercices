from math import sqrt


def printa_menu():
    print("""|| Benvenuto nella Calcolatrice di Manu ||
      
      [1] = Addizione
      [2] = Sottrazione
      [3] = Moltiplicazione
      [4] = Divisione
      [5] = Calcolo Esponenziale
      [6] = Radice\n""")


def insert_operator():
    num_inserito = input("Inserire il numero corrispondente all'operazione desiderata: ")

    while num_inserito<"1" or num_inserito>"6":
        num_inserito = input("Hai inserito un operazione inesistente, ripetere l'inserimento: ")
    return num_inserito


def operation_procedure(num_inserito):
    if num_inserito == "1":
        print("Hai selezionato l'addizione, inserire i valori \"a\" e \"b\" per ottenere \"c\": a + b = c")

    elif num_inserito == "2":
        print("Hai selezionato la sottrazione, inserire i valori \"a\" e \"b\" per ottenere \"c\": a - b = c")

    elif num_inserito == "3":
        print("Hai selezionato la moltiplicazione, inserire i valori \"a\" e \"b\" per ottenere \"c\": a · b = c")

    elif num_inserito == "4":
        print("Hai selezionato la divisione, inserire i valori \"a\" e \"b\" per ottenere \"c\": a/b = c")

    elif num_inserito == "5":
        print("Hai selezionato il calcolo esponenziale, inserire i valori \"a\" e \"b\" per ottenere \"c\": a^b = c")

    elif num_inserito == "6":
        print("Hai selezionato la radice, inserire i valori \"a\" e \"b\" per ottenere \"c\": radice con indice \"a\" di \"b\" = c ")


def controllo_value_error(message):
    val = input(message)
    while True:
        try:
            val = float(val)
            break
        except ValueError:
            val = input("Valore obsoleto, ripetere l'inserimento: ")
    return val


def calculate_c(num_inserito, a, b):
    if num_inserito == "1":
        c = a+b

    elif num_inserito == "2":
        c = a-b

    elif num_inserito == "3":
        c = a*b

    elif num_inserito == "4":
        if a == 0 and b == 0:
            c = "Indeterminato"
        elif b == 0:
            c = "Impossibile"
        else:
            c = a/b

    elif num_inserito == "5":
        if a == 0 and b == 0:
            c = "Indeterminato"
        else:
            c = a**b

    elif num_inserito == "6":
        if a==0:
            c = "Indeterminato"
        else:
            c = b**(1/a)
    return c


def main():
    printa_menu()

    while True:

        num_inserito = insert_operator()
        operation_procedure(num_inserito)
        a = controllo_value_error("a = ")
        b = controllo_value_error("b = ")
        print("c =", calculate_c(num_inserito,a,b))

        print("\nVuoi ri-utilizzare la calcolatrice?")
        risposta = input("Rispondere con \"si\" oppure \"no\": ")
        while risposta != "si" and risposta != "no":
            risposta = input("Ti preghiamo di rispondere con \"si\" oppure \"no\": ")
        if risposta == "si":
            continue
        else:
            print("A presto.")
            break

main()