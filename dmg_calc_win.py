import tkinter as tk

from get_values import GetValues
from dmg_calc import DamageCalc
from items import Items
from skills import Skills

class DamageCalcWin():
    """Class that manage the damage calc window"""

    def __init__(self, root):
        """Initialize the class"""
        self.root = root
        self.items = Items()
        self.skills = Skills()
        #self.wpn_stats = dict.fromkeys(['raw', 'elem', 'crit', 'sharp'])
        #self.other_stats = dict.fromkeys(['mv', 'hzv', 'ehzv'])

        # Weapon variables
        self.raw = tk.IntVar()
        self.raw.set(300)
        self.elem = tk.IntVar()
        self.elem.set(100)
        self.crit = tk.IntVar()
        self.crit.set(30)
        self.sharp = tk.StringVar()
        self.sharp.set('White')
        # Other variables
        self.mv = tk.DoubleVar()
        self.mv.set(50)
        self.hzv = tk.DoubleVar()
        self.hzv.set(45)
        self.ehzv = tk.DoubleVar()
        self.ehzv.set(30)

        self.root.title("MH Damage Calculator")
        
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
        # Title
        self.top_title = tk.Label(self.top_frame, text="Weapon")
        self.top_title.pack(side='top', fill='none',
                            padx=2, pady=2, expand=True)
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

# -----------------------------------------------------------------------------
# -------------------------------- OPTIONMENU ---------------------------------
# -----------------------------------------------------------------------------

    def _create_optionmenu(self):
        """Create the option menus of the window"""
        # Attack boost
        self.atk_boost_menu = tk.OptionMenu(self.right_optionmenu,
            self.skills.atk_boost_lvl, *self.skills.lvl_list_7)
        self.atk_boost_menu.config(state='disabled')
        self.atk_boost_menu.pack(anchor='w', padx=3, pady=1)

        # Agitator
        self.agitator_menu = tk.OptionMenu(self.right_optionmenu,
            self.skills.agitator_lvl, *self.skills.lvl_list_5)
        self.agitator_menu.config(state='disabled')
        self.agitator_menu.pack(anchor='w', padx=3, pady=1)

        # Elem attack
        self.elem_atk_menu = tk.OptionMenu(self.right_optionmenu,
            self.skills.elem_atk_lvl, *self.skills.lvl_list_5)
        self.elem_atk_menu.config(state='disabled')
        self.elem_atk_menu.pack(anchor='w', padx=3, pady=1)

        # Critical eye
        self.crit_eye_menu = tk.OptionMenu(self.right_optionmenu,
            self.skills.crit_eye_lvl, *self.skills.lvl_list_7)
        self.crit_eye_menu.config(state='disabled')
        self.crit_eye_menu.pack(anchor='w', padx=3, pady=1)

        # Critical boost
        self.crit_boost_menu = tk.OptionMenu(self.right_optionmenu,
            self.skills.crit_boost_lvl, *self.skills.lvl_list_3)
        self.crit_boost_menu.config(state='disabled')
        self.crit_boost_menu.pack(anchor='w', padx=3, pady=1)

        # Critical element
        self.crit_elem_menu = tk.OptionMenu(self.right_optionmenu,
            self.skills.crit_elem_lvl, *self.skills.lvl_list_3)
        self.crit_elem_menu.config(state='disabled')
        self.crit_elem_menu.pack(anchor='w', padx=3, pady=1)

# -----------------------------------------------------------------------------
# -------------------------------- CHECKBOXES ---------------------------------
# -----------------------------------------------------------------------------

    def _create_checkboxes(self):
        """Create the checkboxes of the window"""

