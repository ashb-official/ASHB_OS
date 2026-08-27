import json
import time

def encender_sistema():
    print("=========================================")
    print("        INICIALIZANDO HARDWARE...        ")
    print("=========================================")
    time.sleep(0.5)
    
    try:
        with open('ASHB_UI/colores.json', 'r') as f:
            ui = json.load(f)
        print(f"[BOOT] ¡Bienvenido a {ui['nombre_sistema']}! ({ui['tema_predeterminado']})")
    except FileNotFoundError:
        print("[BOOT] Error al cargar interfaz.")

    try:
        with open('ASHB_CORE/sistema.json', 'r') as f:
            core = json.load(f)
        print(f"[CORE] Seguridad {core['seguridad']['encriptacion_datos']} activa. Batería protegida al {core['configuracion_bateria']['limite_carga_maxima']}%")
    except FileNotFoundError:
        print("[CORE] Error al cargar el núcleo.")

    print("=========================================")
    print("      ASHB OS ESTÁ LISTO PARA USAR      ")
    print("=========================================")
    time.sleep(0.5)

def ejecutar_calculadora():
    try:
        with open('ASHB_APPS/calculadora.json', 'r') as f:
            config_app = json.load(f)
        print(f"\n[ASHB APPS] Abriendo: {config_app['nombre_app']}...")
    except FileNotFoundError:
        print("\n[ERROR] Archivos de la calculadora no encontrados.")
        return

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
        if opcion == '5': break
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
            except ValueError: print("\n❌ ERROR: Ingrese solo números.")
        else: print("\n❌ Opción no válida.")
        time.sleep(0.5)

def ejecutar_ajustes():
    try:
        with open('ASHB_APPS/ajustes.json', 'r') as f:
            config_app = json.load(f)
        print(f"\n[ASHB APPS] Abriendo: {config_app['nombre_app']}...")
    except FileNotFoundError:
        print("\n[ERROR] Archivos de ajustes no encontrados.")
        return

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

if __name__ == "__main__":
    while True:
        encender_sistema()
        print("\n¿Qué aplicación desea abrir?")
        print("1. ASHB Calculadora nativa")
        print("2. ASHB Ajustes del sistema")
        print("3. Apagar el sistema (Salir)")
        print("-----------------------------------------")
        
        menu_principal = input("Seleccione (1-3): ")
        if menu_principal == '1':
            ejecutar_calculadora()
        elif menu_principal == '2':
            ejecutar_ajustes()
        elif menu_principal == '3':
            print("\nApagando ASHB OS de forma segura... Cierre de hardware completo.")
            break
        else:
            print("\n❌ Selección incorrecta.")
        time.sleep(1)
