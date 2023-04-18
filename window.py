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
        self.frame = tk.Frame(self, height=400, width=600)
        #ttk.Label(self.frame, text="Hello World!").grid(column=0, row=0)
        #ttk.Button(self.frame, text="Damage Calculator",
        #           command=self.dmgcalc.).grid(column=1, row=0)
        self.frame.grid()

    def make_window(self):
        """"""
        secondary_window = tk.Toplevel()
        #self.
    
    def make_main_window(self):
        """Create the window"""
        self.mainloop()