import ctypes
import platform

def load_dll(dll_name):

    if platform.system()=="Windows":
         return ctypes.CDLL(f"C:/Program Files/BRL-CAD 7.32.2/bin/{dll_name}")
    else:
         return ctypes.CDLL(f"lib{dll_name}.so")
    
libbu= load_dll("libbu.dll")
libdb= load_dll("libdb.dll")

#obtener version libreria bu
libbu.bu_version.restype = ctypes.c_char_p

#abrir base de datos de brl-cad
libdb.db_open.restype = ctypes.c_void_p
libdb.db_open.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]

#cerrar una base de datos
libdb.db_close.restype = ctypes.c_int
libdb.db_close.argtypes = [ctypes.c_void_p]
