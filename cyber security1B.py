##### Rail Fence Cipher (Transposition Technique)
##print("Hariprasad Vishwakarma T127")
##print("Rail Fence Cipher (Transposition Technique)")
##print()
### Encryption Function
##def encrypt(text, key):
##    rail = [['\n' for i in range(len(text))] for j in range(key)]
##
##    direction_down = False
##    row, col = 0, 0
##
##    for char in text:
##        if row == 0 or row == key - 1:
##            direction_down = not direction_down
##
##        rail[row][col] = char
##        col += 1
##
##        if direction_down:
##            row += 1
##        else:
##            row -= 1
##
##    result = ""
##    for i in range(key):
##        for j in range(len(text)):
##            if rail[i][j] != '\n':
##                result += rail[i][j]
##
##    return result
##
##
### Decryption Function
##def decrypt(cipher, key):
##    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
##
##    direction_down = None
##    row, col = 0, 0
##
##    for i in range(len(cipher)):
##        if row == 0:
##            direction_down = True
##        if row == key - 1:
##            direction_down = False
##
##        rail[row][col] = '*'
##        col += 1
##
##        if direction_down:
##            row += 1
##        else:
##            row -= 1
##
##    index = 0
##    for i in range(key):
##        for j in range(len(cipher)):
##            if rail[i][j] == '*' and index < len(cipher):
##                rail[i][j] = cipher[index]
##                index += 1
##
##
##    result = ""
##    row, col = 0, 0
##
##    for i in range(len(cipher)):
##        if row == 0:
##            direction_down = True
##        if row == key - 1:
##            direction_down = False
##
##        result += rail[row][col]
##        col += 1
##
##        if direction_down:
##            row += 1
##        else:
##            row -= 1
##
##    return result
##
##text = input("Enter the message: ")
##key = int(input("Enter the key (number of rails): "))
##
##encrypted = encrypt(text, key)
##print("Encrypted Message:", encrypted)
##
##decrypted = decrypt(encrypted, key)
##print("Decrypted Message:", decrypted)
##
##
##
##
##




### ---------------- GUI ---------------- #


import tkinter as tk
from tkinter import messagebox


# ---------------- Encryption ---------------- #

def encrypt(text, key):
    if key <= 1:
        return text

    rail = [['\n' for _ in range(len(text))] for _ in range(key)]

    row = 0
    col = 0
    direction_down = False

    for ch in text:

        if row == 0 or row == key - 1:
            direction_down = not direction_down

        rail[row][col] = ch
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    result = ""

    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]

    return result


 #---------------- Decryption ---------------- #

def decrypt(cipher, key):
    if key <= 1:
        return cipher

    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]

    row = 0
    col = 0
    direction_down = None

    # Mark zig-zag path
    for i in range(len(cipher)):

        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    # Fill marked places
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = ""
    row = 0
    col = 0

    for i in range(len(cipher)):

        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        result += rail[row][col]
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return result

def encrypt_text():
    try:
        text = message_entry.get()
        key = int(key_entry.get())

        if key < 2:
            messagebox.showerror("Error", "Key must be greater than 1.")
            return

        result = encrypt(text, key)

        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, result)
        result_entry.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid key.")


def decrypt_text():
    try:
        text = message_entry.get()
        key = int(key_entry.get())

        if key < 2:
            messagebox.showerror("Error", "Key must be greater than 1.")
            return

        result = decrypt(text, key)

        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, result)
        result_entry.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid key.")


def clear():
    message_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)

    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.config(state="readonly")



root = tk.Tk()
root.title("Rail Fence Cipher - Transposition Technique")
root.geometry("550x330")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Rail Fence Cipher (Transposition Technique)",
    font=("Arial", 16, "bold")
)
title.pack(pady=15)

tk.Label(root, text="Enter Message:", font=("Arial", 11)).pack()

message_entry = tk.Entry(root, width=50, font=("Arial", 11))
message_entry.pack(pady=5)

tk.Label(root, text="Enter Key (Rails):", font=("Arial", 11)).pack()

key_entry = tk.Entry(root, width=10, font=("Arial", 11))
key_entry.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=15)

encrypt_btn = tk.Button(
    frame,
    text="Encrypt",
    width=12,
    bg="lightgreen",
    command=encrypt_text
)
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = tk.Button(
    frame,
    text="Decrypt",
    width=12,
    bg="lightblue",
    command=decrypt_text
)
decrypt_btn.grid(row=0, column=1, padx=10)

clear_btn = tk.Button(
    frame,
    text="Clear",
    width=12,
    bg="tomato",
    command=clear
)
clear_btn.grid(row=0, column=2, padx=10)

tk.Label(root, text="Result:", font=("Arial", 11, "bold")).pack()

result_entry = tk.Entry(root, width=50, font=("Arial", 11), state="readonly")
result_entry.pack(pady=5)

root.mainloop()


