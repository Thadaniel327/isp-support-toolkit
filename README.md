# isp-support-toolkit
# 🔍 Identificador de Fabricantes por MAC (OUI Lookup)

Un script interactivo en Python diseñado para agilizar las tareas de diagnóstico en redes y soporte técnico de Nivel 1. Permite identificar rápidamente la marca o fabricante de cualquier equipo (CPEs, routers de clientes, dispositivos desconocidos) conectado a la red, consultando su identificador único (OUI).

## 🚀 Características

* **Consulta en Tiempo Real:** Se conecta directamente a la API pública de MacVendors para obtener datos actualizados.
* **Limpieza de Formato:** El usuario puede ingresar la dirección MAC con guiones, dos puntos o espacios; el script formatea la entrada automáticamente para evitar errores de consulta.
* **Menú Interactivo:** Utiliza un bucle infinito que permite realizar múltiples consultas seguidas sin necesidad de reiniciar el programa, ahorrando tiempo durante el *troubleshooting*.
* **Versión Portátil (.exe):** Diseñado para ser compilado en un ejecutable independiente, permitiendo su uso en cualquier equipo con Windows sin requerir la instalación de Python.

## 🛠️ Requisitos

Si deseas ejecutar el código fuente directamente, solo necesitas:
* Python 3.x
* Conexión a internet (para la consulta a la API).
* *Nota: Este script utiliza únicamente librerías nativas de Python (`urllib`, `os`), por lo que no requiere instalaciones adicionales vía `pip`.*
Tambien puedes ir a mi seccion "Releases" para descargar el archivo .EXE del programa sin necesidad de instalar python o cualquier otra libreria.

## 🌐 Casos de Uso Comunes
Detección de intrusos: Identificar dispositivos no autorizados conectados a la red Wi-Fi o cableada.

Soporte ISP: Verificar si la MAC registrada en el sistema de gestión (Radius/MikroTik) corresponde efectivamente a la marca del CPE o router instalado en la casa del cliente.

Auditoría de Redes: Clasificar los dispositivos descubiertos en un escaneo ARP.

## 💻 Uso

1. Ejecuta el archivo `Identificador_Equipo_programa.py` (o el `.exe` si ya lo compilaste).
2. Selecciona la opción **1** en el menú principal.
3. Ingresa la dirección MAC del dispositivo sospechoso o a identificar (ej. `00:1A:2B:3C:4D:5E`).
4. El sistema devolverá inmediatamente el nombre del fabricante.

🤝 Feedback y Contribuciones
Este script nació de la necesidad de crear algo verdaderamente útil y funcional para el día a día. Está pensado tanto para verificar equipos en redes domésticas como para agilizar los diagnósticos en el soporte técnico de proveedores de internet (ISPs).

Sé que la teoría a veces choca con la práctica, así que si al usar esta herramienta en un entorno real notas detalles que no "acoplan" del todo bien, encuentras errores o tienes ideas para que funcione mejor, ¡estoy totalmente abierto a escucharlas!

¿Cómo puedes aportar?

Ve a la pestaña de [Issues] aquí en GitHub y cuéntame qué se puede mejorar o qué falló.
Si sabes cómo optimizar el código, siéntete libre de hacer un Fork y enviarme un Pull Request.
📬 Contacto: Si quieres charlar sobre redes, Python o darme feedback directo, puedes escribirme a: jdanielpintotrabajo@gmail.com


### Ejemplo de salida en consola del programa:

```text
===================================
   IDENTIFICADOR DE FABRICANTE MAC   
===================================
1. Consultar una dirección MAC
2. Salir del sistema

Elige una opción (1 o 2): 1
Ingresa la MAC (ej. 00:1A:2B:3C:4D:5E): 00:1A:2B:3C:4D:5E

Buscando en la base de datos: 00:1A:2B:3C:4D:5E...
✅ Fabricante detectado: Apple, Inc.

Presiona ENTER para continuar...
