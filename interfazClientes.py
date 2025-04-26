import tkinter as tk
from tkinter import messagebox, ttk
from cliente import Cliente

class InterfazClientes:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.cliente = Cliente(db)
        self.root.title("Gestión de Clientes")
        
        # Treeview para mostrar clientes
        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "Apellidos", "Email", "Historial Compras"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellidos", text="Apellidos")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Historial Compras", text="Historial Compras")
        self.tree.pack(pady=10)
        
        # Botones CRUD
        btn_agregar = tk.Button(root, text="Agregar", command=self.agregar_cliente)
        btn_agregar.pack(side="left", padx=5)
        
        btn_editar = tk.Button(root, text="Editar", command=self.editar_cliente)
        btn_editar.pack(side="left", padx=5)
        
        btn_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_cliente)
        btn_eliminar.pack(side="left", padx=5)
        
        # Botones de informes
        btn_total_cliente = tk.Button(root, text="Total por Cliente", command=self.mostrar_total_cliente)
        btn_total_cliente.pack(side="left", padx=5)
        
        btn_valor_total = tk.Button(root, text="Valor Total Compras", command=self.mostrar_valor_total)
        btn_valor_total.pack(side="left", padx=5)
        
        self.actualizar_lista()

    def actualizar_lista(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        clientes = self.cliente.listar()
        for cli in clientes:
            self.tree.insert("", "end", values=cli)

    def agregar_cliente(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Cliente")
        
        tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
        nombre = tk.Entry(ventana)
        nombre.grid(row=0, column=1)
        
        tk.Label(ventana, text="Apellidos:").grid(row=1, column=0)
        apellidos = tk.Entry(ventana)
        apellidos.grid(row=1, column=1)
        
        tk.Label(ventana, text="Email:").grid(row=2, column=0)
        email = tk.Entry(ventana)
        email.grid(row=2, column=1)
        
        tk.Label(ventana, text="Historial Compras:").grid(row=3, column=0)
        historial = tk.Entry(ventana)
        historial.grid(row=3, column=1)
        
        def guardar():
            self.cliente.insertar(nombre.get(), apellidos.get(), email.get(), float(historial.get()))
            self.actualizar_lista()
            ventana.destroy()
        
        tk.Button(ventana, text="Guardar", command=guardar).grid(row=4, column=1)

    def editar_cliente(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona un cliente para editar.")
            return
        
        id = self.tree.item(selected[0])['values'][0]
        cliente = self.tree.item(selected[0])['values']
        
        ventana = tk.Toplevel(self.root)
        ventana.title("Editar Cliente")
        
        tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
        nombre = tk.Entry(ventana)
        nombre.insert(0, cliente[1])
        nombre.grid(row=0, column=1)
        
        tk.Label(ventana, text="Apellidos:").grid(row=1, column=0)
        apellidos = tk.Entry(ventana)
        apellidos.insert(0, cliente[2])
        apellidos.grid(row=1, column=1)
        
        tk.Label(ventana, text="Email:").grid(row=2, column=0)
        email = tk.Entry(ventana)
        email.insert(0, cliente[3])
        email.grid(row=2, column=1)
        
        tk.Label(ventana, text="Historial Compras:").grid(row=3, column=0)
        historial = tk.Entry(ventana)
        historial.insert(0, cliente[4])
        historial.grid(row=3, column=1)
        
        def guardar():
            self.cliente.actualizar(id, nombre.get(), apellidos.get(), email.get(), float(historial.get()))
            self.actualizar_lista()
            ventana.destroy()
        
        tk.Button(ventana, text="Guardar", command=guardar).grid(row=4, column=1)

    def eliminar_cliente(self):
        selected = self.tree.selection()
        if selected:
            id = self.tree.item(selected[0])['values'][0]
            self.cliente.eliminar(id)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Selecciona un cliente para eliminar.")

    def mostrar_total_cliente(self):
        clientes = self.cliente.total_compras_por_cliente()
        texto = "\n".join([f"{cli[0]} {cli[1]}: {cli[2]}" for cli in clientes])
        messagebox.showinfo("Total por Cliente", texto)

    def mostrar_valor_total(self):
        total = self.cliente.valor_total_compras()
        messagebox.showinfo("Valor Total Compras", f"El valor total de compras es: {total}")