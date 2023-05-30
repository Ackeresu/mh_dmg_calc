import tkinter as tk

class Other():
    """A class that manage buffs that are not skill-related"""

    def __init__(self):
        """Initialize the variables"""
    # ---------- ITEMS ----------
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
    
    # ---------- HH SONGS ----------
        self.attack_song = tk.IntVar()
        self.attack_song.set(0)

        self.affinity_song = tk.IntVar()
        self.affinity_song.set(0)

        self.element_song = tk.IntVar()
        self.element_song.set(0)

        self.infernal_melody = tk.IntVar()
        self.infernal_melody.set(0)

    # ---------- OTHER ----------
        self.scroll_color = tk.IntVar()
        self.scroll_color.set(0)

        self.beaten_frenzy = tk.IntVar()
        self.beaten_frenzy.set(0)