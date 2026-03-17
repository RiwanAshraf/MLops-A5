FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

# Create environment (conda automatically accepts necessary channels)
RUN conda env create -f environment.yml

# Make sure the environment is activated
SHELL ["conda", "run", "-n", "env_rl_project", "/bin/bash", "-c"]

# Copy your code last for efficient caching
COPY . .

CMD ["python", "Build_my_first_GAN.py"]