import csv
from pet import Pet

def validate_pet_data(name, species, vaccination_date):
    return name and species and vaccination_date

def save_pets_to_csv(pets, filename="pets.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Species", "Vaccination Date"])
        for pet in pets:
            writer.writerow([pet.name, pet.species, pet.vaccination_date])

def load_pets_from_csv(filename="pets.csv"):
    pets = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                pets.append(Pet(row["Name"], row["Species"], row["Vaccination Date"]))
    except FileNotFoundError:
        pass
    return pets
