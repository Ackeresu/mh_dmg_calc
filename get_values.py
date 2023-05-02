class GetValues():
    """Class that get the values"""

    def __init__(self, dmg_calc_win):
        """Initialize the class"""
        self.dmg_calc_win = dmg_calc_win

    def get_values(self):
        """Get the values"""
        self._get_weapon_values()
        self._get_items_values()
        self._get_skills_values()
    
    def _get_weapon_values(self):
        """Get the values from the entries and convert them if necessary"""
        self.raw = float(self.dmg_calc_win.raw_entry.get())
        self.elem = float(self.dmg_calc_win.elem_entry.get())
        self.crit = float(self.dmg_calc_win.crit_entry.get())
        self.sharp = self.dmg_calc_win.sharp_entry.get()

        self.mv = float(self.dmg_calc_win.mv_entry.get())
        self.mv = self.mv / 100
        self.hzv = float(self.dmg_calc_win.hzv_entry.get())
        self.hzv = self.hzv / 100
        self.ehzv = float(self.dmg_calc_win.ehzv_entry.get())
        self.ehzv = self.ehzv / 100

        self.atk_mltp = 1
        self.atk_buffs = 0
        self.elem_mltp = 1
        self.elem_buffs = 0
        self.crit_buffs = 0

    def _get_items_values(self):
        """Get the values from the active items"""
        powercharm = self.dmg_calc_win.items.powercharm.get()
        powertalon = self.dmg_calc_win.items.powertalon.get()
        might_seed = self.dmg_calc_win.items.might_seed.get()
        demon_powder = self.dmg_calc_win.items.demon_powder.get()
        demondrug = self.dmg_calc_win.items.demondrug.get()
        mega_demondrug = self.dmg_calc_win.items.mega_demondrug.get()

        if powercharm == 1:
            self.atk_buffs += 6
        if powertalon == 1:
            self.atk_buffs += 9
        if mega_demondrug == 1:
            self.atk_buffs += 7
        if demondrug == 1:
            self.atk_buffs += 5
        if might_seed == 1:
            self.atk_buffs += 10
        if demon_powder == 1:
            self.atk_buffs += 10

    def _get_skills_values(self):
        """Get the values from the active skills"""
        # ----- Attack -----
        # Attack boost
        atk_boost = self.dmg_calc_win.skills.atk_boost.get()
        atk_boost_lvl = self.dmg_calc_win.skills.atk_boost_lvl.get()

        if atk_boost == 1 and atk_boost_lvl == 1:
            self.atk_buffs += 3
        elif atk_boost == 1 and atk_boost_lvl == 2:
            self.atk_buffs += 6
        elif atk_boost == 1 and atk_boost_lvl == 3:
            self.atk_buffs += 9
        elif atk_boost == 1 and atk_boost_lvl == 4:
            self.atk_mltp = 1.05
            self.atk_buffs += 7
        elif atk_boost == 1 and atk_boost_lvl == 5:
            self.atk_mltp = 1.06
            self.atk_buffs += 8
        elif atk_boost == 1 and atk_boost_lvl == 6:
            self.atk_mltp = 1.08
            self.atk_buffs += 9
        elif atk_boost == 1 and atk_boost_lvl == 7:
            self.atk_mltp = 1.10
            self.atk_buffs += 10

        # Agitator
        agitator = self.dmg_calc_win.skills.agitator.get()
        agitator_lvl = self.dmg_calc_win.skills.agitator_lvl.get()

        if agitator == 1 and agitator_lvl == 1:
            self.atk_buffs += 4
            self.crit_buffs += 3
        elif agitator == 1 and agitator_lvl == 2:
            self.atk_buffs += 8
            self.crit_buffs += 5
        elif agitator == 1 and agitator_lvl == 3:
            self.atk_buffs += 12
            self.crit_buffs += 7
        elif agitator == 1 and agitator_lvl == 4:
            self.atk_buffs += 16
            self.crit_buffs += 10
        elif agitator == 1 and agitator_lvl == 5:
            self.atk_buffs += 20
            self.crit_buffs += 15
        
        # Peak performance
        peak_perf = self.dmg_calc_win.skills.peak_perf.get()
        peak_perf_lvl = self.dmg_calc_win.skills.peak_perf_lvl.get()

        if peak_perf == 1 and peak_perf_lvl == 1:
            self.atk_buffs += 5
        elif peak_perf == 1 and peak_perf_lvl == 2:
            self.atk_buffs += 10
        elif peak_perf == 1 and peak_perf_lvl == 3:
            self.atk_buffs += 20

        # Resentment
        resentment = self.dmg_calc_win.skills.resentment.get()
        resentment_lvl = self.dmg_calc_win.skills.resentment_lvl.get()

        if resentment == 1 and resentment_lvl == 1:
            self.atk_buffs += 5
        elif resentment == 1 and resentment_lvl == 2:
            self.atk_buffs += 10
        elif resentment == 1 and resentment_lvl == 3:
            self.atk_buffs += 15
        elif resentment == 1 and resentment_lvl == 4:
            self.atk_buffs += 20
        elif resentment == 1 and resentment_lvl == 5:
            self.atk_buffs += 25

        # Resuscitate
        resuscitate = self.dmg_calc_win.skills.resuscitate.get()
        resuscitate_lvl = self.dmg_calc_win.skills.resuscitate_lvl.get()

        if resuscitate == 1 and resuscitate_lvl == 1:
            self.atk_buffs += 5
        elif resuscitate == 1 and resuscitate_lvl == 2:
            self.atk_buffs += 10
        elif resuscitate == 1 and resuscitate_lvl == 3:
            self.atk_buffs += 20
        
        # ----- Element -----
        # Elem attack
        elem_atk = self.dmg_calc_win.skills.elem_atk.get()
        elem_atk_lvl = self.dmg_calc_win.skills.elem_atk_lvl.get()

        if elem_atk == 1 and elem_atk_lvl == 1:
            self.elem_buffs += 2
        elif elem_atk == 1 and elem_atk_lvl == 2:
            self.elem_buffs += 3
        elif elem_atk == 1 and elem_atk_lvl == 3:
            self.elem_mltp = 1.05
            self.elem_buffs += 4
        elif elem_atk == 1 and elem_atk_lvl == 4:
            self.elem_mltp = 1.10
            self.elem_buffs += 4
        elif elem_atk == 1 and elem_atk_lvl == 5:
            self.elem_mltp = 1.20
            self.elem_buffs += 4

        # ----- Affinity -----
        # Critical eye
        crit_eye = self.dmg_calc_win.skills.crit_eye.get()
        crit_eye_lvl = self.dmg_calc_win.skills.crit_eye_lvl.get()

        if crit_eye == 1 and crit_eye_lvl == 1:
            self.crit_buffs += 5
        elif crit_eye == 1 and crit_eye_lvl == 2:
            self.crit_buffs += 10
        elif crit_eye == 1 and crit_eye_lvl == 3:
            self.crit_buffs += 15
        elif crit_eye == 1 and crit_eye_lvl == 4:
            self.crit_buffs += 20
        elif crit_eye == 1 and crit_eye_lvl == 5:
            self.crit_buffs += 25
        elif crit_eye == 1 and crit_eye_lvl == 6:
            self.crit_buffs += 30
        elif crit_eye == 1 and crit_eye_lvl == 7:
            self.crit_buffs += 40

        # Critical boost
        crit_boost = self.dmg_calc_win.skills.crit_boost.get()
        crit_boost_lvl = self.dmg_calc_win.skills.crit_boost_lvl.get()

        if crit_boost == 0:
            self.crit_mltp = 1.25
            self.crit_mltp_value = 25
        elif crit_boost == 1 and crit_boost_lvl == 1:
            self.crit_mltp = 1.30
            self.crit_mltp_value = 30
        elif crit_boost == 1 and crit_boost_lvl == 2:
            self.crit_mltp = 1.35
            self.crit_mltp_value = 35
        elif crit_boost == 1 and crit_boost_lvl == 3:
            self.crit_mltp = 1.40
            self.crit_mltp_value = 40
        
        # Critical element
        crit_elem = self.dmg_calc_win.skills.crit_elem.get()
        crit_elem_lvl = self.dmg_calc_win.skills.crit_elem_lvl.get()

        if crit_elem == 0:
            self.crit_elem_mltp = 1.0
        elif crit_elem == 1 and crit_elem_lvl == 1:
            self.crit_elem_mltp = 1.05
        elif crit_elem == 1 and crit_elem_lvl == 2:
            self.crit_elem_mltp = 1.10
        elif crit_elem == 1 and crit_elem_lvl == 3:
            self.crit_elem_mltp = 1.15

        # Weakness exploit
        weak_ex = self.dmg_calc_win.skills.weak_ex.get()
        weak_ex_lvl = self.dmg_calc_win.skills.weak_ex_lvl.get()

        if self.hzv < 0.45:
            pass
        elif weak_ex == 1 and weak_ex_lvl == 1:
            self.crit_buffs += 15
        elif weak_ex == 1 and weak_ex_lvl == 2:
            self.crit_buffs += 30
        elif weak_ex == 1 and weak_ex_lvl == 3:
            self.crit_buffs += 50