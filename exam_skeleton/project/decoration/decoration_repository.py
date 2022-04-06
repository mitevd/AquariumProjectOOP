from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        if decoration not in self.decorations:
            return False
        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type: str):
        decorations_of_this_type = [obj for obj in self.decorations if obj.__class__.__name__ == decoration_type]
        if not decorations_of_this_type:
            return "None"
        current_decoration = decorations_of_this_type[0]
        return current_decoration
