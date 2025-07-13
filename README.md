# 📄 SEBI Enforcement Orders Dashboard

A Streamlit-based dashboard to analyze and visualize **SEBI Enforcement Orders** with sentiment classification, filters, and CSV export — powered by **Snowflake** and hosted on **Streamlit Cloud**.

---

## 🚀 Live Demo

🔗 [Open Dashboard](https://sebi-dashboard.streamlit.app)

---

## 📊 Features

- ✅ Loads data directly from Snowflake
- ✅ Sentiment classification of SEBI order titles (Positive / Neutral / Negative / Unknown)
- ✅ Interactive filtering by sentiment
- ✅ Order-level table with PDF links
- ✅ CSV export of filtered results
- ✅ Fully deployed using Streamlit Community Cloud

---

## 🛠️ Tech Stack

| Layer         | Technology            |
|---------------|------------------------|
| Data Warehouse| 🧊 Snowflake           |
| Backend       | 🔵 Python              |
| Dashboard     | 🌟 Streamlit           |
| Hosting       | ☁️ Streamlit Cloud     |
| Version Control| 🐙 Git + GitHub        |

---

## 🧠 Sentiment Classification Logic

Using keywords in `TITLE`, each order is tagged as:
- **NEGATIVE** → Penalty, Fraud, Violation, Debar, etc.
- **NEUTRAL** → Settlement, Approval, Agreement
- **POSITIVE** → Disposed, Revoked, Relief, Closed
- **UNKNOWN** → If none of the above match

---

## 📁 Project Structure

sebi-dashboard/
├── streamlit_app.py # Main dashboard code
├── requirements.txt # Python dependencies
└── .streamlit/
└── secrets.toml # Snowflake credentials (ignored via .gitignore)

📌 Author
Mohammad Parvez
Snowflake | dbt | Streamlit | Data Engineering
📧 parvez2114@gmail.com


