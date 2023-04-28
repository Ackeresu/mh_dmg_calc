import tkinter as tk
from tkinter import ttk

from items import Items
from skills import Skills

class DamageCalc():
    """Class that manage the damage calc window"""

    def __init__(self):
        """Initialize the class"""
        self.items = Items()
        self.skills = Skills()
        #self.wpn_stats = dict.fromkeys(['raw', 'elem', 'crit', 'sharp'])
        #self.other_stats = dict.fromkeys(['mv', 'hzv', 'ehzv'])

        # Weapon variables
        self.raw = tk.IntVar()
        self.raw.set(160)
        self.elem = tk.IntVar()
        self.elem.set(0)
        self.crit = tk.IntVar()
        self.crit.set(0)
        self.sharp = tk.StringVar()
        self.sharp.set('Green')
        # Other variables
        self.mv = tk.DoubleVar()
        self.mv.set(46)
        self.hzv = tk.DoubleVar()
        self.hzv.set(68)
        self.ehzv = tk.DoubleVar()
        self.ehzv.set(0)

        self.atk_buffs = tk.IntVar()
        self.atk_buffs.set(0)
        self.display_atk = tk.IntVar()
        self.display_atk.set(0)

    def calculate(self):
        """Call the necessary functions to calculate the damage"""
        # Check for a previous output and delete it if present.
        try:
            self.output_label.destroy()
        except AttributeError:
            pass
        self._get_values()
        self._do_calcs()
        self._show_results()

    def _get_values(self):
        """"""
        self._get_weapon_values()
        self._get_items_values()
        self._get_skills_values()
    
    def _get_weapon_values(self):
        """Get the values from the entries and convert them if necessary"""
        self.raw = float(self.raw_entry.get())
        self.elem = float(self.elem_entry.get())
        self.crit = float(self.crit_entry.get())
        self.sharp = self.sharp_entry.get()

        self.mv = float(self.mv_entry.get())
        self.mv = self.mv / 100
        self.hzv = float(self.hzv_entry.get())
        self.hzv = self.hzv / 100
        self.ehzv = float(self.ehzv_entry.get())
        self.ehzv = self.ehzv / 100

    def _get_items_values(self):
        """Get the values from the active items"""
        atk_buffs = 0
        powercharm = self.items.powercharm.get()
        powertalon = self.items.powertalon.get()
        might_seed = self.items.might_seed.get()
        demon_powder = self.items.demon_powder.get()
        demondrug = self.items.demondrug.get()
        mega_demondrug = self.items.mega_demondrug.get()

        if powercharm == 1:
            atk_buffs += 6
        if powertalon == 1:
            atk_buffs += 9
        if mega_demondrug == 1:
            atk_buffs += 7
        if demondrug == 1:
            atk_buffs += 5
        if might_seed == 1:
            atk_buffs += 10
        if demon_powder == 1:
            atk_buffs += 10

        self.atk_buffs = atk_buffs

    def _get_skills_values(self):
        """Get the values from the active skills"""
        # Critical boost
        crit_boost = self.skills.crit_boost.get()
        crit_boost_lvl_n = self.skills.crit_boost_lvl_n.get()

        if crit_boost == 0:
            self.crit_mltp = 1.25
            self.crit_value = 25
        elif crit_boost == 1 and crit_boost_lvl_n == 1:
            self.crit_mltp = 1.30
            self.crit_value = 30
        elif crit_boost == 1 and crit_boost_lvl_n == 2:
            self.crit_mltp = 1.35
            self.crit_value = 35
        elif crit_boost == 1 and crit_boost_lvl_n == 3:
            self.crit_mltp = 1.40
            self.crit_value = 40
        
        # Critical element
        crit_elem = self.skills.crit_elem.get()
        crit_elem_lvl_n = self.skills.crit_elem_lvl_n.get()

        if crit_elem == 0:
            self.crit_elem_mltp = 1.0
        elif crit_elem == 1 and crit_elem_lvl_n == 1:
            self.crit_elem_mltp = 1.05
        elif crit_elem == 1 and crit_elem_lvl_n == 2:
            self.crit_elem_mltp = 1.10
        elif crit_elem == 1 and crit_elem_lvl_n == 3:
            self.crit_elem_mltp = 1.15

    def _do_calcs(self):
        """Do the calculations"""
        # Calculate the sharpness multiplier
        self._sharp_mod()
        raw_sharp_mltp = self.sharp_mltp[0]
        elem_sharp_mltp = self.sharp_mltp[1]

        # Sum the raw with the atk buffs
        self.display_atk = round(self.raw + self.atk_buffs)

        phys_atk = (self.display_atk * raw_sharp_mltp) * self.mv
        elem_atk = (self.elem * elem_sharp_mltp)

        # Calculate the effective raw/elem
        crit_calc = 1 + ((self.crit / 100) * (self.crit_value / 100))

        self.eff_raw = round((self.display_atk * raw_sharp_mltp) * crit_calc)
        self.eff_elem = round(self.elem * elem_sharp_mltp)

        # Calculate the damage
        self.phys_dmg = round(phys_atk * self.hzv)
        self.elem_dmg = round(elem_atk * self.ehzv)

        self.phys_crit_dmg = round(self.phys_dmg * self.crit_mltp)
        self.elem_crit_dmg = round(self.elem_dmg * self.crit_elem_mltp)

        self.tot_dmg = self.phys_dmg + self.elem_dmg

    def _show_results(self):
        """Print the results"""
        self.output_label = tk.Label(self.bot_frame, justify='left',
            text=f"Displayed attack: {self.display_atk}\n"
                 f"Effective raw: {self.eff_raw}\n"
                 f"Effective element: {self.eff_elem}\n\n"
                 f"Total damage: {self.tot_dmg}\n"
                 f"If crit: {self.phys_crit_dmg + self.elem_crit_dmg}\n\n"
                 f"Physical: {self.phys_dmg}\n"
                 f"If crit: {self.phys_crit_dmg}\n\n"
                 f"Elemental: {self.elem_dmg}\n"
                 f"If crit: {self.elem_crit_dmg}")
        self.output_label.pack(side='bottom')
    
    def _sharp_mod(self):
        """Calculate the sharpness modifier"""
        if self.sharp.lower() == 'red':
            self.sharp_mltp = [0.5, 0.25]
        elif self.sharp.lower() == 'orange':
            self.sharp_mltp = [0.75, 0.5]
        elif self.sharp.lower() == 'yellow':
            self.sharp_mltp = [1, 0.75]
        elif self.sharp.lower() == 'green':
            self.sharp_mltp = [1.05, 1]
        elif self.sharp.lower() == 'blue':
            self.sharp_mltpr = [1.2, 1.063]
        elif self.sharp.lower() == 'white':
            self.sharp_mltp = [1.32, 1.15]
        elif self.sharp.lower() == 'purple':
            self.sharp_mltp = [1.39, 1.27]