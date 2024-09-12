from turtle import color
from math import pi, sqrt
class Figure:
    sides_count = 0
    def __init__(self,__color, __sides: int, filled: bool = False ):
        self.__sides = __sides #(список сторон(целые числа))
        self.__color = __color #(список цветов в формате RGB)
        self.filled = filled #(закрашенный, bool)
    def get_color(self):
        """возвращает список RGB цветов."""
        return self.__color
    def __is_valid_color(self, r, g, b):
        """проверяет корректность переданных значений перед установкой нового цвета"""
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            return True if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 else False
        else:
            return False
    def set_color(self,r, g, b):
        """принемает парраметры из Колора"""
        if self.__is_valid_color(r, g, b) == True:
            self.__color = r,g,b
            return self.__color
        else:
            return self.__color

    def __is_valid_sides(self, *new_sides):
        for i in new_sides:
            if len(new_sides) == self.sides_count:
               # print(len(new_sides),self.sides_count )
                return True if isinstance(i, int) and i > 0 else False
            return False
    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):#должен принимать новые стороны
        for new in new_sides:
            if self.__is_valid_sides(new) == True:
                self.__sides = list(new_sides)
                return self.__sides
            else:
                return self.__sides

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        self.__sides = [sides[0]] * self.sides_count
        super().__init__(color, self.__sides)
        self.__radius = self.__sides[0] / (2 * pi)
    def get_radius(self):
        return self.__radius
    def get_square(self):
        rad = (self.__radius ** 2) * pi
        return rad
class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = sides
        p = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        self.__height = 2 * (sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))) / self.sides[0]

    def get_square(self):
        S_trian = (self.__height * self.sides[0]) / 2
        return S_trian

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        self.__sides = [sides[0]] * self.sides_count
        super().__init__(color, self.__sides )
    def get_volume(self):
        V = self.__sides[0] ** 3
        return V



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
