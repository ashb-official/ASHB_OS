import json
import logging
from pathlib import Path
from ASHB_STORE.loader import StoreLoader

class Kernel:
    def __init__(self):
        self.state = "OFF"
        self.store = StoreLoader(self)
        self.system_config = {}
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            filename='ashb_system.log',
            level=logging.INFO,
            format='[%(asctime)s] %(levelname)s - %(name)s: %(message)s'
        )
        self.logger = logging.getLogger("Kernel")

    def load_system_config(self):
        print(">> [KERNEL] Leyendo configuraciones de bajo nivel (sistema.json)...")
        config_path = Path("ASHB_CORE/sistema.json")
        
        try:
            if config_path.exists():
                with open(config_path, 'r', encoding='utf-8') as f:
                    self.system_config = json.load(f)
                
                # Simulamos la lectura de los datos de tu JSON
                seguridad = self.system_config.get("seguridad", {})
                if seguridad.get("verificacion_arranque") == "activa":
                    encriptacion = seguridad.get("encriptacion_datos", "Desconocida")
                    print(f">> [SECURE BOOT] Verificación de hardware activa. Encriptación: {encriptacion}")
                
                bateria = self.system_config.get("configuracion_bateria", {})
                print(f">> [ENERGÍA] Modo de batería: {bateria.get('modo_ahorro_energia', 'normal')}")
                
            else:
                self.logger.warning("No se encontró sistema.json. Usando valores seguros por defecto.")
        except Exception as e:
            self.logger.error(f"Error crítico al leer configuraciones del sistema: {e}")

    def boot(self):
        self.state = "BOOTING"
        print(">> Inicializando ASHB_OS Kernel...")
        self.logger.info("Kernel arrancando.")
        
        # 1. Cargamos tu archivo sistema.json
        self.load_system_config()
        
        # 2. Le pedimos al Store que descubra las apps
        self.store.discover_apps()
        self.state = "RUNNING"
        print(">> Arranque completado con éxito.\n")

    def main_loop(self):
        while self.state == "RUNNING":
            print("\n" + "="*30)
            print(" 💻 ESCRITORIO ASHB_OS")
            print("="*30)
            
            apps = self.store.list_apps()
            if not apps:
                print(" [!] No hay aplicaciones instaladas.")
            else:
                for idx, app_name in enumerate(apps, 1):
                    print(f" {idx}. {app_name}")
            
            print("\n 0. Apagar Sistema")
            print("="*30)

            choice = input("Seleccione una opción > ").strip()
            
            if choice == '0':
                self.shutdown()
            elif choice.isdigit() and 1 <= int(choice) <= len(apps):
                selected_app = apps[int(choice)-1]
                self.store.launch_app(selected_app)
            else:
                print(" [!] Comando inválido.")

    def shutdown(self):
        print("\n>> Iniciando secuencia de apagado...")
        self.state = "SHUTTING_DOWN"
        self.logger.info("Sistema apagado de forma segura.")
        print(">> ASHB_OS finalizado. Hasta luego.")
