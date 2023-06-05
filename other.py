import tkinter as tk

class Other():
    """A class that manage buffs that are not skill-related"""

    def __init__(self):
        """Initialize the variables"""
        self.rampage_deco_list = ['none', 'anti species', 'blight exploit',
                                  'bloody heart', 'element exploit',
                                  'hellion mode', 'kushala daora soul',
                                  'magnamalo soul', 'narwa soul',
                                  'small monster exploit', 'valstrax soul']
        self.rampage_deco_list = [item.title() for item in self.rampage_deco_list]

        self.petalace_list = ('None', 'Hunting III', 'Strength III', 'Fortitude III',
                              'Demon III', 'Absolute', 'Underworld')

        self.items_list = ['powercharm', 'powertalon', 'might seed',
                           'demon powder']
        self.items_list = [item.title() for item in self.items_list]

        self.hh_songs_list = ['attack up', 'affinity up', 'element up',
                              'infernal melody']
        self.hh_songs_list = [item.title() for item in self.hh_songs_list]

        self.other_list = ['blue scroll', 'beaten frenzy', 'power drum',
                           'rousing roar', 'butterflame', 'cutterfly']
        self.other_list = [item.title() for item in self.other_list]

    # ---------- RAMPAGE DECO ---------- 
        for item in self.rampage_deco_list:
            formatted_item = self._format_name(item)
            setattr(self, formatted_item, 0)

    # ---------- PETALACE ----------
        for item in self.petalace_list:
            formatted_item = self._format_name(item)
            setattr(self, formatted_item, 0)

    # ---------- ITEMS ----------
        self.powercharm = tk.IntVar()
        self.powercharm.set(1)

        self.powertalon = tk.IntVar()
        self.powertalon.set(1)

        self.might_seed = tk.IntVar()
        self.might_seed.set(0)

        self.demon_powder = tk.IntVar()
        self.demon_powder.set(0)

        self.demondrug = tk.IntVar()
        self.demondrug.set(0)

        self.mega_demondrug = tk.IntVar()
        self.mega_demondrug.set(0)

    # ---------- FOOD ----------
        self.dango_booster = tk.IntVar()
        self.dango_booster.set(0)
        self.dango_booster_lvl = tk.IntVar()
        self.dango_booster_lvl.set(4)
        self.dango_booster_lvl_list = list(range(1, 5))

        self.dango_adrenaline = tk.IntVar()
        self.dango_adrenaline.set(0)
        self.dango_adrenaline_lvl = tk.IntVar()
        self.dango_adrenaline_lvl.set(4)
        self.dango_adrenaline_lvl_list = list(range(1, 5))

        self.dango_bulker = tk.IntVar()
        self.dango_bulker.set(0)
    
    # ---------- HH SONGS ----------
        #for item in self.hh_songs_list:
        #    formatted_item = self._format_name(item)
        #    self.formatted_item = tk.IntVar()
        #    self.formatted_item.set(0)

        self.attack_up = tk.IntVar()
        self.attack_up.set(0)

        self.affinity_up = tk.IntVar()
        self.affinity_up.set(0)

        self.element_up = tk.IntVar()
        self.element_up.set(0)

        self.infernal_melody = tk.IntVar()
        self.infernal_melody.set(0)

    # ---------- OTHER ----------
        self.blue_scroll = tk.IntVar()
        self.blue_scroll.set(0)
        
        self.beaten_frenzy = tk.IntVar()
        self.beaten_frenzy.set(0)

        self.rousing_roar = tk.IntVar()
        self.rousing_roar.set(0)

        self.power_drum = tk.IntVar()
        self.power_drum.set(0)

        self.butterflame = tk.IntVar()
        self.butterflame.set(0)

        self.cutterfly = tk.IntVar()
        self.cutterfly.set(0)

    def _format_name(self, item):
        """Format the name for logical purposes"""
        item_name = item.lower()
        item_name = item_name.replace(' ', '_')
        return item_name
    
    def _initialize_intvar(self, item):
        self.formatted_item = self._format_name(item)
        self.formatted_item = tk.IntVar()
        self.formatted_item.set(0)