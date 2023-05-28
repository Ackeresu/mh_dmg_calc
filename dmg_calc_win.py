import tkinter as tk
from tkinter import ttk

from get_values import GetValues
from dmg_calc import DamageCalc
from options import Options
from items import Items
from skills import Skills

class DamageCalcWin():
    """Class that manage the damage calc window"""

    def __init__(self, root):
        """Initialize the class"""
        self.root = root
        self.options = Options()
        self.items = Items()
        self.skills = Skills()
        self.active_skills = {}

        # Weapon variables
        self.raw = tk.IntVar()
        self.raw.set(300)
        self.elem = tk.IntVar()
        self.elem.set(100)
        self.crit = tk.IntVar()
        self.crit.set(30)
        self.sharp = tk.StringVar()
        self.sharp.set('White')
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
        self.calc_btn.pack(side='top', fill='both')

    def _create_window(self):
        """Call the functions necessary to build the window"""
        self._create_main_frames()
        self._create_wpn_box()
        self._create_results_box()
        self._create_items_box()
        self._create_options_box()
        self._create_skills_box()

    def _create_main_frames(self):
        """Create the frames of the window"""
        self.canvas = tk.Frame(self.root, width=300, height=200, bg='lightgrey')
        self.canvas.pack(fill='both', expand=True)

        self.top_frame = tk.Frame(self.canvas, bg='purple')
        self.top_frame.pack(side='top', padx=5, pady=5, expand=True)

        self.center_frame = tk.Frame(self.canvas, bg='pink')
        self.center_frame.pack(side='top', fill='both', padx=5, pady=0,
                               expand=True)

        self.bot_left_frame = tk.Frame(self.canvas, bg='blue')
        self.bot_left_frame.pack(side='left', padx=5, pady=5, expand=True)
        
        self.bot_right_frame = tk.Frame(self.canvas, bg='cyan')
        self.bot_right_frame.pack(side='right', padx=5, pady=5, expand=True)

    def _create_wpn_box(self):
        """Create the box that manage the wpn data."""
        # ----- Frames -----
        # Main frame
        self.wpn_main_frame = tk.Frame(self.top_frame,bg='green')
        self.wpn_main_frame.pack(side='left', anchor='w', fill='none',
                             padx=2, pady=2, expand=True)
        # Title
        self.top_title = tk.Label(self.wpn_main_frame, text="Weapon")
        self.top_title.pack(side='top', fill='none',
                            padx=2, pady=2, expand=True)
        # Labels frame
        self.wpn_labels = tk.Frame(self.wpn_main_frame,bg='blue')
        self.wpn_labels.pack(side='left', anchor='w', fill='none',
                             padx=2, pady=2, expand=True)
        # Entries frame
        self.wpn_entries = tk.Frame(self.wpn_main_frame, bg='blue')
        self.wpn_entries.pack(side='left', anchor='w', fill='none',
                              padx=2, pady=2, expand=True)
        # Other labels frame
        self.other_labels = tk.Frame(self.wpn_main_frame, bg='blue')
        self.other_labels.pack(side='left', anchor='w', fill='none',
                               padx=2, pady=2, expand=True)
        # Other entries frame
        self.other_entries = tk.Frame(self.wpn_main_frame, bg='blue')
        self.other_entries.pack(side='left', anchor='w', fill='none',
                                padx=2, pady=2, expand=True)
        
        # ----- Labels -----
        # Raw
        self.raw_label = tk.Label(self.wpn_labels, text="Raw: ")
        self.raw_label.pack(anchor='w', padx=3, pady=3)
        # Element
        self.elem_label = tk.Label(self.wpn_labels, text="Element: ")
        self.elem_label.pack(anchor='w', padx=3, pady=3)
        # Affinity
        self.crit_label = tk.Label(self.wpn_labels, text="Affinity: ")
        self.crit_label.pack(anchor='w', padx=3, pady=3)
        # Sharpness
        self.sharp_label = tk.Label(self.wpn_labels, text="Sharpness: ")
        self.sharp_label.pack(anchor='w', padx=3, pady=3)
        # MV
        self.mv_label = tk.Label(self.other_labels, text="Motion value: ")
        self.mv_label.pack(anchor='w', padx=3, pady=3)
        # Hitzone
        self.hzv_label = tk.Label(self.other_labels, text="Hitzone: ")
        self.hzv_label.pack(anchor='w', padx=3, pady=3)
        # Elem hitzone
        self.ehzv_label = tk.Label(self.other_labels, text="Elem. hitzone: ")
        self.ehzv_label.pack(anchor='w', padx=3, pady=3)

        # ----- Entries -----
        # Raw
        self.raw_entry = tk.Entry(self.wpn_entries, width=8, justify='center',
                                  textvariable=self.raw)
        self.raw_entry.pack(anchor='w', padx=3, pady=4)
        # Element
        self.elem_entry = tk.Entry(self.wpn_entries, width=8, justify='center',
                                   textvariable=self.elem)
        self.elem_entry.pack(anchor='w', padx=3, pady=4)
        # Affinity
        self.crit_entry = tk.Entry(self.wpn_entries, width=8, justify='center',
                                   textvariable=self.crit)
        self.crit_entry.pack(anchor='w', padx=3, pady=4)
        # Sharp
        self.sharp_entry = tk.Entry(self.wpn_entries, width=8, justify='center',
                                    textvariable=self.sharp)
        self.sharp_entry.pack(anchor='w', padx=3, pady=4)
        # MV
        self.mv_entry = tk.Entry(self.other_entries, width=8, justify='center',
                                 textvariable=self.mv)
        self.mv_entry.pack(anchor='w', padx=3, pady=4)
        # Hitzone
        self.hzv_entry = tk.Entry(self.other_entries, width=8, justify='center',
                                  textvariable=self.hzv)
        self.hzv_entry.pack(anchor='w', padx=3, pady=4)
        # Elem hitzone
        self.ehzv_entry = tk.Entry(self.other_entries, width=8,
                                   justify='center', textvariable=self.ehzv)
        self.ehzv_entry.pack(anchor='w', padx=3, pady=4)

    def _create_results_box(self):
        """Create the box that manage the results."""
        # Frame
        self.results_frame = tk.Frame(self.top_frame, bg='green')
        self.results_frame.pack(side='left', anchor='w', fill='none',
                              padx=5, pady=5, expand=True)
        # Title
        self.results_title = tk.Label(self.results_frame, text="Results")
        self.results_title.pack(side='top', fill='none',
                            padx=2, pady=2, expand=True)
        
    def _create_items_box(self):
        """Create the box that manage the items."""
        # Frame
        self.items_frame = tk.Frame(self.bot_left_frame, bg='pink')
        self.items_frame.pack(side='left', anchor='w', fill='none',
                              padx=2, pady=2, expand=True)
        # Title
        self.items_title = tk.Label(self.items_frame, text="Items")
        self.items_title.pack(side='top', fill='none',
                                    padx=2, pady=2, expand=True)
        
        # ----- Items -----
        # Powercharm
        self.powercharm_check = tk.Checkbutton(self.items_frame,
            text='Powercharm', variable=self.items.powercharm,
            onvalue=1, offvalue=0)
        self.powercharm_check.pack(anchor='w', padx=3, pady=4)

        # Powertalon
        self.powertalon_check = tk.Checkbutton(self.items_frame,
            text='Powertalon', variable=self.items.powertalon,
            onvalue=1, offvalue=0)
        self.powertalon_check.pack(anchor='w', padx=3, pady=4)

        # Might Seed
        self.might_seed_check = tk.Checkbutton(self.items_frame,
            text='Might Seed', variable=self.items.might_seed,
            onvalue=1, offvalue=0)
        self.might_seed_check.pack(anchor='w', padx=3, pady=4)

        # Demon Powder
        self.demon_powder_check = tk.Checkbutton(self.items_frame,
            text='Demon Powder', variable=self.items.demon_powder,
            onvalue=1, offvalue=0)
        self.demon_powder_check.pack(anchor='w', padx=3, pady=4)

        # Demondrug
        self.demondrug_check = tk.Checkbutton(self.items_frame,
            text='Demondrug', variable=self.items.demondrug,
            onvalue=1, offvalue=0, state='active')
        self.demondrug_check.config(command=lambda:self._mutually_ex(
                                                    self.items.demondrug,
                                                    self.mega_demondrug_check))
        self.demondrug_check.pack(anchor='w', padx=3, pady=4)

        # Mega Demondrug
        self.mega_demondrug_check = tk.Checkbutton(self.items_frame,
            text='Mega Demondrug', variable=self.items.mega_demondrug,
            onvalue=1, offvalue=0, state='active')
        self.mega_demondrug_check.config(command=lambda:self._mutually_ex(
                                                    self.items.mega_demondrug,
                                                    self.demondrug_check))
        self.mega_demondrug_check.pack(anchor='w', padx=3, pady=4)

    def _create_options_box(self):
        """Create the box that manage the options."""
        # Frame
        self.options_frame = tk.Frame(self.bot_left_frame, bg='pink')
        self.options_frame.pack(side='left', anchor='w', fill='none',
                              padx=2, pady=2, expand=True)
        # Title
        self.options_title = tk.Label(self.options_frame, text="Options")
        self.options_title.pack(side='top', fill='none',
                                    padx=2, pady=2, expand=True)
        
        # ----- Options -----
        # Scroll change
        self.scroll_check = tk.Checkbutton(self.options_frame,
            text='Use Blue Scroll', variable=self.options.scroll_color,
            onvalue=1, offvalue=0)
        self.scroll_check.pack(anchor='w', padx=3, pady=4)

        # Frenzy
        self.frenzy_check = tk.Checkbutton(self.options_frame,
            text='Beaten Frenzy', variable=self.options.beaten_frenzy,
            onvalue=1, offvalue=0)
        self.frenzy_check.pack(anchor='w', padx=3, pady=4)

    def _create_skills_box(self):
        """Create the box that manage the skills."""
        # Title
        self.skills_title = tk.Label(self.bot_right_frame, text="Skills")
        self.skills_title.pack(side='top', fill='none',
                                     padx=2, pady=2, expand=True)
        # Select frame
        self.skills_select_frame = tk.Frame(self.bot_right_frame, bg='pink')
        self.skills_select_frame.pack(side='left', anchor='e', fill='none',
                               padx=2, pady=2, expand=True)
        # Skills frame
        self.skills_main_frame = tk.Frame(self.bot_right_frame, bg='pink')
        self.skills_main_frame.pack(side='bottom', anchor='s', fill='both',
                               padx=2, pady=2, expand=True)
        # Skill labels frame
        self.skills_labels = tk.Frame(self.skills_main_frame, bg='orange')
        self.skills_labels.pack(side='left', anchor='n', fill='both',
                               padx=2, pady=2, expand=True)
        # Option menus frame
        self.skills_optionmenu = tk.Frame(self.skills_main_frame, bg='yellow')
        self.skills_optionmenu.pack(side='left', anchor='n', fill='both',
                                   padx=2, pady=2, expand=True)
        # Remove btn frame
        self.skills_btn = tk.Frame(self.skills_main_frame, bg='red')
        self.skills_btn.pack(side='left', anchor='s', fill='both',
                                   padx=5, pady=2, expand=True)
        
        # ----- Skill selection -----
        new_skill = tk.StringVar()
        dropdown = ttk.Combobox(self.bot_right_frame,
                                textvariable=new_skill,
                                values=self.skills.skill_list, state='readonly')
        dropdown.pack(side='left', anchor='w', padx=3, pady=4)

        self.add_skill_btn = tk.Button(self.bot_right_frame, width=10,
                                    text='Add Skill',
                                    command=lambda:self._add_skill(new_skill))
        self.add_skill_btn.pack(side='left', anchor='e')

    def _add_skill(self, new_skill):
        """Add the new skill."""
        # Get the skill name
        self.skill_name = new_skill.get()
        
        #for key in self.active_skills.keys():
            
        if self.skill_name != '':
            self._format_skill_name(self.skill_name)
            self._create_skill_elements()
            # Flag the newly added skill as active
            setattr(self.skills, self.skill_name_edit, 1)

            for key, value in self.active_skills.items():
                print(f"Key: {key}\n"
                      f"Value: {value}")
            print()
        else:
            pass

    def _format_skill_name(self, new_skill):
        """Format the name of the newly added skill for use in the logic"""
        self.skill_name_edit = new_skill.lower()
        self.skill_name_edit = self.skill_name_edit.replace(' ', '_')

        # Create two variables from the formatted name to access the
        # skill's data
        skill_lvl_name = self.skill_name_edit + '_lvl'
        skill_lvl_list_name = self.skill_name_edit + '_lvl_list'

        # Get the necessary attributes of the skills from the edits
        self.skill_lvl = getattr(self.skills, skill_lvl_name)
        self.skill_lvl_list = getattr(self.skills, skill_lvl_list_name)

    def _create_skill_elements(self):
        """Create the elements of the newly added skill and add them
           to the list of active skills"""
        # Create a new list to store the elements
        skill = self.skill_name_edit
        skill_lvl = self.skill_lvl
        skill_lvl_list = self.skill_lvl_list
        skill_elements =[]
        
        # Create the elements
        # Optionmenu
        skill_menu = tk.OptionMenu(self.skills_optionmenu,
                                   skill_lvl, *skill_lvl_list)
        skill_menu.pack(anchor='n', padx=3, pady=1)
        # Label
        skill_label = tk.Label(self.skills_labels, text=self.skill_name)
        skill_label.pack(padx=3, pady=6)
        # Remove btn
        skill_btn = tk.Button(self.skills_btn, width=3, text='X',
                              command=lambda:self._remove_skill(skill))
        skill_btn.pack(anchor='s', padx=3, pady=3)

        # Add the elements to the list and add then add the skill in the dict 
        # of active skills
        skill_elements.extend([skill_menu, skill_label, skill_btn])
        self.active_skills[self.skill_name_edit] = skill_elements

    def _remove_skill(self, skill):
        """Remove the skill and relative elements"""
        # Flag the skill as inactive
        setattr(self.skills, skill, 0)

        # Remove the elements from the UI then the skill itself from the dict
        for element in self.active_skills[skill]:
            element.destroy()
        del self.active_skills[skill]

        for key, value in self.active_skills.items():
                print(f"Key: {key}\n"
                      f"Value: {value}")
        print()

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
        # Check for a previous result and delete it if present.
        try:
            self.results_label_1.destroy()
            self.results_label_2.destroy()
        except AttributeError:
            pass
        self.get_values = GetValues(self)
        self.get_values.get_values()
        self.calc = DamageCalc(self.get_values)
        self.calc.do_calcs()
        self._show_results()

    def _show_results(self):
        """Print the results"""
        self.results_label_1 = tk.Label(self.results_frame, justify='left',
            text=f"Displayed attack: {self.calc.display_atk}\n"
                 f"Displayed element: {self.calc.display_elem}\n\n"
                 f"Affinity: {self.calc.final_crit}\n\n\n"
                 f"Effective raw: {self.calc.eff_raw}\n"
                 f"Effective element: {self.calc.eff_elem}")
        self.results_label_1.pack(side='left', padx=3, pady=3)

        self.results_label_2 = tk.Label(self.results_frame, justify='left',
            text=f"Total damage: {self.calc.tot_dmg}\n"
                 f"If crit: {self.calc.phys_crit_dmg + self.calc.elem_crit_dmg}"
                 f"\n\nPhysical: {self.calc.phys_dmg}\n"
                 f"If crit: {self.calc.phys_crit_dmg}\n\n"
                 f"Elemental: {self.calc.elem_dmg}\n"
                 f"If crit: {self.calc.elem_crit_dmg}")
        self.results_label_2.pack(side='left', padx=3, pady=3)

if __name__ == '__main__':
    # Make an app istance and run the app
    root = tk.Tk()
    app = DamageCalcWin(root)
    #app.root.title("MH Builder")
    root.mainloop()