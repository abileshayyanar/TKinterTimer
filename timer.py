import tkinter as tk

window = tk.Tk()
window.title("Timer")

# Create frame to hold widgets
frame = tk.Frame(master=window, width=350, height=150)
frame.pack()

# Create and place labels and entry boxes
label = tk.Label(master=frame, text="Set timer:")
hourLabel = tk.Label(master=frame, text = "Hours")
hourEntry = tk.Entry(master=frame, width = 4)

minLabel = tk.Label(master=frame, text = "Minutes")
minEntry = tk.Entry(master=frame, width = 4)

secLabel = tk.Label(master=frame, text = "Seconds")
secEntry = tk.Entry(master=frame, width = 4)

label.place(x=5, y=0)

hourEntry.place(x=60, y=35)
hourLabel.place(x=20, y=35)

minEntry.place(x=150, y=35)
minLabel.place(x=100, y=35)

secEntry.place(x=240, y=35)
secLabel.place(x=190, y=35)

#Create button to start and stop timer
pauseButton = tk.Button(master=frame, text="Start/Pause", width = 10)
pauseButton.place(x=120, y=80)

window.mainloop()