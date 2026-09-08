import sys
from ASHB_CORE.kernel import Kernel

def main():
    os_kernel = Kernel()
    try:
        os_kernel.boot()
        os_kernel.main_loop()
    except KeyboardInterrupt:
        print("\n\n [!] Interrupción de hardware detectada (Ctrl+C).")
    except Exception as e:
        print(f"\n [KERNEL PANIC] Error catastrófico en núcleo: {e}")
    finally:
        os_kernel.shutdown()
        sys.exit(0)

if __name__ == "__main__":
    main()
