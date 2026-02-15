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