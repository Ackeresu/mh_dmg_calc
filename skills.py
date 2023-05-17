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

# -----------------------------------------------------------------------------
# --------------------------------- ATTACK ------------------------------------
# -----------------------------------------------------------------------------

        # Attack boost
        self.atk_boost = tk.IntVar()
        self.atk_boost_lvl = tk.IntVar()
        self.atk_boost_lvl.set(7)

        # Agitator
        self.agitator = tk.IntVar()
        self.agitator_lvl = tk.IntVar()
        self.agitator_lvl.set(5)

        # Peak performance
        self.peak_perf = tk.IntVar()
        self.peak_perf_lvl = tk.IntVar()
        self.peak_perf_lvl.set(3)

        # Resentment
        self.resentment = tk.IntVar()
        self.resentment_lvl = tk.IntVar()
        self.resentment_lvl.set(5)

        # Resuscitate
        self.resuscitate = tk.IntVar()
        self.resuscitate_lvl = tk.IntVar()
        self.resuscitate_lvl.set(3)

        # Buildup boost
        self.bu_boost = tk.IntVar()
        self.bu_boost_lvl = tk.IntVar()
        self.bu_boost_lvl.set(3)

        # Foray
        self.foray = tk.IntVar()
        self.foray_lvl = tk.IntVar()
        self.foray_lvl.set(3)

        # Counterstrike
        self.counterstrike = tk.IntVar()
        self.counterstrike_lvl = tk.IntVar()
        self.counterstrike_lvl.set(3)

        # Offensive guard
        self.off_guard = tk.IntVar()
        self.off_guard_lvl = tk.IntVar()
        self.off_guard_lvl.set(3)

        # Heroics
        self.heroics = tk.IntVar()
        self.heroics_lvl = tk.IntVar()
        self.heroics_lvl.set(5)

        # Fortify
        self.fortify = tk.IntVar()
        self.fortify_lvl = tk.IntVar()
        self.fortify_lvl.set(2)

# -----------------------------------------------------------------------------
# -------------------------------- ELEMENT ------------------------------------
# -----------------------------------------------------------------------------

        # Elem attack
        self.elem_atk = tk.IntVar()
        self.elem_atk_lvl = tk.IntVar()
        self.elem_atk_lvl.set(5)

        # Element exploit
        self.elem_ex = tk.IntVar()
        self.elem_ex_lvl = tk.IntVar()
        self.elem_ex_lvl.set(3)

        # Burst
        self.burst = tk.IntVar()
        self.burst_lvl = tk.IntVar()
        self.burst_lvl.set(3)

        # Coalescence
        self.coalescence = tk.IntVar()
        self.coalescence_lvl = tk.IntVar()
        self.coalescence_lvl.set(3)

        # Bloodlust
        self.bloodlust = tk.IntVar()
        self.bloodlust_lvl = tk.IntVar()
        self.bloodlust_lvl.set(3)

        # Mail of hellfire
        self.mail_hellfire = tk.IntVar()
        self.mail_hellfire_lvl = tk.IntVar()
        self.mail_hellfire_lvl.set(3)

# -----------------------------------------------------------------------------
# -------------------------------- AFFINITY -----------------------------------
# -----------------------------------------------------------------------------

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

        # Critical draw
        self.crit_draw = tk.IntVar()
        self.crit_draw_lvl = tk.IntVar()
        self.crit_draw_lvl.set(3)

        # Latent power
        self.latent_power = tk.IntVar()
        self.latent_power_lvl = tk.IntVar()
        self.latent_power_lvl.set(5)

        # Maximum might
        self.max_might = tk.IntVar()
        self.max_might_lvl = tk.IntVar()
        self.max_might_lvl.set(3)

        # Weakness exploit
        self.weak_ex = tk.IntVar()
        self.weak_ex_lvl = tk.IntVar()
        self.weak_ex_lvl.set(3)