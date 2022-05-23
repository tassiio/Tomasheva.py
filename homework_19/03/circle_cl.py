import math


class Circle:
    def __init__(self, center_x=0, center_y=0, radius=1):
        self.__center_x = center_x
        self.__center_y = center_y
        self.radius = radius

    # @property
    # def radius(self):
        # return self.radius

    # @radius.setter
    # def radius(self, r):
        # if r > 0:
            # self.radius = r
        # else:
            # raise ValueError

    def get_center(self):
        return [self.__center_x, self.__center_y]

    def circle_area(self):
        return math.pi * pow(self.radius, 2)

    def circle_perimeter(self):
        return 2 * math.pi * self.radius

    def circle_scale(self, coefficient):
        self.radius *= coefficient

    def circle_intersection(self, c_x, c_y, rad):
        rad_sum = rad + self.radius
        distance = pow((pow(c_x - self.__center_x, 2) + pow(c_y - self.__center_y, 2)), 0.5)
        if distance < rad_sum:
            return True
        else:
            return False
