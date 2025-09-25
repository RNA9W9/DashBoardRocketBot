# Imagen base de Python
FROM python:3.11-slim

# Configurar directorio de trabajo
WORKDIR /app

# Copiar tu aplicación
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir flask

# Exponer el puerto que uses (ej: 5000 o 8080)
EXPOSE 8000

# Ejecutar Flask
CMD ["python", "login.py"]
