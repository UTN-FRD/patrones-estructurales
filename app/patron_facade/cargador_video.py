# Subsystem class 1
class CargadorVideo:
    def cargar(self, nombre_archivo):
        print(f"📂 Cargando video: {nombre_archivo}")
        return f"datos_binarios({nombre_archivo})"