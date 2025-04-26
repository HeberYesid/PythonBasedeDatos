import tkinter as tk
from tkinter import messagebox, ttk
from producto import Producto

class InterfazProductos:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.producto = Producto(db)
        self.root.title("Gestión de Productos")
        
        # Treeview para mostrar productos
        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "Precio", "Stock", "Categoría"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.pack(pady=10)
        
        # Botones CRUD
        btn_agregar = tk.Button(root, text="Agregar", command=self.agregar_producto)
        btn_agregar.pack(side="left", padx=5)
        
        btn_editar = tk.Button(root, text="Editar", command=self.editar_producto)
        btn_editar.pack(side="left", padx=5)
        
        btn_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_producto)
        btn_eliminar.pack(side="left", padx=5)
        
        # Botones de informes
        btn_valor_total = tk.Button(root, text="Valor Total Inventario", command=self.mostrar_valor_total)
        btn_valor_total.pack(side="left", padx=5)
        
        btn_valor_categoria = tk.Button(root, text="Valor por Categoría", command=self.mostrar_valor_categoria)
        btn_valor_categoria.pack(side="left", padx=5)
        
        btn_stock_bajo = tk.Button(root, text="Stock Bajo", command=self.mostrar_stock_bajo)
        btn_stock_bajo.pack(side="left", padx=5)
        
        self.actualizar_lista()

    def actualizar_lista(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        productos = self.producto.listar()
        for prod in productos:
            self.tree.insert("", "end", values=prod)

    def agregar_producto(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Producto")
        
        tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
        nombre = tk.Entry(ventana)
        nombre.grid(row=0, column=1)
        
        tk.Label(ventana, text="Precio:").grid(row=1, column=0)
        precio = tk.Entry(ventana)
        precio.grid(row=1, column=1)
        
        tk.Label(ventana, text="Stock:").grid(row=2, column=0)
        stock = tk.Entry(ventana)
        stock.grid(row=2, column=1)
        
        tk.Label(ventana, text="Categoría:").grid(row=3, column=0)
        categoria = tk.Entry(ventana)
        categoria.grid(row=3, column=1)
        
        def guardar():
            self.producto.insertar(nombre.get(), float(precio.get()), int(stock.get()), categoria.get())
            self.actualizar_lista()
            ventana.destroy()
        
        tk.Button(ventana, text="Guardar", command=guardar).grid(row=4, column=1)

    def editar_producto(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona un producto para editar.")
            return
        
        id = self.tree.item(selected[0])['values'][0]
        producto = self.tree.item(selected[0])['values']
        
        ventana = tk.Toplevel(self.root)
        ventana.title("Editar Producto")
        
        tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
        nombre = tk.Entry(ventana)
        nombre.insert(0, producto[1])
        nombre.grid(row=0, column=1)
        
        tk.Label(ventana, text="Precio:").grid(row=1, column=0)
        precio = tk.Entry(ventana)
        precio.insert(0, producto[2])
        precio.grid(row=1, column=1)
        
        tk.Label(ventana, text="Stock:").grid(row=2, column=0)
        stock = tk.Entry(ventana)
        stock.insert(0, producto[3])
        stock.grid(row=2, column=1)
        
        tk.Label(ventana, text="Categoría:").grid(row=3, column=0)
        categoria = tk.Entry(ventana)
        categoria.insert(0, producto[4])
        categoria.grid(row=3, column=1)
        
        def guardar():
            self.producto.actualizar(id, nombre.get(), float(precio.get()), int(stock.get()), categoria.get())
            self.actualizar_lista()
            ventana.destroy()
        
        tk.Button(ventana, text="Guardar", command=guardar).grid(row=4, column=1)

    def eliminar_producto(self):
        selected = self.tree.selection()
        if selected:
            id = self.tree.item(selected[0])['values'][0]
            self.producto.eliminar(id)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Selecciona un producto para eliminar.")

    def mostrar_valor_total(self):
        total = self.producto.valor_total_inventario()
        messagebox.showinfo("Valor Total Inventario", f"El valor total del inventario es: {total}")

    def mostrar_valor_categoria(self):
        categorias = self.producto.valor_por_categoria()
        texto = "\n".join([f"{cat[0]}: {cat[1]}" for cat in categorias])
        messagebox.showinfo("Valor por Categoría", texto)

    def mostrar_stock_bajo(self):
        cantidad = self.producto.productos_stock_bajo()
        messagebox.showinfo("Stock Bajo", f"Cantidad de productos con stock bajo: {cantidad}")