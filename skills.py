import tkinter as tk

class Skills:
    """A class that manage the skills data"""

    def __init__(self):
        """Initialize the skills"""
        # ----- Affinity -----
        # Critical boost
        self.crit_boost = tk.IntVar()
        self.crit_boost_lvl = [1, 2, 3]
        self.crit_boost_lvl_n = tk.IntVar()
        self.crit_boost_lvl_n.set(3)
        
        # Critical element
        self.crit_elem = tk.IntVar()
        self.crit_elem_lvl = [1, 2, 3]
        self.crit_elem_lvl_n = tk.IntVar()
        self.crit_elem_lvl_n.set(3)