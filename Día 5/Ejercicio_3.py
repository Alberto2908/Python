def funcion(*args):
    anterior = 1
    for arg in args:
        if arg == 0:
            if anterior==0:
                return True
                break
            else:
                anterior=arg
        elif arg != 0:
            anterior=arg
    return False

print(funcion(1,2,2,0,1,0,2,2))