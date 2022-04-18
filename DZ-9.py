#Задание 1

import time
import enum


class Colour(enum.Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2


class TrafficLight:
    __colour: Цвет
    __move: int = 1

    def __init__(self, color: Color) -> Нет:
        self.__color = цвет

    def running(self, green_t=7, red_t=7, yellow_t=2):

        for _ in range(10): # while True:
            если self.__color == Color.RED:
                print(self.__colour.name)
                time.sleep(red_t)
            elif self.__colour == Colour.YELLOW:
                print(self.__colour.name)
                time.sleep(yellow_t)
            elif self.__colour == Colour.GREEN:
                print(self.__colour.name)
                time.sleep(green_t)

            if self.__colour.value == 2:
                self.__move = -1
            elif self.__colour.value == 0:
                self.__move = 1

            self.__colour = Colour(self.__colour.value + self.__move)


if __name__ == "__main__":
    traffic = TrafficLight(Colour.GREEN)
    traffic.running()

#Задание 2

class Road:

    _length: float
    _width: float

    def __init__(self, length: float = 0, width: float = 0) -> None:
        self._length = length
        self._width = width

    def calc(self, density: float, thickness: float) -> float:
        return self._length * self._width * density * thickness


if __name__ == "__main__":
    road = Road(length=20, width=5000)
    print(road.calc(25, 5))

    # or if we in module
    road = Road()
    road._length = 20
    road._width = 5000
    print(road.calc(density=25, thickness=5))

class Worker:
    name: str
    surname: str
    position: str
    _income: dict = {"wage": 0.0, "bonus": 1.0}

    def __init__(self, name: str, surname: str, position: str, income: dict = {"wage": 0, "bonus": 1.0}) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

#Задание 3

class Position(Worker):

    def __init__(self, name: str, surname: str, position: str, income: dict = {"wage": 0, "bonus": 1.0}) -> None:
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income["wage"] * self._income["bonus"]

if __name__ == "__main__":
    position = Position("Alex", "Zhem", "Programmer",
                        {"wage": 100, "bonus": 1.5})

    position.name = "Alexandr"
    position.position += "|MedTech"

    position._income["bonus"] = 1.0

    print(position.get_full_name.__name__, position.get_full_name())
    print(position.position)
    print(position.get_total_income.__name__, position.get_total_income())

#Задание 4

class Stationery:

    title: str




    def draw(self) -> None:

        print("Запуск отрисовки")







class Pen(Stationery):

    def __init__(self) -> None:

        super().__init__()

        self.title = "ручка"




    def draw(self) -> None:

        print("Пишем текст")

        return None







class Pencil(Stationery):

    def __init__(self) -> None:

        super().__init__()

        self.title = "карандаш"




    def draw(self) -> None:

        print("Чертим чертеж")

        return None







class Handle(Stationery):

    def __init__(self) -> None:

        super().__init__()

        self.title = "маркер"




    def draw(self) -> None:

        print("Выделяем заголовки")

        return None







if __name__ == "__main__":

    pen = Pen()

    pencil = Pencil()

    handle = Handle()




    for some in [pen, pencil, handle]:

        print(f"{some.__class__}:title = {some.title}")

        print(f"{some.__class__}.draw() =>\t", end="")

        some.draw()

        print()