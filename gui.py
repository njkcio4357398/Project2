
import tkinter as tk
from tkinter import messagebox
from typing import List
from pet import Pet
from storage import validate_pet_data, save_pets_to_csv, load_pets_from_csv
#ChatGPT class PetAPP:
class PetApp:
    """Tkinter GUI Application for tracking pet vaccinations."""
#Chat GPT def __init__(self):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pet Vaccination Tracker")

        
        tk.Label(self.window, text="Pet Name").pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        
        tk.Label(self.window, text="Species").pack()
        self.species_entry = tk.Entry(self.window)
        self.species_entry.pack()

        tk.Label(self.window, text="Vaccination Date (YYYY-MM-DD)").pack()
        self.date_entry = tk.Entry(self.window)
        self.date_entry.pack()

        self.add_button = tk.Button(self.window, text="Add Pet", command=self.add_pet)
        self.add_button.pack()

        self.pet_listbox = tk.Listbox(self.window, width=50)
        self.pet_listbox.pack()

        self.pets: List[Pet] = load_pets_from_csv()
        for pet in self.pets:
            self.pet_listbox.insert(tk.END, str(pet))

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
#Chat GPT def add_pet(self)->None:
    def add_pet(self) -> None:
        """Add a pet if inputs are valid."""
        name = self.name_entry.get()
        species = self.species_entry.get()
        date = self.date_entry.get()
#ChatGPT if validate_pet_data(name, species, date):
        if validate_pet_data(name, species, date):
            new_pet = Pet(name, species, date)
            self.pets.append(new_pet)
            self.pet_listbox.insert(tk.END, str(new_pet))
            self.clear_entries()
        else:
            messagebox.showerror("Invalid Input", "Please fill in all fields.")

    def clear_entries(self) -> None:
        """Clear input fields."""
        self.name_entry.delete(0, tk.END)
        self.species_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def on_close(self) -> None:
        """Handle application close event."""
        save_pets_to_csv(self.pets)
        self.window.destroy()

    def run(self) -> None:
        """Run the Tkinter main loop."""
        self.window.mainloop()
