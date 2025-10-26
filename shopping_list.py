"""PROG: app lista de la compra
OPCIONES:
1. Añadir producto
2. Eliminar producto
3. Mostrar lista
0. Salir
"""

def mostrar_menu():
       print('\n--- Lista de la compra ---')
       print('1. Añadir producto')
       print('2. Eliminar producto')
       print('3. Mostrar lista')
       print('0. Salir')

def main():
    lista = []
    while True:
        mostrar_menu()
        opcion = input('\nElige una opcion: ')

        if opcion == '1':
            producto = input('Introduce el producto a añadir: ')
            lista.append(producto)
            print(f'{producto} añadido a la lista')

        if opcion == '2':
            producto = input('Introduce el producto a eliminar: ')
            lista.remove(producto)
            print(f'{producto} sacado de la lista')
            pausa()

        if opcion == '3':
            print('\nTu lista de la compra: ')
            for producto in lista:
                print('-', producto)
            pausa()

        if opcion == '0':
            break

def pausa():
    input('\nPulsa ENTER para volver al menu: ')

main()