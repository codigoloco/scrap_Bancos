import app
from bd import LEER_2

def eliminar():
    import shutil
    import os

    # Ruta de la carpeta cuyo contenido se va a eliminar
    carpeta_a_vaciar = 'C:\AdjuntosQSL\BNC'

    # Eliminar todo el contenido de la carpeta
    try:
        for filename in os.listdir(carpeta_a_vaciar):
            file_path = os.path.join(carpeta_a_vaciar, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"No se pudo eliminar {file_path}. Razón: {e}")
    except:
        print("carpeta a eliminar no existe")

    print("El contenido de la carpeta ha sido eliminado exitosamente.")

def proceso():
    LEER_2()
    for i in LEER_2():
        if i[3]=="BNC":
            eliminar()
            app.BNC()
        elif i[3]=="BVC":
            eliminar()
            #app.BVC()


proceso()

