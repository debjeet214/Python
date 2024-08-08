import time
import tkinter as tk

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

# Set the window size to 400x200 pixels
root.geometry("400x200")

# Create a bright and bold font
font = ("Arial", 120, "bold")

# Create a label with a black background and neon green text color
clock_label = tk.Label(root, font=font, background="#000000", foreground="#33CC33")
clock_label.pack(fill="both", expand=True)

# Add some shading to the label
clock_label.config(relief="ridge", bd=10)

# Add some glow effect to the text
clock_label.config(highlightbackground="#66FF66", highlightthickness=2)

update_time()
root.mainloop()
