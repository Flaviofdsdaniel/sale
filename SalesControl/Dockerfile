#Cria uma imagem Python 3.8.
FROM python:3.8-alpine
#Define o diretório de trabalho como /code
WORKDIR /code
#Define variáveis de ambiente usadas pelo comando flask
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
#Instala o gcc para que pacotes Python, como
#MarkupSafe e SQLAlchemy, possam compilar mais rápido
RUN apk add --no-cache gcc musl-dev linux-headers
#Copia o requirements.txt para dentro do contêiner
#COPY <src> <dest>
COPY requirements.txt requirements.txt
#Instala as dependências do Python
RUN pip install -r requirements.txt
#Copia o diretório atual . no projeto, para a workdir . na imagem
COPY . .
#Define o comando padrão para o contêiner executar.
CMD ["flask", "run"]
