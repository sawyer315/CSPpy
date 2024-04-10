polygon = []
vert_in = 0.0
vert_in2 = 0.0
sum = 0
n = int(input('How many vertices?'))
for i in range(0, n):
  vert_in = float(input(f'Vertex {i+1} x: '))
  vert_in2 = float(input(f'Vertex {i+1} y: '))
  polygon.append([vert_in, vert_in2])

for i in range(0, n - 1):
  sum += (polygon[i][0] * polygon[i + 1][1]) - (polygon[i + 1][0] *
                                                polygon[i][1])
  print(sum)
sum += (polygon[n - 1][0] * polygon[0][1]) - (polygon[0][0] *
                                              polygon[n - 1][1])
area = sum / 2
print('The area is: ', area)
