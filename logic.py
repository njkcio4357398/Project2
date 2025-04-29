# logic.py

import csv
from pet import Pet
from typing import List

def validate_pet_data(name: str, species: str, vaccination_date: str) -> bool:
    """
    Validate the input data for a pet.

    Args:
        name (str): Name of the pet.
        species (str): Species of the pet.
        vaccination_date (str): Vaccination date of the pet.

    Returns:
        bool: True if all fields are valid, False otherwise.
    """
    return all([name.strip(), species.strip(), vaccination_date.strip()])

def save_pets_to_csv(pets: List[Pet], filename: str = "data/pets.csv") -> None:
    """
    Save a list of Pet objects to a CSV file.

    Args:
        pets (List[Pet]): List of Pet objects.
        filename (str): CSV filename.
    """
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Species", "Vaccination Date"])
            for pet in pets:
                writer.writerow([pet.name, pet.species, pet.vaccination_date])
    except Exception as e:
        print(f"Error saving pets: {e}")

def load_pets_from_csv(filename: str = "data/pets.csv") -> List[Pet]:
    """
    Load Pet objects from a CSV file.

    Args:
        filename (str): CSV filename.

    Returns:
        List[Pet]: List of Pet objects.
    """
    pets = []
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                pet = Pet(row["Name"], row["Species"], row["Vaccination Date"])
                pets.append(pet)
    except FileNotFoundError:
        print("No saved pets yet.")
    except Exception as e:
        print(f"Error loading pets: {e}")
    return pets

