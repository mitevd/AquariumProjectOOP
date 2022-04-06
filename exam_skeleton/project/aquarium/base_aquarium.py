from abc import ABC, abstractmethod

from project.core.validator import Validator
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    POSSIBLE_FISH_TYPES = ["FreshwaterFish", "SaltwaterFish"]

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_message_if_string_is_empty(value, "Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([decoration.comfort for decoration in self.decorations])

    def add_fish(self, fish: BaseFish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."
        if fish.__class__.__name__ in self.POSSIBLE_FISH_TYPES:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:"
        if self.fish:
            result += '\n' + f"Fish: {' '.join([fish.name for fish in self.fish])}"
        else:
            result += '\n' + "Fish: none"
        result += '\n' + f"Decorations: {len(self.decorations)}"
        result += '\n' + f"Comfort: {self.calculate_comfort()}"
        return result.strip()

