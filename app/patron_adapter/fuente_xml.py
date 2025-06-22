
# 3- Service es alguna clase útil (normalmente de una tercera parte o heredada). 
# El cliente no puede utilizar directamente esta clase porque tiene una interfaz incompatible
class FuenteXML:
    def obtener_datos_xml(self) -> str:
        return """<mercado>
                    <accion><nombre>ABC</nombre><precio>123</precio></accion>
                    <accion><nombre>XYZ</nombre><precio>456</precio></accion>
                  </mercado>"""
    