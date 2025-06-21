def sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = sort(lista[:medio])
    der = sort(lista[medio:])
    return merge(izq, der)

def merge(izq, der):
    resultado = []
    while izq and der:
        if izq[0] < der[0]:
            resultado.append(izq.pop(0))
        else:
            resultado.append(der.pop(0))
    resultado.extend(izq or der)
    return resultado