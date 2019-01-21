import math
class Point3D:
      def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
      def __str__(self):
            return '{}, {}, {}'.format(self.x, self.y, self.z)
      def dist(self):
            return math.sqrt(self.x**2+self.y**2+self.z**2)
