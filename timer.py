import tkinter as tk
from tkinter import ttk
from time import strftime


window = tk.Tk()
window.title("Timer")

# Create frame to hold widgets
frame = tk.Frame(master=window, width=440, height=180)
frame.configure(bg="seashell2")
frame.pack()

running = False
timeLeft = 0

# Clock functionality
def clock():
    currentTime = strftime("%H:%M:%S")
    amPm = strftime("%p")
    clockLabel.config(text=currentTime)
    amPmLabel.config(text=amPm)
    clockLabel.after(1000, clock)

amPmLabel = tk.Label(master=frame, font=("helvetica", 30, "bold"), bg='seashell2')
clockLabel = tk.Label(master=frame, font=("helvetica", 70, "bold"), bg='seashell2')

def switchMode(event=None):
    mode = modeVar.get()
    if mode == "Clock":
        hourEntry.place_forget()
        hourLabel.place_forget()
        minEntry.place_forget()
        minLabel.place_forget()
        secEntry.place_forget()
        secLabel.place_forget()
        pauseButton.place_forget()
        resetButton.place_forget()
        timerLabel.place_forget()

        clockLabel.place(x=1, y=40)
        amPmLabel.place(x=375, y=55)
        clock()
    else:
        clockLabel.place_forget()
        amPmLabel.place_forget()

        hourEntry.place(x=63, y=15)
        hourLabel.place(x=20, y=15)

        minEntry.place(x=180, y=15)
        minLabel.place(x=125, y=15)

        secEntry.place(x=295, y=15)
        secLabel.place(x=240, y=15)

        pauseButton.place(x=100, y=50)
        resetButton.place(x=250, y=50)
        timerLabel.place(x=20, y=70)

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
    timerLabel.config(text=formatTime(timeLeft))


# Create and place labels and entry
timerLabel = tk.Label(master=frame, text=formatTime(0), font=("helvetica", 75, "bold"), bg="seashell2")
timerLabel.place(x=20, y=110)
hourLabel = tk.Label(master=frame, text="Hours:")
hourEntry = tk.Entry(master=frame, width=4)

minLabel = tk.Label(master=frame, text="Minutes:")
minEntry = tk.Entry(master=frame, width=4)

secLabel = tk.Label(master=frame, text="Seconds:")
secEntry = tk.Entry(master=frame, width=4)


# hourEntry.place(x=63, y=15)
# hourLabel.place(x=20, y=15)

# minEntry.place(x=180, y=15)
# minLabel.place(x=125, y=15)

# secEntry.place(x=295, y=15)
# secLabel.place(x=240, y=15)

modeVar = tk.StringVar(value="Timer")
dropDown = ttk.Combobox(master=frame, width=10, textvariable=modeVar)
dropDown['values'] = ('Timer', 'Clock')
dropDown.place(x=330, y=15)
dropDown.bind("<<ComboboxSelected>>", switchMode)

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
            timerLabel.config(text=formatTime(timeLeft))

        # Only start if there is time to count down
        if timeLeft > 0:
            running = True
            updateTime()
    else:
        # pause
        running = False

def flashScreen(count = 0):
    if count < 10:
        newColor = "red" if count % 2 == 0 else "white"
        frame.configure(bg=newColor)
        timerLabel.configure(bg=newColor)
        frame.after(500, flashScreen, count + 1)
    else:
        frame.configure(bg="seashell2")
        timerLabel.configure(bg="seashell2")

    
def updateTime():
    global timeLeft, running
    if running and timeLeft > 0:
        timeLeft -= 1
        timerLabel.config(text=formatTime(timeLeft))
        window.after(1000, updateTime)
        if timeLeft == 0:
            running = False
            flashScreen()


# Create buttons
pauseButton = tk.Button(master=frame, text="Start/Pause", width=10)
pauseButton.config(command=startStop)

resetButton = tk.Button(master=frame, text="Reset", width=10)
resetButton.config(command=resetTimer)

updateTime()
switchMode()

window.mainloop()