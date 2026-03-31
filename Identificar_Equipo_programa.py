import urllib.request
import urllib.error
import os

os.system("color 0B")

# Bucle infinito para consultar todas las MACs que necesites sin reiniciar
while True:
    print("\n" + "="*35)
    print("   IDENTIFICADOR DE FABRICANTE MAC   ")
    
    print("="*35)
    print("1. Consultar una dirección MAC")
    print("2. Salir del sistema")
    
    opcion = input("\nElige una opción (1 o 2): ")
    
    if opcion == '1':
        mac_input = input("Ingresa la MAC (ej. 00:1A:2B:3C:4D:5E): ")
        
        # Limpiamos el formato por si la copias con guiones o espacios
        mac_limpia = mac_input.replace(" ", "").replace("-", ":")
        url = f"https://api.macvendors.com/{mac_limpia}"
        
        print(f"\nBuscando en la base de datos: {mac_limpia}...")
        
        try:
            # Hacemos la consulta web directa
            respuesta = urllib.request.urlopen(url)
            fabricante = respuesta.read().decode('utf-8')
            print(f"✅ Fabricante detectado: {fabricante}")
            
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print("❌ No se encontró ningún fabricante para esta MAC.")
            else:
                print(f"❌ Error de conexión. Código HTTP: {e.code}")
        except Exception as e:
            print(f"❌ Ocurrió un error inesperado: {e}")
            
        # Pausa para que leas el resultado antes de limpiar y volver al menú
        input("\nPresiona ENTER para continuar...")
        
    elif opcion == '2':
        print("\nSaliendo del sistema...")
        break
        
    else:
        print("\n[!] Opción inválida. Por favor, escribe 1 o 2.")