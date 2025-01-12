FROM python:3.11

# Instalando dependências necessárias
RUN pip install --upgrade pip
RUN pip install sqlalchemy psycopg2 python-dotenv

# Copiando o código do projeto para o contêiner
COPY ./src/db /app/

# Definindo o diretório de trabalho
WORKDIR /app

# Rodando o script Python
CMD ["python3", "tables.py"]
