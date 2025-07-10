# Definimos el diccionario de los productos disponibles
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7' 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    'UWU1331HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

# En este bloque definimos el stock y la cantidad de modelos disponibles
stock = {
    '8475HD': [387990,10],
    '2175HD': [327990,4],
    'JjFHD': [424990,1],
    'fgdxFHD': [664990,21],
    '123FHD': [290890,32],
    '342FHD': [444990,7],
    'GF75HD': [749990,2],   
    'UWU131HD': [349990,1]
}

def stock_marca(marca):
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower() and modelo in stock:
            total += stock[modelo][1]
    print(f"El stock total de {marca} es: {total}")

# Este bloque sirve para definir la opción 2 (busqueda por precio)
def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, datos in stock.items():
        precio, cantidad = datos
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            resultados.append(f"{marca} -- {modelo}")
    if resultados:
        print("Los notebooks entre los precios consultados son:", sorted(resultados))
    else:
        print("No hay notebooks en ese rango de precios, lo sentimos")

# Este bloque define el menú principal 

def menu():
    while True:
        print("\n*** Bienvenido al Menu Principal ***")
        print("¿Qué deseas realizar el día de hoy?")
        print("__________________________________________")
        print("1. Stock por marca.")
        print("2. Búsqueda por precio.")
        print("3. Eliminar producto.")
        print("4. Salir.")

        opcion = input("Ingrese opción: ")

        if opcion == '1':
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)
        elif opcion == '2':
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                busqueda_precio(p_min, p_max)
            except ValueError:
                print("No hay notebooks en ese rango de precio, favor vuelva a intentar")
        elif opcion == '3':
            while True:
                modelo = input("Ingrese el producto a eliminar: ")
                try:
                    eliminar_producto = (input("Reingrese el producto a eliminar para confirmar: "))
                    if modelo in productos or stock:
                        print("Producto eliminado con éxito.")
                    else:
                        print("El modelo no existe.")
                except ValueError:
                    print("Debe ingresar un modelo válido.")
                seguir = input("¿Desea eliminar otro producto? (s/n): ").lower()
                if seguir != 's':
                    break
        elif opcion == '4':
            print("Menú finalizado.")
            print("Gracias por su preferencia.")
            break
        else:
            print("Debe seleccionar una opción válida.")

menu()