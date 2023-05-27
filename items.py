import tkinter as tk

class Items():
    """A class that manage the items data"""

    def __init__(self):
        """Initialize the options and items"""
        # Options
        self.scroll_color = tk.IntVar()
        self.scroll_color.set(0)

        self.beaten_frenzy = tk.IntVar()
        self.beaten_frenzy.set(0)

        # Items
        self.powercharm = tk.IntVar()
        self.powercharm.set(1)

        self.powertalon = tk.IntVar()
        self.powertalon.set(1)

        self.might_seed = tk.IntVar()
        self.might_seed.set(0)

        self.demon_powder = tk.IntVar()
        self.demon_powder.set(0)

        self.demondrug = tk.IntVar()
        self.demondrug.set(0)

        self.mega_demondrug = tk.IntVar()
        self.mega_demondrug.set(0)