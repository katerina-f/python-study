import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

discriminant = b ** 2 - 4 * a * c
x_1 = (-b + discriminant ** 0.5 ) / (2 * a)
x_2 = (-b - discriminant ** 0.5 ) / (2 * a)
print(int(x_1))
print(int(x_2))
