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
reps = 0
check = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global timer
    global check
    global reps
    window.after_cancel(timer)
    reps = 0
    check = ""
    timer = None
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", fg=GREEN)
    mark_label.config(text=check)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global check
    global timer
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    count_s_tens = math.floor(count_seconds/10)
    count_s_ones = count_seconds % 10
    count_m_tens = math.floor(count_minute / 10)
    count_m_ones = count_minute % 10
    canvas.itemconfig(timer_text, text=f"{count_m_tens}{count_m_ones}:{count_s_tens}{count_s_ones}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 != 0 and reps > 2:
            check += "✔"
            mark_label.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Labels
timer_label = Label(text="TIMER", bg=YELLOW, font=(FONT_NAME, 50, "bold"), fg=GREEN)
timer_label.grid(row=0, column=1)
mark_label = Label(bg=YELLOW, fg=GREEN)
mark_label.grid(row=3, column=1)

# Buttons
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
