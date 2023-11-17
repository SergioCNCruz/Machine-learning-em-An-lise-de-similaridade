# Etapa 1: Escolha da imagem base
FROM python:3.8-slim

# Definir variável de ambiente para evitar a escrita de arquivos .pyc no contêiner
ENV PYTHONDONTWRITEBYTECODE 1
# Definir variável de ambiente para evitar o buffer da saída do Python
ENV PYTHONUNBUFFERED 1

# Definir o diretório de trabalho no contêiner
WORKDIR /code

# Instalar dependências do sistema operacional
RUN apt-get update \
    && apt-get -y install libgl1-mesa-glx \
    && apt-get clean

# Copiar o arquivo requirements.txt para o contêiner
COPY requirements.txt /code/

# Instalar as dependências do Python
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copiar o conteúdo do diretório local para o contêiner
COPY . /code/

# Comando para executar o aplicativo usando Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
