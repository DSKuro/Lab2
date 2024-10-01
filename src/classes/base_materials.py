from abc import ABCMeta, abstractmethod, abstractproperty

class BaseMaterials:
    result_cost = 0.0
    count = 0
    square = 0.0
    __metaclass__=ABCMeta

    def __init__(self, width : float, height : float, cost_per_unit : float) -> None:
        self.cost_per_unit = cost_per_unit
        self.calculate_square(width, height)

    def __str__(self) -> str:
        return f'Значения базового класса: цена: {self.result_cost}, количество: {self.count}'

    @property
    def get_count(self) -> int:
        return self.count

    @property
    def get_square(self) -> float:
        return self.square

    @property
    def get_cost(self) -> float:
        return self.result_cost

    @abstractmethod
    def calculate_square(self, width: float, height : float) -> None:
        pass

    @abstractmethod
    def calculate_cost(self, s : float) -> float:
        pass

    @abstractmethod
    def calculate_count(self, s : float):
        pass
