import csv
import pandas as pd

def menu():
    ventas = []  # Lista donde se guardarán las ventas

    while True:
        try:
            print('\nMenu de opciones:')
            print('1. Registrar venta')
            print('2. Guardar cambios CSV')
            print('3. Consultar ventas')
            print('4. Salir')
            opcion = int(input('Seleccione una opcion (1-4): '))

            if opcion == 1:
                registrar_venta(ventas)
            elif opcion == 2:
                guardar_ventas(ventas)
            elif opcion == 3:
                consultar_ventas()
            elif opcion == 4:
                print('Saliendo del sistema. ¡Hasta luego!')
                break
            else:
                print('Opción no válida. Por favor, intente de nuevo.') 
        except ValueError:
            print('Opción inválida. Ingrese un número entre 1 y 4.')

def registrar_venta(ventas: list):
    while True:
        try:
            producto = input('Ingrese el nombre del producto: ')
            cantidad = int(input('Ingrese la cantidad vendida: '))
            precio = float(input('Ingrese el precio por unidad: '))
            fecha = input('Ingrese la fecha de la venta (AAAA-MM-DD): ')
            cliente = input('Ingrese el nombre del cliente: ')

            if cantidad <= 0 or precio <= 0:
                print('La cantidad y el precio deben ser mayores que cero. Intente de nuevo.')
                continue

            venta = {
                'producto': producto,
                'cantidad': cantidad,
                'precio': precio,
                'fecha': fecha,
                'cliente': cliente
            }
            ventas.append(venta)
            print('Venta registrada exitosamente.')

            continuar = input('¿Desea registrar otra venta? (s/n): ').lower()
            if continuar != 's':
                break

        except ValueError:
            print('Entrada inválida. Por favor, intente de nuevo.')

def guardar_ventas(ventas: list):
    if not ventas:
        print('No hay ventas para guardar.')
        return
    try:
        with open('ventas.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['producto','cantidad','precio','fecha','cliente'])
            writer.writeheader()
            writer.writerows(ventas)
        print('Ventas guardadas exitosamente en ventas.csv')
    except Exception as e:
        print(f'Error al guardar las ventas: {e}')

def consultar_ventas():
    try:
        df = pd.read_csv('ventas.csv')
        if df.empty:
            print('No hay ventas registradas.')
            return

        df['Subtotal'] = df['cantidad'] * df['precio']
        total_ventas = df['Subtotal'].sum()
        print('\nVentas registradas:')
        print(df)
        print(f'Total de ventas: ${total_ventas:.2f}')

        producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
        print(f'Producto más vendido: {producto_mas_vendido}')

        cliente_top = df['cliente'].value_counts().idxmax()
        print(f'Cliente con más compras: {cliente_top}')

    except FileNotFoundError:
        print('El archivo ventas.csv no existe. No hay ventas registradas.')
    except Exception as e:
        print(f'Error al consultar las ventas: {e}')

if __name__ == "__main__":
    print('Bienvenido al sistema de gestión de ventas')
    menu()
