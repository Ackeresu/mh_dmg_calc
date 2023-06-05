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
        self.atk_global_mltp = value.atk_global_mltp

        self.elem_mltp = value.elem_mltp
        self.elem_buffs = value.elem_buffs
        self.elem_global_mltp = value.elem_global_mltp
        
        self.crit_mltp = value.crit_mltp
        self.crit_elem_mltp = value.crit_elem_mltp
        self.crit_buffs = value.crit_buffs

        self.buildup_boost_calc = value.buildup_boost_calc
        self.buildup_boost_eff_raw = value.buildup_boost_eff_raw

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
        self.display_atk = round(((self.raw * self.atk_mltp) + self.atk_buffs) // 1)
        self.display_elem = round(((self.elem * self.elem_mltp) + self.elem_buffs) // 1)

        phys_atk = round(self.display_atk * raw_sharp_mltp * self.atk_global_mltp * self.mv)
        elem_atk = round(self.display_elem * elem_sharp_mltp * self.elem_global_mltp)

        # Calculate the effective raw/elem
        # Crit multiplier
        self.final_crit = round(self.crit + self.crit_buffs)
        # Convert the crit multipliers from float (1.xx) to int (xx)
        crit_mltp_value = (self.crit_mltp * 100) - 100
        crit_elem_mltp_value = (self.crit_elem_mltp * 100) - 100

        if self.final_crit >= 100:
            crit_calc = (1 + (crit_mltp_value / 100)) // 1
            elem_crit_calc = (1 + (crit_elem_mltp_value / 100)) // 1
        else:
            crit_calc = 1 + ((self.final_crit / 100) * (crit_mltp_value / 100))
            elem_crit_calc = 1 + ((self.final_crit / 100) * (crit_elem_mltp_value / 100))

        if self.buildup_boost_calc != 0:
            self.atk_global_mltp = ((self.atk_global_mltp - self.buildup_boost_calc)
                                    + self.buildup_boost_eff_raw)

        self.eff_raw = round(((self.display_atk * raw_sharp_mltp
                             * self.atk_global_mltp * crit_calc) + 0.1) // 1)
        self.eff_elem = round(((self.display_elem * elem_sharp_mltp *
                              self.elem_global_mltp * elem_crit_calc) + 0.1) // 1)

        # Calculate the damage
        self.phys_dmg = round(phys_atk * self.hzv)
        self.elem_dmg = round(elem_atk * self.ehzv)

        self.phys_crit_dmg = round(self.phys_dmg * self.crit_mltp)
        self.elem_crit_dmg = round(self.elem_dmg * self.crit_elem_mltp)

        self.tot_dmg = self.phys_dmg + self.elem_dmg
        self.tot_crit_dmg = self.phys_crit_dmg + self.elem_crit_dmg
        
    def _sharp_mod(self):
        """Calculate the sharpness modifier"""
        if self.sharp == 'Red':
            self.sharp_mltp = [0.5, 0.25]
        elif self.sharp == 'Orange':
            self.sharp_mltp = [0.75, 0.5]
        elif self.sharp == 'Yellow':
            self.sharp_mltp = [1, 0.75]
        elif self.sharp == 'Green':
            self.sharp_mltp = [1.05, 1]
        elif self.sharp == 'Blue':
            self.sharp_mltp = [1.2, 1.063]
        elif self.sharp == 'White':
            self.sharp_mltp = [1.32, 1.15]
        elif self.sharp == 'Purple':
            self.sharp_mltp = [1.39, 1.27]