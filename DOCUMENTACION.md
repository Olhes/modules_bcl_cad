# BRL-CAD Python Bindings

Proyecto para crear bindings de Python para BRL-CAD, permitiendo acceder a la API de C desde Python usando ctypes.

## Estado Actual

### ✅ Completado
- **Conexión con BRL-CAD**: Carga exitosa de DLLs `libbu.dll` y `librt.dll`
- **Obtención de versión**: Función `bu_version()` implementada y funcionando
- **Apertura de bases de datos**: Función `db_open()` implementada y funcionando
- **Cierre de bases de datos**: Función `db_close()` implementada y funcionando
- **Detección de archivos**: Sistema que encuentra 37 bases de datos disponibles
- **Manejo de errores**: Sistema robusto para archivos inexistentes
- **Mapeo de `db_lookup`**: Función configurada con ctypes (requiere directory handles)

### ⚠️ En Desarrollo
- **Acceso a objetos individuales**: `db_lookup` requiere investigación de API para directory handles
- **Listado de contenidos**: Necesita funciones adicionales para enumerar objetos

### 🔄 Pendiente
- Mapear estructuras geométricas (primitivas)
- Funciones de alto nivel (operaciones geométricas)
- Análisis de propiedades
- Exportación/importación

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

# Cerrar base de datos
close_result = close_db(db_handle)
print(f"Database closed with result: {close_result}")

# Buscar objeto en la base de datos
obj_handle = lookup_object(db_handle, "object_name")
if obj_handle:
    print(f"Object found with handle: {obj_handle}")
else:
    print("Object not found")
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
librt.db_close(handle)      # Cierra base de datos
librt.db_lookup(handle, name, noisy)  # Busca objetos en la base de datos
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

#### `close_db(db_handle)`
Cierra una base de datos de BRL-CAD.

**Parámetros:**
- `db_handle` (int): Handle a la base de datos

**Retorna:**
- `int`: 0 si éxito, !=0 si error

#### `lookup_object(db_handle, obj_name, noisy=1)`
Busca un objeto en la base de datos de BRL-CAD.

**Parámetros:**
- `db_handle` (int): Handle a la base de datos
- `obj_name` (str): Nombre del objeto a buscar
- `noisy` (int): 1 para mostrar errores, 0 para silencioso

**Retorna:**
- `int`: Handle al objeto encontrado, 0 si no existe

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

--- Probando búsqueda de objetos ---
Con noisy=1 (mostrar errores):
db_lookup(object_name) failed: object_name does not exist
❌ No encontrado: 'object_name'

[Resultados de búsqueda de objetos]

Base de datos cerrada. Resultado: 0
✅ Todos los tests pasaron correctamente
```

**Nota:** La búsqueda de objetos puede no encontrar resultados si los nombres no coinciden exactamente con los objetos en la base de datos. Use `noisy=1` para ver mensajes de error detallados.

## Test Simple

Ejecuta el test simple para estado actual:

```bash
python simple_test.py
```

Salida esperada:
```
🚀 BRL-CAD Python Bindings - Estado Actual
==================================================
✅ BRL-CAD Version: BRL-CAD Release 7.32.2

📁 Bases de datos disponibles: 37 archivos .g
   1. aet.g, 2. axis.g, 3. bearing.g, [...]

🔍 Probando apertura de bases de datos:
   📂 castle.g: ✅ Abierta correctamente
   📂 axis.g: ✅ Abierta correctamente  
   📂 aet.g: ✅ Abierta correctamente

🎯 ESTADO ACTUAL DEL PROYECTO:
   ✅ Puede leer bases de datos BRL-CAD
   ✅ Puede abrir y cerrar archivos .g
   ✅ Conexión con DLLs funcionando
   ⚠️  Acceso a objetos requiere investigación adicional

🎉 CONCLUSIÓN:
   ¡El proyecto SÍ puede leer bases de datos BRL-CAD!
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

- ✅ `db_close(handle)` - Cerrar base de datos
- ✅ `db_lookup(handle, name, noisy)` - Buscar objetos
- `db_get(handle, obj_name)` - Obtener datos de objetos
- `db_walk(handle, func, data)` - Recorrer todos los objetos
- `db_put_internal(handle, dp, name, where)` - Agregar objetos

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
