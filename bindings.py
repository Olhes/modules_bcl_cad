import ctypes

# Cargar bibliotecas de BRL-CAD
libbu = ctypes.CDLL("C:/Program Files/BRL-CAD 7.32.2/bin/libbu.dll")
librt = ctypes.CDLL(r"C:\Program Files\BRL-CAD 7.32.2\bin\librt.dll")

# Configurar función bu_version
libbu.bu_version.restype = ctypes.c_char_p
libbu.bu_version.argtypes = []

# Configurar función db_open
librt.db_open.restype = ctypes.c_void_p
librt.db_open.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

# Configurar función db_close
librt.db_close.restype = ctypes.c_int
librt.db_close.argtypes = [ctypes.c_void_p]

librt.db_lookup.restype = ctypes.c_void_p
librt.db_lookup.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_int
]
