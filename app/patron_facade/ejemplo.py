from patron_facade.video_facade import VideoFacade

# Client
fachada = VideoFacade()  # ← linksToSubsystemObjects
url = fachada.procesar_y_subir("gato_lindo.mp4", "avi")  # ← subsystemOperation()
print(f"\n🐱 Video disponible en: {url}")
