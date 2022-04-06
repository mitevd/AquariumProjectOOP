from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    # POSSIBLE_FISH_TYPES = ["FreshwaterFish"]

    def __init__(self, name: str):
        super().__init__(name, 50)

