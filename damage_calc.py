class DamageCalc():
    """Class that manage the damage calc"""

    def __init__(self):
        """Initialize the class"""
        self.weapon_stats = {}
        
    def get_weapon_stats(self, raw, elem, affinity, sharp):
        """Get the weapon stats and add them to a dictionary"""
        self.weapon_stats = {'raw': raw,
                             'elem': elem,
                             'affinity': affinity,
                             'sharp': sharp}
        
    def do_calc(self, motion, hitzone, elemhitzone):
        """Do the calc"""
        self.sharp_mod()

        raw = self.weapon_stats['raw']
        elem = self.weapon_stats['elem']
        raw_sharp_multiplier = self.sharp_multiplier[0]
        elem_sharp_multiplier = self.sharp_multiplier[1]

        phys_atk = (raw * raw_sharp_multiplier) * motion
        elem_atk = (elem * elem_sharp_multiplier)

        self.phys_dmg = int(phys_atk * hitzone)
        self.elem_dmg = int(elem_atk * elemhitzone)

        self.tot_dmg = self.phys_dmg + self.elem_dmg

    def show_results(self):
        """Print the results"""
        print(f"\nTotal damage: {self.tot_dmg}\n"
              f"Physical: {self.phys_dmg}\n"
              f"Elemental: {self.elem_dmg}")
    
    def sharp_mod(self):
        """Calculate the sharpness modifier"""
        sharp = self.weapon_stats['sharp']
        if sharp.lower() == 'red':
            self.sharp_multiplier = [0.5, 0.25]
        elif sharp.lower() == 'orange':
            self.sharp_multiplier = [0.75, 0.5]
        elif sharp.lower() == 'yellow':
            self.sharp_multiplier = [1, 0.75]
        elif sharp.lower() == 'green':
            self.sharp_multiplier = [1.05, 1]
        elif sharp.lower() == 'blue':
            self.sharp_multiplier = [1.2, 1.063]
        elif sharp.lower() == 'white':
            self.sharp_multiplier = [1.32, 1.15]
        elif sharp.lower() == 'purple':
            self.sharp_multiplier = [1.39, 1.27]