# Utiliser une image officielle de Python
FROM python:3.11-slim

# Définir le dossier de travail
WORKDIR /app

# Copier les fichiers dans l'image Docker
COPY . .

# Installer les dépendances
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Exposer le port Flask
EXPOSE 5000

# Définir la commande de lancement de l'app Flask
CMD ["python", "api/app.py"]
