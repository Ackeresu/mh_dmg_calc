class DamageCalc():
    """Class that manage the calculations"""

    def __init__(self, value):
        """Initialize the variables"""
        self.raw = value.raw
        self.elem = value.elem
        self.crit = value.crit
        self.sharp = value.sharp

        self.mv = value.mv
        self.hzv = value.hzv
        self.ehzv = value.ehzv

        self.atk_mltp = value.atk_mltp
        self.atk_buffs = value.atk_buffs
        self.elem_mltp = value.elem_mltp
        self.elem_buffs = value.elem_buffs
        
        self.crit_mltp = value.crit_mltp
        self.crit_mltp_value = value.crit_mltp_value
        self.crit_elem_mltp = value.crit_elem_mltp
        self.crit_buffs = value.crit_buffs

    def do_calcs(self):
        """Do the calculations"""
        # Damage formula:
        # ((base raw/ele * base multipliers + flat bonuses)
        # * horn multipliers + 0.1)
        # * global multiplier * hitzone * rage modifier
        #
        # Base muliplier, as a rule of thumb, are all the skills that are
        # reflected in the UI (green numbers)
        # Global multipliers include sharpness, crit damage multipliers
        # (crit boost/Ele) and various total damage multipliers.

        # Calculate the sharpness multiplier
        self._sharp_mod()
        raw_sharp_mltp = self.sharp_mltp[0]
        elem_sharp_mltp = self.sharp_mltp[1]

        # Calculate the displayed atk and elem
        self.display_atk = round(
            (self.raw * self.atk_mltp + self.atk_buffs) * 1 + 0.1)
        self.display_elem = round(
            (self.elem * self.elem_mltp + self.elem_buffs) * 1 + 0.1)

        phys_atk = self.display_atk * raw_sharp_mltp * self.mv
        elem_atk = self.elem * elem_sharp_mltp

        # Calculate the effective raw/elem
        self.final_crit = round(self.crit + self.crit_buffs)
        if self.final_crit >= 100:
            crit_calc = 1 + (self.crit_mltp_value / 100)
        else:
            crit_calc = 1 + ((self.final_crit / 100)
                             * (self.crit_mltp_value / 100))

        self.eff_raw = round((self.display_atk * raw_sharp_mltp) * crit_calc)
        self.eff_elem = round(self.elem * elem_sharp_mltp)

        # Calculate the damage
        self.phys_dmg = round(phys_atk * self.hzv)
        self.elem_dmg = round(elem_atk * self.ehzv)

        self.phys_crit_dmg = round(self.phys_dmg * self.crit_mltp)
        self.elem_crit_dmg = round(self.elem_dmg * self.crit_elem_mltp)

        self.tot_dmg = self.phys_dmg + self.elem_dmg
        
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