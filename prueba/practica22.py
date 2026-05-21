import sqlite3

conexion = sqlite3.connect("Inventario2.db")
cursor = conexion.cursor()

cursor.execute('''
         CREATE TABLE IF NOT EXITS Inventario2(
            id NTEGER PRYMARY KEY AUTOINCREMENT,
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
        "INSERT INTO inventario2 (nombre, descripcion, cantidad, precio, categoria) VALUE (?, ?, ?, ?, ?)",
        (nombre, descripcion, cantidad, precio, categoria)
                
    )
    conexion.commit()
    print(" producto agregado con éxito.")
    
    
def mostrar_productos():
    """Acá se muestran todos los productos en la base de datos"""
    cursor.execute("SELECT * FROM invetario2")
    productos = cursor.fetchall()
    
    print("\nLista de productos:")
    for producto in productos:
        print(f"ID: {producto[0]}, nombre: {producto[1]}, Descripcion: {producto[2]}, Cantidad:{producto[3]}, Precio: {producto[4]}, Categoria:{producto[5]}")
    
    
    def actualizar_producto(id_producto, nuevo_nombre, nuevo_precio):
        cursor.execute(
            "UPDATE inventario2 SET nombre = ?, precio = ? WHERE id = ?",
            (nuevo_nombre, nuevo_precio, id_producto)
        )
        conexion.commit()
        print("Producto actualizado correctamente.")
        
        
        def eliminar_producto(id_producto):
        