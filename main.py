import tkinter as tk

from dmg_calc_win import DamageCalcWin

class MHMain():
    """Main class"""

    def __init__(self, root):
        """Initialize the program"""
        self.root = root

        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()

        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        """Generate the widgets"""
        # ----- DIFF -----
        # Input
        self.name_input = tk.Entry(self.root)
        # Button
        self.print_name = tk.Button(self.root,
                                    text="clicca se vuoi venire diffato",
                                    command=self.mimmo)
        
        # ----- CALCULATOR -----
        self.calc = tk.Button(self.root, text="clicca se vuoi calcolare",
                              command=lambda:
                              self.make_calc_window(DamageCalcWin))
        self.calc.pack(side="right")

    def place_widgets(self):
        """Place the widgets in the window"""
        # ----- DIFF -----
        # Input
        self.canvas.create_window(200, 120, window=self.name_input)
        # Button
        self.canvas.create_window(200, 150, window=self.print_name)

    def mimmo(self):
        """Mimmo diff"""
        name = self.name_input.get()
        
        name_output = tk.Label(self.root, text=f"{name} diff")
        self.canvas.create_window(200, 180, window=name_output)

    def make_calc_window(self, _class):
        """Create the calculator window"""
        self.calc = tk.Toplevel(self.root)
        _class(self.calc)

if __name__ == '__main__':
    # Make an app istance and run the app
    root = tk.Tk()
    app = MHMain(root)
    app.root.title("MH Builder")
    root.mainloop()