import tkinter as tk

class Skills:
    """A class that manage the skills data"""

    def __init__(self):
        """Initialize the skills"""
        # Initialize the lists that set the skill's maximum level
        self.lvl_list_2 = list(range(1, 3))
        self.lvl_list_3 = list(range(1, 4))
        self.lvl_list_4 = list(range(1, 5))
        self.lvl_list_5 = list(range(1, 6))
        self.lvl_list_6 = list(range(1, 7))
        self.lvl_list_7 = list(range(1, 8))

        # ----- Attack -----
        # Attack boost
        self.atk_boost = tk.IntVar()
        self.atk_boost_lvl = tk.IntVar()
        self.atk_boost_lvl.set(7)

        # Agitator
        self.agitator = tk.IntVar()
        self.agitator_lvl = tk.IntVar()
        self.agitator_lvl.set(5)
        
        # ----- Element -----
        # Elem attack
        self.elem_atk = tk.IntVar()
        self.elem_atk_lvl = tk.IntVar()
        self.elem_atk_lvl.set(5)

        # ----- Affinity -----
        # Critical eye
        self.crit_eye = tk.IntVar()
        self.crit_eye_lvl = tk.IntVar()
        self.crit_eye_lvl.set(7)

        # Critical boost
        self.crit_boost = tk.IntVar()
        self.crit_boost_lvl = tk.IntVar()
        self.crit_boost_lvl.set(3)

        # Critical element
        self.crit_elem = tk.IntVar()
        self.crit_elem_lvl = tk.IntVar()
        self.crit_elem_lvl.set(3)