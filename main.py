from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

header = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
header.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
canvas.create_image(103, 112, image=tomato_img)
canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

check = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25))
check.grid(column=1, row=3)

window.mainloop()