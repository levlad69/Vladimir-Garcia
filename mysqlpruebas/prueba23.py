import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="vlad69",
    password="contraseña",
    database="repuestos"
)

cursor = conexion.cursor()

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        descripcion TEXT,
        precio DECIMAL(10, 2)
    )
''')

# Insertar algunos datos de ejemplo
cursor.execute("INSERT INTO productos (nombre, descripcion, precio) VALUES (%s, %s, %s)",
               ("Filtro de aceite", "Filtro para motor 1.6", 1500.00))
cursor.execute("INSERT INTO productos (nombre, descripcion, precio) VALUES (%s, %s, %s)",
               ("Bujía", "Bujía NGK para motores a gasolina", 800.00))
cursor.execute("INSERT INTO productos (nombre, descripcion, precio) VALUES (%s, %s, %s)",
               ("Pastilla de freno", "Juego delantero para VW", 3200.00))

# Confirmar los cambios
conexion.commit()

# Mostrar todo el contenido de la tabla
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

print("📦 Productos cargados:")
for producto in productos:
    print(producto)

# Cerrar conexión
cursor.close()
conexion.close()
