from point_class import Point
from random import randint
from gui_rectangle import GuiRectangle
import turtle as tr
from gui_point import GuiPoint

rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)),
                             Point(randint(10, 400), randint(10, 400)))

print(f"Rectangle Coordinates: {rectangle.point1.x}, {rectangle.point1.y} and "
      f"{rectangle.point2.x}, {rectangle.point2.y}")

user_point = GuiPoint(float(input("Guess X: ")),
                   float(input("Guess Y: ")))

user_area = float(input("Guess rectangle area: "))

print(f"Your point {user_point.falls_in_rectangle(rectangle)}.")
print(f"Your area was off by : {rectangle.area() - user_area}")


timmy = tr.Turtle()
rectangle.draw(canvas=timmy)
user_point.draw(canvas=timmy)

tr.done()
