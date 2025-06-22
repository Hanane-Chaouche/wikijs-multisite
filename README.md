# 🚀 Plateforme Wiki.js Multi-sites & Webhook PayPal

## CI/CD

Ce projet déploie une plateforme multi-instances de Wiki.js avec Docker Compose.  
Chaque instance a sa propre base PostgreSQL et est accessible via un reverse proxy Nginx avec SSL.  
Le déploiement est automatisé avec GitHub Actions.  
Un module Python/Flask permet de recevoir les notifications PayPal (webhooks).

---

## 📑 Sommaire

- [📁 Structure du projet](#structure-du-projet)
- [🚀 Objectif](#objectif)
- [🛠️ Prérequis](#prérequis)
- [▶️ Démarrage rapide](#démarrage-rapide)
- [🌍 Accès à la plateforme et aux domaines](#accès-à-la-plateforme-et-aux-domaines)
- [📦 Dépendances](#dépendances)
- [📘 Instances Wiki.js](#instances-wikijs)
- [💸 Module PayPal Webhook](#module-paypal-webhook)
- [🤖 Déploiement automatique](#déploiement-automatique)
- [👤 Auteur](#auteur)

---

## 📁 Structure du projet
```

wikijs-multisite/
│
├── instances/ # <– Contient les instances Wiki.js
│ ├── wiki1/
│ ├── wiki2/
│ └── wiki-public/
│
├── nginx/ # <– Config reverse proxy Nginx
│ ├── docker-compose.yml
│ ├── wikijs.conf
│ └── bouton/
│ └── paypal-button.html # <– Page HTML pour bouton PayPal
│
├── paypal-webhook/ # <– Microservice Python/Flask pour webhooks
│ ├── docker-compose.yml
│ ├── requirements.txt
│ ├── webhook.py
│ └── paypal_log.txt
│
├── .github/ # <– CI/CD automatisé via GitHub Actions
│ └── workflows/
│ └── deploy.yml
│
└── README.md # <– Ce fichier
```

---

## 🚀 Objectif

- Déployer plusieurs instances Wiki.js isolées via Docker Compose
- Gérer les accès multi-domaines avec Nginx (reverse proxy SSL)
- Automatiser le déploiement/mise à jour via GitHub Actions
- Recevoir et enregistrer les notifications PayPal via un microservice Python/Flask

---

## 🛠️ Prérequis

- Docker & Docker Compose  
- VM Ubuntu (ex: Azure)  
- Noms de domaines pointant vers la VM  
- Certificats SSL (Let's Encrypt recommandé)  
- Clé SSH pour GitHub Actions  

---

## ▶️ Démarrage rapide

```bash
git clone https://github.com/Hanane-Chaouche/wikijs-multisite.git
cd wikijs-multisite
````

# Lancer les instances Wiki.js
```
docker compose -f instances/wiki1/docker-compose.yml up -d
docker compose -f instances/wiki2/docker-compose.yml up -d
docker compose -f instances/wiki-public/docker-compose.yml up -d
```

# Lancer le reverse proxy Nginx
```
cd nginx
docker compose up -d
```

# (Optionnel) Lancer le microservice webhook PayPal
```
cd ../paypal-webhook
docker compose up -d
```

##🌍 Accès à la plateforme et aux domaines
🔑 Accès SSH à la VM

```
ssh -i sshkey.pem azureuser@4.206.99.81
```

Remplace sshkey.pem par ta clé privée.

##🌐 Accès Wiki.js par domaines
```
    https://publique.wikijspublique.me → wiki-public
```
````
    https://enseignant.wikijspublique.me → wiki2
````
    https://admin.wikijspublique.me → wiki1
````
````
Les DNS doivent pointer vers l’IP publique de la VM Azure (4.206.99.81).
Assure-toi que les DNS pointent vers l’IP publique de ta VM Azure.
---

## 💸 Webhook & Paiement PayPal

Le bouton PayPal :
🔗 Bouton PayPal personnalisé
Webhook de réception après paiement validé :

POST https://enseignant.wikijspublique.me/paypal/webhook
Les transactions sont enregistrées dans paypal_log.txt.
---
## 📦 Dépendances

- Docker
- Docker Compose
- Wiki.js
- GitHub Actions

📘 Instances Wiki.js

| Instance    | Port Interne | Description          |
| ----------- | ------------ | -------------------- |
| wiki1       | 3001         | Wiki privé du site 1 |
| wiki2       | 3002         | Wiki privé du site 2 |
| wiki-public | 3003         | Wiki public général  |
---

## 🤖 Déploiement automatique

Chaque push sur la branche main déclenche un workflow GitHub Actions :
- Se connecte à la VM via SSH
- Exécute git pull et redémarre les services Docker
- Met à jour automatiquement Nginx et les wikis
---
👤 Auteur
Hanane Chaouche
Étudiante en développement Mega données – Collège Bois-de-Boulogne
Projet réalisé dans un contexte DevOps avec CI/CD et documentation technique.
