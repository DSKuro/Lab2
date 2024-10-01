import math
from base import BaseMaterials

class Wallpaper(BaseMaterials):
    def __init__(self, width : float, height : float, cost_per_unit : float, color : tuple) -> None:
        super().__init__(width, height, cost_per_unit)
        self.color = color

    def __str__(self) -> str:
        return f'Значения класса Wallpaper: цена: {self.count}, количество: {self.result_cost}, цвет {self.color}'

    def calculate_square(self, width: float, height : float) -> None:
        self.square = width * height

    def calculate_cost(self, s : float):
        self.calculate_count(s)
        self.result_cost = self.get_count * self.get_cost

    def calculate_count(self, s : float):
        self.count = math.ceil(s / self.get_square)
