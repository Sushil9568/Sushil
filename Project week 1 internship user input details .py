import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF

def generate_pdf():
    # Get user input
    name = entry_name.get()
    aicte_id = entry_aicte_id.get()
    email = entry_email.get()
    phone_no = entry_phone_no.get()
    college_name = entry_college_name.get()

    # Validate data
    if not all([name, aicte_id, email, phone_no, college_name]):
        messagebox.showerror("Error", "Please fill in all fields")
        return
    if not aicte_id.isdigit():
        messagebox.showerror("Error", "AICTE ID must be a number")
        return
    if not email.count("@") == 1 or not email.count(".") >= 1:
        messagebox.showerror("Error", "Invalid email address")
        return
    if not phone_no.isdigit() or len(phone_no) != 10:
        messagebox.showerror("Error", "Invalid phone number")
        return

    # Generate PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Student Registration Details", ln=True, align="C")
    pdf.cell(200, 10, txt="", ln=True)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"AICTE ID: {aicte_id}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Phone No.: {phone_no}", ln=True)
    pdf.cell(200, 10, txt=f"College Name: {college_name}", ln=True)
    pdf_output = f"{name}_registration_details.pdf"
    pdf.output(pdf_output)

    messagebox.showinfo("Success", f"PDF generated successfully: {pdf_output}")

# Create main window
root = tk.Tk()
root.title("Student Registration Form")

# Create labels and entry fields
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_aicte_id = tk.Label(root, text="AICTE ID:")
label_aicte_id.grid(row=1, column=0, sticky="e")
entry_aicte_id = tk.Entry(root)
entry_aicte_id.grid(row=1, column=1)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, sticky="e")
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

label_phone_no = tk.Label(root, text="Phone No.:")
label_phone_no.grid(row=3, column=0, sticky="e")
entry_phone_no = tk.Entry(root)
entry_phone_no.grid(row=3, column=1)

label_college_name = tk.Label(root, text="College Name:")
label_college_name.grid(row=4, column=0, sticky="e")
entry_college_name = tk.Entry(root)
entry_college_name.grid(row=4, column=1)

# Create submit button
submit_button = tk.Button(root, text="Generate PDF", command=generate_pdf)
submit_button.grid(row=5, columnspan=2)

root.mainloop()
