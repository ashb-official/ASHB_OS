import json
from pathlib import Path
from ASHB_CORE.api import AshbApp

class CalculadoraApp(AshbApp):
    """
    Aplicación ejecutable de la Calculadora que lee su configuración desde calculadora.json
    """
    
    @staticmethod
    def get_metadata() -> dict:
        return {
            "nombre": "ASHB Calculadora Lógica",
            "version": "1.0.0",
            "descripcion": "Calculadora nativa del sistema"
        }

    def setup(self) -> None:
        print(" [*] Cargando preferencias de la calculadora...")
        self.config = {}
        # Usamos pathlib para buscar tu archivo JSON en la misma carpeta
        json_path = Path("APLICACIONES ASHB/calculadora.json")
        
        try:
            if json_path.exists():
                with open(json_path, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
                self.logger.info("Archivo calculadora.json cargado correctamente.")
            else:
                self.logger.warning("No se encontró calculadora.json, usando valores por defecto.")
        except Exception as e:
            self.logger.error(f"Error leyendo el JSON: {e}")

    def run(self) -> None:
        # Extraemos los datos del JSON para usarlos en el programa
        nombre = self.config.get("nombre_app", "Calculadora Estándar")
        color_nums = self.config.get("interfaz", {}).get("color_numeros", "#FFFFFF")
        acceso_red = self.config.get("permisos", {}).get("acceso_internet", False)

        print(f"\n=== {nombre.upper()} ===")
        print(f" [Interfaz cargada con color de números: {color_nums}]")
        
        if acceso_red:
            print(" [Aviso: Esta app tiene acceso a internet]")
        else:
            print(" [Modo Offline - Seguro]")

        print("\n 1. Sumar")
        print(" 2. Restar")
        print(" 0. Salir")
        
        # Bucle interno de la aplicación
        while True:
            opcion = input(" Seleccione operación > ")
            if opcion == '0':
                break
            elif opcion == '1':
                print(" Resultado: 1 + 1 = 2 (Simulación)")
            else:
                print(" Operación no válida en esta demo.")

    def cleanup(self) -> None:
        print(" [*] Guardando historial y cerrando calculadora...")
        self.logger.info("Calculadora finalizada correctamente.")
