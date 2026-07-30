# 🚀 AI SQL Chatbot Application

An end-to-end **Generative AI application** that allows users to interact with a PostgreSQL database using natural language.

Instead of writing SQL queries manually, users can ask questions in plain English. The application uses the **Gemini API** to generate SQL queries, executes them against PostgreSQL, and displays the results through an interactive Streamlit interface.

---

## 📌 Project Overview

Modern data platforms contain large amounts of structured data, but accessing this data often requires SQL expertise.

This project demonstrates how **Large Language Models (LLMs)** can bridge the gap between business users and databases by enabling:

> Natural Language → SQL Query → Database Execution → Human-readable Results

Example:

**User Question:**

```
Show me total sales by region for 2025
```

The AI generates:

```sql
SELECT 
    region,
    SUM(sales_amount) AS total_sales
FROM sales
WHERE year = 2025
GROUP BY region;
```

The query is executed on PostgreSQL and results are displayed in the web application.

---

# 🏗️ Architecture

```
                 User
                  |
                  |
          Natural Language Question
                  |
                  ↓
          Streamlit Web Application
                  |
                  ↓
            Gemini API (LLM)
                  |
                  ↓
        SQL Query Generation
                  |
                  ↓
             PostgreSQL
                  |
                  ↓
          Query Results Display
```

---

# ✨ Features

✅ Natural language to SQL conversion  
✅ Gemini API integration  
✅ PostgreSQL database connectivity  
✅ Interactive Streamlit dashboard  
✅ Prompt engineering for accurate SQL generation  
✅ Secure environment configuration using `.env`  
✅ End-to-end AI application architecture  

---

# 🎯 Example Use Cases

### Business Analytics

Question:

```
Which products generated the highest revenue?
```

Generated SQL:

```sql
SELECT 
    product_name,
    SUM(revenue) AS total_revenue
FROM products
GROUP BY product_name
ORDER BY total_revenue DESC;
```

---

### Data Exploration

Question:

```
How many customers joined each month?
```

The AI converts the question into SQL and returns the analysis.

---

# 🛠️ Tech Stack

## Programming Language

- Python 3.13

## AI / LLM

- Google Gemini API
- Prompt Engineering
- Natural Language Processing

## Database

- PostgreSQL
- SQL

## Frontend

- Streamlit

## Development Tools

- uv package manager
- Git
- GitHub
- Python-dotenv

---

# 📂 Project Structure

```
AiChatbotSQLApplication
│
├── app.py                  # Streamlit application
│
├── src/
│   ├── gemini.py           # Gemini API integration
│   ├── sql_generator.py    # Natural language to SQL logic
│   ├── database.py         # PostgreSQL connection
│   └── prompts.py          # LLM prompts
│
├── .env                    # Environment variables
├── .env.example            # Environment template
├── pyproject.toml          # Project dependencies
├── uv.lock                 # Locked dependencies
├── README.md
└── .gitignore
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/junaidbilal5/AiChatbotSQLApplication.git

cd AiChatbotSQLApplication
```

---

## 2. Create Virtual Environment

Using uv:

```bash
uv sync
```

Activate environment:

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## 3. Configure Environment Variables

Create `.env` file:

```bash
touch .env
```

Add:

```env
GEMINI_API_KEY=your_api_key_here

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DATABASE=your_database
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
```

---

## 4. Install Dependencies

```bash
uv sync
```

---

# ▶️ Run Application

Start Streamlit:

```bash
streamlit run app.py
```

Application will open:

```
http://localhost:8501
```

---

# 🔐 Security Considerations

- API keys are stored using environment variables
- Database credentials are not committed to GitHub
- `.env` is excluded using `.gitignore`

---

# 🧠 Key Learning Outcomes

Through this project, I gained practical experience with:

### Generative AI Engineering

- Working with Large Language Models
- Prompt engineering
- Controlling SQL generation
- Building AI-powered workflows

### Data Engineering

- Database integration
- SQL execution pipelines
- Data accessibility solutions

### Application Engineering

- Building production-style AI applications
- Structuring Python projects
- Creating interactive user interfaces

---

# 🚀 Future Improvements

Possible enhancements:

- [ ] Add LangChain SQL Agent
- [ ] Add RAG-based database schema understanding
- [ ] Add query validation layer
- [ ] Add SQL safety checks
- [ ] Add support for multiple databases
- [ ] Add conversation memory
- [ ] Deploy using Docker and cloud services

---

# 👨‍💻 Author

**Junaid Bilal**

Senior Data Engineer | AI Engineering Enthusiast

Focused on:
- Data Engineering
- Cloud Data Platforms
- Generative AI Applications
- LLM-powered Data Solutions

---

# ⭐ Feedback

If you find this project useful, feel free to ⭐ star the repository.

I welcome feedback and discussions about building AI-powered data applications.

---

## 📌 Connect

GitHub:
https://github.com/junaidbilal5

LinkedIn:
https://www.linkedin.com/in/junaid-bilal/