import tkinter as tk
from tkinter import ttk

from get_values import GetValues
from dmg_calc import DamageCalc
from weapon import Weapon
from skills import Skills
from other import Other

class DamageCalcWin():
    """Class that manage the damage calc window"""

    def __init__(self, root):
        """Initialize the class"""
        self.root = root
        self.wpn = Weapon()
        self.skills = Skills()
        self.other = Other()
        self.active_skills = {}
        self.old_wpn_specific = 'none'
        self.old_rampage_deco = 'none'
        self.old_petalace = 'none'
        self.row_pos = 0

        self.root.title("MH Damage Calculator")
        self.root.resizable(False, False)
        
        self._create_window()
        self._calculate()

    def _create_window(self):
        """Call the functions necessary to build the window"""
        self._create_main_frames()
        self._create_wpn_box()
        self._create_equipment_box()
        self._create_skills_box()
        self._create_other_box()
        self._create_calc_btn_box()
        self._create_results_box()

    def _create_main_frames(self):
        """Create the frames of the window"""
        self.canvas = tk.Frame(self.root, width=200, height=180, bg='lightgrey')
        self.canvas.pack(fill='both', expand=True)

        # Left side
        self.left_frame = tk.Frame(self.canvas, bg='blue')
        self.left_frame.pack(side='left')

        self.left_top_frame = tk.Frame(self.left_frame, bg='green')
        self.left_top_frame.pack(padx=2, pady=2)

        self.left_center_frame = tk.Frame(self.left_frame, bg='cyan')
        self.left_center_frame.pack(padx=2, pady=2)

        self.left_bottom_frame = tk.Frame(self.left_frame, bg='violet')
        self.left_bottom_frame.pack(padx=2, pady=2)

        # Right side
        self.right_frame = tk.Frame(self.canvas, bg='red')
        self.right_frame.pack(side='right')

        # ----------------------------------------------------------------------

        # Weapon
        self.wpn_frame = tk.Frame(self.left_top_frame, bg='purple')
        self.wpn_frame.pack(side='left', padx=2, pady=2, anchor='n')
        # Equipment
        self.equipment_frame = tk.Frame(self.left_top_frame, bg='pink')
        self.equipment_frame.pack(side='left', padx=2, pady=2)

        # Skills
        self.skills_frame = tk.Frame(self.left_center_frame, bg='blue')
        self.skills_frame.pack(side='left', padx=2, pady=2, anchor='n')
        # Other
        self.other_frame = tk.Frame(self.left_center_frame, bg='purple')
        self.other_frame.pack(side='left', padx=2, pady=2)

        # Calc btn
        self.calc_btn_frame = tk.Frame(self.left_bottom_frame, bg='cyan')
        self.calc_btn_frame.pack(side='top', padx=2, pady=2)

    def _create_wpn_box(self):
        """Create the box that manage the wpn data."""
        # Title
        self.top_title = tk.Label(self.wpn_frame, text="WEAPON")
        self.top_title.pack(side='top', fill='none',
                            padx=2, pady=2, expand=True)
        # Wpn frame
        self.wpn_data_frame = tk.Frame(self.wpn_frame, bg='cyan')
        self.wpn_data_frame.pack(side='left', anchor='w', fill='none',
                             padx=2, pady=2, expand=True)
        
        # ----------------------------------------------------------------------

        # Raw
        self.raw_label = tk.Label(self.wpn_data_frame, text="Raw: ")
        self.raw_label.grid(row=1, column=1, sticky='w')

        self.raw_entry = tk.Entry(self.wpn_data_frame, width=8, justify='center',
                                  textvariable=self.wpn.raw)
        self.raw_entry.grid(row=1, column=2)

        # Element
        self.elem_label = tk.Label(self.wpn_data_frame, text="Element: ")
        self.elem_label.grid(row=2, column=1, sticky='w')
        
        self.elem_entry = tk.Entry(self.wpn_data_frame, width=8, justify='center',
                                   textvariable=self.wpn.element)
        self.elem_entry.grid(row=2, column=2)

        # Affinity
        self.crit_label = tk.Label(self.wpn_data_frame, text="Affinity: ")
        self.crit_label.grid(row=3, column=1, sticky='w')

        self.crit_entry = tk.Entry(self.wpn_data_frame, width=8, justify='center',
                                   textvariable=self.wpn.affinity)
        self.crit_entry.grid(row=3, column=2)

        # Sharpness
        self.sharp_label = tk.Label(self.wpn_data_frame, text="Sharpness: ")
        self.sharp_label.grid(row=4, column=1, sticky='w')

        self.sharp_menu = tk.OptionMenu(self.wpn_data_frame,
                                        self.wpn.sharpness,
                                        *self.wpn.sharpness_list)
        self.sharp_menu.config(width=6)
        self.sharp_menu.grid(row=4, column=2)

        # MV
        self.mv_label = tk.Label(self.wpn_data_frame, text="Motion value: ")
        self.mv_label.grid(row=1, column=3, sticky='w')

        self.mv_entry = tk.Entry(self.wpn_data_frame, width=8, justify='center',
                                 textvariable=self.wpn.mv)
        self.mv_entry.grid(row=1, column=4)

        # Hitzone
        self.hzv_label = tk.Label(self.wpn_data_frame, text="Hitzone: ")
        self.hzv_label.grid(row=2, column=3, sticky='w')

        self.hzv_entry = tk.Entry(self.wpn_data_frame, width=8, justify='center',
                                  textvariable=self.wpn.raw_hitzone)
        self.hzv_entry.grid(row=2, column=4)
        
        # Elem hitzone
        self.ehzv_label = tk.Label(self.wpn_data_frame, text="Elem. hitzone: ")
        self.ehzv_label.grid(row=3, column=3, sticky='w')

        self.ehzv_entry = tk.Entry(self.wpn_data_frame, width=8,
                                   justify='center', textvariable=self.wpn.elemental_hitzone)
        self.ehzv_entry.grid(row=3, column=4)

    def _create_equipment_box(self):        
        self._create_wpn_specific_box()
        self._create_rampage_deco_box()
        self._create_petalace_box()

    def _create_wpn_specific_box(self):
        """Create the box that manage the weapon specific buffs"""
        # Title
        self.wpn_specific_title = tk.Label(self.equipment_frame, text="WEAPON SPECIFIC")
        self.wpn_specific_title.pack(side='top', fill='none',
                                     padx=2, pady=2, expand=True)
        # Dropdown
        self.active_wpn_specific = tk.StringVar()
        wpn_specific_data = [self.wpn, self.old_wpn_specific, self.active_wpn_specific]
        self.wpn_specific_dropdown = ttk.Combobox(self.equipment_frame,
                                textvariable=self.active_wpn_specific, width=25,
                                values=self.wpn.wpn_specific_list, state='readonly')
        self.wpn_specific_dropdown.bind("<<ComboboxSelected>>", lambda event,
                                    data=wpn_specific_data: self._dropdown_choice(event, data))
        self.wpn_specific_dropdown.pack(side='top', padx=3, pady=4, expand=True)
        
    def _create_rampage_deco_box(self):
        """Create the box that manage the rampage decos"""
        # Title
        self.rampage_deco_title = tk.Label(self.equipment_frame, text="RAMPAGE DECO")
        self.rampage_deco_title.pack(side='top', fill='none',
                                     padx=2, pady=2, expand=True)
        # Dropdown
        self.active_rampage_deco = tk.StringVar()
        rampage_deco_data = [self.other, self.old_rampage_deco, self.active_rampage_deco]
        self.rampage_deco_dropdown = ttk.Combobox(self.equipment_frame,
                                textvariable=self.active_rampage_deco, width=25,
                                values=self.other.rampage_deco_list, state='readonly')
        self.rampage_deco_dropdown.bind("<<ComboboxSelected>>", lambda event,
                                    data=rampage_deco_data: self._dropdown_choice(event, data))
        self.rampage_deco_dropdown.pack(side='top', padx=3, pady=4, expand=True)

    def _create_petalace_box(self):
        """Create the box that manage the petalaces"""
        # Title
        self.petalace_title = tk.Label(self.equipment_frame, text="PETALACE")
        self.petalace_title.pack(side='top', fill='none',
                                     padx=2, pady=2, expand=True)
        # Dropdown
        self.active_petalace = tk.StringVar()
        petalace_data = [self.other, self.old_petalace, self.active_petalace]
        self.petalace_dropdown = ttk.Combobox(self.equipment_frame,
                                textvariable=self.active_petalace, width=25,
                                values=self.other.petalace_list, state='readonly')
        self.petalace_dropdown.bind("<<ComboboxSelected>>", lambda event,
                                    data=petalace_data: self._dropdown_choice(event, data))
        self.petalace_dropdown.pack(side='top', padx=3, pady=4, expand=True)

    def _dropdown_choice(self, event, data):
        """Manage the addition of the selected dropdown choice and remove the old one"""
        instance = data[0]
        old_choice = data[1]
        new_choice = data[2].get()

        setattr(instance, old_choice, 0)
        
        new_choice_name = self._format_name(new_choice)
        setattr(instance, new_choice_name, 1)
        data[1] = new_choice_name

    def _create_results_box(self):
        """Create the box that manage the results"""
        # Frame
        self.results_frame = tk.Frame(self.right_frame, bg='green')
        self.results_frame.pack(side='left', anchor='w', fill='none',
                              padx=5, pady=5, expand=True)
        # Title
        self.results_title = tk.Label(self.results_frame, text="RESULTS")
        self.results_title.pack(side='top', fill='none',
                            padx=2, pady=2, expand=True)
    
    def _create_other_box(self):
        """Create the box that manage all the other buffs"""
        # Items frame
        self.items_frame = tk.Frame(self.other_frame, bg='pink')
        self.items_frame.pack(side='left', anchor='n', fill='none',
                              padx=2, pady=2, expand=True)
        
        self._create_items_box()
        self._create_food_box()

        # Other options frame
        self.other_options_frame = tk.Frame(self.other_frame, bg='pink')
        self.other_options_frame.pack(side='left', anchor='w', fill='none',
                              padx=2, pady=2, expand=True)
        
        self._create_hh_songs_box()
        self._create_other_options_box()

    def _create_items_box(self):
        """Create the box that manage the items"""
        # Title
        self.items_title = tk.Label(self.items_frame, text="ITEMS")
        self.items_title.pack(side='top', fill='none',
                                    padx=2, pady=2, expand=True)
        
        self._make_checkboxes(self.items_frame, self.other,
                              self.other.items_list)

        # Demondrug
        self.demondrug_check = tk.Checkbutton(self.items_frame,
            text='Demondrug', variable=self.other.demondrug,
            onvalue=1, offvalue=0, state='active')
        self.demondrug_check.config(command=lambda:self._mutually_ex(
                                                    self.other.demondrug,
                                                    self.mega_demondrug_check))
        self.demondrug_check.pack(anchor='w')

        # Mega Demondrug
        self.mega_demondrug_check = tk.Checkbutton(self.items_frame,
            text='Mega Demondrug', variable=self.other.mega_demondrug,
            onvalue=1, offvalue=0, state='active')
        self.mega_demondrug_check.config(command=lambda:self._mutually_ex(
                                                    self.other.mega_demondrug,
                                                    self.demondrug_check))
        self.mega_demondrug_check.pack(anchor='w')
    
    def _create_food_box(self):
        """"""
        # Title
        self.food_title = tk.Label(self.items_frame, text="FOOD")
        self.food_title.pack(side='top', fill='none',
                            padx=2, pady=2, expand=True)
        
        # Frame
        self.food_frame = tk.Frame(self.items_frame, bg='red')
        self.food_frame.pack(side='top', fill='none',
                                padx=2, pady=2, expand=True)
        
        # Dango booster menu
        self.dango_booster_menu = tk.OptionMenu(self.food_frame,
                                            self.other.dango_booster_lvl,
                                            *self.other.dango_booster_lvl_list)
        self.dango_booster_menu.config(state='disabled')
        self.dango_booster_menu.grid(row=1, column=2, sticky='w')
        
        # Dango booster check
        self.dango_booster_check = tk.Checkbutton(self.food_frame,
            text='Dango Booster', variable=self.other.dango_booster,
            onvalue=1, offvalue=0)
        self.dango_booster_check.config(command=lambda:self._switch_state(
                                                    self.other.dango_booster,
                                                    self.dango_booster_menu))
        self.dango_booster_check.grid(row=1, column=1, sticky='w')

        # Dango adrenaline menu
        self.dango_adrenaline_menu = tk.OptionMenu(self.food_frame,
                                            self.other.dango_adrenaline_lvl,
                                            *self.other.dango_adrenaline_lvl_list)
        self.dango_adrenaline_menu.config(state='disabled')
        self.dango_adrenaline_menu.grid(row=2, column=2, sticky='w')
        
        # Dango adrenaline check
        self.dango_adrenaline_check = tk.Checkbutton(self.food_frame,
            text='Dango Adrenaline', variable=self.other.dango_adrenaline,
            onvalue=1, offvalue=0)
        self.dango_adrenaline_check.config(command=lambda:self._switch_state(
                                                    self.other.dango_adrenaline,
                                                    self.dango_adrenaline_menu))
        self.dango_adrenaline_check.grid(row=2, column=1, sticky='w')

        # Dango bulker check
        self.dango_bulker_check = tk.Checkbutton(self.food_frame,
            text='Dango Bulker', variable=self.other.dango_bulker,
            onvalue=1, offvalue=0)
        self.dango_bulker_check.grid(row=3, column=1, sticky='w')
    
    def _create_hh_songs_box(self):
        """Create the box that manage the hh songs"""
        self.hh_songs_title = tk.Label(self.other_options_frame, text="HH SONGS")
        self.hh_songs_title.pack(side='top', fill='none',
                                    padx=2, pady=2, expand=True)
        
        self._make_checkboxes(self.other_options_frame, self.other,
                              self.other.hh_songs_list)

    def _create_other_options_box(self):
        """Create the box that manage other options"""
        self.other_title = tk.Label(self.other_options_frame, text="OTHER")
        self.other_title.pack(side='top', fill='none',
                                    padx=2, pady=2, expand=True)
        
        self._make_checkboxes(self.other_options_frame, self.other,
                              self.other.other_list)
        
    def _create_calc_btn_box(self):
        """Create the box that manage the calc btn"""
        self.calc_btn = tk.Button(self.calc_btn_frame, width=50, height=2,
                                  text='CALCULATE', command=self._calculate)
        self.calc_btn.pack(side='top', fill='both')

