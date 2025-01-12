FROM postgres:latest

# Copiando o script de inicialização para o diretório do entrypoint
COPY ./src/db/tables.py /docker-entrypoint-initdb.d/tables.py

# Copiando outros arquivos necessários para o contêiner (opcional)
COPY ./src/db /app/
