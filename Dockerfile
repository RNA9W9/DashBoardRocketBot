# Imagen base de Python
FROM python:3.11-slim

# Configurar directorio de trabajo
WORKDIR /app

# Copiar requirements.txt primero (mejor práctica para cache de Docker)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Crear usuario no-root para seguridad
RUN useradd --create-home --shell /bin/bash appuser && chown -R appuser:appuser /app
USER appuser

# Exponer el puerto correcto
EXPOSE 7888

# Variables de entorno
ENV FLASK_APP=login.py
ENV FLASK_ENV=production

# Ejecutar Flask
CMD ["python", "login.py"]
