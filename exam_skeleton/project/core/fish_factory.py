from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class FishFactory:
    fish = {
        'FreshwaterFish': FreshwaterFish,
        'SaltwaterFish': SaltwaterFish
    }

    @staticmethod
    def create_fish(fish_type: str, fish_name: str, fish_species: str, price: float):
        return FishFactory.fish[fish_type](fish_name, fish_species, price)
