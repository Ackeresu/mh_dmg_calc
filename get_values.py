class GetValues():
    """Class that get the values"""

    def __init__(self, dmg_calc_win):
        """Initialize the class"""
        self.dmg_calc_win = dmg_calc_win

        self.scroll_color = self.dmg_calc_win.items.scroll_color.get()
        self.beaten_frenzy = self.dmg_calc_win.items.beaten_frenzy.get()

    def get_values(self):
        """Get the values"""
        self._get_weapon_values()
        self._get_options_values()
        self._get_items_values()
        self._get_skills_values()
    
    def _get_weapon_values(self):
        """Get the values from the entries and convert them if necessary"""
        self.raw = float(self.dmg_calc_win.raw_entry.get())
        self.elem = float(self.dmg_calc_win.elem_entry.get())
        self.crit = float(self.dmg_calc_win.crit_entry.get())
        self.sharp = self.dmg_calc_win.sharp_entry.get()
        self.sharp = self.sharp.lower()

        self.mv = float(self.dmg_calc_win.mv_entry.get())
        self.mv = self.mv / 100
        self.hzv = float(self.dmg_calc_win.hzv_entry.get())
        self.hzv = self.hzv / 100
        self.ehzv = float(self.dmg_calc_win.ehzv_entry.get())
        self.ehzv = self.ehzv / 100

        self.atk_mltp = 1
        self.atk_buffs = 0
        self.atk_global_mltp = 1

        self.elem_mltp = 1
        self.elem_buffs = 0
        self.elem_global_mltp = 1

        self.crit_mltp = 1.25
        self.crit_elem_mltp = 1.0
        self.crit_buffs = 0

    def _get_options_values(self):
        """Get the values from the options"""
        beaten_frenzy = self.dmg_calc_win.items.beaten_frenzy.get()

        if beaten_frenzy == 1:
            self.crit_buffs += 15

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

