class Cliente:
    def __init__(self, db):
        self.db = db

    def insertar(self, nombre, apellidos, email, historial_compras):
        query = "INSERT INTO clientes (nombre, apellidos, email, historial_compras) VALUES (%s, %s, %s, %s)"
        self.db.execute_query(query, (nombre, apellidos, email, historial_compras))

    def listar(self):
        query = "SELECT * FROM clientes"
        return self.db.fetch_query(query)

    def actualizar(self, id, nombre, apellidos, email, historial_compras):
        query = "UPDATE clientes SET nombre=%s, apellidos=%s, email=%s, historial_compras=%s WHERE id=%s"
        self.db.execute_query(query, (nombre, apellidos, email, historial_compras, id))

    def eliminar(self, id):
        query = "DELETE FROM clientes WHERE id=%s"
        self.db.execute_query(query, (id,))

    # Informes
    def total_compras_por_cliente(self):
        query = "SELECT nombre, apellidos, historial_compras FROM clientes"
        return self.db.fetch_query(query)

    def valor_total_compras(self):
        query = "SELECT SUM(historial_compras) FROM clientes"
        result = self.db.fetch_query(query)
        return result[0][0] if result else 0