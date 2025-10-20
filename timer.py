import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Timer")

running = False
timeLeft = 0


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
frame = tk.Frame(master=window, width=440, height=220)
frame.pack()

# Create and place labels and entry
time_label = tk.Label(master=frame, text=formatTime(0), font=("helvetica", 75, "bold"))
time_label.place(x=20, y=110)
hourLabel = tk.Label(master=frame, text="Hours:")
hourEntry = tk.Entry(master=frame, width=4)

minLabel = tk.Label(master=frame, text="Minutes:")
minEntry = tk.Entry(master=frame, width=4)

secLabel = tk.Label(master=frame, text="Seconds:")
secEntry = tk.Entry(master=frame, width=4)


hourEntry.place(x=63, y=15)
hourLabel.place(x=20, y=15)

minEntry.place(x=180, y=15)
minLabel.place(x=125, y=15)

secEntry.place(x=295, y=15)
secLabel.place(x=240, y=15)


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
pauseButton = tk.Button(master=frame, text="Start/Pause", width=10)
pauseButton.place(x=100, y=70)
pauseButton.config(command=startStop)

resetButton = tk.Button(master=frame, text="Reset", width=10)
resetButton.place(x=250, y=70)
resetButton.config(command=resetTimer)

updateTime()

window.mainloop()