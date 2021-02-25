from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from rc4 import *

def compute():
    # Check if key empty
    file_content = ''
    if(ent_key.get()==''):
        messagebox.showerror('Error', 'Enter key!')
        return
    # Get text and key
    if(file_content == ''):
        text = ent_text.get()
    else:
        text = file_content
    key = ent_key.get()
    # get mode
    mode = var1.get()
    if mode == ('1'): #encryption
        lbl_result_text['text'] = (encrypt(key,text))
    else: #decryption
        lbl_result_text['text'] = (decrypt(key,text))

def openFile(): 
    f = askopenfile(mode ='rb') 
    if f is not None: 
        file_content = f.read() 
# Clear function
def clear():
    ent_text.delete(0,END)
    ent_key.delete(0,END)

# Copy function
def copy():
    window.clipboard_clear()
    window.clipboard_append(lbl_result_text["text"])

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
ent_text = Entry(master=frm_form, width=30)
lbl_text.grid(row=0, column=0, padx=5, pady=5, sticky="w")
ent_text.grid(row=0, column=1, padx=5, pady=5)

# Key label
lbl_key = Label(master=frm_form, text='Enter key:')
ent_key = Entry(master=frm_form, width=30)
lbl_key.grid(row=1, column=0, padx=5, pady=5, sticky='w')
ent_key.grid(row=1, column=1, padx=5, pady=5)

btn_open = Button(master=frm_form, text='Open file', width=8, command=openFile)
btn_open.grid(row=2, column=1, padx=5, pady=5, sticky='w')
btn_clear = Button(master=frm_form, text='Clear', width=5, command=clear)
btn_clear.grid(row=2, column=1, padx=5, pady=5)

# Initialize radio button
var1 = StringVar()
var2 = StringVar()
var1.set(1)
var2.set(1)

# Encryption mode
lbl_mode = Label(master=frm_form, text='Choose mode:')
lbl_mode.grid(row=3, column=0, padx=5, pady=5, sticky="w")
rad_mode = Radiobutton(master=frm_form,text='Encryption', variable = var1, value=1)
rad_mode.grid(row=3, column=1, padx=5, pady=5, sticky='w')
rad_mode = Radiobutton(master=frm_form,text='Decryption', variable = var1, value=2)
rad_mode.grid(row=4, column=1, padx=5, pady=5, sticky='w')

btn_compute = Button(master=frm_form, text='Go!', width=10, height=2, command=compute)
btn_compute.grid(row=13, column=1, padx=5, pady=5, sticky='w')

# Result label
lbl_result = Label(master=frm_form, text='Result:')
lbl_result_text = Label(master=frm_form, text='Click "Go!" to see magic')
lbl_result.grid(row=14, column=0, padx=5, pady=5, sticky="w")
lbl_result_text.grid(row=14, column=1, padx=5, pady=5, sticky="w")

btn_copy = Button(master=frm_form, text='Copy result', width=10, command=copy)
btn_copy.grid(row=15, column=1, padx=5, pady=5, sticky='w')
btn_exit = Button(master=frm_form, text='Exit', width=5, command=qExit)
btn_exit.grid(row=15, column=1, padx=5, pady=5, sticky='e')

# Keeps window alive 
window.mainloop()