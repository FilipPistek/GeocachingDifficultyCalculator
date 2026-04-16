import tkinter as tk
from tkinter import ttk, messagebox
from logic import GeocachingPredictor

class GeocachingUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Geocaching Difficulty Calculator")
        self.root.geometry("450x500")
        self.logic = GeocachingPredictor()
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill="both", expand=True)
        ttk.Label(main_frame, text="Zadejte parametry keše pro odhad:", font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

        # 1. Typ keše
        ttk.Label(main_frame, text="Typ keše:").grid(row=1, column=0, sticky="w")
        self.type_var = tk.StringVar()
        self.type_combo = ttk.Combobox(main_frame, textvariable=self.type_var, values=list(self.logic.le_type.classes_), state="readonly")
        self.type_combo.grid(row=1, column=1, pady=5, sticky="ew")

        if "Traditional Cache" in self.logic.le_type.classes_:
            self.type_combo.set("Traditional Cache")
        else:
            self.type_combo.current(0)

        self.type_combo.bind("<<ComboboxSelected>>", self.check_logic_puzzle)

        # 2. Velikost
        ttk.Label(main_frame, text="Velikost:").grid(row=2, column=0, sticky="w")
        self.size_var = tk.StringVar()
        self.size_combo = ttk.Combobox(main_frame, textvariable=self.size_var, values=list(self.logic.le_size.classes_), state="readonly")
        self.size_combo.grid(row=2, column=1, pady=5, sticky="ew")
        self.size_combo.current(0)

        # 3. Terén
        ttk.Label(main_frame, text="Terén (1-5):").grid(row=3, column=0, sticky="w")
        self.terrain_scale = tk.Scale(main_frame, from_=1, to=5, resolution=0.5, orient="horizontal",command=self.check_logic_terrain)
        self.terrain_scale.grid(row=3, column=1, pady=5, sticky="we")

        # 4. Souřadnice
        ttk.Label(main_frame, text="Zeměpisná šířka (Lat):").grid(row=4, column=0, sticky="w")
        self.lat_entry = ttk.Entry(main_frame)
        self.lat_entry.insert(0, "50.0")
        self.lat_entry.grid(row=4, column=1, pady=5, sticky="ew")

        ttk.Label(main_frame, text="Zeměpisná délka (Lon):").grid(row=5, column=0, sticky="w")
        self.lon_entry = ttk.Entry(main_frame)
        self.lon_entry.insert(0, "14.4")
        self.lon_entry.grid(row=5, column=1, pady=5, sticky="ew")

        # 5. Checkboxy s logikou
        self.drive_in_var = tk.BooleanVar()
        self.chk_drive_in = ttk.Checkbutton(main_frame, text="Drive-in (přístupné autem)", variable=self.drive_in_var, command=self.check_logic_drive_in)
        self.chk_drive_in.grid(row=6, column=0, columnspan=2, pady=(15, 5), sticky="w")

        self.puzzle_var = tk.BooleanVar()
        self.chk_puzzle = ttk.Checkbutton(main_frame, text="Puzzle / Challenge (vyžaduje luštění)", variable=self.puzzle_var)
        self.chk_puzzle.grid(row=7, column=0, columnspan=2, pady=5, sticky="w")

        # 6. Tlačítko pro výpočet a výsledek
        self.btn_predict = ttk.Button(main_frame, text="Vypočítat odhad", command=self.handle_prediction)
        self.btn_predict.grid(row=8, column=0, columnspan=2, pady=20)

        self.result_label = ttk.Label(main_frame, text="Předpokládaná obtížnost: ---", font=('Arial', 12, 'bold'), foreground="blue")
        self.result_label.grid(row=9, column=0, columnspan=2)

    def check_logic_terrain(self, event=None):
        if float(self.terrain_scale.get()) > 1.5:
            self.drive_in_var.set(False)

    def check_logic_drive_in(self):
        if self.drive_in_var.get() and float(self.terrain_scale.get()) > 1.5:
            self.terrain_scale.set(1.5)

    def check_logic_puzzle(self, event=None):
        if self.type_var.get() == "Unknown Cache":
            self.puzzle_var.set(True)

    def handle_prediction(self):
        try:
            res = self.logic.predict(
                self.type_var.get(),
                self.size_var.get(),
                self.terrain_scale.get(),
                self.lat_entry.get(),
                self.lon_entry.get(),
                self.drive_in_var.get(),
                self.puzzle_var.get()
            )
            self.result_label.config(text=f"Předpokládaná obtížnost: {res}")
        except Exception as e:
            messagebox.showerror("Chyba výpočtu", f"Zkontrolujte zadání. Detail: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeocachingUI(root)
    root.mainloop()