import requests
import json
from flask import Flask, render_template_string
from datetime import datetime, timedelta

def InicioSession ():

    url = "https://orchestrator.myrb.io/api/auth/signIn"

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "es-419,es;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "origin": "https://orchestrator.myrb.io",
        "referer": "https://orchestrator.myrb.io/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
    }

    cookies = {
        "auth.strategy": "local",
        "AWSALB": "tXNskBplfk2NWe7lt0uAozwu8rpVEhQKB/b3Mo4Q1F0raXycZx2kSuE2xb3C5wVFshbOe5EiqLflWKQqVtTipdDvjIGtljqgS4lV8S+xR7DWtlQzp783FhEbElqE",
        "AWSALBCORS": "tXNskBplfk2NWe7lt0uAozwu8rpVEhQKB/b3Mo4Q1F0raXycZx2kSuE2xb3C5wVFshbOe5EiqLflWKQqVtTipdDvjIGtljqgS4lV8S+xR7DWtlQzp783FhEbElqE",
        "auth._token.local": "false",
        "auth._token_expiration.local": "false",
        "auth.redirect": "%2F"
    }

    payload = {
        "email": "jmmarin@alico-sa.com",
        "password": "Aas1023625415"
    }

    response = requests.post(url, headers=headers, cookies=cookies, json=payload)
    respuesta = response.json()
    cookies = response.cookies.get_dict()

    # Accedemos a cookies específicas
    aws_alb = cookies.get("AWSALB")
    aws_alb_cors = cookies.get("AWSALBCORS")
    token_expiration = cookies.get("auth._token_expiration.local")

    return {
        "token": respuesta,
        "AWSALB": aws_alb,
        "AWSALBCORS": aws_alb_cors,
        "token_expiration": token_expiration
    }

