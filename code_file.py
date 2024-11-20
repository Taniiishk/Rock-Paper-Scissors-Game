import tkinter as tk
from tkinter import PhotoImage
import random

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("1980x1080")
root.configure(bg="#F0F8FF")  # AliceBlue background

# Heading at the top 
heading = tk.Label(root, text="Rock Paper Scissors Game", font=("Helvetica", 40, "bold underline"), fg="#2E8B57", bg="#F0F8FF") 
heading.place(relx=0.5, rely=0.05, anchor="center")

# Main Frame 
frame = tk.Frame(root, bg="#ADD8E6")
frame.place(relx=0.1, rely=0.17, relwidth=0.80, relheight=0.75)

label = tk.Label(frame, text="Let's play! 🪨 📃 ✂️", font=("Helvetica", 35, "bold"), bg="#ADD8E6", fg="black")
label.place(relx=0.33, rely=0.045)

# Load the images
image_rock = PhotoImage(file="C:\\Users\\tanis\\Downloads\\rock.png")
image_paper = PhotoImage(file="C:\\Users\\tanis\\Downloads\\paper.png")
image_scissors = PhotoImage(file="C:\\Users\\tanis\\Downloads\\scissors.png")

# Create buttons with images
rock_button = tk.Button(frame, image=image_rock)
rock_button.place(relx=0.20, rely=0.45, anchor="center")

paper_button = tk.Button(frame, image=image_paper)
paper_button.place(relx=0.50, rely=0.45, anchor="center")

scissors_button = tk.Button(frame, image=image_scissors)
scissors_button.place(relx=0.80, rely=0.45, anchor="center")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def on_button_click(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Attach commands to buttons
rock_button.config(command=lambda: on_button_click("rock"))
paper_button.config(command=lambda: on_button_click("paper"))
scissors_button.config(command=lambda: on_button_click("scissors"))

# Label to display the result
result_label = tk.Label(root, text="", bg="#F0F8FF", font=("Arial", 35,"bold"))  # AliceBlue background for result label
result_label.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()
