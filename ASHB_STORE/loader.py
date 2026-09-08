import importlib.util
from pathlib import Path
import traceback
from ASHB_CORE.api import AshbApp

class StoreLoader:
    def __init__(self, kernel):
        self.kernel = kernel
        self.apps_dir = Path("APLICACIONES ASHB")
        self.registry = {}

    def discover_apps(self):
        if not self.apps_dir.exists():
            self.apps_dir.mkdir(parents=True)
            self.kernel.logger.warning(f"Se creó el directorio '{self.apps_dir}' automáticamente.")
            return

        print(f">> [STORE] Escaneando volumen de aplicaciones '{self.apps_dir}'...")
        # Busca solo archivos de Python, ignorando los ocultos o de sistema
        for file_path in self.apps_dir.glob("*.py"):
            if not file_path.name.startswith("__"):
                self.registry[file_path.stem] = file_path

        print(f">> [STORE] {len(self.registry)} aplicaciones detectadas y registradas.")

    def list_apps(self) -> list:
        return list(self.registry.keys())

    def launch_app(self, app_name: str):
        app_path = self.registry.get(app_name)
        if not app_path:
            print(f" [!] Error: La app '{app_name}' no se encuentra en el registro.")
            return

        try:
            # 1. Importación dinámica (permite cargar apps en tiempo de ejecución sin detener el SO)
            spec = importlib.util.spec_from_file_location(app_name, app_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # 2. Reflexión: Busca la clase dentro del archivo que herede de AshbApp
            AppClass = None
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, AshbApp) and attr is not AshbApp:
                    AppClass = attr
                    break
            
            if not AppClass:
                raise TypeError(f"Archivo inválido. Falta una clase que herede de 'AshbApp' en {app_name}.py")

            # 3. Ciclo de vida (Sandboxing básico)
            print(f"\n--- INICIANDO ENTORNO: {app_name.upper()} ---")
            app_instance = AppClass(context=self.kernel)
            
            app_instance.setup()    
            app_instance.run()      
            app_instance.cleanup()  

        except Exception as e:
            # Si la app de un tercero falla, el sistema captura el error aquí para que main.py no muera.
            print(f"\n [!] FALLO DE SEGMENTACIÓN: '{app_name}' ha colapsado de forma inesperada.")
            self.kernel.logger.error(f"Excepción crítica en espacio de usuario ({app_name}): {e}\n{traceback.format_exc()}")
        finally:
            print(f"--- CONTEXTO LIBERADO: {app_name.upper()} ---")
