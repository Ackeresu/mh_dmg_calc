import tkinter as tk

class Weapon():
    """A class that manage the weapon and monster values"""

    def __init__(self):
        """Initialize the variables"""
        self.wpn_list = ('Raw', 'Element', 'Affinity', 'Sharpness',
                         'MV', 'Raw Hitzone', 'Elemental Hitzone')

        self.wpn_specific_list = ['None', 'GS Power Sheathe', 'LS White Spirit Gauge',
                               'LS Yellow Spirit Gauge', 'LS Red Spirit Gauge',
                               'DB Demon Mode', 'DB Archdemon Mode',
                               'DB Feral Mode', 'Lance Red Glow',
                               'Lance Orange Glow', 'Lance Yellow Glow',
                               'Lance Blue Glow', 'GL Erupting Cannon',
                               'CB Red Shield', 'Bow Herculean Draw']
        
    # ---------- WEAPON SPECIFIC ----------
        for item in self.wpn_specific_list:
            formatted_item = item.lower()
            formatted_item = formatted_item.replace(' ', '_')
            setattr(self, formatted_item, 0)

    # ---------- WEAPON ----------
        self.raw = tk.IntVar()
        self.raw.set(395)

        self.element = tk.IntVar()
        self.element.set(0)

        self.affinity = tk.IntVar()
        self.affinity.set(0)

        self.sharpness = tk.StringVar()
        self.sharpness.set('Purple')
        self.sharpness_list = ('Red', 'Orange', 'Yellow',
                               'Green', 'Blue', 'White', 'Purple')
        
        self.mv = tk.DoubleVar()
        self.mv.set(80)

        self.raw_hitzone = tk.DoubleVar()
        self.raw_hitzone.set(100)

        self.elemental_hitzone = tk.DoubleVar()
        self.elemental_hitzone.set(30)