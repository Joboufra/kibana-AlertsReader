from datetime import datetime
import json
import re

def logFilter(logs):
    logsFiltrados = []
    for log in logs:
        log_dict = json.loads(log.strip())
        message = log_dict.get('message', '')
        if "Server log: [ALERTA]" in message:
            logsFiltrados.append(log)
    return logsFiltrados

def kibanaAlertsReader(urlLog):
    alertsData = []
    regex = r"Server log: \[ALERTA\];(.*?);(.*?);(.*)"

    with open(urlLog, "r") as f:
        logs = f.readlines()

    logsFiltrados = logFilter(logs)

    for log in logsFiltrados:
        log_dict = json.loads(log.strip())
        mensaje = log_dict.get('message', '')

        regex_inicial = re.search(regex, mensaje)
        if regex_inicial:
            nombre, equipo, mensaje_final = regex_inicial.groups()
            #Dividir el mensaje final en valor y umbral
            partes = mensaje_final.split(" Alert when ")
            if len(partes) >= 2:
                #El valor es la última parte del mensaje antes de "Alert when"
                valor = partes[0].rsplit(';', 1)[-1]
                #El umbral es lo que sigue después de "Alert when"
                umbral = partes[1].rstrip('.,;')

                alertData = {
                    "Alerta generada": nombre,
                    "Hostname": equipo,
                    "Valor": valor.strip(),
                    "Umbral configurado": umbral.strip()
                }
                alertsData.append(alertData)

    return alertsData