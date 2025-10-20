import tkinter as tk

window = tk.Tk()
window.title("Timer")

# State
running = False
timeLeft = 0  # seconds


def format_time(t: int) -> str:
    # Formats time as HH:MM:SS
    if t < 0:
        t = 0
    h = t // 3600
    m = (t % 3600) // 60
    s = t % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def safe_int(s: str) -> int:
    try:
        v = int(s)
        return max(0, v)
    except Exception:
        return 0


def resetTimer():
    global running, timeLeft
    running = False
    timeLeft = 0
    time_label.config(text=format_time(timeLeft))


# Create frame to hold widgets
frame = tk.Frame(master=window, width=450, height=220)
frame.pack()

# Create and place labels and entry boxes
time_label = tk.Label(master=frame, text=format_time(0), font=("arial", 75))
time_label.place(x=40, y=110)
label = tk.Label(master=frame, text="Set timer:")
hourLabel = tk.Label(master=frame, text="Hours")
hourEntry = tk.Entry(master=frame, width=4)

minLabel = tk.Label(master=frame, text="Minutes")
minEntry = tk.Entry(master=frame, width=4)

secLabel = tk.Label(master=frame, text="Seconds")
secEntry = tk.Entry(master=frame, width=4)

label.place(x=5, y=0)

hourEntry.place(x=60, y=35)
hourLabel.place(x=20, y=35)

minEntry.place(x=150, y=35)
minLabel.place(x=100, y=35)

secEntry.place(x=240, y=35)
secLabel.place(x=190, y=35)


def startStop():
    global running, timeLeft
    if not running:
        # If timeLeft is zero, try to read new values from entries
        if timeLeft == 0:
            hours = safe_int(hourEntry.get())
            minutes = safe_int(minEntry.get())
            seconds = safe_int(secEntry.get())
            totalSeconds = hours * 3600 + minutes * 60 + seconds
            timeLeft = totalSeconds
            # update display immediately
            time_label.config(text=format_time(timeLeft))

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
        time_label.config(text=format_time(timeLeft))
        window.after(1000, updateTime)
        if timeLeft == 0:
            running = False


# Create buttons
pauseButton = tk.Button(master=frame, text="Start/Pause", width=10)
pauseButton.place(x=70, y=80)
pauseButton.config(command=startStop)

resetButton = tk.Button(master=frame, text="Reset", width=10)
resetButton.place(x=150, y=80)
resetButton.config(command=resetTimer)

updateTime()
window.mainloop()