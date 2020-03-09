from math import sqrt

a = int(input('Digite o número de A:\n'))
b = int(input('Digite o número de B:\n'))
c = int(input('Digite o número de C:\n'))


def delta(b, a, c):
    return (b ** 2) - (4 * a * c)


def calc_raiz(delta, b, a):
    raiz_um = (-b + sqrt(delta)) / (2 * a)
    raiz_dois = (-b - sqrt(delta)) / (2 * a)

    if delta == 0:
        return raiz_um
    elif delta < 0:
        return 'Está equação não possui raizes reais'
    else:
        return raiz_um, raiz_dois


delta = delta(a, b, c)
resultado = calc_raiz(delta, b, a)
print(resultado)
