from equation import Circle
import equation

circle = Circle()
ell = equation.Ellipse()

circle.radius = 2.0
print(circle.parameter(), circle.area())

ell.minor_axis = 10.0
ell.major_axis = 20.0
print(ell.perimeter(), ell.area())

