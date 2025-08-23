FROM python:3.12-slim

RUN apt-get update && apt-get install -y git curl bash && rm -rf /var/lib/apt/lists/*

COPY --from=jdxcode/mise /usr/local/bin/mise /usr/local/bin/

RUN echo 'eval "$(mise activate bash)"' >> /root/.bashrc 

WORKDIR /app

COPY . /app
