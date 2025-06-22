from abc import ABC, abstractmethod

# 1 - Interfaz común: Component
class ItemPedido(ABC):  # <<interface>> Component
    @abstractmethod
    def calcular_precio(self) -> float:
        pass
    