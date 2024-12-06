# Vehicle Inheritance and Polymorphism

This Python project demonstrates the concepts of **inheritance** and **polymorphism** using a hierarchy of vehicle types. Different vehicle types inherit common properties from a base class (`Vehicle`) and override the `move()` method to exhibit their specific behavior.

---

## Features

1. **Base Class (`Vehicle`)**:
   - Contains common attributes: `brand` and `model`.
   - Defines a generic `move()` method that can be overridden by subclasses.

2. **Subclasses**:
   - `Car`: Inherits the `move()` method without modification.
   - `Boat`: Overrides the `move()` method to display "Sail!".
   - `Plane`: Overrides the `move()` method to display "Fly!".

3. **Polymorphism**:
   - A loop iterates over objects of different subclasses and dynamically calls their specific `move()` methods.

---

## Prerequisites

- Python 3.x installed on your system.

---

## How to Run

1. Save the script to a file named `vehicle_inheritance.py`.
2. Open a terminal or command prompt and navigate to the directory containing the file.
3. Run the script using:
   ```bash
   python vehicle_inheritance.py
