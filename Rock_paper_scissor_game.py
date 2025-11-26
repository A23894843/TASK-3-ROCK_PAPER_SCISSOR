import random
from tkinter import *
from tkinter import messagebox

user_choice = None
global sys_choice

choices = ("rock", "paper", "scissor")

def result():
    global user_choice
    sys_choice = ''.join(random.choice(choices))
    user_choice = user_choice.lower()  # Ensure lowercase
    sys_choice = random.choice(choices)  # Bot changes choice each round

    if sys_choice == user_choice:
        messagebox.showinfo("Tie", f"It's a tie! Both chose {user_choice}")
    elif ((user_choice == "rock" and sys_choice == "scissor") or
          (user_choice == "paper" and sys_choice == "rock") or
          (user_choice == "scissor" and sys_choice == "paper")):
        messagebox.showinfo("You Won!", f"You won! Your choice: {user_choice} | Bot choice: {sys_choice}")
    else:
        messagebox.showinfo("You Lose!", f"You lose! Your choice: {user_choice} | Bot choice: {sys_choice}")


def rock_en()	:
	global user_choice
	user_choice = "rock"
	result()
	
def paper_en()	:
	global user_choice
	user_choice = "paper"
	result()
	
def scissor_en()	:
	global user_choice
	user_choice = "scissor"
	result()


print_rules = ('''\n🎯 Rock–Paper–Scissors Rules 🎯\n /
    1. Choices Available:\n
       - Rock 🪨\n
       - Paper 📄'n
       - Scissors ✂️\n
    \n2. How to Win:\n
       - Rock crushes Scissors → Rock wins\n
       - Paper covers Rock → Paper wins\n
       - Scissors cut Paper → Scissors win\n
    \n3. Tie Condition:\n
       - If both players choose the same thing, it's a tie.''')

gui = Tk()
gui.title("Rock-paper-scissor game")
gui.geometry("400x600")
gui.configure(bg = 'lightblue')

rules = Label(gui, text = print_rules, justify = LEFT, bg = 'lightgreen').pack(pady = 10)

rock = Button(gui, text = "Rock", width = 15, bg = 'lightcoral', command = rock_en).pack(pady = 10)

paper = Button(gui, text = "Paper", width = 15, bg = 'orange', command = paper_en).pack(pady = 10)

scissor = Button(gui, text = "Scissor", width = 15, bg = 'lightyellow', command = scissor_en).pack(pady = 10)

gui.mainloop()	
