from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from decimal import *
import os

def generate():
    try:
        digits = int(entry.get())
        
        if digits >= 100000:
            messagebox.showwarning("Warning", "If you enter too high digits the app may go into \n\"Not Responding\" mode which is completley normal and depends on your computer !")
        
        getcontext().prec = digits
        
            ################################
        reps = digits
        answer = Decimal(3.0)
        op = 1
        n = 2
        iterates = len(list(range(2, 2*reps+1, 2)))
        i = 0
        for n in range(2, 2*reps+1, 2):
            answer += 4/Decimal(n*(n+1)*(n+2)*op)
            op *= -1
            if i % (iterates/100) == 0:
                prog["value"] += 1
                prog.update()
            i += 1
        with open("pi.txt", "w") as f:
            f.write(str(answer))
            f.close()
        prog["value"] = 0
        
        ################################
        
        #messagebox.showinfo("Done !!!", "You can see the number in the pi.txt file in the folder that this app is in.")
        open_pi()
    except ValueError:
        messagebox.showerror("Value Error", "Please enter a number in the entry !!!")

def about():
    messagebox.showinfo("About", "This Software Generates The PI Number To How Many Digits You Want.\nMade by Ge64\nSarina ro faramoosh nakonim...")

def change_theme():
    if window.tk.call("ttk::style", "theme", "use") == "azure-dark":
        window.tk.call("set_theme", "light")
    else:
        window.tk.call("set_theme", "dark")

def open_pi():
    os.system("pi.txt")

window = Tk()
window.title("Pi Number Generator")
window.resizable(width=False, height=False)
window.iconbitmap("pi.ico")

window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")

entry_frame = Frame(window)
text1 = Label(entry_frame, text="Enter The amount of digits :", font=("Helvetica", "20"))
entry = Entry(entry_frame, width=50, font=("Helvetica", "10"))
generate_button = Button(entry_frame, text="Generate", command=generate, width=58)
prog = Progressbar(entry_frame, value=0, length=100)
text1.pack(padx=10, pady=5)
entry.pack(ipadx=35, pady=5)
generate_button.pack(padx=10, pady=5)
prog.pack(ipadx=165, pady=10)
entry_frame.grid(row=0, column=0)

menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Show pi", command=open_pi)
filemenu.add_separator()
filemenu.add_command(label="Close", command=window.quit)

viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_command(label="Change Theme", command=change_theme)

helpmenu = Menu(menubar, tearoff=0)

helpmenu.add_command(label="About", command=about)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="View", menu=viewmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)
window.mainloop()