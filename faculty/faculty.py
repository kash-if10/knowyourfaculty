import pandas as pd
import tkinter as tk
from tkinter import messagebox

faculty_df = pd.read_excel('faculty.xlsx')

def search_faculty():
    faculty_name = entry.get()
    clear_results()  
    try:
        details = faculty_df[faculty_df['Name'].str.contains(faculty_name, case=False, na=False)]
        if not details.empty:
            for index, row in details.iterrows():
                name_result.insert(tk.END, row['Name'] + '\n')
                department_result.insert(tk.END, row['Department'] + '\n')
                email_result.insert(tk.END, row['Email'] + '\n')
                phone_result.insert(tk.END, row['Phone'] + '\n')
        else:
            messagebox.showinfo("Result", "Faculty not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_results():
    name_result.delete('1.0', tk.END)
    department_result.delete('1.0', tk.END)
    email_result.delete('1.0', tk.END)
    phone_result.delete('1.0', tk.END)

root = tk.Tk()
root.title("Know Your Faculty Bot")

label = tk.Label(root, text="Enter Faculty Name:")
entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=search_faculty)

name_label = tk.Label(root, text="Name")
department_label = tk.Label(root, text="Department")
email_label = tk.Label(root, text="Email")
phone_label = tk.Label(root, text="Phone")

name_result = tk.Text(root, height=10, width=20)
department_result = tk.Text(root, height=10, width=20)
email_result = tk.Text(root, height=10, width=30)
phone_result = tk.Text(root, height=10, width=20)

label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
search_button.grid(row=0, column=2, padx=10, pady=10)

name_label.grid(row=1, column=0)
department_label.grid(row=1, column=1)
email_label.grid(row=1, column=2)
phone_label.grid(row=1, column=3)

name_result.grid(row=2, column=0, padx=10, pady=10)
department_result.grid(row=2, column=1, padx=10, pady=10)
email_result.grid(row=2, column=2, padx=10, pady=10)
phone_result.grid(row=2, column=3, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()

