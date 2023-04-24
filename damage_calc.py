import tkinter as tk

class DamageCalc():
    """Class that manage the damage calc window"""

    def __init__(self, root):
        """Initialize the class"""
        self.root = root
        #self.wpn_stats = dict.fromkeys(['raw', 'elem', 'crit', 'sharp'])
        #self.other_stats = dict.fromkeys(['mv', 'hitzone', 'elemhitzone'])

        self.raw = tk.StringVar()
        self.raw.set(0)
        self.elem = tk.StringVar()
        self.elem.set(0)
        self.crit = tk.StringVar()
        self.crit.set(0)
        self.sharp = tk.StringVar()
        self.sharp.set('green')

        self.mv = tk.StringVar()
        self.mv.set(0)
        self.hitzone = tk.StringVar()
        self.hitzone.set(0)
        self.elemhitzone = tk.StringVar()
        self.elemhitzone.set(0)

        self.root.title("Calculator")

        self.canvas = tk.Frame(self.root, width=300, height=200, bg='lightgrey')
        self.canvas.pack(fill='both', expand=True)

        self.top_frame = tk.Frame(self.canvas, bg='purple')
        self.top_frame.pack(side='top', padx=5, pady=5, expand=True)

        self.bot_frame = tk.Frame(self.canvas, bg='pink')
        self.bot_frame.pack(side='bottom', padx=5, pady=5, expand=True)

        self._create_frames()
        self._create_labels()
        self._create_entries()

        self.calc_btn = tk.Button(self.bot_frame, width=20, text='Calculate',
                                  command=self._calculate)
        self.calc_btn.pack(side='top')

    def _create_frames(self):
        """Create the frames of the window"""
        # ----- Weapon -----
        # Labels
        self.wpn_labels = tk.Frame(self.top_frame,bg='blue')
        self.wpn_labels.pack(side='left', fill='none', padx=2, pady=2,
                             expand=True)
        # Entries
        self.wpn_entries = tk.Frame(self.top_frame, bg='green')
        self.wpn_entries.pack(side='left', fill='none', padx=2, pady=2,
                              expand=True)
        # ----- Other -----
        # Labels
        self.other_labels = tk.Frame(self.top_frame, bg='red')
        self.other_labels.pack(side='left', fill='none', padx=2, pady=2,
                               expand=True)
        # Entries
        self.other_entries = tk.Frame(self.top_frame, bg='yellow')
        self.other_entries.pack(side='left', fill='none', padx=2, pady=2,
                                expand=True)

    def _create_labels(self):
        """Create the labels of the window"""
        # ----- Weapon -----
        self.raw_label = tk.Label(self.wpn_labels, text="Raw: ")
        self.raw_label.pack(padx=3, pady=3)

        self.elem_label = tk.Label(self.wpn_labels, text="Element: ")
        self.elem_label.pack(padx=3, pady=3)

        self.crit_label = tk.Label(self.wpn_labels, text="Affinity: ")
        self.crit_label.pack(padx=3, pady=3)

        self.sharp_label = tk.Label(self.wpn_labels, text="Sharpness: ")
        self.sharp_label.pack(padx=3, pady=3)

        # ----- Other -----
        self.mv_label = tk.Label(self.other_labels, text="Motion value: ")
        self.mv_label.pack(padx=3, pady=3)

        self.hitzone_label = tk.Label(self.other_labels, text="Hitzone: ")
        self.hitzone_label.pack(padx=3, pady=3)

        self.elemhitzone_label = tk.Label(self.other_labels,
                                          text="Elem. hitzone: ")
        self.elemhitzone_label.pack(padx=3, pady=3)

        # ----- Output -----
        

    def _create_entries(self):
        """Create the entries of the window"""
        # ----- Weapon -----
        self.raw_entry = tk.Entry(self.wpn_entries, width=5, justify='center',
                                  textvariable=self.raw)
        self.raw_entry.pack(padx=3, pady=4)

        self.elem_entry = tk.Entry(self.wpn_entries, width=5, justify='center',
                                  textvariable=self.elem)
        self.elem_entry.pack(padx=3, pady=4)

        self.crit_entry = tk.Entry(self.wpn_entries, width=5, justify='center',
                                   textvariable=self.crit)
        self.crit_entry.pack(padx=3, pady=4)

        self.sharp_entry = tk.Entry(self.wpn_entries, width=8, justify='center',
                                  textvariable=self.sharp)
        self.sharp_entry.pack(padx=3, pady=4)

        # ----- Other -----
        self.mv_entry = tk.Entry(self.other_entries, width=5, justify='center',
                                  textvariable=self.mv)
        self.mv_entry.pack(padx=3, pady=4)

        self.hitzone_entry = tk.Entry(self.other_entries, width=5,
                                      justify='center',
                                      textvariable=self.hitzone)
        self.hitzone_entry.pack(padx=3, pady=4)

        self.elemhitzone_entry = tk.Entry(self.other_entries, width=5,
                                          justify='center',
                                          textvariable=self.elemhitzone)
        self.elemhitzone_entry.pack(padx=3, pady=4)

    def _calculate(self):
        """Call the necessary functions to calculate the damage"""
        self._get_values()
        self._do_calc()
        self._show_results()
    
    def _get_values(self):
        """Get the values from the entries and convert them to float"""
        self.raw = float(self.raw_entry.get())
        self.elem = float(self.elem_entry.get())
        self.crit = float(self.crit_entry.get())
        self.sharp = self.sharp_entry.get()

        self.mv = float(self.mv_entry.get())
        self.mv = self.mv /100
        self.hitzone = float(self.hitzone_entry.get())
        self.hitzone = self.hitzone /100
        self.elemhitzone = float(self.elemhitzone_entry.get())
        self.elemhitzone = self.elemhitzone /100

    def _do_calc(self):
        """Do the calculations"""
        self._sharp_mod()
        raw_sharp_mltp = self.sharp_mltp[0]
        elem_sharp_mltp = self.sharp_mltp[1]

        phys_atk = (self.raw * raw_sharp_mltp) * self.mv
        elem_atk = (self.elem * elem_sharp_mltp)

        self.phys_dmg = int(phys_atk * self.hitzone)
        self.elem_dmg = int(elem_atk * self.elemhitzone)

        self.tot_dmg = self.phys_dmg + self.elem_dmg

    def _show_results(self):
        """Print the results"""
        self.output_label = tk.Label(self.bot_frame,
                                     text=f"Total damage: {self.tot_dmg}\n"
                                          f"Physical: {self.phys_dmg}\n"
                                          f"Elemental: {self.elem_dmg}")
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