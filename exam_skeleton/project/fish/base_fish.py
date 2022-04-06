from abc import ABC, abstractmethod

from project.core.validator import Validator


class BaseFish(ABC):
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_message_if_string_is_empty(value, "Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        Validator.raise_message_if_string_is_empty(value, "Fish species cannot be an empty string.")
        self.__species = value
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        Validator.raise_message_if_amount_is_less_or_equal_to_zero(value, "Price cannot be equal to or below zero.")
        self.__price = value

    @abstractmethod
    def eat(self):
        self.size += 5



