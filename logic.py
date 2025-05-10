import csv
from typing import List
from pet import Pet

def validate_pet_data(name: str, species: str, vaccination_date: str) -> bool:
    """
    Validate input fields for a pet.

    Args:
        name (str): Name of the pet.
        species (str): Species of the pet.
        vaccination_date (str): Vaccination date of the pet.

    Returns:
        bool: True if all fields are non-empty, otherwise False.
    """
    return all([name.strip(), species.strip(), vaccination_date.strip()])


def save_pets_to_csv(pets: List[Pet], filename: str = "data/pets.csv") -> None:
    """
    Save a list of Pet objects to a CSV file.

    Args:
        pets (List[Pet]): List of pets to save.
        filename (str): File path where data will be stored.
    """
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Species", "Vaccination Date"])
            for pet in pets:
                writer.writerow([pet.name, pet.species, pet.vaccination_date])
    except IOError as e:
        print(f"[ERROR] Failed to write to {filename}: {e}")


def load_pets_from_csv(filename: str = "data/pets.csv") -> List[Pet]:
    """
    Load Pet objects from a CSV file.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        List[Pet]: List of loaded Pet objects.
    """
    pets: List[Pet] = []
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("Name") and row.get("Species") and row.get("Vaccination Date"):
                    pets.append(Pet(row["Name"], row["Species"], row["Vaccination Date"]))
    except FileNotFoundError:
        print(f"[INFO] File '{filename}' not found. Starting with an empty list.")
    except Exception as e:
        print(f"[ERROR] Failed to read from {filename}: {e}")   
    return pets
