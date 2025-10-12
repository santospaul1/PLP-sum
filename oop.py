class Character:
    """
    Base class representing a generic character in a story, demonstrating
    basic attributes and methods.
    """
    def __init__(self, name: str, health: int, power_level: int):
        """Constructor to initialize the base character attributes."""
        self.name = name
        self.health = health
        self.power_level = power_level
        print(f"Character '{self.name}' created.")

    def display_stats(self):
        """Displays the core statistics of the character."""
        print(f"--- {self.name} STATS ---")
        print(f"Health: {self.health}")
        print(f"Power Level: {self.power_level}")

    def take_damage(self, amount: int):
        """Updates the character's health when taking damage."""
        self.health -= amount
        print(f"{self.name} took {amount} damage. Health is now {self.health}.")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")


class Superhero(Character):
    """
    Derived class demonstrating inheritance from Character.
    It adds unique superhero attributes and methods.
    """
    def __init__(self, name: str, health: int, power_level: int, superpower: str, catchphrase: str):
        # Call the parent class (Character) constructor using super()
        super().__init__(name, health, power_level)
        self.superpower = superpower
        self.catchphrase = catchphrase
        self._secret_identity = "Unknown"  # Encapsulation example (private attribute)

    def use_superpower(self):
        """A method unique to the Superhero class."""
        print(f"\n{self.name} uses their power: {self.superpower}!")
        print(f"'{self.catchphrase}'")
        
    def reveal_identity(self, identity: str):
        """Demonstrates updating the encapsulated attribute."""
        if self._secret_identity == "Unknown":
            self._secret_identity = identity
            print(f"The secret identity of {self.name} is now known: {self._secret_identity}!")
        else:
            print(f"Identity already set as {self._secret_identity}.")

# --- Demonstration ---
if __name__ == "__main__":
    
    print("--- Creating Objects ---")
    
    # Create an instance of the derived class (Superhero)
    hero = Superhero(
        name="The Sentinel",
        health=150,
        power_level=95,
        superpower="Kinetic Absorption",
        catchphrase="The future is protected!"
    )

    # Create an instance of the base class (Character)
    villain = Character(
        name="Dr. Chaos",
        health=120,
        power_level=80
    )

    print("\n--- Interaction and Polymorphism Demo ---")
    
    # Use method unique to Superhero
    hero.use_superpower()
    
    # Use inherited method (from Character)
    hero.display_stats() 
    
    # Use method from Character on the villain
    villain.display_stats()
    
    # Demonstrate encapsulation method
    hero.reveal_identity("Alex Vanguard")
    
    print("\n--- Battle Simulation ---")
    hero.take_damage(20)
    villain.take_damage(100)
