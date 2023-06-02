class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_bounding_rectangle(self, other):
        min_x = min(self.x, other.x)
        min_y = min(self.y, other.y)
        max_x = max(self.x + self.width, other.x + other.width)
        max_y = max(self.y + self.height, other.y + other.height)
        width = max_x - min_x
        height = max_y - min_y
        return Rectangle(min_x, min_y, width, height)
    
    def get_intersection_rectangle(self, other):
        x1 = max(self.x, other.x)
        y1 = max(self.y, other.y)
        x2 = min(self.x + self.width, other.x + other.width)
        y2 = min(self.y + self.height, other.y + other.height)
        if x1 < x2 and y1 < y2:
            width = x2 - x1
            height = y2 - y1
            return Rectangle(x1, y1, width, height)
        return None


# Пример использования класса
rect1 = Rectangle(0, 0, 5, 5)
rect2 = Rectangle(3, 3, 7, 4)

print("Прямоугольник 1:")
print("Площадь:", rect1.get_area())
print("Периметр:", rect1.get_perimeter())
print()

print("Прямоугольник 2:")
print("Площадь:", rect2.get_area())
print("Периметр:", rect2.get_perimeter())
print()

rect1.move(2, 3)
rect2.resize(10, 6)

print("Прямоугольник 1 (после перемещения):")
print("Координаты (x, y):", rect1.x, rect1.y)
print()

print("Прямоугольник 2 (после изменения размеров):")
print("Ширина:", rect2.width)
print("Высота:", rect2.height)
print()

bounding_rect = rect1.get_bounding_rectangle(rect2)
print("Наименьший прямоугольник, содержащий оба прямоугольника:")
print("Координаты (x, y):", bounding_rect.x, bounding_rect.y)
print("Ширина:", bounding_rect.width)
print("Высота:", bounding_rect.height)
print()

intersection_rect = rect1.get_intersection_rectangle(rect2)
if intersection_rect:
    print("Прямоугольник, являющийся общей частью двух прямоугольников:")
    print("Координаты (x, y):", intersection_rect.x, intersection_rect.y)