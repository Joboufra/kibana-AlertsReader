from tabulate import tabulate
import alerts_reader
import Utils.banner
import pandas as pd
import os

def guardar_excel(df):
    os.makedirs('results', exist_ok=True)
    urlguardar = "results/Kibana-AlertsReader.xlsx"
    df.to_excel(urlguardar, index=True)
    print(f"Datos guardados en '{urlguardar}'.")

if __name__ == "__main__":
    Utils.banner.printStartApp()

    #Mostrar el DataFrame completo
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    urlLog = input("Por favor, indica la URL del archivo de log de Kibana a analizar: ")
    try:
        logData = alerts_reader.kibanaAlertsReader(urlLog)
        if logData:
            df = pd.DataFrame(logData)
            print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
            
            #Preguntar al usuario si desea guardar los datos para Excel
            respuesta = input("¿Deseas descargar los datos a un archivo Excel (.xlsx) ? (s/n): ").lower()
            if respuesta == 's' or respuesta == 'si':
                guardar_excel(df)
        else:
            print("No se encontraron mensajes que coincidan con el patrón en los logs.")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo en la ubicación especificada: {urlLog}")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")
