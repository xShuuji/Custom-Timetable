import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Lecture Timetable")
window.geometry("700x160")

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
        # Iterate through each row in the timetable
        for row in range(len(times)):
            # Create a list to hold the row entries
            row_entries = []
            # Iterate through each column in the row
            for col in range(len(days)):
                # Get the entry data and append it to the row entries list
                entry_data = timetable[row][col].get()
                row_entries.append(entry_data)
            
            # Write the row entries to the file, joined by commas
            file.write(",".join(row_entries))
            # Write a newline character after each row
            file.write("\n")

# function to load the timetable
def load_timetable():
    try:
        with open("timetable.txt", "r") as file:
            # Read each line from the file
            for row, line in enumerate(file):
                # Split the line into entries
                entries = line.strip().split(",")
                
                # Handle missing entries
                if len(entries) < len(days):
                    # Fill missing entries with empty strings
                    entries.extend([""] * (len(days) - len(entries)))
                
                # Check if the number of entries matches the number of columns in the timetable
                if len(entries) != len(days):
                    print(f"Warning: Inconsistent number of columns at line {row + 1}. Line skipped.")
                    continue
                
                # Fill the timetable with the loaded entries
                for col, entry in enumerate(entries):
                    # Update the entry in the timetable
                    timetable[row][col].delete(0, tk.END)
                    timetable[row][col].insert(0, entry)
                
    except FileNotFoundError:
        print("No saved timetable found.")
    except Exception as e:
        print(f"An error occurred while loading the timetable: {e}")

# create buttons for saving and loading the timetable
save_button = tk.Button(window, text="Save Timetable", command=save_timetable)
save_button.grid(row=len(times) + 5, column=0, columnspan=2)

load_button = tk.Button(window, text="Load Timetable", command=load_timetable)
load_button.grid(row=len(times) + 5, column=3, columnspan=2)

window.mainloop()