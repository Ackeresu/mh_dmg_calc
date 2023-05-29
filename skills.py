import tkinter as tk

class Skills:
    """A class that manage the skills data"""

    def __init__(self):
        """Initialize the skills"""
        # Initialize the list of skills
        self.skill_list = ('attack boost', 'agitator', 'peak performance',
                           'resentment', 'resuscitate', 'buildup boost',
                           'foray', 'counterstrike', 'offensive guard',
                           'heroics', 'fortify', 'elemental attack',
                           'element exploit', 'burst', 'coalescence',
                           'bloodlust', 'mail of hellfire', 'critical eye',
                           'critical boost', 'critical element',
                           'critical draw', 'latent power', 'maximum might',
                           'weakness exploit', 'sneak attack',
                           'kushala teostra blessing', 'stormsoul',
                           'dragonheart', )
        
        # Format the skills and then order them in alphabetical order
        self.skill_list = [skill.title() for skill in self.skill_list]
        self.skill_list = sorted(self.skill_list)

# -----------------------------------------------------------------------------
# --------------------------------- SKILLS ------------------------------------
# -----------------------------------------------------------------------------

        # Attack boost
        self.attack_boost = 0
        self.attack_boost_lvl = tk.IntVar()
        self.attack_boost_lvl.set(7)
        self.attack_boost_lvl_list = list(range(1, 8))

        # Agitator
        self.agitator = 0
        self.agitator_lvl = tk.IntVar()
        self.agitator_lvl.set(5)
        self.agitator_lvl_list = list(range(1, 6))

        # Peak performance
        self.peak_performance = 0
        self.peak_performance_lvl = tk.IntVar()
        self.peak_performance_lvl.set(3)
        self.peak_performance_lvl_list = list(range(1, 4))

        # Resentment
        self.resentment = 0
        self.resentment_lvl = tk.IntVar()
        self.resentment_lvl.set(5)
        self.resentment_lvl_list = list(range(1, 6))

        # Resuscitate
        self.resuscitate = 0
        self.resuscitate_lvl = tk.IntVar()
        self.resuscitate_lvl.set(3)
        self.resuscitate_lvl_list = list(range(1, 4))

        # Buildup boost
        self.buildup_boost = 0
        self.buildup_boost_lvl = tk.IntVar()
        self.buildup_boost_lvl.set(3)
        self.buildup_boost_lvl_list = list(range(1, 4))

        # Foray
        self.foray = 0
        self.foray_lvl = tk.IntVar()
        self.foray_lvl.set(3)
        self.foray_lvl_list = list(range(1, 4))

        # Counterstrike
        self.counterstrike = 0
        self.counterstrike_lvl = tk.IntVar()
        self.counterstrike_lvl.set(3)
        self.counterstrike_lvl_list = list(range(1, 4))

        # Offensive guard
        self.offensive_guard = 0
        self.offensive_guard_lvl = tk.IntVar()
        self.offensive_guard_lvl.set(3)
        self.offensive_guard_lvl_list = list(range(1, 4))

        # Heroics
        self.heroics = 0
        self.heroics_lvl = tk.IntVar()
        self.heroics_lvl.set(5)
        self.heroics_lvl_list = list(range(1, 6))

        # Fortify
        self.fortify = 0
        self.fortify_lvl = tk.IntVar()
        self.fortify_lvl.set(1)
        self.fortify_lvl_list = [1]

        # Elemental attack
        self.elemental_attack = 0
        self.elemental_attack_lvl = tk.IntVar()
        self.elemental_attack_lvl.set(5)
        self.elemental_attack_lvl_list = list(range(1, 6))

        # Element exploit
        self.element_exploit = 0
        self.element_exploit_lvl = tk.IntVar()
        self.element_exploit_lvl.set(3)
        self.element_exploit_lvl_list = list(range(1, 4))

        # Burst
        self.burst = 0
        self.burst_lvl = tk.IntVar()
        self.burst_lvl.set(3)
        self.burst_lvl_list = list(range(1, 4))
        self.burst_lvl_list = list(range(1, 4))

        # Coalescence
        self.coalescence = 0
        self.coalescence_lvl = tk.IntVar()
        self.coalescence_lvl.set(3)
        self.coalescence_lvl_list = list(range(1, 4))

        # Bloodlust
        self.bloodlust = 0
        self.bloodlust_lvl = tk.IntVar()
        self.bloodlust_lvl.set(3)
        self.bloodlust_lvl_list = list(range(1, 4))

        # Mail of hellfire
        self.mail_of_hellfire = 0
        self.mail_of_hellfire_lvl = tk.IntVar()
        self.mail_of_hellfire_lvl.set(3)
        self.mail_of_hellfire_lvl_list = list(range(1, 4))

        # Critical eye
        self.critical_eye = 0
        self.critical_eye_lvl = tk.IntVar()
        self.critical_eye_lvl.set(7)
        self.critical_eye_lvl_list = list(range(1, 8))

        # Critical boost
        self.critical_boost = 0
        self.critical_boost_lvl = tk.IntVar()
        self.critical_boost_lvl.set(3)
        self.critical_boost_lvl_list = list(range(1, 4))

        # Critical element
        self.critical_element = 0
        self.critical_element_lvl = tk.IntVar()
        self.critical_element_lvl.set(3)
        self.critical_element_lvl_list = list(range(1, 4))

        # Critical draw
        self.critical_draw = 0
        self.critical_draw_lvl = tk.IntVar()
        self.critical_draw_lvl.set(3)
        self.critical_draw_lvl_list = list(range(1, 4))

        # Latent power
        self.latent_power = 0
        self.latent_power_lvl = tk.IntVar()
        self.latent_power_lvl.set(5)
        self.latent_power_lvl_list = list(range(1, 4))

        # Maximum might
        self.maximum_might = 0
        self.maximum_might_lvl = tk.IntVar()
        self.maximum_might_lvl.set(3)
        self.maximum_might_lvl_list = list(range(1, 4))

        # Weakness exploit
        self.weakness_exploit = 0
        self.weakness_exploit_lvl = tk.IntVar()
        self.weakness_exploit_lvl.set(3)
        self.weakness_exploit_lvl_list = list(range(1, 4))

        # Sneak attack
        self.sneak_attack = 0
        self.sneak_attack_lvl = tk.IntVar()
        self.sneak_attack_lvl.set(3)
        self.sneak_attack_lvl_list = list(range(1, 4))

        # Kushala/Teostra blessing
        self.kushala_teostra_blessing = 0
        self.kushala_teostra_blessing_lvl = tk.IntVar()
        self.kushala_teostra_blessing_lvl.set(4)
        self.kushala_teostra_blessing_lvl_list = list(range(1, 5))

        # Stormsoul
        self.stormsoul = 0
        self.stormsoul_lvl = tk.IntVar()
        self.stormsoul_lvl.set(5)
        self.stormsoul_lvl_list = list(range(1, 6))

        # Dragonheart
        self.dragonheart = 0
        self.dragonheart_lvl = tk.IntVar()
        self.dragonheart_lvl.set(5)
        self.dragonheart_lvl_list = list(range(1, 6))