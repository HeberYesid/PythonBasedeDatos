# Ejemplo de Conexión a MariaDB con Python

Este proyecto muestra cómo conectarse a una base de datos MariaDB utilizando Python.

## Requisitos

- Python 3.6 o superior
- MariaDB 10.5 o superior
- Módulo `mariadb` para Python

## Instalación

1. Instala el módulo de MariaDB para Python:

```bash
pip install mariadb
```

2. Asegúrate de tener una base de datos MariaDB funcionando. Por defecto, el código se conecta a:
   - Host: localhost
   - Usuario: root
   - Contraseña: (vacía)
   - Base de datos: python
   - Puerto: 3306

Si necesitas modificar estos parámetros, edítalos en el archivo `ejemplo_uso.py`.

## Ejecutar el código

Para ejecutar el ejemplo, simplemente usa:

```bash
python main.py
```

Este script creará una tabla de ejemplo llamada `usuarios`, insertará un registro y mostrará los datos almacenados.

## Estructura del proyecto

-`main.py`: Punto de entrada del programa, inicializa la interfaz principal.

-`database.py`: Maneja la conexión a la base de datos MariaDB (asumiré que ya lo tienes, pero lo incluiré para referencia).

-`producto.py`: Clase para gestionar las operaciones CRUD de productos y generar informes relacionados.

-`cliente.py`: Clase para gestionar las operaciones CRUD de clientes y generar informes relacionados.

-`interfaz_principal.py`: Ventana principal con accesos a los módulos de productos y clientes.

-`interfaz_productos.py`: Interfaz para gestionar productos (CRUD e informes).

-`interfaz_clientes.py`: Interfaz para gestionar clientes (CRUD e informes).

