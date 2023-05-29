import tkinter as tk

class Options():
    """A class that manage the options"""

    def __init__(self):
        """Initialize the options"""
        self.scroll_color = tk.IntVar()
        self.scroll_color.set(0)

        self.beaten_frenzy = tk.IntVar()
        self.beaten_frenzy.set(0)

        self.carted_once = tk.IntVar()
        self.carted_once.set(0)

        self.carted_twice = tk.IntVar()
        self.carted_twice.set(0)