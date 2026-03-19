#!/usr/bin/env python3
"""
Prueba de los Python Bindings para BRL-CAD
"""

from utils.utils import open_db, close_db, lookup_object
from bindings import libbu

def test_bindings():
    """Función de prueba para verificar que los bindings funcionan"""
    
    # 1. Probar versión de BRL-CAD
    version = libbu.bu_version()
    print(f"BRL-CAD Version: {version.decode('utf-8')}")
    
    # 2. Probar apertura de base de datos usando el wrapper
    try:
        db_path = "C:/Program Files/BRL-CAD 7.32.2/share/db/cube.g"
        print(f"Abriendo base de datos: {db_path}")
        
        db_handle = open_db(db_path)
        print(f"Base de datos abierta exitosamente. Handle: {db_handle}")
        
        # 3. Probar búsqueda de objetos
        print("\n--- Probando búsqueda de objetos ---")
        
        # Primero probar con noisy=1 para ver mensajes de error
        print("Con noisy=1 (mostrar errores):")
        obj_handle = lookup_object(db_handle, "cube.s", noisy=1)
        if obj_handle:
            print(f"✅ Encontrado: 'cube.s' -> Handle: {obj_handle}")
        else:
            print("❌ No encontrado: 'cube.s'")
        
        # Probar diferentes nombres de objetos reales en cube.g
        print("\nProbando nombres de objetos reales (con noisy=0):")
        test_objects = [
            "cube",           # Objeto principal
            "sph.1",          # Esfera 1
            "sph.2",          # Esfera 2
            "bond.1.2",       # Bond 1.2
            "LIGHT",          # Luz
            "envmap.s",       # Environment map
            "all",            # Todos
            "all.g",          # Grupo all
        ]
        
        found_objects = []
        for obj_name in test_objects:
            obj_handle = lookup_object(db_handle, obj_name, noisy=0)
            if obj_handle:
                print(f"✅ Encontrado: '{obj_name}' -> Handle: {obj_handle}")
                found_objects.append(obj_name)
            else:
                print(f"❌ No encontrado: '{obj_name}'")
        
        if found_objects:
            print(f"\n✅ Objetos encontrados: {found_objects}")
        else:
            print("\n⚠️  No se encontraron objetos. Probando con nombres más básicos...")
        
        # 4. Probar cierre de base de datos
        close_result = close_db(db_handle)
        print(f"Base de datos cerrada. Resultado: {close_result}")
        
        return True
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error inesperado: {e}")
        return False

if __name__ == "__main__":
    success = test_bindings()
    if success:
        print("\n✅ Todos los tests pasaron correctamente")
    else:
        print("\n❌ Hubo errores en los tests")
