#!/usr/bin/python3
""" square class """


class Square():
    """ square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ instantiation """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ area of my square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ this is the permiter of my square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ the printable of the coordinations """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create a square object """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
