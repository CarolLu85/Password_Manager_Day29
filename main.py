from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    #  turned above three for loops into three lines via using list comprehension

    password_letter = [random.choice(letters) for n in range(nr_letters)]
    password_symbol = [random.choice(symbols) for n in range(nr_symbols)]
    password_number = [random.choice(numbers) for n in range(nr_numbers)]
    password_list = password_number + password_symbol + password_letter
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    # using join to put everything inside this list into one string
    password = "".join(password_list)
    output_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web = input_website.get()
    user = input_username.get()
    pwd = output_password.get()
    # if web == "" or user == "" or pwd == "":
    if len(web) == 0 or len(user) == 0 or len(pwd) ==  0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askyesno(title=web, message=f"These are the details entered:"
                                               f"\nEmail: {user} \nPassword: n{pwd} "
                                               f"\nIs it ok to save?")
        if is_ok:
            # below is angela's version
            with open("data.txt", "a") as file:
                file.write(f"{web} | {user} | {pwd}\n")
                input_website.delete(0, END)
                output_password.delete(0,END)


    # below is my code
    # with open("data.txt", "a") as file:
    #     file.write(f"{web} | {user} | {pwd}\n")
    # file.close()
    # input_website.delete(0, END)
    # output_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(width=500, height=500)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Lable
website = Label(text="Website:")
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

# Entry
input_website = Entry(width=52)
input_website.grid(column=1, row=1, columnspan=2,sticky="w")
input_website.focus()

input_username = Entry(width=52)
input_username.grid(column=1, row=2,columnspan=2, sticky="w")
# input_username.insert(0, "carollu@gamil.com")

output_password = Entry(width=32)
output_password.grid(column=1, row=3, sticky="w")

# Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=44,command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")












window.mainloop()