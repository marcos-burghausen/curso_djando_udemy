# Use uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Instala as dependências do sistema
RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get clean

# Copia os arquivos de requisitos e instala as dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto
COPY app /app/

# Executa o comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["python", "manage.py", "runserver"]
