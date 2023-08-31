from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
import pandas


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    password_letters = [random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    password_symbols = [random.choice(symbols) for sym in range(nr_symbols)]

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #     password += char

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email :{email}\nPassword:{password}")
    except FileNotFoundError:
        messagebox.showinfo(title='Oops', message='No Data File Found')
    except KeyError:
        messagebox.showinfo(title='Oops', message="No details for the website exists.")


def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': username,
            'password': password,
        }
    }
    if website == '' or password == '':
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', mode='r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', mode='w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
password_logo = PhotoImage(file='c:/Users/HP/Documents/Tech Bro FIles/Python Stuff/100 DOC/Day 29/logo.png')
canvas.create_image(100, 100, image=password_logo)
canvas.grid(padx=70, pady=20, row=0, column=1)

# Labels
website_label = Label(text='Website:', bg='white')
website_label.grid(row=1, column=0)

username_label = Label(text='Email/Username:', bg='white')
username_label.grid(row=2, column=0)

password_label = Label(text='Password:', bg='white')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, 'mdadelaja@gmail.com')

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

# Buttons
gen_button = Button(text='Generate\nPassword', command=generate_password)
gen_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text='Search', command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
