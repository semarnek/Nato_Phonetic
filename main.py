import pandas
import tkinter
from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#FFFFFF"
FONT_NAME = "Courier"

data_file = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {key:value for (key,value) in data_file.values}



def generate_phonetic():

    user_word = input_label.get().upper()
    try:
        user_word_list = [data_dict[letter] for letter in user_word]
        user_word_list = ", ".join(user_word_list)

    except KeyError:

        result_label.configure(text="Sorry, only letters in the alphabet please.")

        generate_phonetic()

    else:

        result_label.configure(text=f"{user_word_list}")



window = tkinter.Tk()
window.title("NATO Phonetic Alphabet")
window.config(padx=100, pady=50, bg=WHITE, highlightthickness=1)

# generate_phonetic()
label = Label(text="Enter word:", font=(FONT_NAME, 15, "bold"), fg=PINK, bg=WHITE)
label.grid(column=0, row=0, pady=30)

input_label = Entry(highlightthickness=5, highlightcolor=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=PINK)
input_label.insert(0,"Word")
input_label.grid(column=0, row=1)

result_label = Label(font=(FONT_NAME, 15, "bold"), fg=PINK,
                             bg=WHITE)
result_label.grid(column=0, row=3)


button = Button(text="OK", command=generate_phonetic, font=(FONT_NAME, 15, "bold"), width=10, highlightcolor=YELLOW, bg=GREEN, fg=PINK)
button.grid(column=0, row=2, pady=30)

window.mainloop()
