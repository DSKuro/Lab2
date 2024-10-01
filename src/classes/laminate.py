import math
from base_materials import BaseMaterials

class Laminate(BaseMaterials):
    def __init__(self, width : float, height : float, cost_per_unit : float) -> None:
        super().__init__(width, height, cost_per_unit)

    def __str__(self) -> str:
        return f'Значения класса Laminate: цена: {self.result_cost}, количество: {self.count}'

    def calculate_square(self, width: float, height : float) -> None:
        self.square = width * height

    def calculate_cost(self, s : float):
        self.calculate_count(s)
        self.result_cost = self.get_count * self.cost_per_unit

    def calculate_count(self, s : float):
        self.count = math.ceil(s / self.get_square)
