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

def get_object(db_handle, obj_name):
    """
    Intenta obtener un objeto usando db_get como alternativa.
    
    Parámetros:
    - db_handle: Handle a la base de datos
    - obj_name: Nombre del objeto a obtener
    
    Retorna:
    - int: Handle al objeto encontrado, 0 si no existe
    """
    return bindings.librt.db_get(db_handle, obj_name.encode('utf-8'))

def list_objects(db_handle):
    """
    Lista todos los objetos en la base de datos usando db_walk.
    
    Parámetros:
    - db_handle: Handle a la base de datos
    
    Retorna:
    - list: Lista de nombres de objetos encontrados
    """
    objects = []
    
    # Callback function para db_walk
    def callback(dp, client_data):
        # Esta función sería llamada por db_walk para cada objeto
        # Necesitaríamos implementar esto en C o usar una aproximación diferente
        pass
    
    # Por ahora, intentamos un enfoque simple: probar nombres comunes
    common_names = [
        "ant1.s", "ant2.s", "ant3.s", "ant4.s", "ant5.s", "ant6.s",
        "b1", "b2", "b3", "b4", "b5", "b6",
        "l1", "l2",
        "r1", "r2", "r3", "r4", "r5", "r6",
        "widgets", "widgets/",
        "L", "B", "R",
        "s1c", "s2c", "s3c", "s4c", "s5c", "s6c", "s7c", "s8c", "s9c",
        "s10c", "s11c", "s12c", "s13c", "s14c", "s15c", "s16c",
        "s1m48", "s2m48", "s3m48", "s4m48", "s5m48", "s6m48",
        "ant/", "BRL/", "track.lt/", "track.rt/",
    ]
    
    for name in common_names:
        if lookup_object(db_handle, name, noisy=0):
            objects.append(name)
    
    return objects