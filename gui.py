# gui.py

import tkinter as tk

class PetApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pet Tracker")

        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        self.add_button = tk.Button(self.window, text="Add Pet", command=self.add_pet)
        self.add_button.pack()

        self.pet_listbox = tk.Listbox(self.window)
        self.pet_listbox.pack()

        self.pets = []

    def add_pet(self):
        name = self.name_entry.get()
        if name:
            self.pets.append(name)
            self.pet_listbox.insert(tk.END, name)
            self.name_entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()
