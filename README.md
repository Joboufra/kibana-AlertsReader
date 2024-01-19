---
runme:
  id: 01HMHDT9NHMY1PW5CWNBPFKNFF
  version: v2.2
---

# Kibana Alerts Reader

## Descripción
Este proyecto se basa en Python para leer y procesar archivos de log de Kibana. 

Se ha creado para un caso de uso concreto. En ese caso, analizamos el log de Kibana para encontrar las líneas que coincidan con el patrón ``[ALERTA];{{alertName}};{{context.group}};{{context.threshold}};{{context.metric}};{{context.value}};{{tags}};{{context.reason}}``.
Dicho patrón ha sido previamente indicado en la configuración de alertas de Kibana a través del apartado ``Actions`` dentro de la sección de ``Rules``(Kibana 8.x) o ``Rules and Connectors``(Kibana 7.x), indicando como connector type "Server Log".  

Con ese connector, se escribe una línea de log con level INFO en el log de Kibana siguiendo el patrón indicado. Ese patrón es válido para Kibana 7.x como 8.x y no hay necesidad de tener suscripciones habilitadas para la escritura y lectura del propio log de Kibana.

## Características
- Filtrado de logs de Kibana basado en el formato de alertas especificado.
- Presentación de datos en formato tabular en la consola.
- Opción para exportar los datos filtrados a un archivo Excel.

## Requisitos
- Python 3.x
- Pandas
- openpyxl (para la exportación a Excel)

## Instalación
Clonar el repositorio:
> git clone https://github.com/Joboufra/kibana-AlertsReader.git

Instalar dependencias:
> pip install pandas openpyxl

## Uso
Ejecutar el script `main.py` y seguir las instrucciones en pantalla. Se pedirá que indiques la ruta del archivo de log a procesar. 
Después de procesar los logs, tendrá la opción de exportar los resultados a un archivo Excel.

> py main.py