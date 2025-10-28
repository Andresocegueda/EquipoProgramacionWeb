# 1. Imagen Base (Sistema Operativo y Python)
FROM python:3.10-slim
# 2. Directorio de Trabajo dentro del contenedor
WORKDIR /app
# 3. Copiar y Instalar dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt
# 4. Copiar el código de la aplicación Flask (incluyendo la carp
COPY . .

# 5. Puerto que la aplicación escucha internamente
EXPOSE 80

# 6. Comando para iniciar el servidor Flask
CMD [ "python", "app.py" ]