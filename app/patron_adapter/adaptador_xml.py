from patron_adapter.client_interface import ClientInterface
from patron_adapter.fuente_xml import FuenteXML
import xml.etree.ElementTree as ET

# 4- La clase Adaptadora es capaz de trabajar tanto con la clase cliente como con la clase de servicio: 
# implementa la interfaz con el cliente, mientras envuelve el objeto de la clase de servicio.
# 
# La clase adaptadora recibe llamadas del cliente a través de la interfaz adaptadora y las traduce 
# en llamadas al objeto envuelto de la clase de servicio, pero en un formato que pueda comprender.
class AdaptadorXML(ClientInterface):
    def __init__(self, fuente_xml: FuenteXML):
        self.fuente = fuente_xml

    def obtener_datos(self) -> dict:
        xml_data = self.fuente.obtener_datos_xml()
        root = ET.fromstring(xml_data)
        acciones = []
        for accion in root.findall('accion'):
            nombre = accion.find('nombre').text
            precio = accion.find('precio').text
            acciones.append({'nombre': nombre, 'precio': precio})
        return {'mercado': acciones}
    