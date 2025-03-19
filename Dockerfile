FROM python:3.12-slim

WORKDIR /app
RUN apt-get update && apt-get install --no-install-recommends -y curl coreutils \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc | tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
    && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | tee /etc/apt/sources.list.d/ngrok.list \
    && apt update && apt install ngrok \
    && rm -rf /var/lib/apt/lists/*


# Copiar los archivos del proyecto al contenedor
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ARG AUTH_TOKEN_NGROK
RUN ngrok config add-authtoken $AUTH_TOKEN_NGROK

EXPOSE 8000
CMD ["sh", "-c", "ngrok http --url=relative-grackle-glorious.ngrok-free.app 8000 --log=stdout & uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]