# -----------------------------------------------------------------------------
# ---------------------------- SKILL FUNCTIONS --------------------------------
# -----------------------------------------------------------------------------

    def _create_skills_box(self):
        """Create the box that manage the skills"""
        # Title
        self.skills_title = tk.Label(self.skills_frame, text="SKILLS")
        self.skills_title.pack(side='top', fill='none',
                                     padx=2, pady=2, expand=True)
        # Frame
        self.skills_data_frame = tk.Frame(self.skills_frame, bg='pink')
        self.skills_data_frame.pack(side='bottom', anchor='s', fill='both',
                               padx=2, pady=2, expand=True)
        # Skill selection dropdown
        self.new_skill = tk.StringVar()
        self.skill_dropdown = ttk.Combobox(self.skills_frame,
                                textvariable=self.new_skill, width=25,
                                values=self.skills.skill_list, state='readonly')
        self.skill_dropdown.bind("<<ComboboxSelected>>", self._add_skill)
        self.skill_dropdown.pack(side='left', padx=3, pady=4, expand=True)

    def _add_skill(self, event):
        """Add the new skill"""
        self.skill_name = self.new_skill.get()

        # Format the skill name then check if the skill is not already active
        self._format_skill_name()
        skill_check = False

        for key in self.active_skills.keys():
            if key == self.formatted_skill_name:
                skill_check = True

        if self.skill_name != '' and skill_check == False:
            self._create_skill_elements()
            # Flag the newly added skill as active
            setattr(self.skills, self.formatted_skill_name, 1)

    def _format_skill_name(self):
        """Format the name of the newly added skill for use in the logic"""
        self.formatted_skill_name = self.skill_name.lower()
        self.formatted_skill_name = self.formatted_skill_name.replace(' ', '_')

        skill_lvl_str = self.formatted_skill_name + '_lvl'
        skill_lvl_list_str = self.formatted_skill_name + '_lvl_list'

        self.skill_lvl = getattr(self.skills, skill_lvl_str)
        self.skill_lvl_list = getattr(self.skills, skill_lvl_list_str)

    def _format_special_skill_name(self):
        """Format the name of the newly added skill for use in the logic"""
        special_name = self.formatted_skill_name + '_special_name'
        special_lvl = self.formatted_skill_name + '_special'
        special_lvl_list = self.formatted_skill_name + '_special_list'

        self.special_name = getattr(self.skills, special_name)
        self.special_lvl = getattr(self.skills, special_lvl)
        self.special_lvl_list = getattr(self.skills, special_lvl_list)

    def _create_skill_elements(self):
        """Create the elements of the newly added skill and add them
           to the list of active skills"""
        formatted_skill_name = self.formatted_skill_name
        skill_lvl = self.skill_lvl
        skill_lvl_list = self.skill_lvl_list
        skill_elements = []

        # Create the elements
        # Optionmenu
        skill_menu = tk.OptionMenu(self.skills_data_frame,
                                   skill_lvl, *skill_lvl_list)
        skill_menu.grid(row=self.row_pos, column=3, sticky='w')
        # Label
        skill_label = tk.Label(self.skills_data_frame, text=self.skill_name)
        skill_label.grid(row=self.row_pos, column=2, sticky='w')
        # Remove btn
        skill_btn = tk.Button(self.skills_data_frame, width=3, height=1, text='X',
                              command=lambda:self._remove_skill(formatted_skill_name))
        skill_btn.grid(row=self.row_pos, column=1, sticky='w', padx=5)
        
        # Check if the skill is labeled as "special" and needs other options
        if self.skill_name.lower() in self.skills.special_skill_list:
            self._format_special_skill_name()

            special_name = self.special_name
            special_lvl = self.special_lvl
            special_lvl_list = self.special_lvl_list

            # Option menu
            special_menu = tk.OptionMenu(self.skills_data_frame,
                                         special_lvl, *special_lvl_list)
            special_menu.grid(row=self.row_pos, column=5, sticky='w')
            # Label
            special_label = tk.Label(self.skills_data_frame, text=special_name)
            special_label.grid(row=self.row_pos, column=4, sticky='w')
        else:
            # Empty option menu
            special_menu = tk.Label(self.skills_data_frame, text='')
            special_menu.grid(row=self.row_pos, column=5, sticky='w')
            # Empty label
            special_label = tk.Label(self.skills_data_frame, text='')
            special_label.grid(row=self.row_pos, column=4, sticky='w')

        # Add the skill and relative elements to the dict of active skills
        skill_elements.extend([skill_menu, skill_label, skill_btn,
                               special_menu, special_label])
        self.active_skills[formatted_skill_name] = skill_elements

        self.row_pos += 1

    def _remove_skill(self, skill_to_remove):
        """Remove the skill and relative elements"""
        # Flag the skill as inactive
        setattr(self.skills, skill_to_remove, 0)

        # Remove the elements from the UI then the skill itself from the dict
        for element in self.active_skills[skill_to_remove]:
            element.destroy()
        del self.active_skills[skill_to_remove]

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

    def _make_checkboxes(self, frame, instance, list):
        """Automatically generate the checkboxes elements from a list,
           then place them in the specified frame"""
        self.frame = frame
        self.list = list

        for item in list:
            item_name = self._format_name(item)
            item_name = getattr(instance, item_name)

            item_checkbox = tk.Checkbutton(self.frame,
                                       text=item, variable=item_name,
                                       onvalue=1, offvalue=0)
            item_checkbox.pack(anchor='w')

    def _format_name(self, item):
        """Format the name for logical purposes"""
        item_name = item.lower()
        item_name = item_name.replace(' ', '_')
        return item_name

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
            self.results_label.destroy()
        except AttributeError:
            pass
        self.get_values = GetValues(self)
        self.get_values.get_values()
        self.calc = DamageCalc(self.get_values)
        self.calc.do_calcs()
        self._show_results()

    def _show_results(self):
        """Print the results"""
        self.results_label = tk.Label(self.results_frame, justify='left',
            text=f"Displayed attack: {self.calc.display_atk}\n"
                 f"Displayed element: {self.calc.display_elem}\n\n"
                 f"Affinity: {self.calc.final_crit}\n\n"
                 f"Effective raw: {self.calc.eff_raw}\n"
                 f"Effective element: {self.calc.eff_elem}\n\n"
                 f"Total damage: {self.calc.tot_dmg}\n"
                 f"If crit: {self.calc.phys_crit_dmg + self.calc.elem_crit_dmg}"
                 f"\n\nPhysical: {self.calc.phys_dmg}\n"
                 f"If crit: {self.calc.phys_crit_dmg}\n\n"
                 f"Elemental: {self.calc.elem_dmg}\n"
                 f"If crit: {self.calc.elem_crit_dmg}")
        self.results_label.pack(side='left', padx=3, pady=3)

if __name__ == '__main__':
    # Make an app istance and run the app
    root = tk.Tk()
    app = DamageCalcWin(root)
    #app.root.title("MH Builder")
    root.mainloop()