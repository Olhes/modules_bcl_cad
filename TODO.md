# TODO - BRL-CAD Python Bindings

## Fase 1: Funciones CRUD Básicas (Priority: HIGH)

### Database Operations
- [ ] `db_close(handle)` - Cerrar base de datos
- [ ] `db_lookup(handle, name)` - Buscar objetos por nombre
- [ ] `db_dir(handle, path)` - Listar contenidos del directorio
- [ ] `db_get(handle, obj_name)` - Obtener datos de objetos

### Object Operations
- [ ] `rt_db_get_internal(handle, obj_name, &intern, &mat, &rt_uniresource)` - Obtener datos internos
- [ ] `rt_db_put_internal(handle, obj_name, &intern, &mat)` - Guardar objeto modificado
- [ ] `db_delete(handle, obj_name)` - Eliminar objeto

## Fase 2: Estructuras de Datos (Priority: HIGH)

### Core Structures
- [ ] Mapear `struct db_i` - Database instance
- [ ] Mapear `struct directory` - Directory structure
- [ ] Mapear `struct rt_db_internal` - Internal object representation
- [ ] Mapear primitivas geométricas:
  - [ ] `struct rt_arb_internal` - Arbitrary polyhedron
  - [ ] `struct rt_tor_internal` - Torus
  - [ ] `struct rt_tgc_internal` - Truncated general cone
  - [ ] `struct rt_ell_internal` - Ellipsoid
  - [ ] `struct rt_part_internal` - Particle
  - [ ] `struct rpc_internal` - Right parabolic cylinder

## Fase 3: Operaciones Geométricas (Priority: MEDIUM)

### Boolean Operations
- [ ] Implementar union (u)
- [ ] Implementar intersection (+)
- [ ] Implementar difference (-)
- [ ] Implementar region (R)

### Transformations
- [ ] Translation
- [ ] Rotation
- [ ] Scaling
- [ ] Matrix operations

## Fase 4: Funciones de Alto Nivel (Priority: MEDIUM)

### Analysis Functions
- [ ] Volume calculation
- [ ] Surface area calculation
- [ ] Mass properties
- [ ] Bounding box calculation

### Import/Export
- [ ] STL export
- [ ] OBJ export
- [ ] STEP import/export
- [ ] DXF import/export

## Fase 5: Pythonic API (Priority: MEDIUM)

### Classes
- [ ] `BRLCADDatabase` class
- [ ] `GeometryObject` base class
- [ ] Specific geometry classes (Sphere, Box, Cylinder, etc.)
- [ ] `Region` class for boolean combinations

### Convenience Methods
- [ ] Context managers for database operations
- [ ] Iterator support for directory traversal
- [ ] Property access for object attributes
- [ ] Method chaining for transformations

## Fase 6: Testing & Documentation (Priority: MEDIUM)

### Unit Tests
- [ ] Test all CRUD operations
- [ ] Test geometry creation and modification
- [ ] Test boolean operations
- [ ] Test import/export functions

### Documentation
- [ ] API reference documentation
- [ ] Tutorial examples
- [ ] Performance benchmarks
- [ ] Integration examples

## Fase 7: Advanced Features (Priority: LOW)

### Ray Tracing Integration
- [ ] Ray-object intersection
- [ ] Shadow ray casting
- [ ] Lighting models

### Visualization
- [ ] Basic 3D visualization
- [ ] Wireframe rendering
- [ ] Solid rendering

## Current Status
- ✅ Project structure
- ✅ Basic ctypes setup
- ✅ db_open function mapping
- ✅ open_db wrapper function
- ✅ Basic testing framework

## Next Immediate Steps
1. Implement `db_close` function
2. Add `db_lookup` for object search
3. Create basic structure mapping for `db_i`
4. Test with real database objects
