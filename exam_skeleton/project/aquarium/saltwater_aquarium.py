from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    # POSSIBLE_FISH_TYPES = ["SaltwaterFish"]

    def __init__(self, name: str):
        super().__init__(name, 25)
