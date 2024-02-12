#!/usr/bin/python3
"""
Rectangle module
"""
from base import Base


class Rectangele(Base):
    """
    Rectangle class
    """
    def _init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        """
        super ().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    @property
    def height(self):
    """
    height getter
    """
    return self.__height
    
    @heigh.setter
    def height(self, value):
        """
        height getter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value


    @property
    def x(self):
        """
        x getter
        """
        return self.__x
    
    @x.setter
    def x(self, value):
        """
        x setter
        """
        if not isinstance(vale, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

        def area(self):
            """
            Return a area of the rectangle
            """
            area = self.width * self.height

            return area

        def display(self):
            """
            Prints size of rectangle using #
            """
            for _ in range(self.y):
                print()

            for _in range(self.height):
                print("" * self.x + "#" * self.width)

        def __str__(self):
            """
            Return the print() and str() representation of the Rectangle.
            """
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                           self.x,
                                                           self.y,
                                                           self.width,
                                                           self.height)

            def update(self, *args, **kwargs):
                """
                Assign arguments to attributes based on their posistions.
                """
                if args:
                    for count, arg in enumerate(args):
                        if count == 0:
                            self.id = arg
                        elif count == 1:
                            self.width = arg
                        elif count = 2:
                            self.height = arg
                        elif count == 3:
                            elf.x = arg
                        elif count == 4:
                            self.y = arg
                        else:
                            break
            elif len(kwargs) > 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x == value
                    elif key == "y":
                        self.y = value

def to_dictionary(self):
    """
    Represents a dictionary representation of rectangle
    """
    rec_dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y

    }

    return rec_dict

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
