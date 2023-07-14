from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(time_label, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
time_label = canvas.create_text(100, 130, text="00.00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Timer Label
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW, highlightthickness=0)
title_label.grid(column=1, row=0)

# Start Button
start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"))
reset_button.grid(column=2, row=2)

# checkmark label
checkmark_label = Label(text="✔", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 18))
checkmark_label.grid(column=1, row=3)

window.mainloop()
