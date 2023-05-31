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

    # ---------- FOOD ----------
        self.dango_booster = tk.IntVar()
        self.dango_booster.set(0)
        self.dango_booster_lvl = tk.IntVar()
        self.dango_booster_lvl.set(4)
        self.dango_booster_lvl_list = list(range(1, 5))

        self.dango_adrenaline = tk.IntVar()
        self.dango_adrenaline.set(0)
        self.dango_adrenaline_lvl = tk.IntVar()
        self.dango_adrenaline_lvl.set(4)
        self.dango_adrenaline_lvl_list = list(range(1, 5))

        self.dango_bulker = tk.IntVar()
        self.dango_bulker.set(0)
    
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