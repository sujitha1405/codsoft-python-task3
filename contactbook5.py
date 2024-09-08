import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root_window):
        self.contacts_list = []
        self.root_window = root_window
        self.root_window.title("Contact Manager")

        # Menu setup
        self.menu_bar = tk.Menu(self.root_window)
        self.root_window.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="View Contacts", command=self.show_all_contacts)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root_window.quit)

        # Add Contact Section
        self.add_contact_frame = tk.LabelFrame(self.root_window, text="Add New Contact", padx=10, pady=10)
        self.add_contact_frame.pack(padx=10, pady=10, fill="x")

        self.name_label = tk.Label(self.add_contact_frame, text="Name")
        self.name_label.grid(row=0, column=0, sticky="e")
        self.name_input = tk.Entry(self.add_contact_frame)
        self.name_input.grid(row=0, column=1, pady=2, padx=5, sticky="w")

        self.phone_label = tk.Label(self.add_contact_frame, text="Phone Number")
        self.phone_label.grid(row=1, column=0, sticky="e")
        self.phone_input = tk.Entry(self.add_contact_frame)
        self.phone_input.grid(row=1, column=1, pady=2, padx=5, sticky="w")

        self.add_contact_button = tk.Button(self.add_contact_frame, text="Add Contact", command=self.add_new_contact)
        self.add_contact_button.grid(row=2, columnspan=2, pady=10)

        # View Contacts Section
        self.view_frame = tk.Frame(self.root_window)
        self.view_frame.pack(pady=10)

        self.contacts_listbox = tk.Listbox(self.view_frame, width=50)
        self.contacts_listbox.pack()

        self.contacts_listbox.bind("<Double-1>", self.select_contact_from_listbox)

        # Button Actions (Update/Delete)
        self.actions_frame = tk.Frame(self.root_window)
        self.actions_frame.pack(pady=10)

        self.update_contact_button = tk.Button(self.actions_frame, text="Update Contact", command=self.update_contact_info)
        self.update_contact_button.grid(row=0, column=0, padx=5)
        self.delete_contact_button = tk.Button(self.actions_frame, text="Delete Contact", command=self.remove_selected_contact)
        self.delete_contact_button.grid(row=0, column=1, padx=5)

        # Search Section
        self.search_frame = tk.LabelFrame(self.root_window, text="Search Contact", padx=10, pady=10)
        self.search_frame.pack(padx=10, pady=10, fill="x")

        self.search_label = tk.Label(self.search_frame, text="Search by Name or Phone Number")
        self.search_label.grid(row=0, column=0, sticky="e")
        self.search_input = tk.Entry(self.search_frame)
        self.search_input.grid(row=0, column=1, pady=2, padx=5, sticky="w")

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_contacts)
        self.search_button.grid(row=1, columnspan=2, pady=10)

    def add_new_contact(self):
        name = self.name_input.get()
        phone = self.phone_input.get()
        if name and phone:
            self.contacts_list.append({"name": name, "phone": phone})
            self.contacts_listbox.insert(tk.END, f"{name} - {phone}")
            self.name_input.delete(0, tk.END)
            self.phone_input.delete(0, tk.END)
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Warning", "Name and Phone Number are required!")

    def show_all_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts_list:
            self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def select_contact_from_listbox(self, event):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            contact = self.contacts_list[index]
            self.name_input.delete(0, tk.END)
            self.name_input.insert(tk.END, contact['name'])
            self.phone_input.delete(0, tk.END)
            self.phone_input.insert(tk.END, contact['phone'])

    def update_contact_info(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            name = self.name_input.get()
            phone = self.phone_input.get()
            if name and phone:
                self.contacts_list[index] = {"name": name, "phone": phone}
                self.show_all_contacts()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showwarning("Warning", "Name and Phone Number are required!")
        else:
            messagebox.showwarning("Warning", "No contact selected!")

    def search_contacts(self):
        search_query = self.search_input.get().lower()
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts_list:
            if search_query in contact['name'].lower() or search_query in contact['phone']:
                self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def remove_selected_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            del self.contacts_list[index]
            self.show_all_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Warning", "No contact selected!")

if __name__ == "__main__":
    root_window = tk.Tk()
    app = ContactManager(root_window)
    root_window.mainloop()
