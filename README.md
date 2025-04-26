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
python ejemplo_uso.py
```

Este script creará una tabla de ejemplo llamada `usuarios`, insertará un registro y mostrará los datos almacenados.

## Estructura del proyecto

- `main.py`: Contiene la clase `Database` que gestiona la conexión con MariaDB
- `ejemplo_uso.py`: Un ejemplo de cómo usar la clase Database 