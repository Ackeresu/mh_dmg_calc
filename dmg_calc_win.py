import tkinter as tk
from tkinter import ttk

from dmg_calc import DamageCalc
from items import Items
from skills import Skills

class DamageCalcWin():
    """Class that manage the damage calc window"""

    def __init__(self, root):
        """Initialize the class"""
        self.root = root
        self.dmg_calc = DamageCalc()
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

        self.root.title("Calculator")
        
        self._create_window()

        self.calc_btn = tk.Button(self.bot_frame, width=20, text='Calculate',
                                  command=self._calculate)
        self.calc_btn.pack(side='top')

    def _create_window(self):
        """Call the functions necessary to build the window"""
        self._create_main_frames()
        self._create_sub_frames()
        self._create_labels()
        self._create_entries()
        self._create_optionmenu()
        self._create_checkboxes()
        

    def _create_main_frames(self):
        """Create the frames of the window"""
        self.canvas = tk.Frame(self.root, width=300, height=200, bg='lightgrey')
        self.canvas.pack(fill='both', expand=True)

        self.top_frame = tk.Frame(self.canvas, bg='purple')
        self.top_frame.pack(side='top', padx=5, pady=5, expand=True)

        self.center_frame = tk.Frame(self.canvas, bg='red')
        self.center_frame.pack(side='top', fill='both', padx=5, pady=0,
                               expand=True)

        self.bot_frame = tk.Frame(self.canvas, bg='pink')
        self.bot_frame.pack(side='top', fill='both',padx=5, pady=5, expand=True)

    def _create_sub_frames(self):
        """Create the subframes of the window"""
        # ---------- Top frame ----------
        # ----- Weapon -----
        # Labels
        self.wpn_labels = tk.Frame(self.top_frame,bg='blue')
        self.wpn_labels.pack(side='left', anchor='w', fill='none',
                             padx=2, pady=2, expand=True)
        # Entries
        self.wpn_entries = tk.Frame(self.top_frame, bg='green')
        self.wpn_entries.pack(side='left', anchor='w', fill='none',
                              padx=2, pady=2, expand=True)
        
        # ----- Other -----
        # Labels
        self.other_labels = tk.Frame(self.top_frame, bg='blue')
        self.other_labels.pack(side='left', anchor='w', fill='none',
                               padx=2, pady=2, expand=True)
        # Entries
        self.other_entries = tk.Frame(self.top_frame, bg='green')
        self.other_entries.pack(side='left', anchor='w', fill='none',
                                padx=2, pady=2, expand=True)
        
        # ---------- Center frame ----------
        # ----- Left -----
        self.left_center = tk.Frame(self.center_frame, bg='pink')
        self.left_center.pack(side='left', anchor='w', fill='none',
                              padx=2, pady=2, expand=True)
        # Title
        self.left_center_title = tk.Label(self.left_center, text="Items")
        self.left_center_title.pack(side='top', fill='none',
                                    padx=2, pady=2, expand=True)
        # Checks
        self.left_checks = tk.Frame(self.left_center, bg='orange')
        self.left_checks.pack(side='left', anchor='w', fill='none',
                              padx=2, pady=2, expand=True)
        # Option menus
        self.left_optionmenu = tk.Frame(self.left_center, bg='yellow')
        self.left_optionmenu.pack(side='left', anchor='w', fill='none',
                                  padx=2, pady=2, expand=True)
        
        # ----- Right -----
        self.right_center = tk.Frame(self.center_frame, bg='pink')
        self.right_center.pack(side='right', anchor='e', fill='none',
                               padx=2, pady=2, expand=True)
        # Title
        self.right_center_title = tk.Label(self.right_center, text="Skills")
        self.right_center_title.pack(side='top', fill='none',
                                     padx=2, pady=2, expand=True)
        # Checks
        self.right_checks = tk.Frame(self.right_center, bg='orange')
        self.right_checks.pack(side='left', anchor='w', fill='none',
                               padx=2, pady=2, expand=True)
        # Option menus
        self.right_optionmenu = tk.Frame(self.right_center, bg='yellow')
        self.right_optionmenu.pack(side='left', anchor='w', fill='none',
                                   padx=2, pady=2, expand=True)
        
    def _create_labels(self):
        """Create the labels of the window"""
        # ---------- Top frame ----------
        # ----- Weapon -----
        self.raw_label = tk.Label(self.wpn_labels, text="Raw: ")
        self.raw_label.pack(anchor='w', padx=3, pady=3)

        self.elem_label = tk.Label(self.wpn_labels, text="Element: ")
        self.elem_label.pack(anchor='w', padx=3, pady=3)

        self.crit_label = tk.Label(self.wpn_labels, text="Affinity: ")
        self.crit_label.pack(anchor='w', padx=3, pady=3)

        self.sharp_label = tk.Label(self.wpn_labels, text="Sharpness: ")
        self.sharp_label.pack(anchor='w', padx=3, pady=3)

        # ----- Other -----
        self.mv_label = tk.Label(self.other_labels, text="Motion value: ")
        self.mv_label.pack(anchor='w', padx=3, pady=3)

        self.hzv_label = tk.Label(self.other_labels, text="Hitzone: ")
        self.hzv_label.pack(anchor='w', padx=3, pady=3)

        self.ehzv_label = tk.Label(self.other_labels, text="Elem. hitzone: ")
        self.ehzv_label.pack(anchor='w', padx=3, pady=3)        

    def _create_entries(self):
        """Create the entries of the window"""
        # ---------- Weapon ----------
        self.raw_entry = tk.Entry(self.wpn_entries, width=8, justify='center',
                                  textvariable=self.raw)
        self.raw_entry.pack(anchor='w', padx=3, pady=4)

        self.elem_entry = tk.Entry(self.wpn_entries, width=8, justify='center',
                                   textvariable=self.elem)
        self.elem_entry.pack(anchor='w', padx=3, pady=4)

        self.crit_entry = tk.Entry(self.wpn_entries, width=8, justify='center',
                                   textvariable=self.crit)
        self.crit_entry.pack(anchor='w', padx=3, pady=4)

        self.sharp_entry = tk.Entry(self.wpn_entries, width=8, justify='center',
                                    textvariable=self.sharp)
        self.sharp_entry.pack(anchor='w', padx=3, pady=4)

        # ---------- Other ----------
        self.mv_entry = tk.Entry(self.other_entries, width=8, justify='center',
                                 textvariable=self.mv)
        self.mv_entry.pack(anchor='w', padx=3, pady=4)

        self.hzv_entry = tk.Entry(self.other_entries, width=8, justify='center',
                                  textvariable=self.hzv)
        self.hzv_entry.pack(anchor='w', padx=3, pady=4)

        self.ehzv_entry = tk.Entry(self.other_entries, width=8,
                                   justify='center', textvariable=self.ehzv)
        self.ehzv_entry.pack(anchor='w', padx=3, pady=4)

    def _create_optionmenu(self):
        """Create the option menus of the window"""
        # Critical boost
        self.crit_boost_menu = tk.OptionMenu(self.right_optionmenu,
            self.skills.crit_boost_lvl_n, *self.skills.crit_boost_lvl)
        self.crit_boost_menu.config(state='disabled')
        self.crit_boost_menu.pack(anchor='w', padx=3, pady=2)

        # Critical element
        self.crit_elem_menu = tk.OptionMenu(self.right_optionmenu,
            self.skills.crit_elem_lvl_n, *self.skills.crit_elem_lvl)
        self.crit_elem_menu.config(state='disabled')
        self.crit_elem_menu.pack(anchor='w', padx=3, pady=2)

    def _create_checkboxes(self):
        """Create the checkboxes of the window"""
        # ----- Items -----
        # Powercharm
        self.powercharm_check = tk.Checkbutton(self.left_checks,
            text='Powercharm', variable=self.items.powercharm,
            onvalue=1, offvalue=0)
        self.powercharm_check.pack(anchor='w', padx=3, pady=3)

        # Powertalon
        self.powertalon_check = tk.Checkbutton(self.left_checks,
            text='Powertalon', variable=self.items.powertalon,
            onvalue=1, offvalue=0)
        self.powertalon_check.pack(anchor='w', padx=3, pady=3)

        # Might Seed
        self.might_seed_check = tk.Checkbutton(self.left_checks,
            text='Might Seed', variable=self.items.might_seed,
            onvalue=1, offvalue=0)
        self.might_seed_check.pack(anchor='w', padx=3, pady=3)

        # Demon Powder
        self.demon_powder_check = tk.Checkbutton(self.left_checks,
            text='Demon Powder', variable=self.items.demon_powder,
            onvalue=1, offvalue=0)
        self.demon_powder_check.pack(anchor='w', padx=3, pady=3)

        # Demondrug
        self.demondrug_check = tk.Checkbutton(self.left_checks,
            text='Demondrug', variable=self.items.demondrug,
            onvalue=1, offvalue=0, state='active')
        self.demondrug_check.config(command=lambda:self._mutually_ex(
                                                    self.items.demondrug,
                                                    self.mega_demondrug_check))
        self.demondrug_check.pack(anchor='w', padx=3, pady=3)

        # Mega Demondrug
        self.mega_demondrug_check = tk.Checkbutton(self.left_checks,
            text='Mega Demondrug', variable=self.items.mega_demondrug,
            onvalue=1, offvalue=0, state='active')
        self.mega_demondrug_check.config(command=lambda:self._mutually_ex(
                                                    self.items.mega_demondrug,
                                                    self.demondrug_check))
        self.mega_demondrug_check.pack(anchor='w', padx=3, pady=3)

        # ----- Skills -----
        # Critical boost
        self.crit_boost_check = tk.Checkbutton(self.right_checks,
            text='Critical Boost', variable=self.skills.crit_boost,
            onvalue=1, offvalue=0)
        self.crit_boost_check.config(command=lambda:self._switch_state(
                                                    self.skills.crit_boost,
                                                    self.crit_boost_menu))
        self.crit_boost_check.pack(anchor='w', padx=3, pady=3)

        # Critical element
        self.crit_elem_check = tk.Checkbutton(self.right_checks,
            text='Critical Element', variable=self.skills.crit_elem,
            onvalue=1, offvalue=0)
        self.crit_elem_check.config(command=lambda:self._switch_state(
                                                    self.skills.crit_elem,
                                                    self.crit_elem_menu))
        self.crit_elem_check.pack(anchor='w', padx=3, pady=4)

    def _switch_state(self, flag, menu):
        """Switch the state of the selected item"""
        check = flag.get()
        if check == 1:
            menu['state'] = 'active'
        else:
            menu['state'] = 'disabled'

    def _mutually_ex(self, flag, menu):
        """Check for mutually exclusive items"""
        check = flag.get()
        if check == 1:
            menu['state'] = 'disabled'
        else:
            menu['state'] = 'active'

# -----------------------------------------------------------------------------
# ------------------------------- CALCULATIONS --------------------------------
# -----------------------------------------------------------------------------

    def _calculate(self):
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