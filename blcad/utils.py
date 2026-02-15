from . import bindings

class Database:
    def __init__(self, file_path):
        # Abre la base de datos usando la función de bajo nivel
        self.db_handle = bindings.libdb.db_open(file_path.encode('utf-8'), "r".encode('utf-8'))
        if not self.db_handle:
            raise FileNotFoundError(f"Could not open BRL-CAD database at {file_path}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.db_handle:
            bindings.libdb.db_close(self.db_handle)
            self.db_handle = None

    def get_version(self):
        """Devuelve la versión de la librería BRL-CAD."""
        version_bytes = bindings.libbu.bu_version()
        return version_bytes.decode('utf-8')

# Puedes agregar más métodos para leer, escribir y manipular objetos