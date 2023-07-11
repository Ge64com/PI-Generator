import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import sys
import os

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
#si.wShowWindow = subprocess.SW_HIDE # default
subprocess.call('taskkill /F /IM exename.exe', startupinfo=si)
CREATE_NO_WINDOW = 0x08000000
subprocess.call('taskkill /F /IM exename.exe', creationflags=CREATE_NO_WINDOW)

def pi_generator():
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while True:
        p, q, k = k*k, 2*k+1, k+1
        a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
        d, d1 = a//b, a1//b1
        while d == d1:
            yield int(d)
            a, a1 = 10*(a%b), 10*(a1%b1)
            d, d1 = a//b, a1//b1

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Application:
    def __init__(self) -> None:
        #Run the app upon creation
        self.run()

    def generate_pi(self):
        try:
            digits = int(self.entry.get())
            if digits >= 100000:
                messagebox.showwarning(
                    "Warning", 
                    """If you enter digits that are too high the app may go into\n
                    \"Not Responding\" mode which is completley normal and depends on your computer hardware !""")
            
            pi = pi_generator()
            next(pi)
            p = ""
            for i in range(digits):
                p += str(next(pi))
                if i % (digits/100) == 0:
                    self.progress_bar["value"] += 1
                    self.progress_bar.update()
                
            answer = "3." + p
            with open(resource_path("pi.txt"), "w") as f:
                f.write(str(answer))
                f.close()
            self.progress_bar["value"] = 0
            self.open_file()
        except ValueError:
            messagebox.showerror("Value Error", "Please enter a number in the entry !!!")

    def about_window(self):
        #Show the about window
        messagebox.showinfo(
            "About", 
"""This Software Generates The PI Number To How Many Digits You Want.\n
Made by Ge64
Sarina ro faramoosh nakonim...""")

    def change_theme(self):
        if self.window.tk.call("ttk::style", "theme", "use") == "azure-dark":
            self.window.tk.call("set_theme", "light")
        else:
            self.window.tk.call("set_theme", "dark")

    def open_file(self):
        subprocess.call(resource_path("pi.txt"), shell=True)

    def connect_with_creator(self):
        subprocess.call("start https://zil.ink/ge64", shell=True)

    def draw_scene(self):
        #Creating the window
        self.window = Tk()
        self.window.title("Pi Generator")
        self.window.resizable(width=False, height=False)
        self.window.iconbitmap(resource_path("pi.ico"))

        #Setting window's theme
        self.window.tk.call("source", resource_path("azure.tcl"))
        self.window.tk.call("set_theme", "dark")

        #Creating scene's elements
        self.entry_frame = Frame(self.window)
        self.text1 = Label(self.entry_frame, text="Enter The Amount Of Digits:", font=("Helvetica", "20"))
        self.entry = Entry(self.entry_frame, width=50, font=("Helvetica", "10"))
        self.generate_button = Button(self.entry_frame, text="Generate", command=self.generate_pi, width=58)
        self.progress_bar = Progressbar(self.entry_frame, value=0, length=100)
        self.text1.pack(padx=10, pady=5)
        self.entry.pack(ipadx=35, pady=5)
        self.generate_button.pack(padx=10, pady=5)
        self.progress_bar.pack(ipadx=165, pady=10)
        self.entry_frame.grid(row=0, column=0)

        #Creating the toolbar
        self.menubar = Menu(self.window)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Show Pi", command=self.open_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close", command=self.window.quit)

        self.viewmenu = Menu(self.menubar, tearoff=0)
        self.viewmenu.add_command(label="Change Theme", command=self.change_theme)

        self.helpmenu = Menu(self.menubar, tearoff=0)

        self.helpmenu.add_command(label="Developer Details", command=self.connect_with_creator)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="Software Details", command=self.about_window)

        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.window.config(menu=self.menubar)
        self.window.mainloop()

    def run(self):
        self.draw_scene()

if __name__ == "__main__":
    app = Application()
