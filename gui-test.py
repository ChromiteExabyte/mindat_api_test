
############################

## Package Imports ##

############################


# GUI Related
import tkinter as tk


# Network Related
import socket




############################

## Function Definitions ##

############################




# Check internet connectivity on startup

def check_internet():
    try:
        socket.create_connection(("www.mindat.org", 80))
        label.config(text="Connection with Mindat.org has been established.")
    except OSError:
        label.config(text="Connection with Mindat.org could not be established.")







############################

## The GUI Starts Up ##

############################





# Create a new Tkinter window
window = tk.Tk()

# Set the window title
window.title("Mindat API Test")

# Set the window size
window.geometry("400x300")  # Width: 400 pixels, Height: 300 pixels

# Add a label to the window
label = tk.Label(window, text="Label window text check")
label.pack()

# Configure label to align text in the middle of the window
label.pack(expand=True, fill='both', anchor='center')

# Check internet connectivity when the window is opened
window.bind("<Map>", lambda event: check_internet())

# Start the Tkinter event loop
window.mainloop()







