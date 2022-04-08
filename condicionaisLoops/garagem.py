x = input().split(" ")
width_garage = int(x[0])
length_garage = int(x[1])
height_garage = int(x[2])
width_car = int(x[3])
length_car = int(x[4])
height_car = int(x[5])

if width_garage >= width_car and length_garage >= length_car and height_garage >= height_car:
    print('SIM')
else:
    print('NAO')
