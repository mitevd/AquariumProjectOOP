from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.controller import Controller
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

decoration1 = Ornament()
decoration2 = Plant()
decoration_repo = DecorationRepository()
decoration_repo.add(decoration1)
decoration_repo.add(decoration2)
print(decoration_repo.find_by_type('Ornament'))

# fish1 = FreshwaterFish("name1", "Fresh_WaterFish", 10)
# fish2 = SaltwaterFish("name2", "Fresh_WaterFish", 10)
#
# aquarium = FreshwaterAquarium('FRESH Aquarium')
# aquarium.add_decoration(decoration1)
# aquarium.add_decoration(decoration2)
# print(aquarium.add_fish(fish1))
# print(aquarium.add_fish(fish2))
# print(aquarium)
controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", "Name1"))
print(controller.add_aquarium("SaltwaterAquarium", "Name2"))
print(controller.add_aquarium("SaltwaterAdquarium", "Name2"))  # wrong type aquarium

print(controller.add_decoration("Plant"))
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("Ornahment"))
#
# print(controller.insert_decoration('Name1', "Ornament"))
# print(controller.insert_decoration('Name1', "Plant1"))

print(controller.add_fish('Name1', "FreshwaterFish", "fish name", "species", 100))
print(controller.add_fish('Name1', "SaltwaterFish", "fish name", "species", 100))
# print(controller.feed_fish('Name1'))
# print(controller.calculate_value('Name1'))
# print('----------------report-------------')
# print(controller.report())