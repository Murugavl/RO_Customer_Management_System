import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymongo

class Customer:
    def __init__(self, root):
        self.root = root
        self.root.title("RO Customer Management System")
        
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        self.root.config(bg=self.clr(200, 207, 219))

        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["customer_management"]
        self.collection = self.db["customers"]

        # Title
        title = tk.Label(self.root, bg=self.clr(87, 81, 189), text="RO Customer Management System", bd=3, relief="groove", font=("Times New Roman", 50, "bold"))
        title.pack(side="top", fill="x", pady=10)

        # Main Frame
        inFrame = tk.Frame(self.root, bd=4, relief="groove", bg=self.clr(169, 202, 226))
        inFrame.place(width=self.width / 3, height=self.height - 180, x=10, y=100)

        # Create form fields
        self.create_form_fields(inFrame)

        # Button to create a new customer
        okBtn = tk.Button(inFrame, text="Create", command=self.insertFun, bd=2, relief="raised", bg=self.clr(0, 142, 220), font=("Times New Roman", 20, "bold"), width=20)
        okBtn.grid(padx=30, pady=25, columnspan=2)

        # Details frame for search, update, and delete actions
        self.detFrame = tk.Frame(self.root, bd=4, relief="groove", bg=self.clr(197, 223, 199))
        self.detFrame.place(width=self.width / 2 + 230, height=self.height - 180, x=self.width / 3 + 15, y=100)

        # Initialize customer action buttons (view, update, delete, etc.)
        self.create_customer_actions()

        # Initialize table for displaying customer data
        self.tabFun()

    def create_form_fields(self, inFrame):
        """ Create and place the form fields inside the provided frame """
        
        # Initialize form fields
        self.idIn = self.create_form_input(inFrame, "Enter ID:", 0)
        self.nameIn = self.create_form_input(inFrame, "Customer Name:", 1)
        self.phIn = self.create_form_input(inFrame, "Phone Number:", 2)
        self.dateIn = self.create_form_input(inFrame, "Date of Installation:", 3)
        self.amount_receivedIn = self.create_form_input(inFrame, "Amount Received:", 4)
        self.balance_amountIn = self.create_form_input(inFrame, "Balance Amount:", 5)
        self.addressIn = self.create_form_input(inFrame, "Address:", 6)
        self.modelIn = self.create_form_input(inFrame, "Model:", 7)

    def create_form_input(self, frame, label_text, row):
        """ Helper method to create form fields with label and input field """
        label = tk.Label(frame, text=label_text, bg=self.clr(169, 202, 226), font=("Times New Roman", 15, "bold"))
        label.grid(row=row, column=0, padx=20, pady=15, sticky="w")
        
        entry = tk.Entry(frame, width=20, bd=2, font=("Times New Roman", 15))
        entry.grid(row=row, column=1, padx=10, pady=15)
        
        return entry

    def create_customer_actions(self):
        """ Create action buttons for customer search, update, delete, etc. """
        pIdLbl = tk.Label(self.detFrame, text="Customer Name:", bg=self.clr(197, 223, 199), font=("Times New Roman", 15))
        pIdLbl.grid(row=0, column=0, padx=10, pady=15, sticky="w")
        self.pIdIn = tk.Entry(self.detFrame, bd=1, width=12, font=("Times New Roman", 15))
        self.pIdIn.grid(row=0, column=1, padx=7, pady=15)

        # Action buttons
        view_customerBtn = tk.Button(self.detFrame, command=self.viewCustomerFun, text="View Customer", width=12, font=("Times New Roman", 15, "bold"), bd=2, relief="raised")
        view_customerBtn.grid(row=0, column=2, padx=8, pady=15)

        amount_updateBtn = tk.Button(self.detFrame, command=self.Amount_UpdateFun, text="Amount Update", width=12, font=("Times New Roman", 15, "bold"), bd=2, relief="raised")
        amount_updateBtn.grid(row=0, column=3, padx=8, pady=15)

        deleteBtn = tk.Button(self.detFrame, command=self.deleteFun, text="Delete", width=10, font=("Times New Roman", 15, "bold"), bd=2, relief="raised")
        deleteBtn.grid(row=0, column=4, padx=8, pady=15)

        viewAllBtn = tk.Button(self.detFrame, command=self.viewAllcustomers, text="View All Customers", width=14, font=("Times New Roman", 15, "bold"), bd=2, relief="raised", bg=self.clr(0, 142, 220))
        viewAllBtn.grid(row=0, column=5, padx=8, pady=15)

    def tabFun(self):
        """ Setup the table to display customer details """
        self.tabFrame = tk.Frame(self.detFrame, bd=3, relief="ridge", bg="cyan")
        self.tabFrame.place(width=self.width / 2 + 140, height=self.height - 280, x=12, y=80)

        x_scrol = tk.Scrollbar(self.tabFrame, orient="horizontal")
        x_scrol.pack(side="bottom", fill="x")

        y_scrol = tk.Scrollbar(self.tabFrame, orient="vertical")
        y_scrol.pack(side="right", fill="y")

        self.table = ttk.Treeview(self.tabFrame, columns=("Id", "Name", "Ph.no", "Date", "Amount_Received", "Balance_Amount", "Address", "Model"),
                                  xscrollcommand=x_scrol.set, yscrollcommand=y_scrol.set)

        x_scrol.config(command=self.table.xview)
        y_scrol.config(command=self.table.yview)

        self.table.heading("Id", text="Customer ID")
        self.table.heading("Name", text="Customer Name")
        self.table.heading("Ph.no", text="Ph.No")
        self.table.heading("Date", text="Date")
        self.table.heading("Amount_Received", text="Amount_Received")
        self.table.heading("Balance_Amount", text="Balance_Amount")
        self.table.heading("Address", text="Customer Address")
        self.table.heading("Model", text="Model")  # Added heading for Model
        self.table["show"] = "headings"

        self.table.column("Id", width=100, anchor="center")
        self.table.column("Name", width=150, anchor="center")
        self.table.column("Ph.no", width=100, anchor="center")
        self.table.column("Date", width=120, anchor="center")
        self.table.column("Amount_Received", width=100, anchor="center")
        self.table.column("Balance_Amount", width=150, anchor="center")
        self.table.column("Address", width=200, anchor="center")
        self.table.column("Model", width=100, anchor="center")  # Added column for Model

        self.table.pack(fill="both", expand=1)

    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"

    def insertFun(self):
        customer_id = self.idIn.get()
        if not customer_id:
            tk.messagebox.showerror("Error", "Customer ID is required.")
            return

        existing_customer = self.collection.find_one({"Id": customer_id})
        if existing_customer:
            tk.messagebox.showerror("Error", f"Customer ID {customer_id} already exists.")
            return

        customer = {
            "Id": customer_id,
            "Name": self.nameIn.get(),
            "Ph.no": self.phIn.get(),
            "Date": self.dateIn.get(),
            "Amount_Received": int(self.amount_receivedIn.get()) if self.amount_receivedIn.get().isdigit() else 0,
            "Balance_Amount": self.balance_amountIn.get(),
            "Address": self.addressIn.get(),
            "Model": self.modelIn.get()  # Add the model field here
        }

        if all(customer.values()):
            try:
                self.collection.insert_one(customer)
                self.viewAllcustomers()
                tk.messagebox.showinfo("Success", f"Customer {customer['Name']} has been created.")
                self.clearFun()
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")
        else:
            tk.messagebox.showerror("Error", "Please fill in all the fields!")

    def updateTable(self):
        customers = self.collection.find()
        for customer in customers:
            self.table.insert('', tk.END, values=(
                customer["Id"],
                customer["Name"].upper(),
                customer["Ph.no"].upper(),
                customer["Date"].upper(),
                str(customer["Amount_Received"]),
                customer["Balance_Amount"].upper(),
                customer["Address"].upper(),
                customer.get("Model", "N/A").upper()  # If Model doesn't exist, show "N/A"
            ))

    def clearFun(self):
        self.idIn.delete(0, tk.END)
        self.nameIn.delete(0, tk.END)
        self.phIn.delete(0, tk.END)
        self.dateIn.delete(0, tk.END)
        self.amount_receivedIn.delete(0, tk.END)
        self.balance_amountIn.delete(0, tk.END)
        self.addressIn.delete(0, tk.END)
        self.modelIn.delete(0, tk.END)

    def viewCustomerFun(self):
        # Function to view a customer
        pass

    def Amount_UpdateFun(self):
        # Function to update customer amounts
        pass

    def deleteFun(self):
        # Function to delete a customer
        pass

    def viewAllcustomers(self):
        for row in self.table.get_children():
            self.table.delete(row)
        self.updateTable()

# Entry point
if __name__ == "__main__":
    root = tk.Tk()
    obj = Customer(root)
    root.mainloop()
