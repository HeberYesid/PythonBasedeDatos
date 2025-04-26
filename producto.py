class Producto:
    def __init__(self, db):
        self.db = db

    def insertar(self, nombre, precio, stock, categoria):
        query = "INSERT INTO productos (nombre, precio, stock, categoria) VALUES (%s, %s, %s, %s)"
        self.db.execute_query(query, (nombre, precio, stock, categoria))

    def listar(self):
        query = "SELECT * FROM productos"
        return self.db.fetch_query(query)

    def actualizar(self, id, nombre, precio, stock, categoria):
        query = "UPDATE productos SET nombre=%s, precio=%s, stock=%s, categoria=%s WHERE id=%s"
        self.db.execute_query(query, (nombre, precio, stock, categoria, id))

    def eliminar(self, id):
        query = "DELETE FROM productos WHERE id=%s"
        self.db.execute_query(query, (id,))

    # Informes
    def valor_total_inventario(self):
        query = "SELECT SUM(precio * stock) FROM productos"
        result = self.db.fetch_query(query)
        return result[0][0] if result else 0

    def valor_por_categoria(self):
        query = "SELECT categoria, SUM(precio * stock) FROM productos GROUP BY categoria"
        return self.db.fetch_query(query)

    def productos_stock_bajo(self, umbral=10):
        query = "SELECT COUNT(*) FROM productos WHERE stock < %s"
        result = self.db.fetch_query(query, (umbral,))
        return result[0][0] if result else 0