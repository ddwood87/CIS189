"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 9
Topic: 1
Assignment: Python Module import
Date: 03/07/2023
"""
import tkinter as tk

def check_click(): 
    count_checks = 0
    for i in range(len(check_names)):
        if is_checked[i].get():
            label.config(text= check_names[i] +' is your favorite!')
            count_checks += 1
        if count_checks > 1:
            label.config(text='Two favorites are nice.')
        if count_checks > 2:
            label.config(text='You can\'t have that many favorites!')
        if count_checks > 3:
            label.config(text='C\'mon, man!')

m = tk.Tk()
m.title('Favorite Meal')
m.geometry('300x300+100+100')
f = tk.Frame(m)
f.place(relx=.5, rely=.5,anchor=tk.CENTER)

check_names = ['Breakfast', 'Second Breakfast', 'Lunch', 'Dinner']
is_checked = []
for i in range(len(check_names)):
    is_checked.append(tk.BooleanVar())
    check = tk.Checkbutton(f, text=check_names[i], variable=is_checked[i], width=25, command=check_click)
    check.grid(row=i)

label_text = 'Waiting'
label = tk.Label(f, text=label_text)
label.grid(row=len(check_names))

button = tk.Button(f, text='Exit', width=20, command=m.destroy)
button.grid(row=len(check_names)+1)

m.mainloop()
