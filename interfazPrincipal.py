import tkinter as tk
from interfazProductos import InterfazProductos
from interfazClientes import InterfazClientes

class InterfazPrincipal:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Sistema de Gestión de Tienda")
        
        # Botones para acceder a los módulos
        btn_productos = tk.Button(root, text="Gestionar Productos", command=self.abrir_productos)
        btn_productos.pack(pady=10)
        
        btn_clientes = tk.Button(root, text="Gestionar Clientes", command=self.abrir_clientes)
        btn_clientes.pack(pady=10)
        
        btn_salir = tk.Button(root, text="Salir", command=root.quit)
        btn_salir.pack(pady=10)

    def abrir_productos(self):
        ventana_productos = tk.Toplevel(self.root)
        InterfazProductos(ventana_productos, self.db)

    def abrir_clientes(self):
        ventana_clientes = tk.Toplevel(self.root)
        InterfazClientes(ventana_clientes, self.db)