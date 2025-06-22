from patron_facade.cargador_video import CargadorVideo
from patron_facade.codificador import Codificador
from patron_facade.compresor import Compresor
from patron_facade.subidor import Subidor

# Facade
class VideoFacade:
    def __init__(self):
        self.cargador = CargadorVideo()
        self.codificador = Codificador()
        self.compresor = Compresor()
        self.subidor = Subidor()

    def procesar_y_subir(self, nombre_archivo, formato):
        print("\n🎬 Iniciando proceso con la fachada...")
        datos = self.cargador.cargar(nombre_archivo)
        archivo_codificado = self.codificador.codificar(datos, formato)
        archivo_comprimido = self.compresor.comprimir(archivo_codificado)
        url = self.subidor.subir(archivo_comprimido)
        print("✅ Proceso finalizado.")
        return url
    