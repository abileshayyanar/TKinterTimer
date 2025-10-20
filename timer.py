import tkinter as tk
from tkinter import ttk

import sv_ttk

window = tk.Tk()
sv_ttk.set_theme("dark")
window.title("Timer")

# State
running = False
timeLeft = 0  # seconds


def formatTime(t: int) -> str:
    # Formats time as HH:MM:SS
    if t < 0:
        t = 0
    h = t // 3600
    m = (t % 3600) // 60
    s = t % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def safeInt(s: str) -> int:
    try:
        v = int(s)
        return max(0, v)
    except Exception:
        return 0


def resetTimer():
    global running, timeLeft
    running = False
    timeLeft = 0
    time_label.config(text=formatTime(timeLeft))


# Create frame to hold widgets
frame = ttk.Frame(master=window, width=460, height=220)
frame.pack()

# Create and place labels and entry boxes
time_label = ttk.Label(master=frame, text=formatTime(0), font=("arial", 75))
time_label.place(x=40, y=110)
label = ttk.Label(master=frame, text="Set timer:")
hourLabel = ttk.Label(master=frame, text="Hours", font=(bold))
hourEntry = ttk.Entry(master=frame, width=4)

minLabel = ttk.Label(master=frame, text="Minutes")
minEntry = ttk.Entry(master=frame, width=4)

secLabel = ttk.Label(master=frame, text="Seconds")
secEntry = ttk.Entry(master=frame, width=4)

label.place(x=15, y=4)

hourEntry.place(x=65, y=35)
hourLabel.place(x=20, y=40)

minEntry.place(x=180, y=35)
minLabel.place(x=125, y=40)

secEntry.place(x=300, y=35)
secLabel.place(x=245, y=40)


def startStop():
    global running, timeLeft
    if not running:
        # If timeLeft is zero, try to read new values from entries
        if timeLeft == 0:
            hours = safeInt(hourEntry.get())
            minutes = safeInt(minEntry.get())
            seconds = safeInt(secEntry.get())
            totalSeconds = hours * 3600 + minutes * 60 + seconds
            timeLeft = totalSeconds
            # update display immediately
            time_label.config(text=formatTime(timeLeft))

        # Only start if there is time to count down
        if timeLeft > 0:
            running = True
            updateTime()
    else:
        # pause
        running = False


def updateTime():
    global timeLeft, running
    if running and timeLeft > 0:
        timeLeft -= 1
        time_label.config(text=formatTime(timeLeft))
        window.after(1000, updateTime)
        if timeLeft == 0:
            running = False


# Create buttons
pauseButton = ttk.Button(master=frame, text="Start/Pause", width=10)
pauseButton.place(x=100, y=80)
pauseButton.config(command=startStop)

resetButton = ttk.Button(master=frame, text="Reset", width=10)
resetButton.place(x=250, y=80)
resetButton.config(command=resetTimer)

updateTime()

window.mainloop()