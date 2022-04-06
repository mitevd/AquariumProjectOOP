from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationsFactory:
    decorations = {
        'Ornament': Ornament,
        'Plant': Plant
    }

    @staticmethod
    def make_decoration(decoration_type):
        return DecorationsFactory.decorations[decoration_type]()
