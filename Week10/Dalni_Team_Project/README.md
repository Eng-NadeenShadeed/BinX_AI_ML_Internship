<div align="center">

# 🗺️ دلني — Dalni

## Palestine Tourism Recommendation System

**A personalized travel-discovery platform for Palestine — cross-track team capstone project.**

![TEAM PROJECT](https://img.shields.io/badge/TEAM%20PROJECT-f8a5c2?style=flat-square) ![AI/ML](https://img.shields.io/badge/AI%2FML-C44569?style=flat-square&logoColor=white) ![PALESTINE](https://img.shields.io/badge/PALESTINE-8B1E3F?style=flat-square&logoColor=white) ![RECOMMENDATION](https://img.shields.io/badge/RECOMMENDATION-C44569?style=flat-square&logoColor=white)

</div>

---

## 🧠 The Problem

Generic "Top 10 places in Palestine" lists don't account for who is actually traveling. A young adventure traveler on a tight budget and a family looking for a relaxed cultural weekend need completely different recommendations — even within the same city.

دلني solves this by collecting a traveler's actual preferences and returning a ranked, personalized set of places.

---

## 💡 The Solution

```
User Preferences
(city · trip type · age group · budget · group size)
            ↓
  Web App (دلني) / Mobile App (AI Travel Squad)
            ↓
      ASP.NET Core Backend API
            ↓
      AI Recommendation Service
            ↓
  Content-Based Model → Filtering → MMR Re-ranking
            ↓
  Personalized, Ranked Place Recommendations
```

---

## 🏗️ System Architecture

| Layer | Technology | Responsibility |
|-------|-----------|----------------|
| **AI/ML** | Python · scikit-learn · joblib | Recommendation model, scoring, MMR |
| **Backend** | ASP.NET Core · SQL Server | Business logic, database, API |
| **Frontend** | HTML · JS · Tailwind · Leaflet | دلني web interface |
| **Mobile** | Flutter · Dart | AI Travel Squad mobile app |

---

## 🤖 AI/ML Component

### My Role

I was responsible for the entire AI/ML component — from dataset collection to model deployment.

**Dataset:**
- Researched tourist attractions across Palestinian cities
- Collected part of the dataset manually — place names, types, coordinates, and descriptions in Arabic and English
- Final dataset: **308 places × 17 columns**

**Model Pipeline:**

```
User Input
    → Input Translation
    → User Profile Vector
    → One-Hot Encoding
    → Cosine Similarity
    → Recommendation Score
    → Filtering (city · trip type · age · budget)
    → MMR Re-ranking
    → Top-N Recommendations
```

**Scoring components:**
- **Cosine similarity** between user preference vector and each place's feature vector
- **Direct match signals** — city, trip type, age group overlap
- **Budget fit** — estimated cost × group size vs. total budget

**MMR (Maximal Marginal Relevance):** applied after scoring and filtering to reduce repetitive results and improve diversity in the final list.

**Exported artifacts:**

| Artifact | Purpose |
|----------|---------|
| `encoder.pkl` | Fitted OneHotEncoder for new user input |
| `feature_matrix.pkl` | Pre-computed feature matrix for all 308 places |
| `tourism_data.pkl` | Exported dataset for backend use |

**AI Service deployed at:**
```
https://palestine-tourism-recommendation-api.onrender.com
```

---

## 🗺️ Dataset

| | |
|---|---|
| **File** | `palestine_tourist_attractions_v2.csv` |
| **Size** | 308 places × 17 columns |
| **Model features** | `type`, `City`, `Budget_Level`, `Age_Group`, `Trip_Type` |
| **Other columns** | `Place_Name`, `Place_Name_AR`, `Description_AR`, `Description_EN`, `Latitude`, `Longitude`, `Estimated_Cost_ILS`, `Image_URL` |

---

## 🖥️ Web App — دلني Features

- 5-step preference form (cities, trip type, age group, group size, budget)
- Ranked results with match percentage
- Interactive map (Leaflet + OpenStreetMap)
- Side-by-side place comparison
- Favorites (stored locally)
- Trip sharing via link and QR code
- Fully Arabic (RTL), mobile-responsive UI

---

## 📱 Mobile App — AI Travel Squad Features

- Preference collection (city, budget, group size, trip type, age group)
- Ranked place results with match percentage
- Place details with favorites toggle
- Flutter + Dart, Material Design

---

## 🔗 Links

| Resource | Link |
|----------|------|
| **AI Service (live)** | [palestine-tourism-recommendation-api.onrender.com](https://palestine-tourism-recommendation-api.onrender.com) |
| **Presentation** | `Dalni_Presentation.pptx` — see this folder |
| **Demo** | `Dalni_Demo.mp4` — see this folder |

---

## ⚠️ Limitations

- Dataset covers 308 verified places — not exhaustive across all Palestinian cities
- Content-based only — no user history or ratings to learn from
- Most coordinates use city-center fallback rather than precise location
- AI service on Render may be slow on first request after inactivity (allow ~90 seconds)
- Mobile app's current matching uses city + trip type rules, not the live AI service

---

## 🔮 Future Improvements

- Semantic / TF-IDF similarity on place descriptions
- Collaborative or hybrid filtering using user ratings
- Larger, more geographically verified dataset
- Persistent account-based favorites and booking (mobile)
- Live weather and GPS-based suggestions (mobile)

---

## 👥 Team

Cross-track team from the BinX Tech AI & ML Internship Program — AI/ML, Backend, Frontend, Mobile, and Cybersecurity tracks.

---

<div align="center">

**BinX Tech · AI & ML Internship · 2026**

</div>
