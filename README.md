# SafeTransfer - Système de virements et prélèvements interbancaires sécurisés

Ilyess Batal<br>
Cyril Rameaux<br>
Julien Rameaux<br>
Arvinde Senguttuvan

## Sommaire

- [Objectif du projet](#1-objectif-du-projet)
- [Structure du projet](#2-structure-du-projet)
- [Lancer le projet en local](#3-lancer-le-projet-en-local)
- [Lancer le projet avec Docker](#4-lancer-le-projet-avec-docker)

## 1. Objectif du projet

SafeTransfer est un système complet simulant des **virements** et **prélèvements** interbancaires, avec des garanties de
**sécurité renforcée** via une **double authentification** pour l’émetteur et le bénéficiaire. Il intègre :

- Un module bancaire (gestion des utilisateurs, comptes, transactions)
- Un module interbancaire (validation inter-système, génération de codes, détection de fraude)
- Un système de détection **automatisée de fraudes par IA**
- Une interface **front-end Streamlit** pour visualiser et interagir avec l’ensemble du système

L’objectif est de simuler un processus bancaire **réaliste et sécurisé**, basé sur des APIs REST avec coordination
multi-services.

## 2. Structure du projet

```
safe-transfer/
├── bank_server/             # Backend pour la banque (comptes, transactions locales)
├── safe_transfer_server/    # Backend pour SafeTransfer (validation, IA, interbancaire)
├── web_app/                 # Interface front-end (Streamlit)
├── docker-compose.yml       # Lancement global des services
└── README.md
```

## 3. Lancer le projet en local

### 3.1. Créer un environnement virtuel

```bash
python -m venv .venv
```

```bash
source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows
```

### 3.2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3.3. ...

### 3.4. Lancer les serveurs

- Lancer le backend banque : Exécuter le fichier `safe-transfer-Groupe1/bank_server/main/webapi/main.py`
- Lancer le backend SafeTransfer : Exécuter le fichier `safe-transfer-Groupe1/safe-transfer_server/main/webapi/main.py`
- Lancer l'interface Streamlit : Ouvrir un terminal et entrer la commande suivante :

```bash
streamlit run web_app/Home.py
```

L'interface est accessible sur : http://localhost:8501

## 4. Lancer le projet avec Docker

- Il faut que l'application "Docker Desktop" soit ouverte
- Dans le terminal entrer la commande suivante :

```bash
docker-compose up --build
```

Cela lancera automatiquement :

- Les serveurs banque et SafeTransfer
- Les bases de données PostgreSQL associées
- L’interface Streamlit

L'interface est accessible sur : : http://localhost:8501


