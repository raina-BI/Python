# Tkinter Geometry Validator
A simple Python application built using Tkinter that validates user-provided geometry input in the format `WIDTHxHEIGHT` and resizes the window dynamically. It demonstrates robust error handling and safe widget placement.

---

## Features

1. **Geometry Input Validation**:
   - Ensures the format is `WIDTHxHEIGHT`.
   - Checks that both dimensions are positive integers.
   - Displays error messages for invalid input.

2. **Dynamic Window Resizing**:
   - Users can resize the application window dynamically by entering valid dimensions.

3. **Robust Error Handling**:
   - Error messages are displayed using Tkinter's `messagebox`.
   - Handles both invalid input and runtime geometry errors gracefully.

4. **Widget Placement**:
   - Demonstrates the use of different geometry managers (`pack()` and `place()`).
   - Avoids mixing incompatible managers (`grid()` and `pack()`).

---

## Installation

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-username/tkinter-geometry-validator.git
   cd tkinter-geometry-validator
