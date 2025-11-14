# Imagem base
FROM python:3.11-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app

# Cria e define o diretório de trabalho
WORKDIR $APP_HOME

# Copia os arquivos de dependência e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY app $APP_HOME/app

# Comando para rodar a aplicação
# uvicorn app.main:app --host 0.0.0.0 --port 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
