from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from rc4 import *

def compute():
    # Get key and mode
    key = ent_key.get()
    mode = var1.get()

    if(mode == '1' and checkErrorInput()): #input text
        lbl_result_text['text'] = execute(key, ent_message.get(), mode)
    elif(mode == '2' and checkErrorFile()): #file
        text = bytearray(execute(key, openFile('.temporary'), mode), 'latin-1')
        filename = ent_file_name.get() + '.' + ent_file_ext.get()
        writeFile(text, filename)
        lbl_result_text['text'] = 'Success! Saved in ' + filename

def checkErrorInput():
    status = True
    if(ent_message.get() == ''):
        messagebox.showerror('Error', 'Enter message!')
        status = False
    elif(ent_key.get() == ''):
        messagebox.showerror('Error', 'Enter key!')
        status = False
    return status

def checkErrorFile():
    status = True
    if(lbl_file_status['text'] == ''):
        messagebox.showerror('Error', 'Open file first!')
        status = False
    else:
        try:
            openFile('.temporary')
        except: # failed to open file
            lbl_file_status['text'] = ''
            messagebox.showerror('Error', 'Open file first!')
            status = False
        else: # success
            if(ent_key.get() == ''):
                messagebox.showerror('Error', 'Enter key!')
                status = False
            elif(not(ent_file_name.get() and ent_file_ext.get())):
                messagebox.showerror('Error', 'Enter file name and extension!')
                status = False
    return status

def askOpenFile(): 
    f = askopenfile(mode ='rb') 
    if f is not None: 
        writeFile(f.read(),'.temporary')
        var1.set(2)
        lbl_file_status['text'] = 'File successfully loaded'

# Open file in read only and binary mode
def openFile(file):
    with open(file, 'rb') as f:
        return f.read()

# Write file in write and binary mode
def writeFile(text, filename):
    with open(filename, 'wb') as f:
        f.write(text)

# Clear function
def clear():
    ent_message.delete(0,END)
    ent_key.delete(0,END)
    ent_file_name.delete(0,END)
    ent_file_ext.delete(0,END)
    lbl_file_status['text'] = ''

# Copy function
def copy():
    if(lbl_result_text['text'] == 'Click button above to see magic'):
        messagebox.showerror('Error', 'Encrypt something please!')
        return
    window.clipboard_clear()
    window.clipboard_append(lbl_result_text['text'])

# Save function
def save():
    if(lbl_result_text['text'] == 'Click button above to see magic'):
        messagebox.showerror('Error', 'Encrypt something please!')
        return
    if(not(ent_file_name.get() and ent_file_ext.get())):
        messagebox.showerror('Error', 'Enter file name and extension!')
        return
    text = bytearray(lbl_result_text['text'], 'latin-1')
    filename = ent_file_name.get() + '.' + ent_file_ext.get()
    writeFile(text, filename)
    lbl_result_text['text'] = 'Success! Saved in ' + filename

# Exit function 
def qExit(): 
    window.destroy() 


# Main window
window = Tk()
window.title('Encrypt & Decrypt')

# Title label
lbl_title = Label(text='Welcome to Modified RC4!')
lbl_title.pack()

frm_form = Frame(relief=RIDGE, borderwidth=3)
frm_form.pack()

# Message label
lbl_text = Label(master=frm_form, text='Enter message:')
ent_message = Entry(master=frm_form, width=30)
lbl_text.grid(row=0, column=0, padx=5, pady=5, sticky="w")
ent_message.grid(row=0, column=1, padx=5, pady=5)

# Key label
lbl_key = Label(master=frm_form, text='Enter key:')
ent_key = Entry(master=frm_form, width=30)
lbl_key.grid(row=1, column=0, padx=5, pady=5, sticky='w')
ent_key.grid(row=1, column=1, padx=5, pady=5)

# File
btn_open = Button(master=frm_form, text='Open file', width=8, command=askOpenFile)
btn_open.grid(row=2, column=1, padx=5, pady=5, sticky='w')
lbl_file_status = Label(master=frm_form)
lbl_file_status.grid(row=3, column=1, padx=5, pady=5, sticky='w')

btn_clear = Button(master=frm_form, text='Clear', width=5, command=clear)
btn_clear.grid(row=2, column=1, padx=5, pady=5)

# Initialize radio button
var1 = StringVar()
var1.set(1)

# Encryption mode
lbl_mode = Label(master=frm_form, text='Choose mode:')
lbl_mode.grid(row=4, column=0, padx=5, pady=5, sticky="w")
rad_mode = Radiobutton(master=frm_form,text='Input Text', variable = var1, value=1)
rad_mode.grid(row=4, column=1, padx=5, pady=5, sticky='w')
rad_mode = Radiobutton(master=frm_form,text='File', variable = var1, value=2)
rad_mode.grid(row=5, column=1, padx=5, pady=5, sticky='w')

# File option
lbl_file_name = Label(master=frm_form, text='File name:')
ent_file_name = Entry(master=frm_form, width=30)
lbl_file_name.grid(row=6, column=0, padx=5, pady=5, sticky="w")
ent_file_name.grid(row=6, column=1, padx=5, pady=5)
lbl_file_ext = Label(master=frm_form, text='File extension:')
ent_file_ext = Entry(master=frm_form, width=30)
lbl_file_ext.grid(row=7, column=0, padx=5, pady=5, sticky="w")
ent_file_ext.grid(row=7, column=1, padx=5, pady=5)

# Encrypt/decrypt
btn_compute = Button(master=frm_form, text='Encrypt', width=10, height=2, command=compute)
btn_compute.grid(row=13, column=1, padx=5, pady=5, sticky='w')
btn_compute = Button(master=frm_form, text='Decrypt', width=10, height=2, command=compute)
btn_compute.grid(row=13, column=2, padx=5, pady=5)

# Result label
lbl_result = Label(master=frm_form, text='Result:')
lbl_result_text = Label(master=frm_form, text='Click button above to see magic')
lbl_result.grid(row=14, column=0, padx=5, pady=5, sticky="w")
lbl_result_text.grid(row=14, column=1, padx=5, pady=5, sticky="w")

# Action button
btn_copy = Button(master=frm_form, text='Copy result', width=10, command=copy)
btn_copy.grid(row=15, column=1, padx=5, pady=5, sticky='w')
btn_save = Button(master=frm_form, text='Save to file', width=10, command=save)
btn_save.grid(row=15, column=2, padx=5, pady=5)
btn_exit = Button(master=frm_form, text='Exit', width=5, command=qExit)
btn_exit.grid(row=15, column=3, padx=5, pady=5, sticky='e')

# Keeps window alive 
window.mainloop()