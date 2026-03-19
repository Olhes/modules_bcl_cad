import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import bindings

def open_db(file_path, mode="r"):
    """
    Abre una base de datos de BRL-CAD y devuelve un puntero a la estructura.
    """
    # Llama a la función de la API de C
    db_handle = bindings.librt.db_open(file_path.encode('utf-8'), mode.encode('utf-8'))
    
    if not db_handle:
        # Maneja el error si la apertura falla
        raise FileNotFoundError(f"No se pudo abrir la base de datos en: {file_path}")
        
    return db_handle

def close_db(db_handle):
    """
    Cierra una base de datos de BRL-CAD.
    
    Parámetros:
    - db_handle: Handle a la base de datos
    
    Retorna:
    - int: 0 si éxito, !=0 si error
    """
    return bindings.librt.db_close(db_handle)

def lookup_object(db_handle, obj_name, noisy=1):
    """
    Busca un objeto en la base de datos de BRL-CAD.
    
    Parámetros:
    - db_handle: Handle a la base de datos
    - obj_name: Nombre del objeto a buscar
    - noisy: 1 para mostrar errores, 0 para silencioso
    
    Retorna:
    - int: Handle al objeto encontrado, 0 si no existe
    """
    return bindings.librt.db_lookup(db_handle, obj_name.encode('utf-8'), noisy)