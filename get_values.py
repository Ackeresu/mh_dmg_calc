class GetValues():
    """Class that get the values"""

    def __init__(self, dmg_calc_win):
        """Initialize the class"""
        self.dmg_calc_win = dmg_calc_win

        self.atk_mltp = 1
        self.atk_buffs = 0
        self.atk_global_mltp = 1

        self.elem_mltp = 1
        self.elem_buffs = 0
        self.elem_global_mltp = 1

        self.crit_mltp = 1.25
        self.crit_elem_mltp = 1.0
        self.crit_buffs = 0

    def get_values(self):
        """Get the values"""
        self._get_wpn_specific_values()
        self._get_wpn_values()
        self._get_other_values()
        self._get_skills_values()
    
    def _get_wpn_values(self):
        """Get the values from the entries and convert them if necessary"""
        self.raw = float(self.dmg_calc_win.raw_entry.get())
        self.elem = float(self.dmg_calc_win.elem_entry.get())
        self.crit = float(self.dmg_calc_win.crit_entry.get())
        self.sharp = self.dmg_calc_win.wpn.sharpness.get()

        self.mv = float(self.dmg_calc_win.mv_entry.get())
        self.mv = self.mv / 100
        self.hzv = float(self.dmg_calc_win.hzv_entry.get())
        self.hzv = self.hzv / 100
        self.ehzv = float(self.dmg_calc_win.ehzv_entry.get())
        self.ehzv = self.ehzv / 100

    def _get_wpn_specific_values(self):
        """"""
        gs_power_sheathe = self.dmg_calc_win.wpn.gs_power_sheathe
        ls_white_spirit_gauge = self.dmg_calc_win.wpn.ls_white_spirit_gauge
        ls_yellow_spirit_gauge = self.dmg_calc_win.wpn.ls_yellow_spirit_gauge
        ls_red_spirit_gauge = self.dmg_calc_win.wpn.ls_red_spirit_gauge
        db_demon_mode = self.dmg_calc_win.wpn.db_demon_mode
        db_archdemon_mode = self.dmg_calc_win.wpn.db_archdemon_mode
        db_feral_mode = self.dmg_calc_win.wpn.db_feral_mode
        lance_red_glow = self.dmg_calc_win.wpn.lance_red_glow
        lance_orange_glow = self.dmg_calc_win.wpn.lance_orange_glow
        lance_yellow_glow = self.dmg_calc_win.wpn.lance_yellow_glow
        lance_blue_glow = self.dmg_calc_win.wpn.lance_blue_glow
        gl_erupting_cannon = self.dmg_calc_win.wpn.gl_erupting_cannon
        cb_red_shield = self.dmg_calc_win.wpn.cb_red_shield
        bow_herculean_draw = self.dmg_calc_win.wpn.bow_herculean_draw

        if gs_power_sheathe == 1:
            self.atk_mltp += 0.1

        if ls_white_spirit_gauge == 1:
            self.atk_mltp += 0.04
        if ls_yellow_spirit_gauge == 1:
            self.atk_mltp += 0.08
        if ls_red_spirit_gauge == 1:
            self.atk_mltp += 0.12

        if db_demon_mode == 1:
            self.elem_mltp += 0.35
        if db_archdemon_mode == 1:
            self.elem_mltp += 0.2
        if db_feral_mode == 1:
            self.atk_mltp += 0.2

        if lance_red_glow == 1:
            self.atk_mltp += 0.05
        if (lance_orange_glow or lance_blue_glow) == 1:
            self.atk_mltp += 0.1
        if lance_yellow_glow == 1:
            self.atk_mltp += 0.15

        if gl_erupting_cannon == 1:
            self.atk_mltp += 0.3

        if cb_red_shield == 1:
            self.atk_mltp += 0.1

        if bow_herculean_draw == 1:
            self.atk_mltp += 0.1

    def _get_other_values(self):
        """Get the values not skill related"""
        # ---------- RAMPAGE DECO ----------
        element_exploit = self.dmg_calc_win.other.element_exploit
        hellion_mode = self.dmg_calc_win.other.hellion_mode
        anti_species = self.dmg_calc_win.other.anti_species
        small_monster_exploit = self.dmg_calc_win.other.small_monster_exploit
        blight_exploit = self.dmg_calc_win.other.blight_exploit
        magnamalo_soul = self.dmg_calc_win.other.magnamalo_soul
        valstrax_soul = self.dmg_calc_win.other.valstrax_soul
        kushala_daora_soul = self.dmg_calc_win.other.kushala_daora_soul
        narwa_soul = self.dmg_calc_win.other.narwa_soul
        bloody_heart = self.dmg_calc_win.other.bloody_heart

        if element_exploit == 1:
            self.elem_global_mltp += 0.15

        if hellion_mode == 1:
            self.crit_buffs += 20
        
        if anti_species == 1:
            self.atk_global_mltp += 0.05

        if small_monster_exploit == 1:
            self.atk_global_mltp += 0.5

        if blight_exploit == 1:
            self.atk_global_mltp += 0.1

        if magnamalo_soul == 1:
            self.atk_buffs += 12

        if valstrax_soul == 1:
            self.elem_global_mltp += 0.2

        if kushala_daora_soul == 1:
            self.crit_buffs += 15

        if narwa_soul == 1:
            self.crit_buffs += 40

        if bloody_heart == 1:
            self.atk_buffs += 30
            self.elem_global_mltp += 0.2

        # ---------- PETALACE ----------
        hunting_iii = self.dmg_calc_win.other.hunting_iii
        strength_iii = self.dmg_calc_win.other.strength_iii
        fortitude_iii = self.dmg_calc_win.other.fortitude_iii
        demon_iii = self.dmg_calc_win.other.demon_iii
        absolute = self.dmg_calc_win.other.absolute
        underworld = self.dmg_calc_win.other.underworld

        if hunting_iii == 1:
            self.atk_buffs += 13
        
        if strength_iii == 1:
            self.atk_buffs += 10

        if fortitude_iii == 1:
            self.atk_buffs += 8

        if demon_iii == 1:
            self.atk_buffs += 20

        if (absolute or underworld) == 1:
            self.atk_buffs += 15

        # ---------- ITEMS ----------
        powercharm = self.dmg_calc_win.other.powercharm.get()
        powertalon = self.dmg_calc_win.other.powertalon.get()
        might_seed = self.dmg_calc_win.other.might_seed.get()
        demon_powder = self.dmg_calc_win.other.demon_powder.get()
        demondrug = self.dmg_calc_win.other.demondrug.get()
        mega_demondrug = self.dmg_calc_win.other.mega_demondrug.get()

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

        # ---------- FOOD ----------
        dango_booster = self.dmg_calc_win.other.dango_booster.get()
        dango_booster_lvl = self.dmg_calc_win.other.dango_booster_lvl.get()
        dango_adrenaline = self.dmg_calc_win.other.dango_adrenaline.get()
        dango_adrenaline_lvl = self.dmg_calc_win.other.dango_adrenaline_lvl.get()
        dango_bulker = self.dmg_calc_win.other.dango_bulker.get()

        if dango_booster == 0:
            pass
        else:
            # Buff value per level: 6/9/12/15
            self.atk_buffs += (dango_booster_lvl * 3) + 3

        if dango_adrenaline == 0:
            pass
        elif dango_adrenaline_lvl == 1:
            self.atk_mltp += 0.25
        elif dango_adrenaline_lvl >= 2:
            self.atk_mltp += 0.3

        if dango_bulker == 1:
            self.atk_buffs += 15
        
        # ---------- HH SONGS ----------
        self.attack_song = self.dmg_calc_win.other.attack_up.get()
        self.affinity_song = self.dmg_calc_win.other.affinity_up.get()
        self.element_song = self.dmg_calc_win.other.element_up.get()
        self.infernal_melody = self.dmg_calc_win.other.infernal_melody.get()

        if self.attack_song == 1:
            self.atk_mltp += 0.1

        if self.affinity_song == 1:
            self.crit_buffs += 20

        if self.element_song == 1:
            self.elem_mltp += 0.1

        if self.infernal_melody == 1:
            self.atk_mltp += 0.2

        # ---------- OTHER ----------
        self.blue_scroll = self.dmg_calc_win.other.blue_scroll.get()
        self.beaten_frenzy = self.dmg_calc_win.other.beaten_frenzy.get()
        self.power_drum = self.dmg_calc_win.other.power_drum.get()
        self.rousing_roar = self.dmg_calc_win.other.rousing_roar.get()
        self.butterflame = self.dmg_calc_win.other.butterflame.get()
        self.cutterfly = self.dmg_calc_win.other.cutterfly.get()

        if self.beaten_frenzy == 1:
            self.crit_buffs += 15

        if self.power_drum == 1:
            self.atk_mltp += 0.05

        if self.rousing_roar == 1:
            self.crit_buffs += 30

        if self.butterflame == 1:
            self.atk_buffs += 25

        if self.cutterfly == 1:
            self.crit_buffs += 50

    def _get_skills_values(self):
        """Get the values from the active skills"""
         # Attack boost
        attack_boost = self.dmg_calc_win.skills.attack_boost
        attack_boost_lvl = self.dmg_calc_win.skills.attack_boost_lvl.get()

        if attack_boost == 0:
            pass
        elif attack_boost_lvl == 1:
            self.atk_buffs += 3
        elif attack_boost_lvl == 2:
            self.atk_buffs += 6
        elif attack_boost_lvl == 3:
            self.atk_buffs += 9
        elif attack_boost_lvl == 4:
            self.atk_mltp += 0.05
            self.atk_buffs += 7
        elif attack_boost_lvl == 5:
            self.atk_mltp += 0.06
            self.atk_buffs += 8
        elif attack_boost_lvl == 6:
            self.atk_mltp += 0.08
            self.atk_buffs += 9
        elif attack_boost_lvl == 7:
            self.atk_mltp += 0.1
            self.atk_buffs += 10

        # Agitator
        agitator = self.dmg_calc_win.skills.agitator
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
        peak_performance = self.dmg_calc_win.skills.peak_performance
        peak_performance_lvl = self.dmg_calc_win.skills.peak_performance_lvl.get()

        if peak_performance == 0:
            pass
        elif peak_performance_lvl == 1:
            self.atk_buffs += 5
        elif peak_performance_lvl == 2:
            self.atk_buffs += 10
        elif peak_performance_lvl == 3:
            self.atk_buffs += 20

        # Resentment
        resentment = self.dmg_calc_win.skills.resentment
        resentment_lvl = self.dmg_calc_win.skills.resentment_lvl.get()

        if resentment == 0:
            pass
        else:
            # Buff value per level: 5/10/15/20/25
            self.atk_buffs += (resentment_lvl * 5)

        # Resuscitate
        resuscitate = self.dmg_calc_win.skills.resuscitate
        resuscitate_lvl = self.dmg_calc_win.skills.resuscitate_lvl.get()

        if resuscitate == 0:
            pass
        #else:
        #    self.atk_buffs += ((resuscitate_lvl * 2) * 5) - 10
        elif resuscitate_lvl == 1:
            self.atk_buffs += 5
        elif resuscitate_lvl == 2:
            self.atk_buffs += 10
        elif resuscitate_lvl == 3:
            self.atk_buffs += 20

        # Buildup boost
        buildup_boost = self.dmg_calc_win.skills.buildup_boost
        buildup_boost_lvl = self.dmg_calc_win.skills.buildup_boost_lvl.get()

        if buildup_boost == 0:
            pass
        else:
            # Buff value per level: 0.1/0.15/0.20
            self.atk_global_mltp += ((buildup_boost_lvl * 5) + 5) / 100

        # Foray
        foray = self.dmg_calc_win.skills.foray
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
        counterstrike = self.dmg_calc_win.skills.counterstrike
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
        offensive_guard = self.dmg_calc_win.skills.offensive_guard
        offensive_guard_lvl = self.dmg_calc_win.skills.offensive_guard_lvl.get()

        if offensive_guard == 0:
            pass
        else:
            # Buff value per level: 0.05/0.1/0.15
            self.atk_mltp += (offensive_guard_lvl * 5) / 100

        # Heroics
        heroics = self.dmg_calc_win.skills.heroics
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

        # Elemental attack
        elemental_attack = self.dmg_calc_win.skills.elemental_attack
        elemental_attack_lvl = self.dmg_calc_win.skills.elemental_attack_lvl.get()

        if elemental_attack == 0:
            pass
        elif elemental_attack_lvl == 1:
            self.elem_buffs += 2
        elif elemental_attack_lvl == 2:
            self.elem_buffs += 3
        elif elemental_attack_lvl == 3:
            self.elem_mltp += 0.05
            self.elem_buffs += 4
        elif elemental_attack_lvl == 4:
            self.elem_mltp += 0.1
            self.elem_buffs += 4
        elif elemental_attack_lvl == 5:
            self.elem_mltp += 0.2
            self.elem_buffs += 4

        # Element exploit
        element_exploit = self.dmg_calc_win.skills.element_exploit
        element_exploit_lvl = self.dmg_calc_win.skills.element_exploit_lvl.get()

        if element_exploit == 0:
            pass
        else:
            # Buff value per level: 0.1/0.125/0.15
            self.elem_global_mltp += ((element_exploit_lvl - 1) * 0.025) + 0.1

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
        coalescence = self.dmg_calc_win.skills.coalescence
        coalescence_lvl = self.dmg_calc_win.skills.coalescence_lvl.get()

        if coalescence == 0:
            pass
        else:
            # Buff value per level: 12/15/18
            self.atk_buffs += (coalescence_lvl * 3) + 9
            # Buff value per level: 2/3/4
            self.elem_buffs += coalescence_lvl + 1

        # Bloodlust
        bloodlust = self.dmg_calc_win.skills.bloodlust
        bloodlust_lvl = self.dmg_calc_win.skills.bloodlust_lvl.get()

        if bloodlust == 0:
            pass
        # Infected
        elif bloodlust_lvl == 1 and self.beaten_frenzy == 0:
            self.atk_buffs += 10
            self.elem_buffs += 5
        elif bloodlust_lvl == 2 and self.beaten_frenzy == 0:
            self.atk_buffs += 15
            self.elem_buffs += 7
        elif bloodlust_lvl == 3 and self.beaten_frenzy == 0:
            self.atk_buffs += 20
            self.elem_buffs += 10
        # Beaten frenzy
        elif bloodlust_lvl == 1 and self.beaten_frenzy == 1:
            self.crit_buffs += 5
        elif bloodlust_lvl >= 2 and self.beaten_frenzy == 1:
            self.crit_buffs += 10

        # Mail of hellfire
        mail_of_hellfire = self.dmg_calc_win.skills.mail_of_hellfire
        mail_of_hellfire_lvl = self.dmg_calc_win.skills.mail_of_hellfire_lvl.get()

        if mail_of_hellfire == 0:
            pass
        # Red scroll
        elif self.blue_scroll == 0:
            # Buff value per level: 15/20/25
            self.atk_buffs += (mail_of_hellfire_lvl * 5) + 10
        # Blue scroll
        elif mail_of_hellfire_lvl == 1 and self.blue_scroll == 1:
            self.elem_mltp += 0.05
        elif mail_of_hellfire_lvl == 2 and self.blue_scroll == 1:
            self.elem_mltp += 0.1
        elif mail_of_hellfire_lvl == 3 and self.blue_scroll == 1:
            self.elem_mltp += 0.2

        # Critical eye
        critical_eye = self.dmg_calc_win.skills.critical_eye
        critical_eye_lvl = self.dmg_calc_win.skills.critical_eye_lvl.get()

        if critical_eye == 0:
            pass
        elif  1 <= critical_eye_lvl <= 6:
            self.crit_buffs += critical_eye_lvl * 5
        elif critical_eye_lvl == 7:
            self.crit_buffs += 40

        # Critical boost
        critical_boost = self.dmg_calc_win.skills.critical_boost
        critical_boost_lvl = self.dmg_calc_win.skills.critical_boost_lvl.get()

        if critical_boost == 0:
            pass
        else:
            # Buff value per level: 1.3/1.35/1.4
            self.crit_mltp = (critical_boost_lvl * 0.05) + 1.25
        
        # Critical element
        critical_element = self.dmg_calc_win.skills.critical_element
        critical_element_lvl = self.dmg_calc_win.skills.critical_element_lvl.get()

        if critical_element == 0:
            pass
        else:
            # Buff value per level: 0.05/0.1/0.15
            self.crit_elem_mltp = (critical_element_lvl * 5) / 100

        # Critical draw
        critical_draw = self.dmg_calc_win.skills.critical_draw
        critical_draw_lvl = self.dmg_calc_win.skills.critical_draw_lvl.get()

        if critical_draw == 0:
            pass
        elif critical_draw_lvl == 1:
            self.crit_buffs += 15
        elif critical_draw_lvl == 2:
            self.crit_buffs += 30
        elif critical_draw_lvl == 3:
            self.crit_buffs += 60

        # Latent power
        latent_power = self.dmg_calc_win.skills.latent_power
        latent_power_lvl = self.dmg_calc_win.skills.latent_power_lvl.get()

        if latent_power == 0:
            pass
        else:
            # Buff value per level: 10/20/30/40/50
            self.crit_buffs += latent_power_lvl * 10

        # Maximum might
        maximum_might = self.dmg_calc_win.skills.maximum_might
        maximum_might_lvl = self.dmg_calc_win.skills.maximum_might_lvl.get()

        if maximum_might == 0:
            pass
        else:
            # Buff value per level: 10/20/30
            self.crit_buffs += maximum_might_lvl * 10

        # Weakness exploit
        weakness_exploit = self.dmg_calc_win.skills.weakness_exploit
        weakness_exploit_lvl = self.dmg_calc_win.skills.weakness_exploit_lvl.get()

        if weakness_exploit == 0 or self.hzv < 0.45:
            pass
        elif weakness_exploit_lvl == 1:
            self.crit_buffs += 15
        elif weakness_exploit_lvl == 2:
            self.crit_buffs += 30
        elif weakness_exploit_lvl == 3:
            self.crit_buffs += 50

        # Sneak attack
        sneak_attack = self.dmg_calc_win.skills.sneak_attack
        sneak_attack_lvl = self.dmg_calc_win.skills.sneak_attack_lvl.get()

        if sneak_attack == 0:
            pass
        elif sneak_attack_lvl == 1:
            self.atk_global_mltp += 0.05
        elif sneak_attack_lvl == 2:
            self.atk_global_mltp += 0.1
        elif sneak_attack_lvl == 3:
            self.atk_global_mltp += 0.2

        # Kushala/Teostra blessing
        kushala_teostra_blessing = self.dmg_calc_win.skills.kushala_teostra_blessing
        kushala_teostra_blessing_lvl = self.dmg_calc_win.skills.kushala_teostra_blessing_lvl.get()

        if kushala_teostra_blessing == 0:
            pass
        elif kushala_teostra_blessing_lvl == 1:
            self.elem_mltp += 0.05
        elif kushala_teostra_blessing_lvl >= 2:
            self.elem_mltp += 0.10

        # Stormsoul
        stormsoul = self.dmg_calc_win.skills.stormsoul
        stormsoul_lvl = self.dmg_calc_win.skills.stormsoul_lvl.get()

        if stormsoul == 0:
            pass
        elif 1 <= stormsoul_lvl <= 2:
            # Buff value per level: 0.05/0.1
            self.elem_mltp += (stormsoul_lvl * 5) / 100
        elif stormsoul_lvl >= 3:
            self.elem_mltp += 0.15

        # Dragonheart
        dragonheart = self.dmg_calc_win.skills.dragonheart
        dragonheart_lvl = self.dmg_calc_win.skills.dragonheart_lvl.get()

        if dragonheart == 0:
            pass
        elif dragonheart_lvl >= 4:
            # Buff value per level: 0.05/0.1
            self.atk_mltp += (dragonheart_lvl - 3) * 0.05

        # Frostcraft
        frostcraft = self.dmg_calc_win.skills.frostcraft
        frostcraft_lvl = self.dmg_calc_win.skills.frostcraft_lvl.get()

        if frostcraft == 0:
            pass
        elif frostcraft_lvl == 1:
            self.atk_global_mltp += 0.05
        elif frostcraft_lvl == 2:
            self.atk_global_mltp += 0.2
        elif frostcraft_lvl == 3:
            self.atk_global_mltp += 0.3

        # Grinder
        grinder = self.dmg_calc_win.skills.grinder

        if grinder == 0:
            pass
        else:
            self.atk_global_mltp += 0.1
            self.elem_global_mltp += 0.075

        # Charge master
        charge_master = self.dmg_calc_win.skills.charge_master
        charge_master_lvl = self.dmg_calc_win.skills.charge_master_lvl.get()

        if charge_master == 0:
            pass
        else:
            # Buff value per level: 0.05/0.1/0.15
            self.elem_global_mltp += (charge_master_lvl * 5) / 100

        # Normal rapid up
        #normal_rapid_up = self.dmg_calc_win.skills.normal_rapid_up
        #normal_rapid_up_lvl = self.dmg_calc_win.skills.normal_rapid_up_lvl.get()

        #if normal_rapid_up == 0:
        #    pass
        #elif normal_rapid_up_lvl == 1:
        #    self.atk_global_mltp += 0.05
        #elif normal_rapid_up_lvl == 2:
        #    self.atk_global_mltp += 0.2
        #elif normal_rapid_up_lvl == 3:
        #    self.atk_global_mltp += 0.3

