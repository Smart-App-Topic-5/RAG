# Utilizzare un'immagine base di Python
FROM python:3.9-slim

# Impostare la directory di lavoro
WORKDIR /app

# Copiare i file del progetto nella directory di lavoro
COPY . .

# Installare le dipendenze di sistema richieste
RUN apt-get update && apt-get install -y \
    build-essential \
    libopenblas-dev \
    libomp-dev \
    libfreetype6-dev \
    libxft-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Installare le dipendenze Python
RUN pip install --no-cache-dir --default-timeout=10000 \
    numpy \
    pandas \
    matplotlib \
    torch \
    transformers \
    langchain \
    langchain-core \
    langchain-openai \
    langchain-community \
    faiss-cpu \
    flask \
    requests \
    tabulate \
    networkx \
    huggingface_hub \
    openai \
    fpdf \
    sentence-transformers

# Specificare il comando di avvio
CMD ["python", "Milestone2/Milestone2.py"]
