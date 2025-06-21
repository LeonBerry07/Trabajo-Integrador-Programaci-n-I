import time
from ordenamiento import bubble_sort, merge_sort, quick_sort

def comparar_algoritmos():
    import random
    datos = random.sample(range(10000), 1000)

    for nombre, func in [
        ("Bubble", bubble_sort.sort),
        ("Merge", merge_sort.sort),
        ("Quick", quick_sort.sort)
    ]:
        copia = datos[:]
        inicio = time.time()
        func(copia)
        fin = time.time()
        print(f"{nombre} tardó {fin - inicio:.4f} segundos")