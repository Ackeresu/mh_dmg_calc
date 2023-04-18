import tkinter as tk
from tkinter import ttk
from damage_calc import DamageCalc

class Window(tk.Tk):
    """Class to manage the program window"""

    def __init__(self):
        """Initialize the window"""
        super().__init__()
        self.dmgcalc = DamageCalc()

        self.wm_title("MH Calculator")
        self.canvas = tk.Canvas(self, width=400, height=300)
        self.canvas.pack()

        self.name_input = tk.Entry(self)
        self.canvas.create_window(200, 120, window=self.name_input)
        
        self.print_name = tk.Button(text="clicca se vuoi venire diffato",
                                    command=self.mimmo)
        self.canvas.create_window(200, 150, window=self.print_name)

    def mimmo(self):
        """"""
        name = self.name_input.get()
        
        name_output = tk.Label(self, text=f"{name} diff")
        self.canvas.create_window(200, 180, window=name_output)

    def make_window(self,):
        """"""
        sec_window = tk.Toplevel()
        sec_window.geometry("200x300")

        sec_window.columnconfigure(0, weight=1)
        sec_window.columnconfigure(1, weight=1)

        sec_window.mainloop()
    
    def make_main_window(self):
        """Create the window"""
        self.mainloop()