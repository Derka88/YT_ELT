# 📊 Pipeline ELT YouTube

## 🚀 Présentation

Projet **ELT complet** utilisant l’**API YouTube**, orchestré avec **Airflow** et containerisé via **Docker**.  
Objectif : extraire, transformer et charger des données vidéo tout en respectant les bonnes pratiques de **tests unitaires, qualité de données et CI/CD**.

---

## 🏗️ Architecture

<p align="center">
  <img width="500" height="400" src="images/project_architecture.png">
</p>

---

## 🔄 Workflow ELT

1. **Extraction** : récupération des données YouTube via Python  
2. **Chargement** : insertion dans le **schéma staging** PostgreSQL  
3. **Transformation** : nettoyage et upsert dans le **schéma core**

- Initial → full load  
- Suivant → upsert des nouvelles données

---

## 📊 Variables extraites

- ID vidéo, titre, date de publication, durée  
- Vues, likes, commentaires  

---

## ⏱️ DAGs Airflow

Accessible via **http://localhost:8080**  

- **produce_json** : extraction API  
- **update_db** : chargement et transformation  
- **data_quality** : tests qualité des données

---

## 🛠️ Stack technique

- **Docker / Docker Compose**  
- **Apache Airflow**  
- **PostgreSQL (staging & core)**  
- **Python / SQL**  
- **Soda Core** pour la qualité des données  
- **Pytest** pour les tests unitaires  
- **GitHub Actions** pour CI/CD  

---

## ▶️ Lancer le projet

```bash
# Démarrer Airflow et les bases
docker compose up -d

# Accéder à l'UI Airflow
# http://localhost:8080
