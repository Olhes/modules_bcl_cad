# BRL-CAD Python Bindings

Proyecto para crear bindings de Python para BRL-CAD, permitiendo acceder a la API de C desde Python usando ctypes.

## Estado Actual

✅ **Completado:**
- Carga de bibliotecas DLL de BRL-CAD
- Mapeo de función `db_open`
- Wrapper `open_db()` en Python
- Tests funcionales
- Estructura modular

## Estructura del Proyecto

```
bcl-cad/
├── __init__.py              # Paquete principal
├── bindings.py              # Configuración de ctypes
├── utils/
│   ├── __init__.py
│   └── utils.py             # Funciones wrapper
├── test.py                  # Tests funcionales
└── DOCUMENTACION.md         # Este archivo
```

## Instalación

### Requisitos
- BRL-CAD 7.32.2 instalado en `C:\Program Files\BRL-CAD 7.32.2\`
- Python 3.x
- Windows (actualmente configurado para Windows)

### Configuración
1. Asegúrate de que BRL-CAD esté instalado en la ruta por defecto
2. Agrega `C:\Program Files\BRL-CAD 7.32.2\bin` al PATH del sistema
3. Clona/Descarga este proyecto

## Uso

### Abrir una base de datos

```python
from utils.utils import open_db
from bindings import libbu

# Obtener versión de BRL-CAD
version = libbu.bu_version()
print(f"BRL-CAD Version: {version.decode('utf-8')}")

# Abrir base de datos
db_path = "C:/Program Files/BRL-CAD 7.32.2/share/db/cube.g"
db_handle = open_db(db_path)
print(f"Database opened with handle: {db_handle}")
```

### Bases de datos disponibles

BRL-CAD incluye múltiples bases de datos de ejemplo en `share/db/`:

**Principales para empezar:**
- `cube.g` - Cubo simple
- `sphere.g` - Esfera  
- `demo.g` - Demostración
- `prim.g` - Primitivas geométricas

**Modelos complejos:**
- `tank_car.g` - Tanque de guerra
- `toyjeep.g` - Jeep de juguete
- `m35.g` - Vehículo militar
- `castle.g` - Castillo

## API Reference

### bindings.py

Configuración de ctypes para las bibliotecas de BRL-CAD:

```python
# Bibliotecas cargadas
libbu = ctypes.CDLL("C:/Program Files/BRL-CAD 7.32.2/bin/libbu.dll")
librt = ctypes.CDLL(r"C:\Program Files\BRL-CAD 7.32.2\bin\librt.dll")

# Funciones configuradas
libbu.bu_version()          # Retorna versión de BRL-CAD
librt.db_open(file, mode)   # Abre base de datos
```

### utils/utils.py

Funciones wrapper de alto nivel:

#### `open_db(file_path, mode="r")`
Abre una base de datos de BRL-CAD.

**Parámetros:**
- `file_path` (str): Ruta al archivo .g
- `mode` (str): Modo de apertura ("r" para lectura)

**Retorna:**
- `int`: Handle a la base de datos

**Lanza:**
- `FileNotFoundError`: Si no se puede abrir la base de datos

## Testing

Ejecuta los tests funcionales:

```bash
python test.py
```

Salida esperada:
```
BRL-CAD Version: BRL-CAD Release 7.32.2  The BRL-CAD Utility Library
Abriendo base de datos: C:/Program Files/BRL-CAD 7.32.2/share/db/cube.g
Base de datos abierta exitosamente. Handle: [número]
✅ Todos los tests pasaron correctamente
```

## Arquitectura

### .dll vs .g

- **.dll (Dynamic Link Library)**: Código ejecutable compilado con funciones de la API
- **.g (Geometry Database)**: Archivos de datos con modelos 3D y geometrías

Las DLLs procesan los datos guardados en los archivos .g.

### Flujo de trabajo

1. **bindings.py** - Configura ctypes y carga DLLs
2. **utils/utils.py** - Proporciona funciones amigables para Python
3. **test.py** - Verifica funcionamiento

## Próximos Pasos

### Mapeo de funciones adicionales

- `db_close(handle)` - Cerrar base de datos
- `db_lookup(handle, name)` - Buscar objetos
- `db_get(handle, obj_name)` - Obtener datos de objetos

### Estructuras de datos

- Mapear `struct db_i` para manejo de bases de datos
- Mapear estructuras geométricas (primitivas)

### Funciones de alto nivel

- Operaciones geométricas comunes
- Análisis de propiedades
- Exportación/importación

## Contribuciones

Este proyecto sigue la guía del issue [GSoC #52](https://github.com/opencax/GSoC/issues/52).

## Licencia

[PENDIENTE - Especificar licencia]

## Contacto

[PENDIENTE - Información de contacto]