# -------------------------------- ITEMS --------------------------------------
        
        # Powercharm
        self.powercharm_check = tk.Checkbutton(self.left_checks,
            text='Powercharm', variable=self.items.powercharm,
            onvalue=1, offvalue=0)
        self.powercharm_check.pack(anchor='w', padx=3, pady=4)

        # Powertalon
        self.powertalon_check = tk.Checkbutton(self.left_checks,
            text='Powertalon', variable=self.items.powertalon,
            onvalue=1, offvalue=0)
        self.powertalon_check.pack(anchor='w', padx=3, pady=4)

        # Might Seed
        self.might_seed_check = tk.Checkbutton(self.left_checks,
            text='Might Seed', variable=self.items.might_seed,
            onvalue=1, offvalue=0)
        self.might_seed_check.pack(anchor='w', padx=3, pady=4)

        # Demon Powder
        self.demon_powder_check = tk.Checkbutton(self.left_checks,
            text='Demon Powder', variable=self.items.demon_powder,
            onvalue=1, offvalue=0)
        self.demon_powder_check.pack(anchor='w', padx=3, pady=4)

        # Demondrug
        self.demondrug_check = tk.Checkbutton(self.left_checks,
            text='Demondrug', variable=self.items.demondrug,
            onvalue=1, offvalue=0, state='active')
        self.demondrug_check.config(command=lambda:self._mutually_ex(
                                                    self.items.demondrug,
                                                    self.mega_demondrug_check))
        self.demondrug_check.pack(anchor='w', padx=3, pady=4)

        # Mega Demondrug
        self.mega_demondrug_check = tk.Checkbutton(self.left_checks,
            text='Mega Demondrug', variable=self.items.mega_demondrug,
            onvalue=1, offvalue=0, state='active')
        self.mega_demondrug_check.config(command=lambda:self._mutually_ex(
                                                    self.items.mega_demondrug,
                                                    self.demondrug_check))
        self.mega_demondrug_check.pack(anchor='w', padx=3, pady=4)

# ---------------------------------- SKILLS -----------------------------------

        # Attack boost
        self.atk_boost_check = tk.Checkbutton(self.right_checks,
            text='Attack Boost', variable=self.skills.atk_boost,
            onvalue=1, offvalue=0)
        self.atk_boost_check.config(command=lambda:self._switch_state(
                                                    self.skills.atk_boost,
                                                    self.atk_boost_menu))
        self.atk_boost_check.pack(anchor='w', padx=3, pady=4)

        # Agitator
        self.agitator_check = tk.Checkbutton(self.right_checks,
            text='Agitator', variable=self.skills.agitator,
            onvalue=1, offvalue=0)
        self.agitator_check.config(command=lambda:self._switch_state(
                                                    self.skills.agitator,
                                                    self.agitator_menu))
        self.agitator_check.pack(anchor='w', padx=3, pady=4)

        # Elem attack
        self.elem_atk_check = tk.Checkbutton(self.right_checks,
            text='Elem Attack', variable=self.skills.elem_atk,
            onvalue=1, offvalue=0)
        self.elem_atk_check.config(command=lambda:self._switch_state(
                                                    self.skills.elem_atk,
                                                    self.elem_atk_menu))
        self.elem_atk_check.pack(anchor='w', padx=3, pady=4)

        # Critical eye
        self.crit_eye_check = tk.Checkbutton(self.right_checks,
            text='Critical Eye', variable=self.skills.crit_eye,
            onvalue=1, offvalue=0)
        self.crit_eye_check.config(command=lambda:self._switch_state(
                                                    self.skills.crit_eye,
                                                    self.crit_eye_menu))
        self.crit_eye_check.pack(anchor='w', padx=3, pady=4)

        # Critical boost
        self.crit_boost_check = tk.Checkbutton(self.right_checks,
            text='Critical Boost', variable=self.skills.crit_boost,
            onvalue=1, offvalue=0)
        self.crit_boost_check.config(command=lambda:self._switch_state(
                                                    self.skills.crit_boost,
                                                    self.crit_boost_menu))
        self.crit_boost_check.pack(anchor='w', padx=3, pady=4)

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

    def _calculate(self):
        """Call the necessary functions to calculate the damage"""
        # Check for a previous output and delete it if present.
        try:
            self.output_label.destroy()
        except AttributeError:
            pass
        self.get_values = GetValues(self)
        self.get_values.get_values()
        self.calc = DamageCalc(self.get_values)
        self.calc.do_calcs()
        self._show_results()

    def _show_results(self):
        """Print the results"""
        self.output_label = tk.Label(self.bot_frame, justify='left',
            text=f"Displayed attack: {self.calc.display_atk}\n"
                 f"Displayed element: {self.calc.display_elem}\n"
                 f"Affinity: {self.calc.final_crit}\n\n"
                 f"Effective raw: {self.calc.eff_raw}\n"
                 f"Effective element: {self.calc.eff_elem}\n\n"
                 f"Total damage: {self.calc.tot_dmg}\n"
                 f"If crit: {self.calc.phys_crit_dmg + self.calc.elem_crit_dmg}"
                 f"\n\nPhysical: {self.calc.phys_dmg}\n"
                 f"If crit: {self.calc.phys_crit_dmg}\n\n"
                 f"Elemental: {self.calc.elem_dmg}\n"
                 f"If crit: {self.calc.elem_crit_dmg}")
        self.output_label.pack(side='bottom')