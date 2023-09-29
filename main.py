from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer, reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label1["text"] = "TIMER"
    tick["text"] = ""
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    if reps % 2 == 1:
        countdown(work_sec)
        label1.config(text="WORK", fg=GREEN)
    elif reps % 8 == 0:
        countdown(long_break_sec)
        label1.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label1.config(text="SHORT BREAK", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps
    minute = math.floor(count/60)
    second = count % 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        mark = ""
        for _ in range(work_sessions):
            mark += "✓"
        tick.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Productivity Manager")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="C:/Users/Akhila Kudrethaya/PycharmProjects/Pomodoro_Final/venv/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT, 30, "bold"))
canvas.grid(row=1, column=1)

label1 = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT, 50, "bold"))
label1.grid(row=0, column=1)

button1 = Button(text="Start", command=start_timer, font=("Ariel", 10, "bold"), highlightthickness=0)
button1.grid(row=2, column=0)

button2 = Button(text="Reset", command=reset_timer, font=("Ariel", 10, "bold"), highlightthickness=0)
button2.grid(row=2, column=2)

tick = Label(bg=YELLOW)
tick.grid(row=3, column=1)

window.mainloop()
