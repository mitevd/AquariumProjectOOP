from project.core.aquariums_factory import AquariumsFactory
from project.core.decorations_factory import DecorationsFactory
from project.core.fish_factory import FishFactory
from project.decoration.decoration_repository import DecorationRepository


class Controller:
    AQUARIUM_TYPES = ["FreshwaterAquarium", "SaltwaterAquarium"]
    DECORATION_TYPES = ["Ornament", "Plant"]
    FISH_TYPES = ["FreshwaterFish", "SaltwaterFish"]

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []
        self.aquariums_factory = AquariumsFactory()
        self.decorations_factory = DecorationsFactory()
        self.fish_factory = FishFactory()

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.AQUARIUM_TYPES:
            return "Invalid aquarium type."
        current_aquarium = self.aquariums_factory.make_aquarium(aquarium_type, aquarium_name)
        self.aquariums.append(current_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.DECORATION_TYPES:
            return "Invalid decoration type."
        current_decoration = self.decorations_factory.make_decoration(decoration_type)
        self.decorations_repository.add(current_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        try:
            current_aquarium = [aquarium for aquarium in self.aquariums if aquarium.name == aquarium_name][0]
            current_decoration = self.decorations_repository.find_by_type(decoration_type)
            if current_decoration == 'None':
                return f"There isn't a decoration of type {decoration_type}."
            current_aquarium.add_decoration(current_decoration)
            self.decorations_repository.remove(current_decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        except:
            pass

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):

        aquarium = [aquarium for aquarium in self.aquariums if aquarium.name == aquarium_name][0]
        if fish_type not in self.FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."
        fish = self.fish_factory.create_fish(fish_type, fish_name, fish_species, price)

        # if len(aquarium.fish) >= aquarium.capacity:
        #     return "Not enough capacity."
        if aquarium.__class__.__name__ != fish.POSSIBLE_AREA:
            return "Water not suitable."
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        current_aquarium = [aquarium for aquarium in self.aquariums if aquarium.name == aquarium_name][0]
        current_aquarium.feed()
        return f"Fish fed: {len(current_aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        current_aquarium = [aquarium for aquarium in self.aquariums if aquarium.name == aquarium_name][0]
        sum_of_fish = sum(fish.price for fish in current_aquarium.fish)
        sum_of_decorations = sum(decoration.price for decoration in current_aquarium.decorations)
        total_sum = sum_of_decorations + sum_of_fish
        return f"The value of Aquarium {aquarium_name} is {total_sum:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium) + '\n'

        return result.strip()
