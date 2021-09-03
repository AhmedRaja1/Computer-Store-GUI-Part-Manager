from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from db import Database

db = Database("store.db")

# Function for data handling


def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

# Function for Add Button


def add_btn():
    if (part_entry.get() == '') or (customer_entry.get() == '') or (vendor_entry.get() == '') or (price_entry.get() == ''):
        messagebox.showerror("Required Fields", "Please include all fields")
        return
    db.insert(part_entry.get(), customer_entry.get(),
              vendor_entry.get(), price_entry.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_entry.get(), customer_entry.get(),
                            vendor_entry.get(), price_entry.get()))
    populate_list()


# Select Function
def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        vendor_entry.delete(0, END)
        vendor_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass

# Function for Remove Button


def remove_btn():
    db.remove(selected_item[0])
    clear_btn()
    populate_list()

#  Function for Update Button


def update_btn():
    db.update(selected_item[0], part_entry.get(), customer_entry.get(),
              vendor_entry.get(), price_entry.get())
    populate_list()

#  Function for Clearing Text Button


def clear_btn():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    vendor_entry.delete(0, END)
    price_entry.delete(0, END)


# Create Window Object
app = Tk()

# Application Title
app.title("Reliance Computer Accessories")

# Application Resolution / Size
app.geometry("700x350")

# Part name & input widget (#1 Accessory name)
part_label = Label(app, text="Accessory Name",
                   font=("bold", 14), pady=10, padx=20)
part_label.grid(row=0, column=0)
part_input = StringVar()
part_entry = Entry(app, textvariable=part_input)
part_entry.grid(row=0, column=1)

# (#2 Customer Name & Text Input)
customer_label = Label(app, text="Customer Name",
                       font=("bold", 14), padx=20)
customer_label.grid(row=0, column=2)
customer_input = StringVar()
customer_entry = Entry(app, textvariable=customer_input)
customer_entry.grid(row=0, column=3)

# (#3 Vendor Name)
vendor_label = Label(app, text="Vendor Name",
                     font=("bold", 14))
vendor_label.grid(row=1, column=0, sticky=W)
vendor_input = StringVar()
vendor_entry = Entry(app, textvariable=vendor_input)
vendor_entry.grid(row=1, column=1)

# (#4 Price)
price_label = Label(app, text="Price of Accessory",
                    font=("bold", 14))
price_label.grid(row=1, column=2)
price_input = StringVar()
price_entry = Entry(app, textvariable=price_input)
price_entry.grid(row=1, column=3)

# (Accessories List, ListBox)
parts_list = Listbox(app, height=10, width=50, border=0)
parts_list.grid(row=2, column=0, pady=30, padx=50, columnspan=2, rowspan=3)

# Scroll bar
scrollbar = Scrollbar(app)
scrollbar.grid(row=2, column=3)

# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# Bind select
parts_list.bind("<<ListboxSelect>>", select_item)

# Add Button # 1
add_button = Button(app, text="Add Accessory", height=1,
                    width=15, command=add_btn)
add_button.grid(row=7, column=0)

# Remove Button # 2
remove_button = Button(app, text="Remove Accessory", height=1,
                       width=15, command=remove_btn)
remove_button.grid(row=7, column=1)

# Remove Button # 3
update_button = Button(app, text="Update Accessory", height=1,
                       width=15,  command=update_btn)
update_button.grid(row=7, column=2)

# Clear Input Button # 4
clear_button = Button(app, text="Clear Input", height=1,
                      width=15, command=clear_btn)
clear_button.grid(row=7, column=3)

# Populate Data
populate_list()


# To Start the Application
app.mainloop()
