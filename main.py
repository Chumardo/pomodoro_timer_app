from tkinter import *
import math

# Constants
PINK = "#e2979c"
RED = "red"
GREEN = "green"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# GUI Setup
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg='black')

canvas = Canvas(width=200, height=234, bg="black", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)

timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

timer_label = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, highlightcolor="black", bg="black")
timer_label.grid(column=1, row=0)

btn_start = Button(text="Start", highlightthickness=0, bg=RED, fg="white")
btn_start.grid(column=0, row=2)

btn_reset = Button(text="Reset", highlightthickness=0, bg=GREEN, fg="white")
btn_reset.grid(column=2, row=2)


window.mainloop()