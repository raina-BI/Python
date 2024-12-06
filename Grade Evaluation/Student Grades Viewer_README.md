# Student Grades Viewer

This Python program calculates and displays student grades for various subjects using **inheritance** and **polymorphism** concepts in object-oriented programming. The results are shown in a simple GUI built with Tkinter.

---

## Features

1. **Object-Oriented Design**:
   - Demonstrates inheritance and polymorphism.
   - Parent class (`Student`) contains shared attributes.
   - Child classes (`English`, `Physics`, `Geography`) override the `grades()` method to calculate subject-specific grades.

2. **Tkinter GUI**:
   - Displays each student’s grade dynamically in a user-friendly window.
   - Includes a button to close the application.

3. **Dynamic Grade Calculation**:
   - Subject percentages are calculated based on different total marks for each subject:
     - English: 100 marks
     - Physics: 75 marks
     - Geography: 80 marks

---

## Installation

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-username/student-grades-viewer.git
   cd student-grades-viewer
