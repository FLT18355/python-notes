# classes.py
# 类与面向对象示例

# 基本类定义
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name}：汪汪！"

    def get_info(self):
        return f"{self.name}，{self.age} 岁"


dog = Dog("旺财", 3)
print(dog.bark())
print(dog.get_info())

# 继承
class GoldenRetriever(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def bark(self):
        return f"{self.name}：汪汪汪！"

    def fetch(self):
        return f"{self.name} 去捡球了"


golden = GoldenRetriever("小金", 2, "金色")
print(golden.bark())
print(golden.get_info())
print(golden.fetch())

# 类方法与静态方法
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return "数学工具类"


print(f"静态方法：{MathUtils.add(3, 5)}")
print(f"类方法：{MathUtils.description()}")

# 属性（getter/setter）
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2


circle = Circle(5)
print(f"半径：{circle.radius}")
print(f"面积：{circle.area:.2f}")

# 特殊方法
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        return 2


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(f"向量加法：{v3}")
print(f"向量长度：{len(v3)}")
