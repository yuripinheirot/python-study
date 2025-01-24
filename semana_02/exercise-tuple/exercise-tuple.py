import math

def calc_distance(distance):
    x,y,z = distance

    x = x ** 2
    y = y ** 2
    z = z ** 2

    return math.sqrt(x+y+z)

def calc_distance2(distance):
    amount = 0
    for item in distance:
        amount += item ** 2

    return math.sqrt(amount)


result = calc_distance((99,55,11))
result2 = calc_distance2((99,55,11))
print(f"Result: {result}, result2: {result2}")