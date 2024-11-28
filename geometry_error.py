"""
Program to validate geometry input format 'WIDTHxHEIGHT' to ensure valid dimensions.

@author: raina
"""
import tkinter as tk
from tkinter import messagebox

def validate_geometry_input(geometry_str):
    """
    Validate geometry input format 'WIDTHxHEIGHT' to ensure valid dimensions.
    """
    try:
        # Split the geometry string by 'x' to separate width and height
        width, height = geometry_str.lower().split('x')
        width = int(width)
        height = int(height)      
        # Check for negative or zero dimensions
        if width <= 0 or height <= 0:
            raise ValueError("Width and Height must be positive integers.")
        return width, height
    except ValueError as ve:
        messagebox.showerror("Invalid Geometry", f"Invalid geometry input: {ve}")
        return None, None

def apply_geometry():
    """
    Apply geometry to the root window after validating the input.
    """
    geometry_str = geometry_entry.get()
    width, height = validate_geometry_input(geometry_str)
    
    if width and height:
        try:
            root.geometry(f"{width}x{height}")
        except Exception as e:
            messagebox.showerror("Geometry Error", f"An error occurred: {e}")

def create_widgets():
    """
    Function to create and place widgets in the root window.
    Demonstrates safe use of geometry managers.
    """
    try:
        label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
        label.pack(pady=10)
        
        button = tk.Button(root, text="Click Me!", command=lambda: messagebox.showinfo("Clicked", "Button Clicked"))
        button.pack(pady=5)
        
        # Example for grid (shouldn't mix with pack or place)
        # Use grid() here only if you use grid for all widgets
        another_label = tk.Label(root, text="Another Label", font=("Arial", 10))
        another_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)  # Using place() for positioning
    except tk.TclError as te:
        messagebox.showerror("Geometry Manager Error", f"Error in widget placement: {te}")

# Main Tkinter application window
root = tk.Tk()
root.title("Handle Bad Geometry Errors")


# Geometry input validation
geometry_entry = tk.Entry(root, width=15)
geometry_entry.pack(pady=10)
geometry_entry.insert(0, "400x300")  # Default valid geometry

# Button to apply geometry
geometry_button = tk.Button(root, text="Apply Geometry", command=apply_geometry)
geometry_button.pack(pady=5)

# Create widgets safely
create_widgets()

# Start the main event loop
root.mainloop()