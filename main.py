import tkinter as tk
from window import Window
from damage_calc import DamageCalc

class MHMain():
    """Overall class to manage everything"""

    def __init__(self):
        """Initialize the program"""
        #self.window = Window()
        self.dmgcalc = DamageCalc()

    def run_program(self):
        """Run the program"""
        #self.window.make_main_window()
        self.weapon_stats()
        self.other_stats()
        self.dmgcalc.get_weapon_stats(self.raw, self.elem,
                                      self.affinity, self.sharp)
        self.dmgcalc.do_calc(self.motion, self.hitzone, self.elemhitzone)
        self.dmgcalc.show_results()

    def weapon_stats(self):
        """Get the weapon stats from the user"""
        self.raw = float(input("--- Weapon stats ---\nRaw: "))
        self.elem = float(input("Element value: "))
        self.affinity = float(input("Affinity: "))
        self.sharp = input("Sharpness color: ")

    def other_stats(self):
        """Get the other stats necessary for the calc"""
        self.motion = float(input("\nMotion value: "))
        self.hitzone = float(input("Monster hit-zone: "))
        self.elemhitzone = float(input("Monster elemental hit-zone: "))
        self.motion = self.motion / 100
        self.hitzone = self.hitzone / 100
        self.elemhitzone = self.elemhitzone / 100

if __name__ == '__main__':
    # Make an app istance and run the app
    mh = MHMain()
    mh.run_program()