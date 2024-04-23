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

# Create a grid layout for the timetable
for row, time in enumerate(times):
    # create a label for each time slot
    tk.Label(window, text=time).grid(row=row + 1, column=0, sticky="e")
    for col, day in enumerate(days):
        # create an entry widget for each time slot and day
        entry = tk.Entry(window, width=20)
        entry.grid(row=row + 1, column=col + 1)
        timetable[row][col] = entry

# create labels for each day of the week
for col, day in enumerate(days):
    tk.Label(window, text=day).grid(row=0, column=col + 1, sticky="n")

# function to save the timetable
def save_timetable():
    with open("timetable.txt", "w") as file:
        for row in range(len(times)):
            for col in range(len(days)):
                file.write(f"{timetable[row][col].get()},")
                file.write("\n")

# function to load the timetable
def load_timetable():
    try:
        with open("timetable.txt", "r") as file:
            for row, line in enumerate(file):
                entries = line.strip().split(",")
                for col, entry in enumerate(entries):
                    timetable[row][col].delete(0, tk.END)
                    timetable[row][col].insert(0, entry)
    except FileNotFoundError:
        print("No saved timetable found.")