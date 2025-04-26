import tkinter as tk
from database import Database
from interfazPrincipal import InterfazPrincipal


if __name__ == "__main__":
    # Inicializar la base de datos (ajusta las credenciales según tu configuración)
    db = Database(user="root", password="", database="python")
    
    # Primero verifica si las tablas existen, si no, créalas
    db.execute_query("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50),
            apellidos VARCHAR(50),
            email VARCHAR(100),
            historial_compras FLOAT
        )
    """)
    
    db.execute_query("""
        CREATE TABLE IF NOT EXISTS productos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50),
            precio FLOAT,
            stock INT,
            categoria VARCHAR(50)
        )
    """)

    # Consultar datos
    resultados = db.fetch_query("SELECT * FROM clientes")
    print(resultados)

    # Iniciar la interfaz gráfica
    root = tk.Tk()
    app = InterfazPrincipal(root, db)
    root.mainloop()

    # Cerrar la conexión
    db.close()