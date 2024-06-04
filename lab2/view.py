import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
from controller.controller import StudentController

class StudentView:
    def __init__(self, master):
        self.master = master
        master.title("Student Management System")

        # Create the controller
        self.controller = StudentController()

        # Create the main frame
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(padx=20, pady=20)

        # Create the top frame for buttons
        self.top_frame = tk.Frame(self.main_frame)
        self.top_frame.pack(side=tk.TOP, pady=10)

        # Add buttons for adding, searching, and deleting students
        self.add_button = tk.Button(self.top_frame, text="Add Student", command=self.open_add_student_window)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.search_button = tk.Button(self.top_frame, text="Search Student", command=self.search_student)
        self.search_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self.top_frame, text="Delete Student", command=self.delete_student)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        # Create the bottom frame for displaying students
        self.bottom_frame = tk.Frame(self.main_frame)
        self.bottom_frame.pack(side=tk.BOTTOM, pady=10)

        # Create the treeview to display students
        self.student_treeview = ttk.Treeview(self.bottom_frame, columns=("Name", "Course", "Group", "Completed Works", "Total Works", "Programming Language"), show="headings")
        self.student_treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure columns
        self.student_treeview.heading("Name", text="Name")
        self.student_treeview.heading("Course", text="Course")
        self.student_treeview.heading("Group", text="Group")
        self.student_treeview.heading("Completed Works", text="Completed Works")
        self.student_treeview.heading("Total Works", text="Total Works")
        self.student_treeview.heading("Programming Language", text="Programming Language")

        # Create the scrollbar
        self.scrollbar = tk.Scrollbar(self.bottom_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Connect the treeview and scrollbar
        self.student_treeview.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.student_treeview.yview)

        # Populate the treeview with the initial list of students
        self.update_student_list()

    def open_add_student_window(self):
        def add_student_to_db():
            name = name_entry.get()
            course = course_entry.get()
            group = group_entry.get()
            total_works = total_works_entry.get()
            completed_works = completed_works_entry.get()
            programming_language = programming_language_entry.get()

            if name and course and group and total_works and completed_works and programming_language:
                try:
                    total_works = int(total_works)
                    completed_works = int(completed_works)
                    student = self.controller.add_student(name, course, group, total_works, completed_works, programming_language)
                    self.update_student_list()
                    messagebox.showinfo("Student Added", f"Student {student.name} has been added.")
                    add_student_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Total Works and Completed Works must be integers.")
            else:
                messagebox.showerror("Error", "Please fill in all fields.")

        add_student_window = tk.Toplevel(self.master)
        add_student_window.title("Add Student")

        # Create labels and entry fields
        name_label = tk.Label(add_student_window, text="Name:")
        name_label.grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(add_student_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        course_label = tk.Label(add_student_window, text="Course:")
        course_label.grid(row=1, column=0, padx=5, pady=5)
        course_entry = tk.Entry(add_student_window)
        course_entry.grid(row=1, column=1, padx=5, pady=5)

        group_label = tk.Label(add_student_window, text="Group:")
        group_label.grid(row=2, column=0, padx=5, pady=5)
        group_entry = tk.Entry(add_student_window)
        group_entry.grid(row=2, column=1, padx=5, pady=5)

        total_works_label = tk.Label(add_student_window, text="Total Works:")
        total_works_label.grid(row=3, column=0, padx=5, pady=5)
        total_works_entry = tk.Entry(add_student_window)
        total_works_entry.grid(row=3, column=1, padx=5, pady=5)

        completed_works_label = tk.Label(add_student_window, text="Completed Works:")
        completed_works_label.grid(row=4, column=0, padx=5, pady=5)
        completed_works_entry = tk.Entry(add_student_window)
        completed_works_entry.grid(row=4, column=1, padx=5, pady=5)

        programming_language_label = tk.Label(add_student_window, text="Programming Language:")
        programming_language_label.grid(row=5, column=0, padx=5, pady=5)
        programming_language_entry = tk.Entry(add_student_window)
        programming_language_entry.grid(row=5, column=1, padx=5, pady=5)

        # Create the add button
        add_button = tk.Button(add_student_window, text="Add", command=add_student_to_db)
        add_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def search_student(self):
        search_options = ["Name", "Group", "Course", "Programming Language", "Completed Works", "Total Works", "Uncompleted Works"]
        selected_option = simpledialog.askstring("Search Student", "Select search criteria:\n" + "\n".join(search_options))

        if selected_option == "Name":
            name = simpledialog.askstring("Search by Name", "Enter student name:")
            students = self.controller.search_student_by_name(name)
        elif selected_option == "Group":
            group = simpledialog.askstring("Search by Group", "Enter student group:")
            students = self.controller.search_student_by_group(group)
        elif selected_option == "Course":
            course = simpledialog.askstring("Search by Course", "Enter student course:")
            students = self.controller.search_student_by_course(course)
        elif selected_option == "Programming Language":
            programming_language = simpledialog.askstring("Search by Programming Language", "Enter programming language:")
            students = self.controller.search_student_by_programming_language(programming_language)
        elif selected_option == "Completed Works":
            completed_works = simpledialog.askinteger("Search by Completed Works", "Enter completed works:")
            students = self.controller.search_student_by_completed_works(completed_works)
        elif selected_option == "Total Works":
            total_works = simpledialog.askinteger("Search by Total Works", "Enter total works:")
            students = self.controller.search_student_by_total_works(total_works)
        elif selected_option == "Uncompleted Works":
            uncompleted_works = simpledialog.askinteger("Search by Uncompleted Works", "Enter uncompleted works:")
            students = self.controller.search_student_by_uncompleted_works(uncompleted_works)
        else:
            return

        self.display_students