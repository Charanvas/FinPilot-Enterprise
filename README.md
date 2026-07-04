# 💰 FinPilot Enterprise

> **AI-Powered Financial Operations Platform**

FinPilot Enterprise is an AI-powered financial invoice auditing platform that automates invoice verification, detects amount mismatches, and assists finance teams by reducing manual effort through an intelligent multi-agent workflow.

---

# ✨ Features

- 📄 Invoice Upload (PDF/Image)
- 🔍 OCR-based Invoice Extraction
- 🤖 AI-Powered Invoice Understanding (Google Gemini)
- 🧠 Multi-Agent Architecture
- 🔄 LangGraph Workflow Orchestration
- 💰 Invoice Amount Validation
- 🎫 Automatic Ticket Creation
- ✅ Auto-Correction Workflow
- 📊 Executive Dashboard
- 📈 Analytics Dashboard
- 💾 SQLite Database Integration
- ⚡ FastAPI Backend
- 🖥️ Streamlit Frontend

---

# 🏗️ System Architecture

```
                Invoice Upload
                      │
                      ▼
             OCR Extraction Agent
                      │
                      ▼
          Document Processing Agent
                      │
                      ▼
          Financial Validation Agent
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   Auto Correct             Raise Ticket
          │                       │
          └───────────┬───────────┘
                      ▼
                SQLite Database
                      │
                      ▼
            Streamlit Dashboard
```

---

# 🧠 AI Workflow

```
Invoice

↓

OCR Extraction

↓

Document Agent

↓

Finance Agent

↓

Action Agent

↓

Database

↓

Dashboard & Analytics
```

---

# 📂 Project Structure

```
FinPilot
│
├── app
│   ├── agents
│   ├── api
│   ├── core
│   ├── database
│   ├── schemas
│   ├── tools
│   ├── ui
│   └── workflow
│
├── uploads
├── tests
├── requirements.txt
└── README.md
```

---

# 🚀 Tech Stack

## AI & ML

- Google Gemini
- LangGraph
- OCR
- Multi-Agent AI

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Frontend

- Streamlit
- Plotly

## Programming

- Python

---

# 📊 Dashboard

The executive dashboard provides:

- Total Invoices Processed
- Money Audited
- Vendor Count
- Ticket Statistics
- Invoice Analytics
- Decision Distribution
- AI Summary
- Recent Invoice Activity

---

# 🎯 Workflow

1. Upload Invoice
2. OCR extracts invoice information
3. Gemini validates financial data
4. AI compares invoice details
5. Auto Correct if valid
6. Raise Ticket if mismatch detected
7. Store results in SQLite
8. Display analytics on dashboard

---

# 📈 Analytics

- Vendor Spending Analysis
- Invoice Distribution
- Auto Correct Rate
- Ticket Statistics
- Average Invoice Value
- Highest Invoice Amount

---

# 🛠 Installation

Clone the repository

```bash
git clone https://github.com/your-username/FinPilot.git
```

Go to the project directory

```bash
cd FinPilot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
python run_api.py
```

Run Streamlit

```bash
python -m streamlit run app/ui/dashboard.py
```

---

# 📷 Screenshots

<h2>📊 Dashboard</h2>

<p align="center">
  <img src="assets/dashboard.png" width="900"/>
</p>

Similarly:

<h2>📄 Invoice Center</h2>

<p align="center">
  <img src="assets/invoice-center.png" width="900"/>
</p>

<h2>📈 Analytics</h2>

<p align="center">
  <img src="assets/analytics.png" width="900"/>
</p>

<h2>🎫 Tickets</h2>

<p align="center">
  <img src="assets/tickets.png" width="900"/>
</p>

---

# 🔮 Future Enhancements

- Purchase Order Matching
- Vendor Risk Analysis
- AI Copilot for Finance Teams
- Fraud Detection
- Email Notifications
- Authentication & Role-Based Access
- PostgreSQL Support
- Docker Deployment
- Cloud Deployment (AWS/Azure)

---

# 💡 Key Highlights

- Enterprise-inspired financial workflow
- AI-assisted invoice validation
- Multi-Agent architecture using LangGraph
- Intelligent decision engine
- Automated ticket generation
- Executive analytics dashboard
- Modular and scalable backend

---

# 👩‍💻 Author

**Samanuri Sri Manasa Varma**

AI & Machine Learning Engineer

- GitHub: https://github.com/manasaavarmaa
- LinkedIn: https://www.linkedin.com/in/smanasavarma/

---

# ⭐ If you found this project interesting, consider giving it a Star!