import requests
import json
from flask import Flask, render_template_string

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

    # Nueva URL
    url = "https://orchestrator.myrb.io/api/robots/execution"

    # Body dinámico con fecha actual
    body = {
        "started": fecha_hoy,
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



#Token = InicioSession()

#hola = extractor(json.dumps(Token))  

#print(hola)


app = Flask(__name__)

@app.route("/")
def home():
    Token = InicioSession()

    hola = extractor(json.dumps(Token))  
    html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Ejecuciones de Robots</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                margin: 0;
                padding: 0;
            }
            .header {
                background-color: #c00;
                color: white;
                text-align: center;
                padding: 20px;
                font-size: 24px;
                font-weight: bold;
            }
            .table-container {
                margin: 30px auto;
                width: 80%;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
            }
            th, td {
                padding: 12px;
                text-align: center;
            }
            th {
                background-color: #f2f2f2;
                color: #333;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            tr:hover {
                background-color: #f1f1f1;
            }
            td {
                border-bottom: 1px solid #ddd;
            }
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
                        <th>Duración</th>
                    </tr>
                </thead>
                <tbody>
                    {% for item in data %}
                    <tr>
                        <td>{{ item.process }}</td>
                        <td>{{ item.robot }}</td>
                        <td>{{ item.duration }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """

    return render_template_string(html_template, data=hola['data'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7888, debug=False)


