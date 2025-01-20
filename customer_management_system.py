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
        self.root.config(bg=self.clr(245, 245, 245))

        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["customer_management"]
        self.collection = self.db["customers"]

        title = tk.Label(self.root, bg=self.clr(92, 132, 179), text="RO Customer Management System", bd=3, relief="groove", font=("Times New Roman", 50, "bold"))
        title.pack(side="top", fill="x", pady=10)

        inFrame = tk.Frame(self.root, bd=4, relief="groove", bg=self.clr(169, 202, 226))
        inFrame.place(width=self.width / 3, height=self.height - 180, x=10, y=100)

        idLbl = tk.Label(inFrame, text="Enter ID:", bg=self.clr(169, 202, 226), font=("Times New Roman", 15, "bold"))
        idLbl.grid(row=0, column=0, padx=20, pady=15, sticky="w")
        self.idIn = tk.Entry(inFrame, width=20, bd=2, font=("Times New Roman", 15))
        self.idIn.grid(row=0, column=1, padx=10, pady=15)

        nameLbl = tk.Label(inFrame, text="Customer Name:", bg=self.clr(169, 202, 226), font=("Times New Roman", 15, "bold"))
        nameLbl.grid(row=1, column=0, padx=20, pady=15, sticky="w")
        self.nameIn = tk.Entry(inFrame, width=20, bd=2, font=("Times New Roman", 15))
        self.nameIn.grid(row=1, column=1, padx=10, pady=15)

        phLbl = tk.Label(inFrame, text="Phone Number:", bg=self.clr(169, 202, 226), font=("Times New Roman", 15, "bold"))
        phLbl.grid(row=2, column=0, padx=20, pady=15, sticky="w")
        self.phIn = tk.Entry(inFrame, width=20, bd=2, font=("Times New Roman", 15))
        self.phIn.grid(row=2, column=1, padx=10, pady=15)

        dateLbl = tk.Label(inFrame, text="Date of Installation:", bg=self.clr(169, 202, 226), font=("Times New Roman", 15, "bold"))
        dateLbl.grid(row=3, column=0, padx=20, pady=15, sticky="w")
        self.deleteIn = tk.Entry(inFrame, width=20, bd=2, font=("Times New Roman", 15))
        self.deleteIn.grid(row=3, column=1, padx=10, pady=15)

        amount_receivedLbl = tk.Label(inFrame, text="Amount Received:", bg=self.clr(169, 202, 226), font=("Times New Roman", 15, "bold"))
        amount_receivedLbl.grid(row=4, column=0, padx=20, pady=15, sticky="w")
        self.amount_receivedIn = tk.Entry(inFrame, width=20, bd=2, font=("Times New Roman", 15))
        self.amount_receivedIn.grid(row=4, column=1, padx=10, pady=15)

        balance_amountLbl = tk.Label(inFrame, text="Balance Amount:", bg=self.clr(169, 202, 226), font=("Times New Roman", 15, "bold"))
        balance_amountLbl.grid(row=5, column=0, padx=20, pady=15, sticky="w")
        self.balance_amountIn = tk.Entry(inFrame, width=20, bd=2, font=("Times New Roman", 15))
        self.balance_amountIn.grid(row=5, column=1, padx=10, pady=15)

        addressLbl = tk.Label(inFrame, text="Address:", bg=self.clr(169, 202, 226), font=("Times New Roman", 15, "bold"))
        addressLbl.grid(row=6, column=0, padx=20, pady=15, sticky="w")
        self.addressIn = tk.Entry(inFrame, width=20, bd=2, font=("Times New Roman", 15))
        self.addressIn.grid(row=6, column=1, padx=10, pady=15)

        modelLbl = tk.Label(inFrame, text="Model:", bg=self.clr(169, 202, 226), font=("Times New Roman", 15, "bold"))
        modelLbl.grid(row=7, column=0, padx=20, pady=15, sticky="w")
        self.modelIn = tk.Entry(inFrame, width=20, bd=2, font=("Times New Roman", 15))  # New Model input field
        self.modelIn.grid(row=7, column=1, padx=10, pady=15)

        okBtn = tk.Button(inFrame, text="Create", command=self.insertFun, bd=2, relief="raised", bg=self.clr(0, 142, 220), font=("Times New Roman", 20, "bold"), width=20)
        okBtn.grid(padx=30, pady=25, columnspan=2)

        self.detFrame = tk.Frame(self.root, bd=4, relief="groove", bg=self.clr(197, 223, 199))
        self.detFrame.place(width=self.width / 2 + 230, height=self.height - 180, x=self.width / 3 + 15, y=100)

        pIdLbl = tk.Label(self.detFrame, text="Customer Name:", bg=self.clr(197, 223, 199), font=("Times New Roman", 15))
        pIdLbl.grid(row=0, column=0, padx=10, pady=15, sticky="w")
        self.pIdIn = tk.Entry(self.detFrame, bd=1, width=12, font=("Times New Roman", 15))
        self.pIdIn.grid(row=0, column=1, padx=7, pady=15)

        view_customerBtn = tk.Button(self.detFrame, command=self.viewCustomerFun, text="View Customer", width=12, font=("Times New Roman", 15, "bold"), bd=2, relief="raised")
        view_customerBtn.grid(row=0, column=2, padx=8, pady=15)

        amount_updateBtn = tk.Button(self.detFrame, command=self.Amount_UpdateFun, text="Amount Update", width=12, font=("Times New Roman", 15, "bold"), bd=2, relief="raised")
        amount_updateBtn.grid(row=0, column=3, padx=8, pady=15)

        deleteBtn = tk.Button(self.detFrame, command=self.deleteFun, text="Delete", width=10, font=("Times New Roman", 15, "bold"), bd=2, relief="raised")
        deleteBtn.grid(row=0, column=4, padx=8, pady=15)

        viewAllBtn = tk.Button(self.detFrame, command=self.viewAllcustomers, text="View All Customers", width=14, font=("Times New Roman", 15, "bold"), bd=2, relief="raised", bg=self.clr(0, 142, 220))
        viewAllBtn.grid(row=0, column=5, padx=8, pady=15)

        self.tabFun()

    def tabFun(self):
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
            "Date": self.deleteIn.get(),
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
        self.idIn.delete(0, "end")
        self.nameIn.delete(0, "end")
        self.phIn.delete(0, "end")
        self.deleteIn.delete(0, "end")
        self.amount_receivedIn.delete(0, "end")
        self.balance_amountIn.delete(0, "end")
        self.addressIn.delete(0, "end")
        self.modelIn.delete(0, "end")

    def viewAllcustomers(self):
        self.table.delete(*self.table.get_children())
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

    def viewCustomerFun(self):
        name = self.pIdIn.get()
        if not name:
            tk.messagebox.showerror("Error", "Please enter the customer Name to view.")
            return

        customer = self.collection.find_one({"Name": name})
        if customer:
            tk.messagebox.showinfo("Customer Details", f"ID: {customer['Id']}\n"
                                                     f"Name: {customer['Name']}\n"
                                                     f"Phone: {customer['Ph.no']}\n"
                                                     f"Date: {customer['Date']}\n"
                                                     f"Amount Received: {customer['Amount_Received']}\n"
                                                     f"Balance: {customer['Balance_Amount']}\n"
                                                     f"Address: {customer['Address']}\n"
                                                     f"Model: {customer.get('Model', 'N/A')}")
        else:
            tk.messagebox.showerror("Error", "Customer not found.")


    def Amount_UpdateFun(self):
        self.pointFrame = tk.Frame(self.root, bg="light gray", bd=3, relief="ridge")
        self.pointFrame.place(width=400, height=150, x=500, y=200)
        
        lbl = tk.Label(self.pointFrame, text="Enter Amount:", bg="light gray", font=("Times New Roman", 15, "bold"))
        lbl.grid(row=0, column=0, padx=20, pady=20)
        
        self.pointIn = tk.Entry(self.pointFrame, width=17, bd=2, font=("Times New Roman", 15, "bold"))
        self.pointIn.grid(row=0, column=1, padx=10, pady=20)
        
        okBtn = tk.Button(self.pointFrame, command=self.addPoint, text="Update Amount", bd=2, relief="raised", font=("Times New Roman", 15, "bold"), width=15, bg=self.clr(157, 112, 207))
        okBtn.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

    def addPoint(self):
        name = self.pIdIn.get().strip()  
        hp_input = self.pointIn.get().strip()

        if name:
            customer = self.collection.find_one({"Name": name})
            if customer:
                try:
                    new_points = int(hp_input)

                    current_received = customer["Amount_Received"]
                    current_balance = float(customer["Balance_Amount"])  


                    updated_received = current_received + new_points
                    updated_balance = current_balance - new_points


                    if updated_balance < 0:
                        tk.messagebox.showerror("Error", "Insufficient balance to deduct the entered amount.")
                        self.pointFrame.destroy()  
                        return


                    self.collection.update_one({"Name": name}, {
                        "$set": {
                            "Amount_Received": updated_received,
                            "Balance_Amount": str(updated_balance)  
                        }
                    })

                    tk.messagebox.showinfo("Success", f"Updated Amount for customer {name}.")
                    self.viewAllcustomers()  
                    self.clearFun()  
                    self.pointFrame.destroy()  
                except ValueError:
                    tk.messagebox.showerror("Error", "Please enter a valid Amount.")
            else:
                tk.messagebox.showerror("Error", "Customer not found.")
        else:
            tk.messagebox.showerror("Error", "Please enter the customer's name.")


    def deleteFun(self):
        name = self.pIdIn.get().strip()
        if name:
            patient = self.collection.find_one({"Name": name})
            if patient:
                self.collection.delete_one({"Name": name})
                tk.messagebox.showinfo("Success", f"Customer {name} has been Deleted.")
                self.viewAllcustomers()
            else:
                tk.messagebox.showerror("Error", "Customer not found.")
        else:
            tk.messagebox.showerror("Error", "Please enter the customer's name.")


if __name__ == "__main__":
    root = tk.Tk()
    obj = Customer(root)
    root.mainloop()