# -----------------------------------------------------------------------------
# --------------------------------- ATTACK ------------------------------------
# -----------------------------------------------------------------------------

        # Attack boost
        atk_boost = self.dmg_calc_win.skills.attack_boost
        atk_boost_lvl = self.dmg_calc_win.skills.attack_boost_lvl.get()

        if atk_boost == 0:
            pass
        elif atk_boost_lvl == 1:
            self.atk_buffs += 3
        elif atk_boost_lvl == 2:
            self.atk_buffs += 6
        elif atk_boost_lvl == 3:
            self.atk_buffs += 9
        elif atk_boost_lvl == 4:
            self.atk_mltp += 0.05
            self.atk_buffs += 7
        elif atk_boost_lvl == 5:
            self.atk_mltp += 0.06
            self.atk_buffs += 8
        elif atk_boost_lvl == 6:
            self.atk_mltp += 0.08
            self.atk_buffs += 9
        elif atk_boost_lvl == 7:
            self.atk_mltp += 0.1
            self.atk_buffs += 10

        # Agitator
        agitator = self.dmg_calc_win.skills.agitator.get()
        agitator_lvl = self.dmg_calc_win.skills.agitator_lvl.get()

        if agitator == 0:
            pass
        elif agitator_lvl == 1:
            self.atk_buffs += 4
            self.crit_buffs += 3
        elif agitator_lvl == 2:
            self.atk_buffs += 8
            self.crit_buffs += 5
        elif agitator_lvl == 3:
            self.atk_buffs += 12
            self.crit_buffs += 7
        elif agitator_lvl == 4:
            self.atk_buffs += 16
            self.crit_buffs += 10
        elif agitator_lvl == 5:
            self.atk_buffs += 20
            self.crit_buffs += 15
        
        # Peak performance
        peak_perf = self.dmg_calc_win.skills.peak_perf.get()
        peak_perf_lvl = self.dmg_calc_win.skills.peak_perf_lvl.get()

        if peak_perf == 0:
            pass
        elif peak_perf_lvl == 1:
            self.atk_buffs += 5
        elif peak_perf_lvl == 2:
            self.atk_buffs += 10
        elif peak_perf_lvl == 3:
            self.atk_buffs += 20

        # Resentment
        resentment = self.dmg_calc_win.skills.resentment.get()
        resentment_lvl = self.dmg_calc_win.skills.resentment_lvl.get()

        if resentment == 0:
            pass
        elif resentment_lvl == 1:
            self.atk_buffs += 5
        elif resentment_lvl == 2:
            self.atk_buffs += 10
        elif resentment_lvl == 3:
            self.atk_buffs += 15
        elif resentment_lvl == 4:
            self.atk_buffs += 20
        elif resentment_lvl == 5:
            self.atk_buffs += 25

        # Resuscitate
        resuscitate = self.dmg_calc_win.skills.resuscitate.get()
        resuscitate_lvl = self.dmg_calc_win.skills.resuscitate_lvl.get()

        if resuscitate == 0:
            pass
        elif resuscitate_lvl == 1:
            self.atk_buffs += 5
        elif resuscitate_lvl == 2:
            self.atk_buffs += 10
        elif resuscitate_lvl == 3:
            self.atk_buffs += 20

        # Buildup boost
        bu_boost = self.dmg_calc_win.skills.bu_boost.get()
        bu_boost_lvl = self.dmg_calc_win.skills.bu_boost_lvl.get()

        if bu_boost == 0:
            pass
        elif bu_boost_lvl == 1:
            self.atk_global_mltp += 0.1
        elif bu_boost_lvl == 2:
            self.atk_global_mltp += 0.15
        elif bu_boost_lvl == 3:
            self.atk_global_mltp += 0.2

        # Foray
        foray = self.dmg_calc_win.skills.foray.get()
        foray_lvl = self.dmg_calc_win.skills.foray_lvl.get()

        if foray == 0:
            pass
        elif foray_lvl == 1:
            self.atk_buffs += 10
        elif foray_lvl == 2:
            self.atk_buffs += 10
            self.crit_buffs += 10
        elif foray_lvl == 3:
            self.atk_buffs += 15
            self.crit_buffs += 20

        # Counterstrike
        counterstrike = self.dmg_calc_win.skills.counterstrike.get()
        counterstrike_lvl = self.dmg_calc_win.skills.counterstrike_lvl.get()

        if counterstrike == 0:
            pass
        elif counterstrike_lvl == 1:
            self.atk_buffs += 10
        elif counterstrike_lvl == 2:
            self.atk_buffs += 15
        elif counterstrike_lvl == 3:
            self.atk_buffs += 25

        # Offensive guard
        off_guard = self.dmg_calc_win.skills.off_guard.get()
        off_guard_lvl = self.dmg_calc_win.skills.off_guard_lvl.get()

        if off_guard == 0:
            pass
        elif off_guard_lvl == 1:
            self.atk_mltp += 0.05
        elif off_guard_lvl == 2:
            self.atk_mltp += 0.1
        elif off_guard_lvl == 3:
            self.atk_mltp += 0.15

        # Heroics
        heroics = self.dmg_calc_win.skills.heroics.get()
        heroics_lvl = self.dmg_calc_win.skills.heroics_lvl.get()

        if heroics == 0:
            pass
        elif heroics_lvl == 1:
            pass
        elif heroics_lvl == 2:
            self.atk_mltp += 0.05
        elif heroics_lvl == 3:
            self.atk_mltp += 0.05
        elif heroics_lvl == 4:
            self.atk_mltp += 0.1
        elif heroics_lvl == 5:
            self.atk_mltp += 0.3

        # Fortify
        fortify = self.dmg_calc_win.skills.fortify.get()
        fortify_lvl = self.dmg_calc_win.skills.fortify_lvl.get()

        if fortify == 0:
            pass
        elif fortify_lvl == 1:
            self.atk_mltp += 0.1
        elif fortify_lvl == 2:
            self.atk_mltp += 0.2