def extractor(cadena_str):
    import json
    import requests
    from datetime import datetime
    
    # convierte string → dict
    data = json.loads(cadena_str)  
    
    fecha_hoy = datetime.today().strftime("%Y-%m-%d")
    fecha_ayer = (datetime.now() - timedelta(days=1)).strftime('%m/%d/%Y') 

    # Nueva URL
    url = "https://orchestrator.myrb.io/api/robots/execution"

    # Body dinámico con fecha actual
    body = {
        "started": fecha_ayer,
        "ended": fecha_hoy
    }

    headers = {
        "accept": "application/json",
        "accept-language": "es-419,es;q=0.9,en;q=0.8",
        "authorization": f"Bearer {data['token']['data']}",
        "content-type": "application/json",
        "origin": "https://orchestrator.myrb.io",
        "referer": "https://orchestrator.myrb.io/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    }

    cookies = {
        "auth.strategy": "local",
        "auth.redirect": "%2F",
        "auth._token.local": f"Bearer%20{data['token']['data']}",
        "auth._token_expiration.local": f"{data['token_expiration']}",
        "AWSALB": f"{data['AWSALB']}",
        "AWSALBCORS": f"{data['AWSALBCORS']}",
    }

    # POST con body JSON
    response = requests.post(url, headers=headers, cookies=cookies, json=body)

    return response.json()


#def enviar_correo():
    url = "https://centralusdtapp73.epicorsaas.com/SaaS5333/api/v2/efx/ALICO/JGRCCHATBOT/email2"
    headers = {
        "x-api-key": "vMGRf6ryrOBOttpzlyBi60qviKImvIMW6Dnsb5GeJewpn",
        "Authorization": "Basic ZXh0ZXJuYWxfYXBpOjEwMjRtYi0xVA==",
        "Content-Type": "application/json"
    }
    payload = {
        "subjetc": "Conexcion caida",
        "body": "Se callo la conexion de rocketbot",
        "emails": "jmmarin@alico-sa.com, eroldan@alico-sa.com, jsalazar@alico-sa.com",
        "emisor": "jmmarin@alico-sa.com"
    }

    response = requests.post(url, headers=headers, json=payload)
    print("Correo enviado:", response.status_code, response.text)

def extractor1(cadena_str):
    import json
    import requests

    # convierte string → dict
    data = json.loads(cadena_str)

    # Nueva URL (de tu curl)
    url = "https://orchestrator.myrb.io/api/insight/66ba07a25e777"

    headers = {
        "accept": "*/*",
        "accept-language": "es-419,es;q=0.9,en;q=0.8",
        "authorization": f"Bearer {data['token']['data']}",  # token dinámico
        "content-length": "0",
        "origin": "https://orchestrator.myrb.io",
        "priority": "u=1, i",
        "referer": "https://orchestrator.myrb.io/",
        "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    }

    cookies = {
        "auth.strategy": "local",
        "auth.redirect": "%2Finsight%2Fcalendar",
        "auth._token.local": f"Bearer%20{data['token']['data']}",
        "auth._token_expiration.local": f"{data['token_expiration']}",
        "AWSALB": f"{data['AWSALB']}",
        "AWSALBCORS": f"{data['AWSALBCORS']}",
    }

    # POST sin body (igual que curl: content-length=0)
    response = requests.post(url, headers=headers, cookies=cookies)
    print(response)
    return response.json()


Token = InicioSession()
response = extractor1(json.dumps(Token))
print(response)
#Token = InicioSession()

#hola = extractor(json.dumps(Token))  

#print(hola)

app = Flask(__name__)

@app.route("/")

def home():
    Token = InicioSession()

    # 👉 Llamar extractor1 y mostrarlo en consola
    respuesta1 = extractor1(json.dumps(Token))
    print("📌 Respuesta extractor1:", respuesta1)

    hola = extractor(json.dumps(Token))  

    # Horarios programados
    horarios_ejecucion = {
        "EnvioCartaBienvenida": ["06:55:00"],
        "Dian": ["01:00:00"],
        "Focuss": ["05:30:00", "09:00:00", "13:35:00", "22:50:00"],
        "Sugerecias MRO": ["05:55:00"],
        "Tasa de Cambio": ["06:30:00"],
        "Completado Trabajos": ["07:00:00"],
        "Terminacion Corte": ["07:10:00"],
        "GenerarTrabajosStockPrincipal": ["10:30:00"],
        "Costos": ["10:00:00", "15:00:00", "19:00:00"],
        "Procesado XML": ["17:00:00"],
        "Envio Orden Compra": ["19:30:00"],
        "Notas Credito": ["18:00:00"],
    }

    # Tiempos fijos de procesos
    tiempos_fijos = {
        "Focuss": "00:01:30",
        "Dian": "00:07:30",
        "Sugerecias MRO": "00:00:08",
        "Costos": "00:02:45",
        "Tasa de Cambio": "00:03:00",
        "Terminacion Corte": "00:02:00",
        "GenerarTrabajosStockPrincipal": "00:02:00",
        "EnvioCartaBienvenida": "00:01:30",
        "Completado Trabajos": "00:02:30",
        "Procesado XML": "00:30:00",
        "Envio Orden Compra": "00:07:00",
        "Notas Credito": "00:01:30",
    }

    margen = timedelta(minutes=1)  # tolerancia de 1 minuto
    fecha_actual = datetime.now()
    fechas_a_revisar = [fecha_actual.date(), (fecha_actual - timedelta(days=1)).date()]  # HOY y AYER

    # Guardar ejecuciones reales por proceso
    ejecuciones_dict = {}
    for item in hola['data']:
        hora_real = datetime.fromisoformat(item['start'].replace("Z", ""))
        ejecuciones_dict.setdefault(item['process'], []).append({
            "hora": hora_real,
            "duration": item.get("duration", "-"),
            "robot": item.get("robot", "-")
        })

    # Generar lista final con todos los horarios programados
    resultados = []
    for proceso, horarios in horarios_ejecucion.items():
        for fecha in fechas_a_revisar:
            for hora in horarios:
                hora_programada = datetime.strptime(
                    f"{fecha} {hora}", "%Y-%m-%d %H:%M:%S"
                )

                estado = "❌ No se ejecutó"
                start = hora_programada.strftime("%Y-%m-%d %H:%M:%S")
                duration = "-"
                robot = "-"

                # Revisar ejecuciones reales del proceso
                for ejec in ejecuciones_dict.get(proceso, []):
                    if hora_programada <= ejec["hora"] <= hora_programada + margen:
                        estado = "✅ Ejecutado"
                        start = ejec["hora"].strftime("%Y-%m-%d %H:%M:%S")
                        duration = ejec["duration"]
                        robot = ejec["robot"]
                        break

                # Si aún no llega la hora → "todavía no se ejecuta"
                if fecha == fecha_actual.date() and fecha_actual < hora_programada:
                    estado = "⏳ Todavía no se ejecuta"

                resultados.append({
                    "process": proceso,
                    "robot": robot,
                    "estado": estado,
                    "start": start,
                    "duration": duration,
                    "tiempo_fijo": tiempos_fijos.get(proceso, "")
                })

    # Ordenar por hora programada
    resultados.sort(key=lambda x: datetime.strptime(x['start'], "%Y-%m-%d %H:%M:%S"))

    # HTML
    html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Ejecuciones de Robots</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f8f9fa; margin: 0; padding: 0; }
            .header { background-color: #c00; color: white; text-align: center; padding: 20px; font-size: 24px; font-weight: bold; }
            .table-container { margin: 30px auto; width: 80%; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
            table { width: 100%; border-collapse: collapse; margin-top: 10px; }
            th, td { padding: 12px; text-align: center; }
            th { background-color: #f2f2f2; color: #333; }
            tr:nth-child(even) { background-color: #f9f9f9; }
            tr:hover { background-color: #f1f1f1; }
            td { border-bottom: 1px solid #ddd; }
        </style>
    </head>
    <body>
        <div class="header">📊 Ejecuciones de Robots</div>
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>Proceso</th>
                        <th>Robot</th>
                        <th>Estado</th>
                        <th>Horario / Ejecución</th>
                        <th>Duración</th>
                        <th>Tiempo Fijo</th>
                    </tr>
                </thead>
                <tbody>
                    {% for item in data %}
                    <tr>
                        <td>{{ item.process }}</td>
                        <td>{{ item.robot }}</td>
                        <td>{{ item.estado }}</td>
                        <td>{{ item.start }}</td>
                        <td>{{ item.duration }}</td>
                        <td>{{ item.tiempo_fijo }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """

    return render_template_string(html_template, data=resultados)





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7888, debug=False)


