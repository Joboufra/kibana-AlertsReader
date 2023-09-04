import kibanaLogParser
import Utils.banner

if __name__ == "__main__":
    Utils.banner.printStartApp() #Encabezado
    urlLog = "Z:\Repos\KibanaLogParser\kibana.log"
    logProcesado = kibanaLogParser.kibanaAlerts(urlLog)
    for timestamp, mensaje in logProcesado:
        print(f"{timestamp} | {mensaje}")