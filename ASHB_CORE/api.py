from abc import ABC, abstractmethod
import logging

class AshbApp(ABC):
    """
    Contrato de interfaz (API) para todas las aplicaciones de ASHB_OS.
    Cualquier app en 'APLICACIONES ASHB' debe heredar de esta clase abstracta.
    """
    def __init__(self, context=None):
        self.context = context
        self.logger = logging.getLogger(self.get_metadata().get('nombre', 'AppDesconocida'))

    @staticmethod
    @abstractmethod
    def get_metadata() -> dict:
        pass

    @abstractmethod
    def setup(self) -> None:
        pass

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def cleanup(self) -> None:
        pass