# -----------------------------------------------------------------------------
# -------------------------------- ELEMENT ------------------------------------
# -----------------------------------------------------------------------------

        # Elem attack
        elem_atk = self.dmg_calc_win.skills.elem_atk.get()
        elem_atk_lvl = self.dmg_calc_win.skills.elem_atk_lvl.get()

        if elem_atk == 0:
            pass
        elif elem_atk_lvl == 1:
            self.elem_buffs += 2
        elif elem_atk_lvl == 2:
            self.elem_buffs += 3
        elif elem_atk_lvl == 3:
            self.elem_mltp += 0.05
            self.elem_buffs += 4
        elif elem_atk_lvl == 4:
            self.elem_mltp += 0.1
            self.elem_buffs += 4
        elif elem_atk_lvl == 5:
            self.elem_mltp += 0.2
            self.elem_buffs += 4

        # Element exploit
        elem_ex = self.dmg_calc_win.skills.elem_ex.get()
        elem_ex_lvl = self.dmg_calc_win.skills.elem_ex_lvl.get()

        if elem_ex == 0:
            pass
        elif elem_ex_lvl == 1:
            self.elem_global_mltp += 0.1
        elif elem_ex_lvl == 2:
            self.elem_global_mltp += 0.125
        elif elem_ex_lvl == 3:
            self.elem_global_mltp += 0.15

        # Burst
        burst = self.dmg_calc_win.skills.burst
        burst_lvl = self.dmg_calc_win.skills.burst_lvl.get()

        if burst == 0:
            pass
        elif burst_lvl == 1:
            self.atk_buffs += 8
            self.elem_buffs += 8
        elif burst_lvl == 2:
            self.atk_buffs += 12
            self.elem_buffs += 10
        elif burst_lvl == 3:
            self.atk_buffs += 15
            self.elem_buffs += 15

        # Coalescence
        coalescence = self.dmg_calc_win.skills.coalescence.get()
        coalescence_lvl = self.dmg_calc_win.skills.coalescence_lvl.get()

        if coalescence == 0:
            pass
        elif coalescence_lvl == 1:
            self.atk_buffs += 12
            self.elem_buffs += 2
        elif coalescence_lvl == 2:
            self.atk_buffs += 15
            self.elem_buffs += 3
        elif coalescence_lvl == 3:
            self.atk_buffs += 18
            self.elem_buffs += 4

        # Bloodlust
        bloodlust = self.dmg_calc_win.skills.bloodlust.get()
        bloodlust_lvl = self.dmg_calc_win.skills.bloodlust_lvl.get()

        if bloodlust == 0:
            pass
        elif bloodlust_lvl == 1 and self.beaten_frenzy == 0:
            self.atk_buffs += 10
            self.elem_buffs += 5
        elif bloodlust_lvl == 1 and self.beaten_frenzy == 1:
            self.crit_buffs += 5
        elif bloodlust_lvl == 2 and self.beaten_frenzy == 0:
            self.atk_buffs += 15
            self.elem_buffs += 7
        elif bloodlust_lvl == 2 and self.beaten_frenzy == 1:
            self.crit_buffs += 10
        elif bloodlust_lvl == 3 and self.beaten_frenzy == 0:
            self.atk_buffs += 20
            self.elem_buffs += 10
        elif bloodlust_lvl == 3 and self.beaten_frenzy == 1:
            self.crit_buffs += 10

        # Mail of hellfire
        mail_hellfire = self.dmg_calc_win.skills.mail_hellfire.get()
        mail_hellfire_lvl = self.dmg_calc_win.skills.mail_hellfire_lvl.get()

        if mail_hellfire == 0:
            pass
        elif mail_hellfire_lvl == 1 and self.scroll_color == 0:
            self.atk_buffs += 15
        elif mail_hellfire_lvl == 1 and self.scroll_color == 1:
            self.elem_mltp += 0.05
        elif mail_hellfire_lvl == 2 and self.scroll_color == 0:
            self.atk_buffs += 20
        elif mail_hellfire_lvl == 2 and self.scroll_color == 1:
            self.elem_mltp += 0.1
        elif mail_hellfire_lvl == 3 and self.scroll_color == 0:
            self.atk_buffs += 25
        elif mail_hellfire_lvl == 3 and self.scroll_color == 1:
            self.elem_mltp += 0.2

