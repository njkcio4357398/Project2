# gui.py

import tkinter as tk
from tkinter import messagebox
from logic import validate_pet_data, save_pets_to_csv, load_pets_from_csv
from pet import Pet
from typing import List

class PetApp:
    """GUI application for managing pet vaccinations."""

    def __init__(self):
        """Initialize the PetApp GUI."""
        self.window = tk.Tk()
        self.window.title("Pet Vaccination Tracker")
        self.window.geometry("400x400")
        self.pets: List[Pet] = []

        # Widgets
        self.name_label = tk.Label(self.window, text="Pet Name:")
        self.name_entry = tk.Entry(self.window)

        self.species_label = tk.Label(self.window, text="Species:")
        self.species_entry = tk.Entry(self.window)

        self.vaccination_label = tk.Label(self.window, text="Vaccination Date (YYYY-MM-DD):")
        self.vaccination_entry = tk.Entry(self.window)

        self.add_button = tk.Button(self.window, text="Add Pet", command=self.add_pet)
        self.save_button = tk.Button(self.window, text="Save Pets", command=self.save_pets)
        self.load_button = tk.Button(self.window, text="Load Pets", command=self.load_pets)

        self.pet_listbox = tk.Listbox(self.window, width=50)

        # Layout
        self.name_label.pack()
        self.name_entry.pack()
        self.species_label.pack()
        self.species_entry.pack()
        self.vaccination_label.pack()
        self.vaccination_entry.pack()
        self.add_button.pack(pady=5)
        self.save_button.pack(pady=5)
        self.load_button.pack(pady=5)
        self.pet_listbox.pack(pady=10)

    def add_pet(self) -> None:
        """Add a new pet to the list."""
        name = self.name_entry.get()
        species = self.species_entry.get()
        vaccination_date = self.vaccination_entry.get()

        if validate_pet_data(name, species, vaccination_date):
            pet = Pet(name, species, vaccination_date)
            self.pets.append(pet)
            self.pet_listbox.insert(tk.END, str(pet))
            self.clear_entries()
        else:
            messagebox.showerror("Invalid Input", "Please fill out all fields.")

    def save_pets(self) -> None:
        """Save the pets to a CSV file."""
        save_pets_to_csv(self.pets)
        messagebox.showinfo("Saved", "Pets saved successfully!")

    def load_pets(self) -> None:
        """Load pets from a CSV file."""
        self.pets = load_pets_from_csv()
        self.pet_listbox.delete(0, tk.END)
        for pet in self.pets:
            self.pet_listbox.insert(tk.END, str(pet))

    def clear_entries(self) -> None:
        """Clear all entry fields."""
        self.name_entry.delete(0, tk.END)
        self.species_entry.delete(0, tk.END)
        self.vaccination_entry.delete(0, tk.END)

    def run(self) -> None:
        """Run the main event loop."""
        self.window.mainloop()

