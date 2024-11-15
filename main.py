from burbuja import burbuja
from insercion import insercion
from seleccion import seleccion
from shell_sort import shell_sort
from quicksort import quicksort
from heapsort import heapsort
from radix_sort import radix_sort

def mostrar_menu_algoritmos():
    print("\nSeleccione el método de ordenamiento directo:")
    print("1. Burbuja")
    print("2. Inserción")
    print("3. Selección")
    print("4. ShellSort")

def mostrar_menu_algoritmos_avanzados():
    print("\nSeleccione el método de ordenamiento algorítmico:")
    print("5. Quicksort")
    print("6. Heapsort")
    print("7. Radix Sort (solo números no negativos)")

def main():
    numeros = []  # Inicializar la lista de números fuera del bucle

    while True:
        if not numeros:  # Solo pedir números si la lista está vacía
            cantidad = int(input("Ingrese la cantidad de números a ordenar: "))
            for i in range(cantidad):
                numero = int(input(f"Ingrese el número {i + 1}: "))
                numeros.append(numero)
        else:
            usar_misma_cantidad = input("\n¿Desea usar la misma cantidad de números ingresados anteriormente? (s/n): ").strip().lower()
            if usar_misma_cantidad == 's':
                pass  # Usar la lista existente
            else:
                cantidad = int(input("Ingrese la nueva cantidad de números a ordenar: "))
                numeros = []  # Reiniciar la lista
                for i in range(cantidad):
                    numero = int(input(f"Ingrese el número {i + 1}: "))
                    numeros.append(numero)

        # Mostrar menú de métodos directos
        mostrar_menu_algoritmos()
        # Mostrar menú de métodos algorítmicos
        mostrar_menu_algoritmos_avanzados()

        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            resultado = burbuja(numeros.copy())
            print("\nLista ordenada con Burbuja:", resultado)
        
        elif opcion == 2:
            resultado = insercion(numeros.copy())
            print("\nLista ordenada con Inserción:", resultado)
        
        elif opcion == 3:
            resultado = seleccion(numeros.copy())
            print("\nLista ordenada con Selección:", resultado)

        elif opcion == 4:
            resultado = shell_sort(numeros.copy())
            print("\nLista ordenada con ShellSort:", resultado)

        elif opcion == 5:
            resultado = quicksort(numeros.copy())
            print("\nLista ordenada con Quicksort:", resultado)

        elif opcion == 6:
            resultado = heapsort(numeros.copy())
            print("\nLista ordenada con Heapsort:", resultado)

        elif opcion == 7:
            if all(num >= 0 for num in numeros):  
                resultado = radix_sort(numeros.copy())
                print("\nLista ordenada con Radix Sort:", resultado)
            else:
                print("Radix Sort solo funciona con números no negativos.")
                continue

        else:
            print("Opción no válida.")
            continue

        repetir = input("\n¿Desea ordenar otra lista? (s/n): ").strip().lower()
        
        if repetir != 's':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()