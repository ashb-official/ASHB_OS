import json
import time
from pathlib import Path
from ASHB_CORE.api import AshbApp

class AjustesApp(AshbApp):
    @staticmethod
    def get_metadata() -> dict:
        return {"nombre": "ASHB Ajustes del sistema", "version": "1.0.0", "descripcion": "Panel de control"}

    def setup(self) -> None:
        try:
            with open('APLICACIONES ASHB/ajustes.json', 'r') as f:
                self.config_app = json.load(f)
            print(f"\n[ASHB APPS] Abriendo: {self.config_app.get('nombre_app', 'Ajustes')}...")
        except FileNotFoundError:
            print("\n[ERROR] Archivos de configuración de ajustes no encontrados.")

    def run(self) -> None:
        while True:
            print("\n-----------------------------------------")
            print("            ASHB SETTINGS MENU           ")
            print("-----------------------------------------")
            print("1. Cambiar Tema (Luz/Oscuro)")
            print("2. Modificar Límite de Batería")
            print("3. Ver Info del Sistema")
            print("4. Salir al Menú de ASHB OS")
            print("-----------------------------------------")
            opcion = input("Seleccione una opción (1-4): ")
            
            if opcion == '4':
                print("\nGuardando cambios en el sistema...")
                break
                
            elif opcion == '1':
                try:
                    with open('ASHB_UI/colores.json', 'r') as f: ui = json.load(f)
                    nuevo_tema = "Modo Claro" if ui['tema_predeterminado'] == "Modo Oscuro" else "Modo Oscuro"
                    ui['tema_predeterminado'] = nuevo_tema
                    with open('ASHB_UI/colores.json', 'w') as f: json.dump(ui, f, indent=2)
                    print(f"\n⚙️ SISTEMA: Tema modificado con éxito a: [{nuevo_tema}]")
                except Exception: print("\n❌ Error al modificar la interfaz.")
                
            elif opcion == '2':
                try:
                    with open('ASHB_CORE/sistema.json', 'r') as f: core = json.load(f)
                    nuevo_limite = int(input("Ingrese el nuevo límite de carga (50-100): "))
                    if 50 <= nuevo_limite <= 100:
                        core['configuracion_bateria']['limite_carga_maxima'] = nuevo_limite
                        with open('ASHB_CORE/sistema.json', 'w') as f: json.dump(core, f, indent=2)
                        print(f"\n⚙️ NÚCLEO: Nuevo límite guardado a un: {nuevo_limite}%")
                    else: print("\n❌ RANGO INVÁLIDO: Use un valor entre 50 y 100.")
                except ValueError: print("\n❌ ERROR: Ingrese un número entero válido.")
                
            elif opcion == '3':
                print("\n=========================================")
                print("         INFORMACIÓN DE ASHB OS          ")
                print("=========================================")
                print("Desarrollador Principal: sharp")
                print("Arquitectura: Linux Virtual Kernel (WSL)")
                print("Estado de Licencia: Código Abierto AOSP")
                print("=========================================")
                
            time.sleep(1)

    def cleanup(self) -> None:
        pass
