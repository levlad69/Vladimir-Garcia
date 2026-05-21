import mysql.Connector



conexion = mysql.Connector.connect(
    host="localhost",
    port=3306,
    user="vlad69",
    password="contraseña",
    database="repuestos"
)

cursor = Conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXITS productos (
    id INT AUTO_INCREMENT PRYMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2)
    )
    ''')



