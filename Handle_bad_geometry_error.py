"""
handle bad geometry errors

@author: raina
"""

import tkinter as tk
from tkinter import messagebox
import random

# Initialize the main window
# Main Tkinter application window


def validate_geometry_input():
     """
     Validate geometry inputs 'WIDTH' and 'HEIGHT' to ensure they are valid dimensions.
     """
     width_ip = geometry_entry.get()
     height_ip = geometry_entry1.get()

     try:
        width = int(width_ip)
        height = int(height_ip)
        
        # Check for negative or zero dimensions
        if width <= 0 or height <= 0:
            raise ValueError("Width and Height must be positive integers.")
        # If valid, show success message
        messagebox.showinfo("Valid Geometry", f"Valid geometry: {width}x{height}")
        return width, height
     except ValueError as ve:
        messagebox.showerror("Invalid Geometry", f"Invalid geometry input: {ve}")
        return None, None

root = tk.Tk()
root.title("Handle Bad Geometry Errors")
root.geometry("300x300")

# Geometry input validation
label = tk.Label(root, text="Width", font=("Corbel", 9))
label.pack(pady=5)
geometry_entry = tk.Entry(root, width=15)
geometry_entry.pack(pady=5)

label1 = tk.Label(root, text="Height", font=("Corbel", 9))
label1.pack(pady=10)
geometry_entry1 = tk.Entry(root, width=15)
geometry_entry1.pack(pady=10)

geometry_button = tk.Button(root, text="Validate Geometry", command=validate_geometry_input)
geometry_button.pack()

# Start the Tkinter main loop
root.mainloop()