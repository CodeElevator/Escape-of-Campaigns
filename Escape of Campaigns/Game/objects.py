# Initialize items
class ItemClass():
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        if self.name and self.description is None:
            self.name = 'Item'
            self.description = 'This is an item that has no name and no description..strange...'

# Initialize potions
class Potion(ItemClass):
    def __init__(self, name: str, description: str, effect: str):
        self.effect = effect
        super().__init__(name, description)

# Initialize Weapons
class Weapon(ItemClass):
    def __init__(self, name: str, damage : int, description: str):
        self.damage = damage
        super().__init__(name, description)

# Initialize the objects
class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword", 40, "This is a sword, it gives many damages to easily defeat enemies.")

class HealthPotion(Potion):
    def __init__(self):
        super().__init__(name='Health Potion', description='This potion gives you 50 HP, so half of your health.', effect='health')

class DamagePotion(Potion):
    def __init__(self):
        super().__init__(name='Damage Potion', description='This potion takes 30 HP from you.', effect='damage')