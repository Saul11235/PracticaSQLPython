import sqlite3

# creando base de datos
conexion = sqlite3.connect('DATABASE.db')

# cerrando conexion
conexion.close()

print("""
DATABASE.db creada
tambien se pudo usar

create database DATABASE

        """)
