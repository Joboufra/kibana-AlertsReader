from datetime import datetime
import json

def logFilter(logs):
    logsFiltrados = []
    for log in logs:
        log_dict = json.loads(log.strip())
        message = log_dict.get('message', '')
        if "Server log: [ALERTA]" in message:
            logsFiltrados.append(log)
    return logsFiltrados

def kibanaAlerts(urlLog):
    kibanaAlerts = []
    with open(urlLog, "r") as f:
        logs = f.readlines()

    logsFiltrados = logFilter(logs)

    for log in logsFiltrados:
        log_dict = json.loads(log.strip())
        raw_timestamp = log_dict.get('@timestamp', '')

        dt_object = datetime.fromisoformat(raw_timestamp.replace("Z", "+00:00"))
        timestamp = dt_object.strftime('%Y-%m-%d %H:%M:%S')

        splitsMessage = log_dict.get('message', '').split(';')

        tipoAlerta = splitsMessage[0]
        detallesAlerta = splitsMessage[1]
        hostname = splitsMessage[2]
        metric = splitsMessage[-1]

        mensaje = f"{tipoAlerta};{detallesAlerta} en {hostname}. Valor: {metric}"
        kibanaAlerts.append((timestamp, mensaje))
        
    return kibanaAlerts
