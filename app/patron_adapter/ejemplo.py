from patron_adapter.fuente_xml import FuenteXML
from patron_adapter.fuente_json import FuenteJSON
from patron_adapter.adaptador_xml import AdaptadorXML
from patron_adapter.cliente_analisis import ClienteDeAnalisis

# el cliente necesita un adaptador para trabajar con la fuente XML
print("Procesando datos de fuente XML a través del adaptador:")
fuente = FuenteXML()
adaptador = AdaptadorXML(fuente)

cliente = ClienteDeAnalisis(adaptador)
cliente.procesar()

# Ahora el cliente puede trabajar directamente con la fuente JSON sin necesidad de adaptador
# y sin necesidad de cambiar el código del cliente.
print("\nProcesando datos de fuente JSON directamente:")
fuente_directa = FuenteJSON()
cliente = ClienteDeAnalisis(fuente_directa)
cliente.procesar()
