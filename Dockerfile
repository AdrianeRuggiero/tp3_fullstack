FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . .

# Installe Chromium pour les tests Selenium headless
RUN apt-get update && apt-get install -y chromium chromium-driver \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Exposer le port utilisé par Flask
EXPOSE 5000

# Lancer l'application Flask
CMD ["python", "api/app.py"]
