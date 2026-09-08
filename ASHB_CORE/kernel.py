import json
import logging
from pathlib import Path
import time
from ASHB_STORE.loader import StoreLoader

class Kernel:
    def __init__(self):
        self.state = "OFF"
        self.store = StoreLoader(self)
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            filename='ashb_system.log', level=logging.INFO,
            format='[%(asctime)s] %(levelname)s - %(name)s: %(message)s'
        )
        self.logger = logging.getLogger("Kernel")

    def load_system_config(self):
        print("=========================================")
        print("        INICIALIZANDO HARDWARE...        ")
        print("=========================================")
        time.sleep(0.5)
        
        # Cargar Interfaz de Usuario
        ui_path = Path("ASHB_UI/colores.json")
        try:
            if ui_path.exists():
                with open(ui_path, 'r', encoding='utf-8') as f:
                    ui = json.load(f)
                print(f"[BOOT] ¡Bienvenido a {ui.get('nombre_sistema', 'ASHB OS')}! ({ui.get('tema_predeterminado', 'Default')})")
        except Exception as e:
            print("[BOOT] Error al cargar interfaz.")

        # Cargar configuraciones del núcleo
        core_path = Path("ASHB_CORE/sistema.json")
        try:
            if core_path.exists():
                with open(core_path, 'r', encoding='utf-8') as f:
                    core = json.load(f)
                seguridad = core.get("seguridad", {})
                bateria = core.get("configuracion_bateria", {})
                print(f"[CORE] Seguridad {seguridad.get('encriptacion_datos', 'Desconocida')} activa. Batería protegida al {bateria.get('limite_carga_maxima', 100)}%")
        except Exception as e:
            print("[CORE] Error al cargar el núcleo.")
            
        print("=========================================")
        print("      ASHB OS ESTÁ LISTO PARA USAR      ")
        print("=========================================")
        time.sleep(0.5)

    def boot(self):
        self.state = "BOOTING"
        self.load_system_config()
        self.store.discover_apps()
        self.state = "RUNNING"

    def main_loop(self):
        while self.state == "RUNNING":
            print("\n¿Qué aplicación desea abrir?")
            
            apps = self.store.list_apps()
            if not apps:
                print(" [!] No hay aplicaciones instaladas.")
            else:
                for idx, app_name in enumerate(apps, 1):
                    print(f"{idx}. {app_name}")
            
            print(f"{len(apps) + 1}. Apagar el sistema (Salir)")
            print("-----------------------------------------")

            choice = input(f"Seleccione (1-{len(apps) + 1}): ").strip()
            
            if choice == str(len(apps) + 1):
                self.shutdown()
            elif choice.isdigit() and 1 <= int(choice) <= len(apps):
                selected_app = apps[int(choice)-1]
                self.store.launch_app(selected_app)
            else:
                print("\n❌ Selección incorrecta.")
            time.sleep(1)

    def shutdown(self):
        print("\nApagando ASHB OS de forma segura... Cierre de hardware completo.")
        self.state = "SHUTTING_DOWN"
