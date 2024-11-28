"""
Generate random strings

@author: raina
"""
from tkinter import *
import random

# Initialize the main window
root = Tk()
root.geometry("400x500")
root.title("OOPs Implementation")

# 3D array for generating random strings
array_3d = [
    [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], ["!", "@", '$', '%'], ["A", "B", "C", "E", "F"]]
]

c = 0  # Counter for dynamic button names
generated_strings = []  # List to store generated strings

# Initialize a label for showing the generated password
label = Label(root, text="")
label.pack(pady=10)

# Initialize a label for showing the number of generated strings
count_label = Label(root, text="Total strings generated: 0")
count_label.pack(pady=10)

# Initialize a text box to display generated strings
generated_strings_label = Label(root, text="Generated Strings:", anchor="w")
generated_strings_label.pack(pady=10)

generated_strings_text = Text(root, height=10, width=40)
generated_strings_text.pack(pady=10)


class CreateElements:
    def __init__(self):
        print("This is CreateElement class")
    
    def newpassword(self):
        # Ensure random indices match the length of the subarrays
        random1 = random.randint(0, len(array_3d[0][0]) - 1)
        random2 = random.randint(0, len(array_3d[0][1]) - 1)
        random3 = random.randint(0, len(array_3d[0][2]) - 1)

        # Retrieve random characters
        letter1 = array_3d[0][0][random1]
        letter2 = array_3d[0][1][random2]
        letter3 = array_3d[0][2][random3]

        # Combine to form the generated string
        generated_string = letter1 + letter2 + letter3

        # Update the label with the generated password
        label["text"] = "Generated string: " + generated_string
        
        # Add the generated string to the list
        generated_strings.append(generated_string)
        
        # Update the count label and generated strings list display
        self.update_display()
    
    def update_display(self):
        # Update the count of generated strings
        count_label["text"] = f"Total no of strings generated: {len(generated_strings)}"

        # Clear and update the text area with all generated strings
        generated_strings_text.delete(1.0, END)
        for string in generated_strings:
            generated_strings_text.insert(END, string + "\n")

    def createNewelements(self):
        global generated_strings
        
        # Create new button for generating random strings
        btn1 = Button(root, text="String{}".format(generated_strings), command=self.newpassword)
        btn1.pack()

        # Adjust the button's position dynamically to avoid overlap
        ypos = 0.2 + (c * 0.05)  # Shift each button slightly downwards
        if ypos >= 0.9:  # Reset if it goes too far down
            ypos = 0.2

        btn1.place(relx=0.5, rely=ypos, anchor=CENTER)
    
    def close_window(self):
        root.destroy()

# Create an object of CreateElements
obj = CreateElements()

# Button for creating new elements (new buttons)
btn = Button(root, text="Generate random strings", command=obj.createNewelements)
btn.pack(pady=10)
btn.place(relx=0.5, rely=0.05, anchor=CENTER)

# Button to close the window
btn2 = Button(root, text="Click to close the window", command=obj.close_window)
btn2.pack(pady=10)
btn2.place(relx=0.5, rely=0.85, anchor=CENTER)

# Main loop to run the Tkinter window
root.mainloop()
