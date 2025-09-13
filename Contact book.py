import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACT_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as f:
            return json.load(f)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contacts.append({"name": name, "phone": phone, "address": address})
        save_contacts(contacts)
        refresh_list()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Name and phone are required.")

# View contacts in listbox
def refresh_list():
    contact_list.delete(0, tk.END)
    for i, contact in enumerate(contacts):
        contact_list.insert(tk.END, f"{i+1}. {contact['name']} - {contact['phone']}")

# Search contact
def search_contact():
    keyword = simpledialog.askstring("Search", "Enter name or phone:")
    if keyword:
        results = [c for c in contacts if keyword.lower() in c["name"].lower() or keyword in c["phone"]]
        contact_list.delete(0, tk.END)
        for i, contact in enumerate(results):
            contact_list.insert(tk.END, f"{i+1}. {contact['name']} - {contact['phone']}")
        if not results:
            messagebox.showinfo("Search Result", "No contact found.")

# Select contact
def on_select(event):
    try:
        index = contact_list.curselection()[0]
        selected = contacts[index]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, selected["name"])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, selected["phone"])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, selected["address"])
    except IndexError:
        pass

# Update contact
def update_contact():
    try:
        index = contact_list.curselection()[0]
        contacts[index]["name"] = name_entry.get()
        contacts[index]["phone"] = phone_entry.get()
        contacts[index]["address"] = address_entry.get()
        save_contacts(contacts)
        refresh_list()
        clear_entries()
    except IndexError:
        messagebox.showerror("Error", "Select a contact to update.")

# Delete contact
def delete_contact():
    try:
        index = contact_list.curselection()[0]
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this contact?")
        if confirm:
            contacts.pop(index)
            save_contacts(contacts)
            refresh_list()
            clear_entries()
    except IndexError:
        messagebox.showerror("Error", "Select a contact to delete.")

# Clear all entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Main GUI
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

contacts = load_contacts()

# Input Fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact,bg='lightgreen').pack(pady=5)
tk.Button(root, text="View All Contacts", command=refresh_list,bg='grey').pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact,bg='skyblue').pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact,bg='red').pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact,bg='yellow').pack(pady=5)
tk.Button(root, text="Clear Fields", command=clear_entries,bg='lightblue').pack(pady=5)

# Contact List Display
contact_list = tk.Listbox(root)
contact_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
contact_list.bind("<<ListboxSelect>>", on_select)

# Load and show contacts on start
refresh_list()

root.mainloop()
