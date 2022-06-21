import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO 1) Use each value of random_number to give the user a random compliment
    for i in range(10):
        random_number = random.randint(1, 5)
        if random_number == 4:
            messagebox.showinfo(title='Validation', message="You are cool!")
        if random_number == 1:
            messagebox.showinfo(title='Validation', message="You are nice!")
        if random_number == 2:
            messagebox.showinfo(title='Validation', message="You are great!")
        if random_number == 3:
            messagebox.showinfo(title='Validation', message="You are strong!")
        if random_number == 5:
            messagebox.showinfo(title='Validation', message="You are incredible!")
        print(random_number)
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
