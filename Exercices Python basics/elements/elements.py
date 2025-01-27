from elements_lists import (ELEMENTS_NAME,ELEMENTS_SYMBOLS,ATOMIC_WEIGHTS,ELEMENTS_COMMON_LOCATIONS,ELEMENTS_HAZARD)

def print_menu():
    print("""                              || ELEMENTS INFORMATIONS ||
          
          This program will show you all the information about a specific element.\n""")
    

def get_searching_metod():
    print("Would you prefer to search the desired element by its name or its atomic number?")
    decision = input("Enter here: ").strip()

    while decision!="name" and decision!="atomic number":
        print("The element must be searched my \"name\" or \"atomic number\".")
        decision = input("Re-enter here: ")

    return decision


def get_element_name():
    name = input("Insert the name of the desired element: ")

    while name not in ELEMENTS_NAME:
        print("There's no known element with the name you typed.")
        name = input("Re-enter here: ")

    return name


def get_atomic_number():
    while True:
        try:
            atomic_number = int(input("Insert the atomic number of the desired element: "))
            break
        except ValueError:
            print("You must insert a number.")
            atomic_number = input("Re-enter here: ")

    while atomic_number<1 or atomic_number>118:
        print("There's no known element with the atomic number you typed.")   
        while True:
            try:
                atomic_number = int(input("Re-enter here: ")) 
                break
            except ValueError:
                print("You must insert a number.")
                atomic_number = input("Re-enter here: ")

    return atomic_number


def print_element_statistic(name,atomic_number):
        print("\nName:", name)
        print("Symbol:", ELEMENTS_SYMBOLS[atomic_number])
        print("Atomic Number:", atomic_number+1)
        print("Atomic Weight:", ATOMIC_WEIGHTS[atomic_number])
        print("Hazard Level:", ELEMENTS_HAZARD[atomic_number])
        print("Most Commonly Found:", ELEMENTS_COMMON_LOCATIONS[atomic_number])
        print("\n")


def main():
    print_menu()
    decision = get_searching_metod()
    
    while True:
        if decision=="name":
            name = get_element_name()
            atomic_number = ELEMENTS_NAME.index(name)
            print_element_statistic(name,atomic_number)
        else:
            atomic_number = get_atomic_number()
            name = ELEMENTS_NAME[atomic_number-1]
            print_element_statistic(name,atomic_number-1)

        print("Would you like to search another element?")
        answer = input("Type your answer here: ")

        while answer!="yes" and answer!="no":
            print("You must responde with\"yes\" \"no\"")
            answer = input("Type your answer here: ")
    
        if answer=="yes":
            continue
        else:
            print("OK, See you soon.")
            break

main()