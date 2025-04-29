
class Pet:
    """Class representing a pet and its vaccination information."""

    def __init__(self, name: str, species: str, vaccination_date: str):
        """
        Initialize a Pet object.

        Args:
            name (str): The name of the pet.
            species (str): The species of the pet.
            vaccination_date (str): The next vaccination date.
        """
        self.name = name
        self.species = species
        self.vaccination_date = vaccination_date

    def __str__(self) -> str:
        """Return a string representation of the Pet."""
        return f"{self.name} ({self.species}) - Vaccination: {self.vaccination_date}"

