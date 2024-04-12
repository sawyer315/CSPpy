import math
r = 3963.1
rad = 3.141592/180
a1 = float(input('Your latitude: ')) *rad
o1 = float(input('Your longitude: '))*rad
a0 = float(input('Car latitude: '))*rad
o0 = float(input('Car longitude: '))*rad

distance = r *math.acos(math.cos(a1)*math.cos(o1)*math.cos(a0)*math.cos(o0)
                       + math.cos(a1)*math.cos(a0)*math.sin(o1)*math.sin(o0)
                       +math.sin(a1)*math.sin(a0))
print(round(distance,3))

