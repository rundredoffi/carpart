# Carpart APIs

Ce projet contient deux APIs pour la gestion des pièces automobiles et des clients, orchestrées avec Docker Compose.
## Author
Nicolas JOUIN--DERRIEN
## Architecture

- **API Stock (carpart-api)** : Gestion des produits et stocks avec MongoDB
- **API Client (carpart-client-api)** : Gestion des clients avec MySQL
- **Réseau Docker** : carpart-network

## Prérequis

- Docker
- Docker Compose

## Configuration

### Variables d'environnement
Copiez le fichier `.env.example` vers `.env` et modifiez les valeurs selon vos besoins :

```bash
cp .env.example .env
```

### CI/CD GitHub Actions
Ce projet utilise GitHub Actions pour l'intégration continue. Voir les fichiers :
- `.github/workflows/ci-cd.yml` - Pipeline principal
- `GITLAB-CI-README.md` - Documentation complète
- `GITHUB-SECRETS-SETUP.md` - Configuration des secrets

## Lancement

```bash
docker-compose up -d
```

## URLs d'accès

### API Stock
- **URL principale** : http://localhost:8001
- **Documentation Swagger** : http://localhost:8001/docs
- **OpenAPI JSON** : http://localhost:8001/openapi.json

### API Client
- **URL principale** : http://localhost:8002
- **Documentation Swagger** : http://localhost:8002/docs
- **OpenAPI JSON** : http://localhost:8002/openapi.json

### Bases de données
- **MongoDB Stock** : localhost:27017
- **MySQL Client** : localhost:3307 (root/password)

## Endpoints principaux

### API Stock (:8001) - MongoDB
- `GET /` - Status de l'API
- `GET /products` - Liste tous les produits
- `POST /products/` - Créer un produit
- `GET /products/{id}` - Détails d'un produit
- `PUT /products/{id}` - Modifier un produit
- `DELETE /products/{id}` - Supprimer un produit

### API Client (:8002) - MySQL
- `GET /` - Status de l'API
- `GET /clients` - Liste tous les clients
- `POST /clients/` - Créer un client
- `GET /clients/{id}` - Détails d'un client
- `PUT /clients/{id}` - Modifier un client
- `DELETE /clients/{id}` - Supprimer un client

## Commandes utiles

```bash
# Démarrer les services
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter les services
docker-compose down

# Voir le statut
docker-compose ps

# Reconstruire les images
docker-compose build --no-cache
```

## Technologies

### API Stock
- **Backend** : FastAPI, Motor (MongoDB async driver)
- **Base de données** : MongoDB 6.0

### API Client
- **Backend** : FastAPI, SQLAlchemy, PyMySQL
- **Base de données** : MySQL 8.0

### Infrastructure
- **Conteneurisation** : Docker, Docker Compose
- **Réseau** : Bridge network Docker