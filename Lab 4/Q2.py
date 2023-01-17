from math import pi

def get_sphere_volume(radius):
    try:
        value = float(radius)
        if value > 0:
            return (round(4 / 3 * pi * value ** 3), "")
        elif value == 0:
            return (0, 'ERROR: Not a sphere')
        else:
            return (0, 'ERROR: Invalid input')
    except ValueError:
        return (0, 'ValueError')
    except TypeError:
        return (0, 'TypeError')



print(get_sphere_volume(10.5))

print()

print(get_sphere_volume(-1))
print(get_sphere_volume(0))

print()

print(get_sphere_volume('ten'))

print()

print(get_sphere_volume([1,2,3]))