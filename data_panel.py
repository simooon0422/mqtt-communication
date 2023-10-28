import tkinter as tk

sensor_value =300.4 #said sensor value
window = tk.Tk()
x = sensor_value #assigned to variable x like you showed
window.minsize(width=400, height=400)
w = tk.Label(window, text=x) #shows as text in the window
w.pack() #organizes widgets in blocks before placing them in the parent.

tk.mainloop()