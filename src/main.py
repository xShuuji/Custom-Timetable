import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Lecture Timetable")
window.geometry("400x300")

# Create a list of days and times for the timetable
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
times = ["8:00-10:00", "10:00-12:00", "12:00-14:00", "14:00-16:00", "16:00-18:00"]

# Create a 2D list to store the lecture data
timetable = [[None for _ in days] for _ in times]