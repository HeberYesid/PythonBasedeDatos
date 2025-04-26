import mariadb
import sys

class Database:
    def __init__(self, host="localhost", user="root", password="", database="python", port=3306):
        """
        Inicializa la conexión a la base de datos MariaDB.
        
        Parámetros:
        - host: Dirección del servidor MariaDB (por defecto: "localhost").
        - user: Nombre de usuario para la conexión (por defecto: "root").
        - password: Contraseña del usuario (por defecto: "").
        - database: Nombre de la base de datos (por defecto: "python").
        - port: Puerto del servidor MariaDB (por defecto: 3306).
        """
        try:
            self.conn = mariadb.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
            )
            self.cursor = self.conn.cursor()
            print(f"Conectado exitosamente a la base de datos '{database}' en MariaDB.")
        except mariadb.Error as e:
            print(f"Error conectando a MariaDB: {e}")
            sys.exit(1)

    def execute_query(self, query, params=()):
        """
        Ejecuta una consulta SQL que modifica datos (INSERT, UPDATE, DELETE).
        
        Parámetros:
        - query: La consulta SQL a ejecutar.
        - params: Tupla de parámetros para la consulta (por defecto: ()).
        """
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            print(f"Consulta ejecutada: {query}")
        except mariadb.Error as e:
            print(f"Error ejecutando consulta: {e}")

    def fetch_query(self, query, params=()):
        """
        Ejecuta una consulta SQL que devuelve datos (SELECT).
        
        Parámetros:
        - query: La consulta SQL a ejecutar.
        - params: Tupla de parámetros para la consulta (por defecto: ()).
        
        Retorna:
        - Lista de tuplas con los resultados de la consulta.
        """
        try:
            self.cursor.execute(query, params)
            results = self.cursor.fetchall()
            print(f"Consulta ejecutada: {query}")
            return results
        except mariadb.Error as e:
            print(f"Error ejecutando consulta: {e}")
            return []

    def close(self):
        """
        Cierra la conexión a la base de datos.
        """
        self.cursor.close()
        self.conn.close()
        print("Conexión a MariaDB cerrada.")