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
        self._calculate()

        self.calc_btn = tk.Button(self.center_frame, width=30, text='Calculate',
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

        self.center_frame = tk.Frame(self.canvas, bg='pink')
        self.center_frame.pack(side='top', fill='both', padx=5, pady=0,
                               expand=True)

        self.bot_frame = tk.Frame(self.canvas, bg='red')
        self.bot_frame.pack(side='top', fill='both', padx=5, pady=5,
                            expand=True)

    def _create_sub_frames(self):
        """Create the subframes of the window"""
        # ---------- Top frame ----------
        # ----- Weapon -----
        # Weapon frame
        self.wpn_frame = tk.Frame(self.top_frame,bg='green')
        self.wpn_frame.pack(side='left', anchor='w', fill='none',
                             padx=2, pady=2, expand=True)
        # Title
        self.top_title = tk.Label(self.wpn_frame, text="Weapon")
        self.top_title.pack(side='top', fill='none',
                            padx=2, pady=2, expand=True)
        # Labels
        self.wpn_labels = tk.Frame(self.wpn_frame,bg='blue')
        self.wpn_labels.pack(side='left', anchor='w', fill='none',
                             padx=2, pady=2, expand=True)
        # Entries
        self.wpn_entries = tk.Frame(self.wpn_frame, bg='blue')
        self.wpn_entries.pack(side='left', anchor='w', fill='none',
                              padx=2, pady=2, expand=True)
        
        # ----- Other -----
        # Labels
        self.other_labels = tk.Frame(self.wpn_frame, bg='blue')
        self.other_labels.pack(side='left', anchor='w', fill='none',
                               padx=2, pady=2, expand=True)
        # Entries
        self.other_entries = tk.Frame(self.wpn_frame, bg='blue')
        self.other_entries.pack(side='left', anchor='w', fill='none',
                                padx=2, pady=2, expand=True)
        
        # ----- Results -----
        # Frame
        self.output_frame = tk.Frame(self.top_frame, bg='green')
        self.output_frame.pack(side='left', anchor='w', fill='none',
                              padx=5, pady=5, expand=True)
        # Title
        self.output_title = tk.Label(self.output_frame, text="Results")
        self.output_title.pack(side='top', fill='none',
                            padx=2, pady=2, expand=True)
        
        # ----- Options -----
        # Frame
        self.options_frame = tk.Frame(self.top_frame, bg='green')
        self.options_frame.pack(side='left', anchor='w', fill='none',
                              padx=5, pady=5, expand=True)
        # Title
        self.options_title = tk.Label(self.options_frame, text="Options")
        self.options_title.pack(side='top', fill='none',
                            padx=2, pady=2, expand=True)
        
        # ---------- Bottom frame ----------
        # ----- Left -----
        self.left_center = tk.Frame(self.bot_frame, bg='pink')
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
        self.right_center = tk.Frame(self.bot_frame, bg='pink')
        self.right_center.pack(side='right', anchor='e', fill='none',
                               padx=2, pady=2, expand=True)
        # Title
        self.right_center_title = tk.Label(self.right_center, text="Skills")
        self.right_center_title.pack(side='top', fill='none',
                                     padx=2, pady=2, expand=True)
        # Checks 1 
        self.right_checks_1 = tk.Frame(self.right_center, bg='orange')
        self.right_checks_1.pack(side='left', anchor='w', fill='none',
                               padx=2, pady=2, expand=True)
        # Option menus 1
        self.right_optionmenu_1 = tk.Frame(self.right_center, bg='yellow')
        self.right_optionmenu_1.pack(side='left', anchor='w', fill='none',
                                   padx=2, pady=2, expand=True)
        # Checks 2
        self.right_checks_2 = tk.Frame(self.right_center, bg='orange')
        self.right_checks_2.pack(side='left', anchor='w', fill='none',
                               padx=2, pady=2, expand=True)
        # Option menus 2
        self.right_optionmenu_2 = tk.Frame(self.right_center, bg='yellow')
        self.right_optionmenu_2.pack(side='left', anchor='w', fill='none',
                                   padx=2, pady=2, expand=True)
        # Checks 3
        self.right_checks_3 = tk.Frame(self.right_center, bg='orange')
        self.right_checks_3.pack(side='left', anchor='w', fill='none',
                               padx=2, pady=2, expand=True)
        # Option menus 3
        self.right_optionmenu_3 = tk.Frame(self.right_center, bg='yellow')
        self.right_optionmenu_3.pack(side='left', anchor='w', fill='none',
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
        # ---------------------------------------------------------------------
        # Attack boost
        self.atk_boost_menu = tk.OptionMenu(self.right_optionmenu_1,
            self.skills.atk_boost_lvl, *self.skills.lvl_list_7)
        self.atk_boost_menu.config(state='disabled')
        self.atk_boost_menu.pack(anchor='w', padx=3, pady=1)

        # Agitator
        self.agitator_menu = tk.OptionMenu(self.right_optionmenu_1,
            self.skills.agitator_lvl, *self.skills.lvl_list_5)
        self.agitator_menu.config(state='disabled')
        self.agitator_menu.pack(anchor='w', padx=3, pady=1)

        # Peak performance
        self.peak_perf_menu = tk.OptionMenu(self.right_optionmenu_1,
            self.skills.peak_perf_lvl, *self.skills.lvl_list_3)
        self.peak_perf_menu.config(state='disabled')
        self.peak_perf_menu.pack(anchor='w', padx=3, pady=1)

        # Resentment
        self.resentment_menu = tk.OptionMenu(self.right_optionmenu_1,
            self.skills.resentment_lvl, *self.skills.lvl_list_5)
        self.resentment_menu.config(state='disabled')
        self.resentment_menu.pack(anchor='w', padx=3, pady=1)

        # Resuscitate
        self.resuscitate_menu = tk.OptionMenu(self.right_optionmenu_1,
            self.skills.resuscitate_lvl, *self.skills.lvl_list_3)
        self.resuscitate_menu.config(state='disabled')
        self.resuscitate_menu.pack(anchor='w', padx=3, pady=1)

        # Buildup boost
        self.bu_boost_menu = tk.OptionMenu(self.right_optionmenu_1,
            self.skills.bu_boost_lvl, *self.skills.lvl_list_3)
        self.bu_boost_menu.config(state='disabled')
        self.bu_boost_menu.pack(anchor='w', padx=3, pady=1)

        # Foray
        self.foray_menu = tk.OptionMenu(self.right_optionmenu_1,
            self.skills.foray_lvl, *self.skills.lvl_list_3)
        self.foray_menu.config(state='disabled')
        self.foray_menu.pack(anchor='w', padx=3, pady=1)

        # Counterstrike
        self.counterstrike_menu = tk.OptionMenu(self.right_optionmenu_1,
            self.skills.counterstrike_lvl, *self.skills.lvl_list_3)
        self.counterstrike_menu.config(state='disabled')
        self.counterstrike_menu.pack(anchor='w', padx=3, pady=1)

        # Offensive guard
        self.off_guard_menu = tk.OptionMenu(self.right_optionmenu_1,
            self.skills.off_guard_lvl, *self.skills.lvl_list_3)
        self.off_guard_menu.config(state='disabled')
        self.off_guard_menu.pack(anchor='w', padx=3, pady=1)

        # Heroics
        self.heroics_menu = tk.OptionMenu(self.right_optionmenu_1,
            self.skills.heroics_lvl, *self.skills.lvl_list_5)
        self.heroics_menu.config(state='disabled')
        self.heroics_menu.pack(anchor='w', padx=3, pady=1)

        # Fortify
        self.fortify_menu = tk.OptionMenu(self.right_optionmenu_1,
            self.skills.fortify_lvl, *self.skills.lvl_list_2)
        self.fortify_menu.config(state='disabled')
        self.fortify_menu.pack(anchor='w', padx=3, pady=1)

        # ---------------------------------------------------------------------

        # Elem attack
        self.elem_atk_menu = tk.OptionMenu(self.right_optionmenu_2,
            self.skills.elem_atk_lvl, *self.skills.lvl_list_5)
        self.elem_atk_menu.config(state='disabled')
        self.elem_atk_menu.pack(anchor='w', padx=3, pady=1)

        # Element exploit
        self.elem_ex_menu = tk.OptionMenu(self.right_optionmenu_2,
            self.skills.elem_ex_lvl, *self.skills.lvl_list_3)
        self.elem_ex_menu.config(state='disabled')
        self.elem_ex_menu.pack(anchor='w', padx=3, pady=1)

        # Burst
        self.burst_menu = tk.OptionMenu(self.right_optionmenu_2,
            self.skills.burst_lvl, *self.skills.lvl_list_3)
        self.burst_menu.config(state='disabled')
        self.burst_menu.pack(anchor='w', padx=3, pady=1)

        # Coalescence
        self.coalescence_menu = tk.OptionMenu(self.right_optionmenu_2,
            self.skills.coalescence_lvl, *self.skills.lvl_list_3)
        self.coalescence_menu.config(state='disabled')
        self.coalescence_menu.pack(anchor='w', padx=3, pady=1)

        # Bloodlust
        self.bloodlust_menu = tk.OptionMenu(self.right_optionmenu_2,
            self.skills.bloodlust_lvl, *self.skills.lvl_list_3)
        self.bloodlust_menu.config(state='disabled')
        self.bloodlust_menu.pack(anchor='w', padx=3, pady=1)

        # Mail of hellfire
        self.mail_hellfire_menu = tk.OptionMenu(self.right_optionmenu_2,
            self.skills.mail_hellfire_lvl, *self.skills.lvl_list_3)
        self.mail_hellfire_menu.config(state='disabled')
        self.mail_hellfire_menu.pack(anchor='w', padx=3, pady=1)

        # ---------------------------------------------------------------------

        # Critical eye
        self.crit_eye_menu = tk.OptionMenu(self.right_optionmenu_3,
            self.skills.crit_eye_lvl, *self.skills.lvl_list_7)
        self.crit_eye_menu.config(state='disabled')
        self.crit_eye_menu.pack(anchor='w', padx=3, pady=1)

        # Critical boost
        self.crit_boost_menu = tk.OptionMenu(self.right_optionmenu_3,
            self.skills.crit_boost_lvl, *self.skills.lvl_list_3)
        self.crit_boost_menu.config(state='disabled')
        self.crit_boost_menu.pack(anchor='w', padx=3, pady=1)

        # Critical element
        self.crit_elem_menu = tk.OptionMenu(self.right_optionmenu_3,
            self.skills.crit_elem_lvl, *self.skills.lvl_list_3)
        self.crit_elem_menu.config(state='disabled')
        self.crit_elem_menu.pack(anchor='w', padx=3, pady=1)

        # Critical draw
        self.crit_draw_menu = tk.OptionMenu(self.right_optionmenu_3,
            self.skills.crit_draw_lvl, *self.skills.lvl_list_3)
        self.crit_draw_menu.config(state='disabled')
        self.crit_draw_menu.pack(anchor='w', padx=3, pady=1)

        # Latent power
        self.latent_power_menu = tk.OptionMenu(self.right_optionmenu_3,
            self.skills.latent_power_lvl, *self.skills.lvl_list_5)
        self.latent_power_menu.config(state='disabled')
        self.latent_power_menu.pack(anchor='w', padx=3, pady=1)

        # Maximum might
        self.max_might_menu = tk.OptionMenu(self.right_optionmenu_3,
            self.skills.max_might_lvl, *self.skills.lvl_list_3)
        self.max_might_menu.config(state='disabled')
        self.max_might_menu.pack(anchor='w', padx=3, pady=1)

        # Weakness exploit
        self.weak_ex_menu = tk.OptionMenu(self.right_optionmenu_3,
            self.skills.weak_ex_lvl, *self.skills.lvl_list_3)
        self.weak_ex_menu.config(state='disabled')
        self.weak_ex_menu.pack(anchor='w', padx=3, pady=1)

# -----------------------------------------------------------------------------
# -------------------------------- CHECKBOXES ---------------------------------
# -----------------------------------------------------------------------------

    def _create_checkboxes(self):
        """Create the checkboxes of the window"""

# ------------------------------- OPTIONS -------------------------------------

        # Scroll change
        self.scroll_check = tk.Checkbutton(self.options_frame,
            text='Use Blue Scroll', variable=self.items.scroll_color,
            onvalue=1, offvalue=0)
        self.scroll_check.pack(anchor='w', padx=3, pady=4)

        # Frenzy
        self.frenzy_check = tk.Checkbutton(self.options_frame,
            text='Beaten Frenzy', variable=self.items.beaten_frenzy,
            onvalue=1, offvalue=0)
        self.frenzy_check.pack(anchor='w', padx=3, pady=4)

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
        self.atk_boost_check = tk.Checkbutton(self.right_checks_1,
            text='Attack Boost', variable=self.skills.atk_boost,
            onvalue=1, offvalue=0)
        self.atk_boost_check.config(command=lambda:self._switch_state(
                                                    self.skills.atk_boost,
                                                    self.atk_boost_menu))
        self.atk_boost_check.pack(anchor='w', padx=3, pady=4)

        # Agitator
        self.agitator_check = tk.Checkbutton(self.right_checks_1,
            text='Agitator', variable=self.skills.agitator,
            onvalue=1, offvalue=0)
        self.agitator_check.config(command=lambda:self._switch_state(
                                                    self.skills.agitator,
                                                    self.agitator_menu))
        self.agitator_check.pack(anchor='w', padx=3, pady=4)

        # Peak performance
        self.peak_perf_check = tk.Checkbutton(self.right_checks_1,
            text='Peak Performance', variable=self.skills.peak_perf,
            onvalue=1, offvalue=0)
        self.peak_perf_check.config(command=lambda:self._switch_state(
                                                    self.skills.peak_perf,
                                                    self.peak_perf_menu))
        self.peak_perf_check.pack(anchor='w', padx=3, pady=4)

        # Resentment
        self.resentment_check = tk.Checkbutton(self.right_checks_1,
            text='Resentment', variable=self.skills.resentment,
            onvalue=1, offvalue=0)
        self.resentment_check.config(command=lambda:self._switch_state(
                                                    self.skills.resentment,
                                                    self.resentment_menu))
        self.resentment_check.pack(anchor='w', padx=3, pady=4)

        # Resuscitate
        self.resuscitate_check = tk.Checkbutton(self.right_checks_1,
            text='Resuscitate', variable=self.skills.resuscitate,
            onvalue=1, offvalue=0)
        self.resuscitate_check.config(command=lambda:self._switch_state(
                                                    self.skills.resuscitate,
                                                    self.resuscitate_menu))
        self.resuscitate_check.pack(anchor='w', padx=3, pady=4)

        # Buildup boost
        self.bu_boost_check = tk.Checkbutton(self.right_checks_1,
            text='Buildup Boost', variable=self.skills.bu_boost,
            onvalue=1, offvalue=0)
        self.bu_boost_check.config(command=lambda:self._switch_state(
                                                    self.skills.bu_boost,
                                                    self.bu_boost_menu))
        self.bu_boost_check.pack(anchor='w', padx=3, pady=4)

        # Foray
        self.foray_check = tk.Checkbutton(self.right_checks_1,
            text='Foray', variable=self.skills.foray,
            onvalue=1, offvalue=0)
        self.foray_check.config(command=lambda:self._switch_state(
                                                    self.skills.foray,
                                                    self.foray_menu))
        self.foray_check.pack(anchor='w', padx=3, pady=4)

        # Counterstrike
        self.counterstrike_check = tk.Checkbutton(self.right_checks_1,
            text='Counterstrike', variable=self.skills.counterstrike,
            onvalue=1, offvalue=0)
        self.counterstrike_check.config(command=lambda:self._switch_state(
                                                    self.skills.counterstrike,
                                                    self.counterstrike_menu))
        self.counterstrike_check.pack(anchor='w', padx=3, pady=4)

        # Offensive guard
        self.off_guard_check = tk.Checkbutton(self.right_checks_1,
            text='Offensive Guard', variable=self.skills.off_guard,
            onvalue=1, offvalue=0)
        self.off_guard_check.config(command=lambda:self._switch_state(
                                                    self.skills.off_guard,
                                                    self.off_guard_menu))
        self.off_guard_check.pack(anchor='w', padx=3, pady=4)

        # Heroics
        self.heroics_check = tk.Checkbutton(self.right_checks_1,
            text='Heroics', variable=self.skills.heroics,
            onvalue=1, offvalue=0)
        self.heroics_check.config(command=lambda:self._switch_state(
                                                    self.skills.heroics,
                                                    self.heroics_menu))
        self.heroics_check.pack(anchor='w', padx=3, pady=4)

        # Fortify
        self.fortify_check = tk.Checkbutton(self.right_checks_1,
            text='Fortify (N° of carts)', variable=self.skills.fortify,
            onvalue=1, offvalue=0)
        self.fortify_check.config(command=lambda:self._switch_state(
                                                    self.skills.fortify,
                                                    self.fortify_menu))
        self.fortify_check.pack(anchor='w', padx=3, pady=4)
        
        # ---------------------------------------------------------------------

        # Elem attack
        self.elem_atk_check = tk.Checkbutton(self.right_checks_2,
            text='Elem Attack', variable=self.skills.elem_atk,
            onvalue=1, offvalue=0)
        self.elem_atk_check.config(command=lambda:self._switch_state(
                                                    self.skills.elem_atk,
                                                    self.elem_atk_menu))
        self.elem_atk_check.pack(anchor='w', padx=3, pady=4)

        # Element exploit
        self.elem_ex_check = tk.Checkbutton(self.right_checks_2,
            text='Element Exploit', variable=self.skills.elem_ex,
            onvalue=1, offvalue=0)
        self.elem_ex_check.config(command=lambda:self._switch_state(
                                                    self.skills.elem_ex,
                                                    self.elem_ex_menu))
        self.elem_ex_check.pack(anchor='w', padx=3, pady=4)

        # Burst
        self.burst_check = tk.Checkbutton(self.right_checks_2,
            text='Burst', variable=self.skills.burst,
            onvalue=1, offvalue=0)
        self.burst_check.config(command=lambda:self._switch_state(
                                                    self.skills.burst,
                                                    self.burst_menu))
        self.burst_check.pack(anchor='w', padx=3, pady=4)

        # Coalescence
        self.coalescence_check = tk.Checkbutton(self.right_checks_2,
            text='Coalescence', variable=self.skills.coalescence,
            onvalue=1, offvalue=0)
        self.coalescence_check.config(command=lambda:self._switch_state(
                                                    self.skills.coalescence,
                                                    self.coalescence_menu))
        self.coalescence_check.pack(anchor='w', padx=3, pady=4)

        # Bloodlust
        self.bloodlust_check = tk.Checkbutton(self.right_checks_2,
            text='Bloodlust', variable=self.skills.bloodlust,
            onvalue=1, offvalue=0)
        self.bloodlust_check.config(command=lambda:self._switch_state(
                                                    self.skills.bloodlust,
                                                    self.bloodlust_menu))
        self.bloodlust_check.pack(anchor='w', padx=3, pady=4)

        # Mail of hellfire
        self.mail_hellfire_check = tk.Checkbutton(self.right_checks_2,
            text='Mail of Hellfire', variable=self.skills.mail_hellfire,
            onvalue=1, offvalue=0)
        self.mail_hellfire_check.config(command=lambda:self._switch_state(
                                                    self.skills.mail_hellfire,
                                                    self.mail_hellfire_menu))
        self.mail_hellfire_check.pack(anchor='w', padx=3, pady=4)

        # ---------------------------------------------------------------------

        # Critical eye
        self.crit_eye_check = tk.Checkbutton(self.right_checks_3,
            text='Critical Eye', variable=self.skills.crit_eye,
            onvalue=1, offvalue=0)
        self.crit_eye_check.config(command=lambda:self._switch_state(
                                                    self.skills.crit_eye,
                                                    self.crit_eye_menu))
        self.crit_eye_check.pack(anchor='w', padx=3, pady=4)

        # Critical boost
        self.crit_boost_check = tk.Checkbutton(self.right_checks_3,
            text='Critical Boost', variable=self.skills.crit_boost,
            onvalue=1, offvalue=0)
        self.crit_boost_check.config(command=lambda:self._switch_state(
                                                    self.skills.crit_boost,
                                                    self.crit_boost_menu))
        self.crit_boost_check.pack(anchor='w', padx=3, pady=4)

        # Critical element
        self.crit_elem_check = tk.Checkbutton(self.right_checks_3,
            text='Critical Element', variable=self.skills.crit_elem,
            onvalue=1, offvalue=0)
        self.crit_elem_check.config(command=lambda:self._switch_state(
                                                    self.skills.crit_elem,
                                                    self.crit_elem_menu))
        self.crit_elem_check.pack(anchor='w', padx=3, pady=4)

        # Critical draw
        self.crit_draw_check = tk.Checkbutton(self.right_checks_3,
            text='Critical Draw', variable=self.skills.crit_draw,
            onvalue=1, offvalue=0)
        self.crit_draw_check.config(command=lambda:self._switch_state(
                                                    self.skills.crit_draw,
                                                    self.crit_draw_menu))
        self.crit_draw_check.pack(anchor='w', padx=3, pady=4)

        # Latent power
        self.latent_power_check = tk.Checkbutton(self.right_checks_3,
            text='Latent Power', variable=self.skills.latent_power,
            onvalue=1, offvalue=0)
        self.latent_power_check.config(command=lambda:self._switch_state(
                                                    self.skills.latent_power,
                                                    self.latent_power_menu))
        self.latent_power_check.pack(anchor='w', padx=3, pady=4)

        # Maximum might
        self.max_might_check = tk.Checkbutton(self.right_checks_3,
            text='Maximum Might', variable=self.skills.max_might,
            onvalue=1, offvalue=0)
        self.max_might_check.config(command=lambda:self._switch_state(
                                                    self.skills.max_might,
                                                    self.max_might_menu))
        self.max_might_check.pack(anchor='w', padx=3, pady=4)

        # Weakness exploit
        self.weak_ex_check = tk.Checkbutton(self.right_checks_3,
            text='Weakness Exploit', variable=self.skills.weak_ex,
            onvalue=1, offvalue=0)
        self.weak_ex_check.config(command=lambda:self._switch_state(
                                                    self.skills.weak_ex,
                                                    self.weak_ex_menu))
        self.weak_ex_check.pack(anchor='w', padx=3, pady=4)

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
            self.output_label_1.destroy()
            self.output_label_2.destroy()
        except AttributeError:
            pass
        self.get_values = GetValues(self)
        self.get_values.get_values()
        self.calc = DamageCalc(self.get_values)
        self.calc.do_calcs()
        self._show_results()

    def _show_results(self):
        """Print the results"""
        self.output_label_1 = tk.Label(self.output_frame, justify='left',
            text=f"Displayed attack: {self.calc.display_atk}\n"
                 f"Displayed element: {self.calc.display_elem}\n\n"
                 f"Affinity: {self.calc.final_crit}\n\n\n"
                 f"Effective raw: {self.calc.eff_raw}\n"
                 f"Effective element: {self.calc.eff_elem}")
        self.output_label_1.pack(side='left', padx=3, pady=3)

        self.output_label_2 = tk.Label(self.output_frame, justify='left',
            text=f"Total damage: {self.calc.tot_dmg}\n"
                 f"If crit: {self.calc.phys_crit_dmg + self.calc.elem_crit_dmg}"
                 f"\n\nPhysical: {self.calc.phys_dmg}\n"
                 f"If crit: {self.calc.phys_crit_dmg}\n\n"
                 f"Elemental: {self.calc.elem_dmg}\n"
                 f"If crit: {self.calc.elem_crit_dmg}")
        self.output_label_2.pack(side='left', padx=3, pady=3)
                 