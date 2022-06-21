import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    num4 = random.randint(1, 100)
    num5 = random.randint(1, 100)
    num6 = random.randint(1, 100)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title='Lottery Ticket', message= str(num1) + " " + str(num2) + " " + str(num3) + " " + str(num4) + " " + str(num5) + " " + str(num6))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
