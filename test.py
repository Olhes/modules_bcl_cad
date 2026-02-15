#!/usr/bin/env python3
"""
Prueba de los Python Bindings para BRL-CAD
"""

from utils.utils import open_db
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
