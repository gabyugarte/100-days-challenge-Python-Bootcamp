# *args = Recieves umlimited arguments

def add(*args):
    suma = 0
    for n in args:
        suma += n
    return suma

print(add(1, 2, 3, 4))
    