# 🚀 Plateforme Wiki.js Multi-sites & Webhook PayPal

![CI/CD](https://github.com/Hanane-Chaouche/wikijs-multisite/actions/workflows/deploy.yml/badge.svg)

Ce projet déploie une plateforme multi-instances de [Wiki.js](https://js.wiki/) avec Docker Compose.  
Chaque instance a sa propre base PostgreSQL et est accessible via un reverse proxy Nginx avec SSL.  
Le déploiement est automatisé avec **GitHub Actions**.  
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
├── instances/
│ ├── wiki1/
│ ├── wiki2/
│ └── wiki-public/
│
├── nginx/
│ ├── docker-compose.yml
│ ├── wikijs.conf
│ └── bouton/
│ └── paypal-button.html
│
├── paypal-webhook/
│ ├── docker-compose.yml
│ ├── requirements.txt
│ ├── webhook.py
│ └── paypal_log.txt
│
├── .github/
│ └── workflows/
│ └── deploy.yml
│
└── README.md
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
- VM Ubuntu (par exemple sur Azure)  
- Noms de domaines ou sous-domaines pointant vers la VM  
- Certificats SSL (Let's Encrypt recommandé)
- Clé SSH pour GitHub Actions  

---

## ▶️ Démarrage rapide


git clone https://github.com/Hanane-Chaouche/wikijs-multisite.git
cd wikijs-multisite

# Lancer les 3 instances de Wiki.js
docker compose -f instances/wiki1/docker-compose.yml up -d
docker compose -f instances/wiki2/docker-compose.yml up -d
docker compose -f instances/wiki-public/docker-compose.yml up -d

# Lancer le reverse proxy Nginx
cd nginx
docker compose up -d

# (Optionnel) Lancer le microservice webhook PayPal
cd ../paypal-webhook
docker compose up -d


# Lancer le reverse proxy Nginx
docker compose -f nginx/docker-compose.yml up -d

## 🌍 Accès à la plateforme et aux domaines

### 🔑 Accès SSH à la VM

Pour se connecter à la machine virtuelle Azure :

```bash
ssh -i sshkey.pem azureuser@4.206.99.81
```

Pour se connecter à la machine virtuelle Azure :


```
ssh -i sshkey.pem azureuser@4.206.99.81
```

sshkey.pem : ta clé privée (à garder secrète)

azureuser : utilisateur admin de la VM

##🌐 Accès aux différentes instances Wiki.js

Les sous-domaines suivants pointent tous vers la même VM (reverse proxy Nginx) :

    Wiki public général
    https://publique.wikijspublique.me/

    Wiki enseignant
    https://enseignant.wikijspublique.me/

    Wiki admin
    https://admin.wikijspublique.me/

    Remarque : Les domaines doivent être configurés chez ton fournisseur DNS pour pointer vers l’IP publique de la VM Azure.
    
##💸 Webhook & Paiement PayPal

   Un bouton PayPal personnalisé est accessible sur
 ```
    https://enseignant.wikijspublique.me/bouton/paypal-button.html
 ```

   Quand un paiement est validé, le frontend envoie un POST vers le webhook :
```
        https://enseignant.wikijspublique.me/paypal/webhook
```
   Le microservice Python/Flask reçoit et logue la transaction dans paypal_log.txt.
   ##💸 Module PayPal Webhook

   Dossier : paypal-webhook/

   Microservice Python/Flask qui reçoit les notifications PayPal sur /paypal/webhook

   Les paiements sont logués dans paypal_log.txt

##📦 Dépendances

   Docker

   Docker Compose

   Wiki.js

   GitHub Actions

##📘 Instances Wiki.js

| Instance    | Port interne | Description          |
| ----------- | ------------ | -------------------- |
| wiki1       | 3001         | Wiki privé du site 1 |
| wiki2       | 3002         | Wiki privé du site 2 |
| wiki-public | 3003         | Wiki public général  |


##🤖 Déploiement automatique

Chaque push sur la branche main déclenche un workflow GitHub Actions (.github/workflows/deploy.yml) qui :

   se connecte à la VM via SSH

   exécute git pull et redémarre les services Docker

   met à jour automatiquement Nginx et les wikis

👤 Auteur

Hanane Chaouche
Étudiante en développeuse en Mega données – Collège Bois-de-Boulogne
Projet réalisé dans un contexte DevOps avec CI/CD et documentation technique.

