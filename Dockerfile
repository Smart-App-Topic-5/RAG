# Use Python as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker caching
COPY Milestone3/Requirements.txt .

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \          
    libopenblas-dev \           
    libomp-dev \                
    libfreetype6-dev \          
    libxft-dev \                
    libjpeg-dev \               
    zlib1g-dev \                
    curl \                      
    && rm -rf /var/lib/apt/lists/*  

# Install Python dependencies using the requirements file
RUN pip install --no-cache-dir -r Requirements.txt
# Use --no-cache-dir to prevent pip from caching dependencies and keep the image lightweight.

# Copy the rest of the project files into the working directory
COPY . .

# Add a healthcheck to ensure the container can communicate with the Ollama service
HEALTHCHECK --interval=30s CMD curl -f http://localhost:11434/v1 || exit 1
# Performs a health check every 30 seconds; fails if the Ollama API endpoint is unreachable.

# Specify the default command to run the Python script
CMD ["python", "Milestone3/generation.py"]
