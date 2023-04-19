"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 13
Topic: 2
Assignment: Database and GUI
Date: 04/16/2023
"""
import connect_sqlite as sql
import tkinter as tk
from tkinter import ttk

class DatabaseEntryWindow(tk.Tk):
    add_person_widgets: dict[int, tk.Widget]
    person_list_widget: tk.Listbox
    add_student_widgets: dict[int, tk.Widget]
    student_list_widget: tk.Listbox
    button_height = '1'
    button_width = '10'
    listbox_width = '30'

    def __init__(self):
        super().__init__()
        self.database_name = 'StudentDatabase.db'
        self.title('Student Database')
        self.geometry('300x600')
        start_button = tk.Button(self, text='Create Database', command= lambda d = self.database_name: sql.create_connection_and_tables(d))
        start_button.pack()
        self.create_add_person_frame()
        self.create_view_persons_frame()
        self.create_add_student_frame()
        self.create_view_students_frame()
        self.mainloop()

    def create_add_person_frame(self):
        frame = tk.Frame(self)
        lines = ('First Name', 'Last Name')
        self.add_person_widgets = self.create_field_lines(frame, lines)
        button = tk.Button(frame, text='Add Person', command=self.add_person, height=self.button_height, width=self.button_width)
        button.pack()

    def create_add_student_frame(self):
        frame = tk.Frame(self)
        #persons = ttk.Listbox(frame, values= lambda d = self.database_name: sql.select_all_persons(d))

        lines = ('Major', 'Start Date')
        self.add_student_widgets = self.create_field_lines(frame, lines)
        button = tk.Button(frame, text='Add Student', command=self.add_student, height=self.button_height, width=self.button_width)
        button.pack()

    def create_view_persons_frame(self):
        frame = ttk.Frame(self)
        button = tk.Button(frame, text='View Persons', command=self.view_persons, height=self.button_height, width=self.button_width)
        button.pack()
        widget = tk.Listbox(frame, width=self.listbox_width)        
        widget.pack()
        self.person_list_widget = widget
        frame.pack()
    
    def create_view_students_frame(self):
        frame = ttk.Frame(self)
        widget = tk.Listbox(frame, width=self.listbox_width)
        button = tk.Button(frame, text='View Students', command= self.view_students, height=self.button_height, width=self.button_width)

        button.pack()
        widget.pack()
        self.student_list_widget = widget
        frame.pack()

    def create_field_lines(self, master_frame, line_names):
        frame = master_frame
        widgets = dict[str, tk.Widget]()
        for l in line_names:
            line_frame = tk.Frame(frame)

            key = l.replace(' ', '_').lower() + '_label'
            widgets[key] = tk.Label(line_frame, text=f'{l}: ', width=10)
            widgets[key].pack(side='left')

            key = l.replace(' ', '_').lower() + '_text'
            widgets[key] = tk.Entry(line_frame)
            widgets[key].pack(side='right')

            line_frame.pack()

        frame.pack()
        return widgets
    
    def add_person(self):
        values = set()
        for key in self.add_person_widgets:
            if '_text' in key:
                values.add(self.add_person_widgets[key].get())
        sql.create_person(self.database_name, person=(values.pop(), values.pop()))

    def add_student(self):
        values = set()
        try:
            person_id = self.person_list_widget.curselection()[0]
            for key in self.add_student_widgets:
                if '_text' in key:
                    values.add(self.add_student_widgets[key].get())
            sql.create_student(self.database_name, student=(person_id, values.pop(), values.pop()))
        except IndexError as e:
            print(e)
        
    def view_persons(self):
        persons = sql.select_all_persons(self.database_name)
        self.person_list_widget.delete(0, tk.END)
        for p in persons:
            self.person_list_widget.insert(p[0], f'{p[2]} {p[1]}')

    def view_students(self):
        persons = sql.select_all_persons(self.database_name)
        students = sql.select_all_students(self.database_name)
        self.student_list_widget.delete(0, tk.END)
        for s in students:
            i = s[0]
            self.student_list_widget.insert(i, f'{persons[i][2]} {persons[i][1]} {s[1]} {s[2]}')

if __name__ == '__main__':
    sql.create_connection_and_tables('StudentDatabase.db')
    rows = sql.select_all_persons('StudentDatabase.db')
    for r in rows:
        print(r)
    DatabaseEntryWindow()
