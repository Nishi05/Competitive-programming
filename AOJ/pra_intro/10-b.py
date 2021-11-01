from math import sin, cos, radians, sqrt

a, b, C = map(float, input().split())

ra = radians(C)
S = (a*b*sin(ra))*0.5
c = (a**2 + b**2 - (2*a*b*cos(ra)))
L = a + b + sqrt(c)
h = (2*S)/a
print(S)
print(L)
print(h)
