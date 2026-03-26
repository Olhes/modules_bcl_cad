#!/usr/bin/env python3
"""
Prueba de los Python Bindings para BRL-CAD
"""

from utils.utils import open_db, close_db, lookup_object, get_object
from bindings import libbu

def test_bindings():
    """Función de prueba para verificar que los bindings funcionan"""
    
    # 1. Probar versión de BRL-CAD
    version = libbu.bu_version()
    print(f"BRL-CAD Version: {version.decode('utf-8')}")
    
    # 2. Probar apertura de base de datos usando el wrapper
    try:
        # Primero, vamos a ver qué archivos .g existen realmente
        import os
        db_dir = "C:/Program Files/BRL-CAD 7.32.2/share/db"
        print(f"\n📁 Archivos .g en {db_dir}:")
        if os.path.exists(db_dir):
            g_files = [f for f in os.listdir(db_dir) if f.endswith('.g')]
            for f in g_files[:10]:  # Mostrar solo los primeros 10
                print(f"   - {f}")
        else:
            print(f"   ❌ Directorio no encontrado: {db_dir}")
        
        # DEBUG: Analicemos qué está pasando con db_open
        print(f"\n🔍 DEBUG: Analizando db_open...")
        
        # Probar abrir un archivo que NO existe
        print("1. Abriendo archivo que NO existe:")
        fake_handle = None
        try:
            fake_handle = open_db("C:/fake/path/nonexistent.g")
            print(f"   Handle: {fake_handle} (hex: {hex(fake_handle)})")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Probar abrir un archivo que SÍ existe
        print("\n2. Abriendo archivo que SÍ existe:")
        real_handle = None
        try:
            real_handle = open_db("C:/Program Files/BRL-CAD 7.32.2/share/db/castle.g")
            print(f"   Handle: {real_handle} (hex: {hex(real_handle)})")
        except Exception as e:
            print(f"   Error: {e}")
        
        # Comparar handles
        print(f"\n3. Comparación:")
        if fake_handle is not None and real_handle is not None:
            print(f"   Fake == Real: {fake_handle == real_handle}")
            print(f"   Fake es 0: {fake_handle == 0}")
            print(f"   Real es 0: {real_handle == 0}")
        
        # Obtener nombres reales usando mged
        print(f"\n🔍 Obteniendo nombres reales con mged...")
        
        # Nombres obtenidos manualmente de castle.g
        castle_objects = [
            "LIGHT", "ggshaft", "r4", "ttop3", "all.g", "gmain",
            "r5", "ttop4", "arch", "gpillar", "rbar", "ttop5",
            "arch1", "gpillar1", "rfwall", "ttop6", "arch2", "gpillar2",
            "shortwall", "ttop7", "archin", "gsh", "slope1", "ttop8",
            "archout", "gshaft", "slope2", "walk", "blend", "gstuff",
            "tbase1", "wall", "botbar", "gtedge1", "tbase2", "wall1",
            "castle", "gtedge2", "topbar", "wall2", "cfloor", "gtedge3",
            "tower", "wall3", "cube", "gtedge4", "tower1", "wbase1",
            "cube3", "gtniche", "tower2", "wbase2", "cube4", "gtop",
            "tower3", "wedge", "cube5", "gtseg1", "tower4", "wedge3",
            "cube6", "gtseg2", "tshaft", "wniche", "cylinder", "gtseg3",
            "tss1", "wseg", "earth", "gtslab", "tsseg", "wseg1",
            "earth.r", "gwedge", "tsw1", "wseg2", "floor", "keystone",
            "tsw2", "wseg3", "gatebot", "lbar", "tsws1", "wseg4",
            "gatehouse", "lfwall", "tsws2", "wseg5", "gatetop", "light.r",
            "tsws3", "wseg6", "gbase1", "midbar", "tsws4", "wseg7",
            "gbase2", "port1", "tsws5", "wseg8", "gbase3", "port2",
            "tsws6", "wseg9", "gbase4", "portcullis", "tsws7", "wslab",
            "gblend", "pyramid", "tswseg", "wtop1", "gcap", "r1",
            "ttop", "wtop2", "gcap1", "r2", "ttop1", "xxx", "gcap2", "r3", "ttop2"
        ]
        
        print(f"   ✅ Objetos manuales en castle.g: {len(castle_objects)}")
        print(f"   Primeros 10 objetos: {castle_objects[:10]}")
        
        # Probar con nombres reales
        print(f"\n🔍 Probando con nombres reales:")
        db_handle = open_db("C:/Program Files/BRL-CAD 7.32.2/share/db/castle.g")
        found_objects = []
        
        # Probar con db_lookup primero
        print("   1. Probando con db_lookup:")
        for obj_name in castle_objects[:5]:  # Solo 5 para no saturar
            result = lookup_object(db_handle, obj_name, noisy=0)
            if result:
                print(f"      ✅ db_lookup encontró: '{obj_name}' -> {result}")
                found_objects.append(obj_name)
            else:
                print(f"      ❌ db_lookup no encontró: '{obj_name}'")
        
        # Probar con db_get como alternativa
        print("\n   2. Probando con db_get:")
        for obj_name in castle_objects[:5]:
            result = get_object(db_handle, obj_name)
            if result:
                print(f"      ✅ db_get encontró: '{obj_name}' -> {result}")
                found_objects.append(obj_name)
            else:
                print(f"      ❌ db_get no encontró: '{obj_name}'")
        
        if found_objects:
            print(f"\n🎉 ÉXITO: Se encontraron {len(found_objects)} objetos!")
            print(f"   Objetos encontrados: {found_objects}")
        else:
            print(f"\n❌ Ninguna función funcionó")
            print("   🔍 Esto sugiere un problema fundamental con la API")
        
        close_db(db_handle)
        
        return True
        
    except Exception as e:
        print(f"Error general: {e}")
        return False

if __name__ == "__main__":
    success = test_bindings()
    if success:
        print("\n✅ Test completado")
    else:
        print("\n❌ Falló el test")
