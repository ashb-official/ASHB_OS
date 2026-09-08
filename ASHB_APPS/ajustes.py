import json
from pathlib import Path
from ASHB_CORE.api import AshbApp

class AjustesApp(AshbApp):
    """
    Aplicación ejecutable de Ajustes que lee la configuración desde ajustes.json
    """
    
    @staticmethod
    def get_metadata() -> dict:
        return {
            "nombre": "ASHB Ajustes",
            "version": "1.0.0",
            "descripcion": "Panel de control y configuración del sistema"
        }

    def setup(self) -> None:
        print(" [*] Iniciando el panel de control...")
        self.config = {}
        # Apuntamos específicamente al archivo JSON de ajustes
        json_path = Path("APLICACIONES ASHB/ajustes.json")
        
        try:
            if json_path.exists():
                with open(json_path, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
                self.logger.info("Archivo ajustes.json cargado correctamente.")
            else:
                self.logger.warning("No se encontró ajustes.json, el sistema usará configuraciones por defecto.")
        except Exception as e:
            self.logger.error(f"Error al leer ajustes.json: {e}")

    def run(self) -> None:
        # Aquí leemos valores hipotéticos que vendrían en tu ajustes.json real
        # Si el JSON no los tiene, usamos un valor por defecto (como "Oscuro" o "Español")
        tema_actual = self.config.get("tema_visual", "Oscuro")
        idioma_actual = self.config.get("idioma", "Español")

        print("\n=== ⚙️ AJUSTES DE ASHB_OS ===")
        print(f" [Tema del Sistema: {tema_actual}]")
        print(f" [Idioma del Sistema: {idioma_actual}]")
        print("-----------------------------")
        print(" 1. Modificar Tema")
        print(" 2. Modificar Idioma")
        print(" 0. Volver al Escritorio")
        
        # Bucle interno de la aplicación de Ajustes
        while True:
            opcion = input(" Seleccione una configuración a editar > ")
            if opcion == '0':
                break
            elif opcion == '1':
                print(" -> Función de cambio de tema en desarrollo...")
            elif opcion == '2':
                print(" -> Función de cambio de idioma en desarrollo...")
            else:
                print(" Opción no válida.")

    def cleanup(self) -> None:
        print(" [*] Guardando nuevas configuraciones del sistema...")
        self.logger.info("Módulo de Ajustes cerrado de forma segura.")