# -----------------------------------------------------------------------------
# -------------------------------- AFFINITY -----------------------------------
# -----------------------------------------------------------------------------

        # Critical eye
        crit_eye = self.dmg_calc_win.skills.crit_eye.get()
        crit_eye_lvl = self.dmg_calc_win.skills.crit_eye_lvl.get()

        if crit_eye == 0:
            pass
        elif crit_eye_lvl == 1:
            self.crit_buffs += 5
        elif crit_eye_lvl == 2:
            self.crit_buffs += 10
        elif crit_eye_lvl == 3:
            self.crit_buffs += 15
        elif crit_eye_lvl == 4:
            self.crit_buffs += 20
        elif crit_eye_lvl == 5:
            self.crit_buffs += 25
        elif crit_eye_lvl == 6:
            self.crit_buffs += 30
        elif crit_eye_lvl == 7:
            self.crit_buffs += 40

        # Critical boost
        crit_boost = self.dmg_calc_win.skills.critical_boost
        crit_boost_lvl = self.dmg_calc_win.skills.critical_boost_lvl.get()

        if crit_boost == 0:
            pass
        elif crit_boost_lvl == 1:
            self.crit_mltp = 1.3
        elif crit_boost_lvl == 2:
            self.crit_mltp = 1.35
        elif crit_boost_lvl == 3:
            self.crit_mltp = 1.4
        
        # Critical element
        crit_elem = self.dmg_calc_win.skills.crit_elem.get()
        crit_elem_lvl = self.dmg_calc_win.skills.crit_elem_lvl.get()

        if crit_elem == 0:
            pass
        elif crit_elem_lvl == 1:
            self.crit_elem_mltp = 1.05
        elif crit_elem_lvl == 2:
            self.crit_elem_mltp = 1.1
        elif crit_elem_lvl == 3:
            self.crit_elem_mltp = 1.15

        # Critical draw
        crit_draw = self.dmg_calc_win.skills.crit_draw.get()
        crit_draw_lvl = self.dmg_calc_win.skills.crit_draw_lvl.get()

        if crit_draw == 0:
            pass
        elif crit_draw_lvl == 1:
            self.crit_buffs += 10
        elif crit_draw_lvl == 2:
            self.crit_buffs += 20
        elif crit_draw_lvl == 3:
            self.crit_buffs += 30

        # Latent power
        latent_power = self.dmg_calc_win.skills.latent_power.get()
        latent_power_lvl = self.dmg_calc_win.skills.latent_power_lvl.get()

        if latent_power == 0:
            pass
        elif latent_power_lvl == 1:
            self.crit_buffs += 10
        elif latent_power_lvl == 2:
            self.crit_buffs += 20
        elif latent_power_lvl == 3:
            self.crit_buffs += 30
        elif latent_power_lvl == 4:
            self.crit_buffs += 40
        elif latent_power_lvl == 5:
            self.crit_buffs += 50

        # Maximum might
        max_might = self.dmg_calc_win.skills.max_might.get()
        max_might_lvl = self.dmg_calc_win.skills.max_might_lvl.get()

        if max_might == 0:
            pass
        elif max_might_lvl == 1:
            self.crit_buffs += 10
        elif max_might_lvl == 2:
            self.crit_buffs += 20
        elif max_might_lvl == 3:
            self.crit_buffs += 30

        # Weakness exploit
        weak_ex = self.dmg_calc_win.skills.weak_ex.get()
        weak_ex_lvl = self.dmg_calc_win.skills.weak_ex_lvl.get()

        if weak_ex == 0 or self.hzv < 0.45:
            pass
        elif weak_ex_lvl == 1:
            self.crit_buffs += 15
        elif weak_ex_lvl == 2:
            self.crit_buffs += 30
        elif weak_ex_lvl == 3:
            self.crit_buffs += 50