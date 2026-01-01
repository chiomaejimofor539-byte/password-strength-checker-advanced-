import tkinter as tk
import re
# Function to evaluate password strength
def evaluate_strength (event=None) :
    password = entry.get ()
    strength = 0
    # Check length
    if len(password) >= 8:
        strength += 1
    # Check uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    # Check lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    # Check digit
    if re.search(r"[0-9]", password):
        strength += 1
    # Check special character
    if re.search(r"[!@#$%^&*()_+=-]", password):
        strength += 1
    # Update label & color
    if strength == 0:
        label.config(text="Enter a password", fg="black")
        bar.config(bg="lightgray", width=0)
    elif strength <= 2:
        label.config(text="Weak", fg="red")
        bar.config(bg="red", width=80)
    elif strength == 3:
        label.config(text="Moderate", fg="orange")
        bar.config(bg="orange", width=160)
    elif strength == 4:
        label.config(text="Strong", fg="blue")
        bar.config(bg="blue", width=240)
    else:
        label.config(text="Very Strong", fg="green")
        bar.config(bg="green", width=320)
# GUI Setup
root = tk.Tk ()
root.title ("Advanced Password Strength Checker")
root.geometry ("400x200")
tk.Label (root, text="Enter Password:", font= ("Arial", 12)).pack (pady=10)
entry = tk.Entry (root, show="*", width=30, font= ("Arial", 12))
entry.pack ()
entry.bind ("<KeyRelease>", evaluate_strength)  # real-time check
label = tk.Label (root, text="Enter a password", font= ("Arial", 12))
label.pack (pady=10)
# Strength bar
bar = tk.Frame (root, bg="lightgray", height=20, width=0)
bar.pack (pady=10)
root.mainloop ()
