from ordenamiento import bubble_sort, merge_sort, quick_sort
from busqueda import lineal, binaria
from estructuras.arbol_avl import AVLTree
from utils import medicion

def menu():
    print("\n--- Proyecto de Búsqueda y Ordenamiento ---")
    print("1. Ordenamiento (Bubble, Merge, Quick)")
    print("2. Búsqueda (Lineal / Binaria)")
    print("3. Árbol AVL (Insertar / Recorrer)")
    print("4. Medir rendimiento")
    print("0. Salir")

def main():
    salir = False
    while not salir:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            datos = [5, 2, 9, 1, 3]
            print("Original:", datos)
            print("Bubble:", bubble_sort.sort(datos[:]))
            print("Merge:", merge_sort.sort(datos[:]))
            print("Quick:", quick_sort.sort(datos[:]))
        elif opcion == "2":
            datos = [1, 2, 3, 4, 5, 6, 7]
            objetivo = 4
            print("Lineal:", lineal.buscar(datos, objetivo))
            print("Binaria:", binaria.buscar(datos, objetivo))
        elif opcion == "3":
            avl = AVLTree()
            for valor in [20, 4, 15, 70, 50]:
                avl.insertar(valor)
            avl.inorden()
        elif opcion == "4":
            medicion.comparar_algoritmos()
        elif opcion == "0":
            print("Saliendo del programa.")
            salir = True
        else:
            print("Opción no válida. Por favor, intentá de nuevo.")

if __name__ == "__main__":
    main()