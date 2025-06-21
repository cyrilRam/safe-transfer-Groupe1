# SafeTransfer - Système de virements et prélèvements interbancaires sécurisés

Ilyess Batal<br>
Cyril Rameaux<br>
Julien Rameaux<br>
Arvinde Senguttuvan

## Sommaire

- [Objectif du projet](#1-objectif-du-projet)
- [Structure du projet](#2-structure-du-projet)
- [Initialiser le projet](#3-initialiser-le-projet)
- [Lancer le projet](#4-lancer-le-projet)
- [Ressources](#5-ressources)

## 1. Objectif du projet

Le projet est un système complet simulant des **virements** et **prélèvements** interbancaires.
Il contient une partie SafeTransfer qui offre des garanties de **sécurité renforcée** via une
**double authentification** pour l’émetteur et le bénéficiaire.

Il intègre :

- Un module bancaire (gestion des utilisateurs, comptes, transactions)
- Un module interbancaire (validation inter-système, génération de codes, détection de fraude)
- Une interface **front-end Streamlit** pour visualiser et interagir avec l’ensemble du système

L’objectif est de simuler un processus bancaire **réaliste et sécurisé**, basé sur des APIs REST avec coordination
multi-services.

## 2. Structure du projet

```
mon-projet/
├── bank_server/             # Backend pour la banque (comptes, transactions locales)
├── safe_transfer_server/    # Backend pour SafeTransfer (validation, IA, interbancaire)
├── web_app/                 # Interface front-end (Streamlit)
├── docker-compose.yml       # Lancement global des services
└── README.md
```

## 3. Initialiser le projet

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

## 4. Lancer le projet

Le projet peut être exécuté de deux manières : avec Docker (recommandé pour la simplicité) ou en local manuellement.

### 4.1. Lancer le projet avec Docker

- Il faut que l'application "Docker Desktop" soit installée et ouverte
- Dans le terminal entrer la commande suivante :

```bash
docker-compose up --build
```

Cela lancera automatiquement :

- Les serveurs banque et SafeTransfer
- Les bases de données PostgreSQL associées et instancier des valeurs via des scripts python
- L’interface Streamlit

L'interface est accessible sur : : http://localhost:8501

### 4.2. Lancer le projet localement

#### 4.2.1. Bases de données

Deux approches sont possibles :

**Option 1 – Partir de Docker et stopper les serveurs :**

- Lancez la commande

```bash
docker-compose up --build
```

- Une fois les bases démarrées (via Docker Desktop), stoppez uniquement les
  conteneurs (`bank-server`, `safe-transfer-server` et `streamlit-front`)
- Les bases restent actives et prêtes à l’emploi

**Option 2 – Lancer entièrement manuellement :**

- Lancer la base de données sur bank-server :

```bash
docker run --name bank-db -e POSTGRES_DB=bank -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -p 5433:5432 -v bank-pgdata:/var/lib/postgresql/data -d postgres:15
```

- Lancer la base de données sur safe-transfer-server :

```bash
docker run --name safe-transfer-db -e POSTGRES_DB=safe-transfer -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -p 5434:5432 -v safe-transfer-pgdata:/var/lib/postgresql/data -d postgres:15
```

#### 4.2.2. Lancer les services un par un

- Lancer le backend banque : Exécuter le fichier `safe-transfer-Groupe1/bank_server/main/webapi/main.py`
- Lancer le backend SafeTransfer : Exécuter le fichier `safe-transfer-Groupe1/safe-transfer_server/main/webapi/main.py`
- Lancer l'interface Streamlit : Ouvrir un terminal et entrer la commande suivante :

```bash
streamlit run web_app/Home.py
```

L'interface est accessible sur : http://localhost:8501

## 5. Ressources
