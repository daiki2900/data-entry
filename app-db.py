import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def print_data():
    if terms_var.get() == "Accepted":
        fname = fname_entry.get()
        lname = lname_entry.get()

        if fname and lname:
            gender = gender_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            registration_status = registration_status_var.get()
            courses = numcourses_spinbox.get()
            semesters = numsemesters_spinbox.get()

            # using sqlite3 database to save data
            # create database
            connection = sqlite3.connect("data-entry-form.db")
            cursor = connection.cursor()
            # create table
            create_table_query = """ CREATE TABLE IF NOT EXISTS Student 
                (fname TEXT, lname TEXT, gender TEXT, age INT, nationality TEXT, 
                registration_status TEXT, courses INT, semesters INT)
            """
            connection.execute(create_table_query)
            # insert data into the table
            insert_data_query = """INSERT INTO Student (fname, lname, gender, age, nationality, 
                registration_status, courses, semesters) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
            data_tuple = (
                fname, lname, gender, age, nationality, registration_status, courses, semesters)
            cursor.execute(insert_data_query, data_tuple)
            connection.commit()
            messagebox.showinfo("Inserted Data", "Data has be inserted")
            # close connection
            connection.close()
        else:
            messagebox.showwarning(
                title="Registration Error", message="First name and Last name are required")
    else:
        messagebox.showwarning(
            title="Registration Error", message="You have not accepted Terms & Conditions")


root = tk.Tk()
root.title("Data Entry Form")
root.geometry("750x500")

standard_font = ("Arial", 16)

# outer frame
outer_frame = tk.Frame(root)
outer_frame.pack()

# User Information LabelFrame
user_info_frame = tk.LabelFrame(
    outer_frame, text="User Information", font=standard_font)
user_info_frame.grid(row=0, column=0, sticky="news", padx=15, pady=15)

fname_label = tk.Label(user_info_frame, text="First Name", font=standard_font)
fname_label.grid(row=0, column=0)

fname_entry = tk.Entry(user_info_frame, font=standard_font)
fname_entry.grid(row=1, column=0)

lname_label = tk.Label(user_info_frame, text="Last Name", font=standard_font)
lname_label.grid(row=0, column=1)

lname_entry = tk.Entry(user_info_frame, font=standard_font)
lname_entry.grid(row=1, column=1)

gender_label = tk.Label(user_info_frame, text="Gender", font=standard_font)
gender_label.grid(row=0, column=2)

gender_combobox = ttk.Combobox(user_info_frame, values=[
                               "", "Male", "Female"], font=standard_font)
gender_combobox.grid(row=1, column=2)

age_label = tk.Label(user_info_frame, text="Age", font=standard_font)
age_label.grid(row=2, column=0)

age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=120, font=standard_font)
age_spinbox.grid(row=3, column=0)

nationality_label = tk.Label(
    user_info_frame, text="Nationality", font=standard_font)
nationality_label.grid(row=2, column=1)

nationality_combobox = ttk.Combobox(
    user_info_frame, values=["Algeria", "Maroco", "Tunisia"], font=standard_font)
nationality_combobox.grid(row=3, column=1)

# create padding fro all widgets of user_info_frame
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# Course LabelFrame
courses_frame = tk.LabelFrame(
    outer_frame, text="Courses Registration", font=standard_font)
courses_frame.grid(row=1, column=0, sticky="news", padx=15, pady=15)

registred_label = tk.Label(
    courses_frame, text="Registration Status", font=standard_font)
registred_label.grid(row=0, column=0)

registration_status_var = tk.StringVar(value="Not Registered")
registration_status_checkbutton = tk.Checkbutton(
    courses_frame, text="Currently Registered", variable=registration_status_var, onvalue="Registered", offvalue="Not Registered", font=standard_font)
registration_status_checkbutton.grid(row=1, column=0)

numcourses_label = tk.Label(
    courses_frame, text="Completed Courses", font=standard_font)
numcourses_label.grid(row=0, column=1)

numcourses_spinbox = tk.Spinbox(
    courses_frame, from_=0, to="infinity", font=standard_font)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tk.Label(
    courses_frame, text="Completed Semesters", font=standard_font)
numsemesters_label.grid(row=0, column=2)

numsemesters_spinbox = tk.Spinbox(
    courses_frame, from_=0, to="infinity", font=standard_font)
numsemesters_spinbox.grid(row=1, column=2)

# create padding fro all widgets of courses_frame
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=5, pady=10)

# Terms and Conditions LabelFrame
terms_frame = tk.LabelFrame(
    outer_frame, text="Terms & Conditions", font=standard_font)
terms_frame.grid(row=2, column=0, sticky="news", padx=15, pady=15)

terms_var = tk.StringVar(value="Not Accepted")
terms_checkbutton = tk.Checkbutton(
    terms_frame, variable=terms_var, onvalue="Accepted", offvalue="Not Accepted", font=standard_font)
terms_checkbutton.grid(row=0, column=0, padx=10, pady=10)

terms_label = tk.Label(
    terms_frame, text="I accept Terms & Conditions", font=standard_font)
terms_label.grid(row=0, column=1, padx=10, pady=10)

# creating Submit button
submit_button = tk.Button(outer_frame, text="Submit",
                          font=standard_font, bg="orange", command=print_data)
submit_button.grid(row=3, column=0, sticky="news", padx=10, pady=10)

root.mainloop()
