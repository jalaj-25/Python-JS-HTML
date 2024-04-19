import openpyxl
from tkinter import messagebox  # Import messagebox directly from tkinter for error handling
import tkinter as tk  # Import tk for use with Treeview and other widgets
from tkinter import ttk  # Import ttk for themed widgets

# Define available products as a global variable
available_products = {
    1001: {"name": "Fruits", "price": 230, "category": "grocery", "quantity": 10, "date": "15/01/2024"},
    1002: {"name": "lotion", "price": 250, "category": "beauty & personal", "quantity": 100, "date": "15/01/2024"},
    1003: {"name": "combiflame", "price": 500, "category": "health", "quantity": 200, "date": "15/01/2024"},
    1004: {"name": "chilli sauce", "price": 20, "category": "grocery", "quantity": 50, "date": "15/01/2024"},
    1005: {"name": "toothbrush", "price": 700, "category": "beauty & personal", "quantity": 100, "date": "15/01/2024"},
    1006: {"name": "icecreams", "price": 33, "category": "grocery", "quantity": 56, "date": "15/01/2024"},
    1007: {"name": "nailpolish", "price": 765, "category": "beauty & personal", "quantity": 70, "date": "15/01/2024"},
    1008: {"name": "vegetables", "price": 764, "category": "grocery", "quantity": 90, "date": "15/01/2024"},
    1009: {"name": "facewash", "price": 87, "category": "beauty & personal", "quantity": 50, "date": "15/01/2024"},
    1011: {"name": "facewash", "price": 87, "category": "beauty & personal", "quantity": 50, "date": "15/01/2024"},
    1010: {"name": "chocolate bars", "price": 30, "category": "grocery", "quantity": 60, "date": "15/01/2024"}
} 

def display_data(tree):
    for item in tree.get_children():
        tree.delete(item)

    for id, product in available_products.items():
        tree.insert("", tk.END, values=(id, product['name'], product['price'], product['category'], product['quantity'], product['date']))

def purchase_product(product_id, quantity, name, contact, tree):
    global available_products  # Use the global available_products dictionary

    if product_id in available_products:
        if available_products[product_id]['quantity'] >= quantity:
            # Reduce the quantity of the purchased product
            available_products[product_id]['quantity'] -= quantity

            # Check if the new quantity is 10 or below
            new_quantity = available_products[product_id]['quantity']
            if new_quantity <= 10:
                messagebox.showinfo("Low Stock", f"Product ID {product_id} is now low in stock! Quantity: {new_quantity}")

            # Update the Treeview to reflect the new quantity
            update_tree_item(tree, product_id, new_quantity)

            # Save purchase data to Excel
            save_purchase_to_excel(product_id, quantity, name, contact)
            return True
        else:
            messagebox.showerror("Error", "Insufficient quantity!")
            return False
    else:
        messagebox.showerror("Error", "Invalid Product ID!")
        return False

def update_tree_item(tree, product_id, new_quantity):
    for item in tree.get_children():
        values = tree.item(item, 'values')
        if values[0] == product_id:
            tree.item(item, values=(values[0], values[1], values[2], values[3], new_quantity, values[5]))
            break

def save_purchase_to_excel(product_id, quantity, customer_name, contact_number):
    try:
        # Load workbook or create a new one if not found
        wb = openpyxl.load_workbook("purchase_data.xlsx")
    except FileNotFoundError:
        wb = openpyxl.Workbook()
        ws = wb.active 
        ws.append(["Product ID", "Name", "Price", "Category", "Quantity", "Date", "Customer Name", "Contact Number"])
    else:
        ws = wb.active

    try:
        product = available_products[product_id]
        ws.append([product_id, product['name'], product['price'], product['category'], quantity, product['date'], customer_name, contact_number])
        wb.save("purchase_data.xlsx")
        print(f"Purchase saved successfully to purchase_data.xlsx")
    except Exception as e:
        print(f"Failed to save purchase to purchase_data.xlsx: {e}")
        messagebox.showerror("Error", f"Failed to save purchase to Excel file: {e}")
