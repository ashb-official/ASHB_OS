import json
import time
from pathlib import Path
from ASHB_CORE.api import AshbApp

class CalculadoraApp(AshbApp):
    @staticmethod
    def get_metadata() -> dict:
        return {"nombre": "ASHB Calculadora nativa", "version": "1.0.0", "descripcion": "Calculadora del sistema"}

    def setup(self) -> None:
        try:
            with open('APLICACIONES ASHB/calculadora.json', 'r') as f:
                self.config_app = json.load(f)
            print(f"\n[ASHB APPS] Abriendo: {self.config_app.get('nombre_app', 'Calculadora')}...")
        except FileNotFoundError:
            print("\n[ERROR] Archivos de configuración de la calculadora no encontrados.")

    def run(self) -> None:
        while True:
            print("\n-----------------------------------------")
            print("          ASHB CALCULATOR MENU           ")
            print("-----------------------------------------")
            print("1. Sumar (+)")
            print("2. Restar (-)")
            print("3. Multiplicar (*)")
            print("4. Dividir (/)")
            print("5. Salir al Menú de ASHB OS")
            print("-----------------------------------------")
            opcion = input("Seleccione una opción (1-5): ")
            
            if opcion == '5': 
                break
            
            if opcion in ['1', '2', '3', '4']:
                try:
                    num1 = float(input("Ingrese primer número: "))
                    num2 = float(input("Ingrese segundo número: "))
                    if opcion == '1': print(f"\n✅ SOLUCIÓN: {num1 + num2}")
                    elif opcion == '2': print(f"\n✅ SOLUCIÓN: {num1 - num2}")
                    elif opcion == '3': print(f"\n✅ SOLUCIÓN: {num1 * num2}")
                    elif opcion == '4':
                        if num2 == 0: print("\n❌ ERROR: No se puede dividir entre cero.")
                        else: print(f"\n✅ SOLUCIÓN: {num1 / num2}")
                except ValueError: 
                    print("\n❌ ERROR: Ingrese solo números.")
            else: 
                print("\n❌ Opción no válida.")
            time.sleep(0.5)

    def cleanup(self) -> None:
        pass