# -----------------------------------------------------------------------------
# ------------------------------ SPECIAL SKILLS -------------------------------
# -----------------------------------------------------------------------------

        # Fortify
        fortify = self.dmg_calc_win.skills.fortify
        carts_n = self.dmg_calc_win.skills.fortify_special.get()

        if fortify == 0:
            pass
        else:
            # Buff value per level: 0.1/0.2
            self.atk_mltp += carts_n / 10

        # Dereliction
        dereliction = self.dmg_calc_win.skills.dereliction
        dereliction_lvl = self.dmg_calc_win.skills.dereliction_lvl.get()
        qurio_n = self.dmg_calc_win.skills.dereliction_special.get()

        if dereliction == 0:
            pass
        # Red scroll
        elif self.blue_scroll == 0:
           self._check_qurio_red(dereliction_lvl, qurio_n)
        # Blue scroll
        elif self.blue_scroll == 1:
           self._check_qurio_blue(dereliction_lvl, qurio_n)

        # Strife
        strife = self.dmg_calc_win.skills.strife
        strife_lvl = self.dmg_calc_win.skills.strife_lvl.get()
        red_health = self.dmg_calc_win.skills.strife_special.get()

        if strife == 0:
            pass
        elif red_health == '<60%':
            if strife_lvl == 1:
                self.elem_mltp += 0.05
                self.crit_buffs += 5
            elif strife_lvl == 2:
                self.elem_mltp += 0.1
                self.crit_buffs += 10
            elif strife_lvl == 3:
                self.elem_mltp += 0.15
                self.crit_buffs += 10
        elif red_health == '>60%':
            # Buff value per level: 0.1/0.15/0.2
            self.elem_mltp += ((strife_lvl * 5) / 100) + 0.05
            # Buff value per level: 10/15/20
            self.crit_buffs += (strife_lvl * 5) + 5

    def _check_qurio_red(self, dereliction_lvl, qurio_n):
        """Check the value for the buff in the red scroll"""
        if dereliction_lvl == 1:
            if qurio_n == 1:
                self.elem_buffs += 5
            elif qurio_n == 2:
                self.elem_buffs += 8
            elif qurio_n == 3:
                self.elem_buffs += 12
        elif dereliction_lvl == 2:
            if qurio_n == 1:
                self.elem_buffs += 7
            elif qurio_n == 2:
                self.elem_buffs += 12
            elif qurio_n == 3:
                self.elem_buffs += 15
        elif dereliction_lvl == 3:
            if qurio_n == 1:
                self.elem_buffs += 10
            elif qurio_n == 2:
                self.elem_buffs += 15
            elif qurio_n == 3:
                self.elem_buffs += 20

    def _check_qurio_blue(self, dereliction_lvl, qurio_n):
        """Calculate the value for the buff in the blue scroll"""
        self.atk_buffs += (dereliction_lvl * 5) + (qurio_n * 5) + 5