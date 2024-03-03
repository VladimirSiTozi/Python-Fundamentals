import re
import tkinter


def validate_email():
    email = entry_email.get()

    if "@" not in email:
        result = "Invalid Email: Missing '@'"
        color = "red"
    elif "." not in email:
        result = "Invalid Email: Missing '.'"
        color = "red"
    else:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            result = "Email is valid!"
            color = "green"
        else:
            result = "Invalid Email. Contains forbidden characters or wrong format."
            color = "red"

    entry_result.delete(0, tkinter.END)
    entry_result.insert(0, result)
    entry_result.config(fg=color)


root = tkinter.Tk()
root.geometry('500x500')  # Windows size
root.title('Email Validator')

label_instruction = tkinter.Label(root, text="Enter an email address. It should include '@' and '.domain'.")
label_instruction.pack()

entry_email = tkinter.Entry(root, width=60)
entry_email.pack()
entry_email.delete(0, tkinter.END)  # clear fields

button_validator = tkinter.Button(root, text='Validate Email', command=validate_email)
button_validator.pack()

entry_result = tkinter.Entry(root, width=60)
entry_result.pack()
entry_result.delete(0, tkinter.END)  # Clear field

root.mainloop()