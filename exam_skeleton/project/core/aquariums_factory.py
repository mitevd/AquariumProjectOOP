from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium


class AquariumsFactory:
    aquariums = {
        'FreshwaterAquarium': FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }

    @staticmethod
    def make_aquarium(aquarium_type, name):
        return AquariumsFactory.aquariums[aquarium_type](name)
