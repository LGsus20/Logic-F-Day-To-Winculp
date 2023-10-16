# Python
import customtkinter
import pyperclip

# Local
import textFunction


def convertText():
    user_input = textbox_input.get('0.0', "end")
    inputs = user_input.split("\n")
    textbox_output.configure(state='normal')
    textbox_output.delete("0.0", "end")

    for input in inputs:
        input = textFunction.stringFormater(input)
        textbox_output.insert('end', input + "\n")

    textbox_output.configure(state='disabled')


def copyText():
    pyperclip.copy(textbox_output.get('0.0', "end"))


# app settings
app = customtkinter.CTk()
app.title("Text Converter")
app.geometry("840x300")
app.grid_columnconfigure(4, weight=1)

# labels
label = customtkinter.CTkLabel(master=app, text="Logic F-day", font=("Arial", 15), fg_color=("transparent"))
label.place(relx=0.2, rely=0)

label2 = customtkinter.CTkLabel(master=app, text="WinCULP", font=("Arial", 15), fg_color=("transparent"))
label2.place(relx=0.72, rely=0)

# text box
textbox_input = customtkinter.CTkTextbox(master=app, width=400)
textbox_input.grid(row=0, column=0, padx=10, pady=25)

textbox_output = customtkinter.CTkTextbox(master=app, width=400, state="disabled")
textbox_output.grid(row=0, column=1, padx=10, pady=10)


# button settings
btt_convert = customtkinter.CTkButton(app, text="Convert Text", command=convertText, hover_color='#2234A8')
btt_convert.grid(row=1, column=0, padx=40, pady=0)

btt_copy = customtkinter.CTkButton(app, text="Copy Text", command=copyText, hover_color='#2234A8')
btt_copy.grid(row=1, column=1, padx=40, pady=0)

# app loop
app.mainloop()

