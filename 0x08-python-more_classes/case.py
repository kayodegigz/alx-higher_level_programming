#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

myrectangle1 = Rectangle(8, 4)
myrectangle2 = Rectangle(2, 3)

print(myrectangle1 == Rectangle.bigger_or_equal(myrectangle1, myrectangle2))
