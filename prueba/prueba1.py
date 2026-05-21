import sqlite3

# Conexion a la base de datos
conexion = sqlite3.connect("Inventario.db")
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio INTEGER NOT NULL,
            categoria TEXT NOT NULL
        )
''')
conexion.commit()

"""Insertar un nuevo producto en la base de datos"""
def agregar_producto(nombre, descripcion, cantidad, precio, categoria):
    cursor.execute(
        "INSERT INTO inventario (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
        (nombre, descripcion, cantidad, precio, categoria)
    )
    conexion.commit()
    print(" producto agregado con exito.")
    
def mostrar_productos():
    """Acá se muestran todos los productos en la base de datos"""
    cursor.execute("SELECT * FROM inventario")
    productos = cursor.fetchall()
    
    print("\nLista de productos:")    
    for producto in productos:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripcion: {producto[2]}, Cantidad:{producto[3]}, Precio:{producto[4]}, Categoria:{producto[5]}")
        
    # En este bloque se actualiza el producto(nombre y precio como ejemplo)
def actualizar_producto(id_producto, nuevo_nombre, nuevo_precio):
    cursor.execute(
        "UPDATE inventario SET nombre = ?, precio = ? WHERE id = ?", 
        (nuevo_nombre, nuevo_precio, id_producto)
    )
    conexion.commit()
    print("Producto actualizado correctamente.")    
    
   # En este bloque se Eliminan los productos 
def eliminar_producto(id_producto):
    cursor.execute("DELETE FROM inventario WHERE id = ?", (id_producto,))
    conexion.commit()
    print("Producto eliminado correctamente.")
    
# En este bloque el Menú interactivo
while True:
    print("\n--- Gestion de Inventario ---")
    print("1. Agregar Producto")
    print("2. Mostrar Producto")
    print("3. Actualizar Producto")
    print("4. Eliminar Producto")
    print("5. Salir")
    
    opcion = input("Selecciona una opcion: ").strip()
    
    if opcion == "1":
        nombre = input("Nombre: ").strip()
        descripcion = input("Descripcion: ").strip()
        cantidad = input("Cantidad: ").strip()
        precio = input("precio: ").strip()
        categoria = input("Categoria: ").strip()

        if cantidad.isdigit() and precio.isdigit():
            agregar_producto(nombre, descripcion, int(cantidad), int(precio), categoria)
        else:
            print("ID y precio deben ser números válidos.")            
            
    elif opcion == "2":
        mostrar_productos() # En este bloque se agregan nuevos productos
    elif opcion == "3":
        id_producto = input("Ingresa el ID del producto a actualizar: ").strip()
        
        nuevo_producto = input("Ingresa el nuevo producto").strip()
        
        if id_producto.isdigit():
            actualizar_producto(nombre, descripcion,  int(cantidad), int(precio), categoria)
        else:
            print("El ID debe ser un numero valido.")
    
    elif opcion == "4": # En este bloque se eliminan productos
        id_producto = input("Ingresa el ID del producto a eliminar: ").strip()
        
        if id_producto.isdigit():
            eliminar_producto(int(id_producto))
        else:
            print("El Id debe ser un numero valido.")
            
    elif opcion == "5": # En este bloque se sale del sistema
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opcion invalida. Intenta nuevamente.")
        
# Cerrar la conexion al finalizar
conexion.close()


# Notas:
# pasos para entrar en el entorno virtual:
# en consola: python -m virtualenv env
# para activar el entorno: .\env\scripts\activate


# Powered by: Vladimir Garcia.